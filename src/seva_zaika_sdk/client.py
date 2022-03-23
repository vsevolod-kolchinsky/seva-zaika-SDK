"""API client"""
from typing import Any

from .base import BaseClient
from .book import BookApi, ChaptersApi
from .character import CharacterApi
from .movie import MovieApi
from .quote import QuoteApi


class Client(BaseClient):
    """LOTR API client SDK"""

    def __getattr__(self, __name: str) -> Any:
        tr = {
            "Book": BookApi,
            "Movie": MovieApi,
            "Character": CharacterApi,
            "Quote": QuoteApi,
            "Chapter": ChaptersApi,
        }
        model = tr.get(__name)
        if not model:
            raise NotImplementedError(f"Unknown API: {__name!r}")
        return model(self)

    def get_book(self, book_id: str, **kwargs) -> dict:
        """Request one specific book"""
        return self._get(self.get_endpoint_url("book", book_id), **kwargs)

    def get_books(self, **kwargs) -> dict:
        """List of all "The Lord of the Rings" books"""
        return self._get(self.get_endpoint_url("book"), **kwargs)

    def get_book_chapters(self, book_id: str) -> dict:
        """Request all chapters of one specific book"""
        return self._get(self.get_endpoint_url("book", book_id, "chapter"))

    def get_movie(self, movie_id, **kwargs) -> dict:
        """Request one specific movie"""
        return self._get(self.get_endpoint_url("movie", movie_id), **kwargs)

    def get_movies(self, **kwargs) -> dict:
        """List of all movies

        including the "The Lord of the Rings" and the "The Hobbit" trilogies
        """
        return self._get(self.get_endpoint_url("movie"), **kwargs)

    def get_movie_quotes(self, movie_id, **kwargs) -> dict:
        """Request all movie quotes for one specific movie

        (only working for the LotR trilogy)
        """
        return self._get(self.get_endpoint_url("movie", movie_id, "quote"), **kwargs)

    def get_character(self, character_id: str, **kwargs) -> dict:
        """Request one specific character"""
        return self._get(self.get_endpoint_url("character", character_id), **kwargs)

    def get_character_quotes(self, character_id: str) -> dict:
        """Request all movie quotes of one specific character"""
        return self._get(self.get_endpoint_url("character", character_id, "quote"))

    def get_characters(self, **kwargs) -> dict:
        """List of characters

        including metadata like name, gender, realm, race and more
        """
        return self._get(self.get_endpoint_url("character"), **kwargs)

    def get_quote(self, quote_id: str, **kwargs) -> dict:
        """Request one specific movie quote"""
        return self._get(self.get_endpoint_url("quote", quote_id), **kwargs)

    def get_quotes(self, **kwargs) -> dict:
        """List of all movie quotes"""
        return self._get(self.get_endpoint_url("quote"), **kwargs)

    def get_chapter(self, chapter_id: str, **kwargs) -> dict:
        """List of all book chapters"""
        return self._get(self.get_endpoint_url("chapter", chapter_id), **kwargs)

    def get_chapters(self, **kwargs) -> dict:
        """Request one specific book chapter"""
        return self._get(self.get_endpoint_url("chapter"), **kwargs)
