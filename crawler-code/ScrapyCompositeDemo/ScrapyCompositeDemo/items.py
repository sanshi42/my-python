# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class BookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    authors = Field()
    catalog = Field()
    comments = Field()
    cover = Field()
    id = Field()
    introduction = Field()
    isbn = Field()
    name = Field()
    page_number = Field()
    price = Field()
    published_at = Field()
    publisher = Field()
    score = Field()
    tags = Field()
    translators = Field()