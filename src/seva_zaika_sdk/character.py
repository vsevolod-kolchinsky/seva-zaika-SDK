from typing import Any, Optional

from .base import BaseEntityApi
from .quote import CharacterQuoteApi


class Character:
    """Character entity model"""

    _id: str
    height: str
    race: str
    gender: str
    birth: str
    spouse: str
    death: str
    realm: str
    hair: str
    name: str
    wiki_url: Optional[str]

    def __init__(
        self,
        api_client,
        _id: str,
        height: str,
        race: str,
        gender: str,
        birth: str,
        spouse: str,
        death: str,
        realm: str,
        hair: str,
        name: str,
        wikiUrl: Optional[str] = None,
    ) -> None:
        # Note: signature variable names are using camelCase because following
        # the API response format
        self._api_client = api_client
        self._id = _id
        self.height = height
        self.race = race
        self.gender = gender
        self.birth = birth
        self.spouse = spouse
        self.death = death
        self.realm = realm
        self.hair = hair
        self.name = name
        self.wiki_url = wikiUrl

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self._id=}, {self.height=}, "
            f"{self.race=}, {self.gender=}, {self.birth=}, {self.spouse=}, "
            f"{self.death=}, {self.realm=}, {self.hair=}, {self.name=}, "
            f"{self.wiki_url=})"
        )

    def get_quotes(self) -> Any:
        """Request all movie quotes of one specific character"""
        return CharacterQuoteApi(self._api_client).query.filter(_id=self._id).fetch()


class CharacterApi(BaseEntityApi):
    """Characters API

    List of characters including metadata like name, gender, realm, race and
    more.
    """

    entity_getter = "get_character"
    entites_getter = "get_characters"
    entity_model = Character
