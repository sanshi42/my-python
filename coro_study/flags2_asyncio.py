import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path

import httpx  # 异步上下文管理器
import tqdm  # type: ignore
from flags2_common import DownloadStatus, main, save_flag

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

async def download_one(client: httpx.AsyncClient, cc: str, base_url: str,
                       semaphore: asyncio.Semaphore, verbose: bool) -> DownloadStatus:
    try:
        async with semaphore:
            image = await get_flag(client, base_url, cc)
    except httpx.HTTPStatusError as exc:
        res = exc.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'not found: {res.url}'
        else:
            raise
    else:
        await asyncio.to_thread(save_flag, image, f'{cc}.gif')  # I/O操作放到线程中运行
        status = DownloadStatus.OK
        msg = 'OK'
    if verbose and msg:
        print(cc, msg)
    return status

async def get_flag(client: httpx.AsyncClient, base_url: str, cc: str) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=3.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content

def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  concur_req: int) -> Counter[DownloadStatus]:
    return asyncio.run(supervisor(cc_list, base_url, verbose, concur_req))

async def supervisor(cc_list: list[str],
                     base_url: str,
                     verbose: bool,
                     concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    semaphore = asyncio.Semaphore(concur_req)
    async with httpx.AsyncClient() as client:
        to_do = [download_one(client, cc, base_url, semaphore, verbose)
                 for cc in sorted(cc_list)]
        to_do_iter = asyncio.as_completed(to_do)
        if not verbose:
            to_do_iter =tqdm.tqdm(to_do_iter, total=len(cc_list))
        error: httpx.HTTPError | None = None
        for coro in to_do_iter:
            try:
                status = await coro
            except httpx.HTTPStatusError as exc:
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=exc.response)
                error = exc
            except httpx.RequestError as exc:
                error_msg = f'{exc} {type(exc)}'.strip()
                error = exc
            except KeyboardInterrupt:
                break

            if error:
                status = DownloadStatus.ERROR
                if verbose:
                    url = str(error.request.url)
                    cc = Path(url).stem.upper()
                    print(f'{cc} error: {error_msg}')
            counter[status] += 1
    return counter

if __name__ == '__main__':
    main(download_many)