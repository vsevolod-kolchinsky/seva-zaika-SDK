from typing import Any, Optional

from .base import BaseEntityApi


class Book:
    """LOTR Book entity model"""

    _id: str
    name: str

    def __init__(self, api_client, _id: str, name: str) -> None:
        self._api_client = api_client
        self._id = _id
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._id=}, {self.name=})"

    def get_chapters(self) -> Any:
        """Request all chapters of one specific book"""
        return BookChaptersApi(self._api_client).query.filter(_id=self._id).fetch()


class BookChapter:
    """LOTR Book chapter entity model"""

    _id: str
    name: str
    book_id: Optional[str]

    def __init__(
        self, api_client, _id: str, chapterName: str, book: Optional[str] = None
    ) -> None:
        # Note: signature variable names are using camelCase because following
        # the API response format
        self._api_client = api_client
        self._id = _id
        self.book_id = book
        self.name = chapterName

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._id=}, {self.name=})"


class BookChaptersApi(BaseEntityApi):
    """Book chapters API

    Request all chapters of one specific book.
    """

    entity_getter = "get_book_chapters"
    entites_getter = "get_book_chapters"
    entity_model = BookChapter


class BookApi(BaseEntityApi):
    """Books API

    List of all "The Lord of the Rings" books.
    """

    entity_getter = "get_book"
    entites_getter = "get_books"
    entity_model = Book


class ChaptersApi(BaseEntityApi):
    """Chapters API

    List of all book chapters.
    """

    entity_getter = "get_chapter"
    entites_getter = "get_chapters"
    entity_model = BookChapter
