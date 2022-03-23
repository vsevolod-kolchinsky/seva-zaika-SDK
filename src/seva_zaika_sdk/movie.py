from typing import Any

from .base import BaseEntityApi
from .quote import MovieQuoteApi


class Movie:
    """Movie entity model"""

    _id: str
    name: str
    runtime_in_minutes: int
    budget_in_millions: int
    box_office_revenue_in_millions: int
    academy_award_nominations: int
    academy_award_wins: int
    rotten_tomatoes_score: int

    def __init__(
        self,
        api_client,
        _id: str,
        name: str,
        runtimeInMinutes: int,
        budgetInMillions: int,
        boxOfficeRevenueInMillions: int,
        academyAwardNominations: int,
        academyAwardWins: int,
        rottenTomatoesScore: int,
    ) -> None:
        # Note: signature variable names are using camelCase because following
        # the API response format
        self._api_client = api_client
        self._id = _id
        self.name = name
        self.runtime_in_minutes = runtimeInMinutes
        self.budget_in_millions = budgetInMillions
        self.box_office_revenue_in_millions = boxOfficeRevenueInMillions
        self.academy_award_nominations = academyAwardNominations
        self.academy_award_wins = academyAwardWins
        self.rotten_tomatoes_score = rottenTomatoesScore

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self._id=}, {self.name=}, "
            f"{self.runtime_in_minutes=}, {self.budget_in_millions=}, "
            f"{self.box_office_revenue_in_millions=}, "
            f"{self.academy_award_nominations=}, {self.academy_award_wins=}, "
            f"{self.rotten_tomatoes_score=})"
        )

    def get_quotes(self) -> Any:
        """Request all movie quotes for one specific movie

        (only working for the LotR trilogy)"""
        return MovieQuoteApi(self._api_client).query.filter(_id=self._id).fetch()


class MovieApi(BaseEntityApi):
    """Movies API

    List of all movies, including the "The Lord of the Rings"
    and the "The Hobbit" trilogies.
    """

    entity_getter = "get_movie"
    entites_getter = "get_movies"
    entity_model = Movie
