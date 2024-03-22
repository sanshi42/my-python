from pathlib import Path
from unicodedata import name

from charindex import InvertedIndex
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

STATIC_PATH = Path(__file__).parent.absolute() / 'static'

app = FastAPI(
    title='Mojifinder Web',
    description='Search Unicode',
)

class CharName(BaseModel):
    char: str
    name: str

def init(app):
    app.state.index = InvertedIndex()
    app.state.form = (STATIC_PATH / 'form.html').read_text()

init(app)

@app.get('/search', response_model=list[CharName])
async def search(q: str):
    chars = sorted(app.state.index.search(q))
    return ({'char': c, 'name': name(c)} for c in chars)

@app.get('/', response_class=HTMLResponse, include_in_schema=False)
def form():
    return app.state.form

# 没有主函数