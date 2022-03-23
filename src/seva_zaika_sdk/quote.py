from .base import BaseEntityApi


class CharacterQuote:
    """Movie quote entity model"""

    _id: str
    dialog: str
    movie_id: str
    character_id: str
    id: str

    def __init__(
        self, api_client, _id: str, dialog: str, movie: str, character: str, id: str
    ) -> None:
        self._api_client = api_client
        self._id = _id
        self.dialog = dialog
        self.movie_id = movie
        self.character_id = character

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self._id=}, {self.dialog=}, "
            f"{self.movie_id=}, {self.character_id=})"
        )


class CharacterQuoteApi(BaseEntityApi):
    """Character movie quotes API

    Request all movie quotes of one specific character.
    """

    entity_getter = "get_character_quotes"
    entites_getter = "get_character_quotes"
    entity_model = CharacterQuote


class MovieQuoteApi(BaseEntityApi):
    """Request all movie quotes for one specific movie

    (only working for the LotR trilogy)"""

    entity_getter = "get_movie_quotes"
    entites_getter = "get_movie_quotes"
    entity_model = CharacterQuote


class QuoteApi(BaseEntityApi):
    """List of all movie quotes"""

    entity_getter = "get_quote"
    entites_getter = "get_quotes"
    entity_model = CharacterQuote
