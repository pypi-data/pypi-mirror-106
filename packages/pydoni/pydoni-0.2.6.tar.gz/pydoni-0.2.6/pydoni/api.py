import pydoni
import goodreads_api_client as gr
from html2text import html2text


class Goodreads(object):
    """
    Interact with the Goodreads API.
    """

    def __init__(self, api_key):

        self.logger = pydoni.logger_setup(
            name=pydoni.what_is_my_name(classname=self.__class__.__name__, with_modname=True),
            level=pydoni.modloglev)

        if not api_key > '':
            errmsg = 'Must enter a valid API key!'
            self.logger.critical(errmsg, exc_info=True)
            raise Exception(errmsg)

        self.client = gr.Client(developer_key=api_key)

    def search(self, id=None, title=None):
        """
        Search the Goodreads API for a book by either its ID or title, and return
        its metadata as a dictionary. If the book cannot be found in the API, return
        an empty dicitonary.
        """
        book_dct = None

        if id is not None:
            # Prefer ID if supplied, else use title
            self.logger.info(f"Searching for ID '{str(id)}'")
            book_dct = self.client.Book.show(id)
            if book_dct is None:
                self.logger.warn(f"No match found for ID '{str(id)}'")

        if title is not None and book_dct is None:
            # Search for title only if ID either not supplied or if book cannot be
            # found by ID
            self.logger.info(f"Searching for title '{str(title)}'")
            book_dct = self.client.Book.title(title)
            if book_dct is None:
                self.logger.warn(f"No match found for title '{str(title)}'")

        return {} if book_dct is None else book_dct

    def extract_all(self, book_dct):
        """
        Return a dictionary with pre-defined keys of interest.
        """
        items = [
            'id',
            'title',
            'publication_year',
            'num_pages',
            'language_code',
            'country_code',
            'description',
            'average_rating',
            'url',
            'ratings_count',
            'text_reviews_count',
        ]

        bookdata = {}

        for item in items:
            if item in self.book.keys():
                bookdata[item] = self.book[item]
            else:
                self.logger.warn(f"Key '{item}' missing from `bookdata`")
                self.logger.debug(f"`item` = '{item}'" % item)
                self.logger.debug(f"`type(item)` = '{type(item)}'" % type(item))
                self.logger.debug(f"`bookdata.keys()` = {str(bookdata.keys())}")

        if 'authors' in self.book.keys():
            if 'author' in self.book['authors'].keys():
                if 'name' in self.book['authors']['author'].keys():
                    bookdata['author'] = self.book['authors']['author']['name']
            else:
                self.logger.warn("Key 'author' missing from `self.book['authors']`")
        else:
            self.logger.warn("Key 'authors' missing from `bookdata`")

        if 'description' in bookdata.keys():
            desc = bookdata['description']
            desc = '' if desc is None else desc
            bookdata['description'] = html2text(desc).strip()
        else:
            self.logger.warn("Key 'description' missing from `bookdata`")

        return bookdata

    def as_data_frame(self):
        """
        Render `bookdata` dictionary as dataframe.
        """
        import pandas as pd

        if not len(bookdata):
            errmsg = 'Must run `extract_all()` method first to populate ' \
            '`bookdata` dictionary!'
            self.logger.error(errmsg)
            raise Exception(errmsg)

        self.bookdf = pd.DataFrame(bookdata, index=0)
        self.logger.info('Coerced `bookdata` dictionary to dataframe')

        return self.bookdf
