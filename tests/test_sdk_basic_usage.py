import vcr


@vcr.use_cassette("tests/test_base_client_usage_get_books.yaml")
def test_base_client_usage_get_books(client):
    books_response = client.get_books()
    assert len(books_response.get("docs", [])) > 0


@vcr.use_cassette("tests/test_base_client_usage_get_book.yaml")
def test_base_client_usage_get_book(client):
    books_response = client.get_books()
    for book in books_response.get("docs", []):
        book_data = client.get_book(book["_id"])
        assert book["_id"] == book_data.get("docs", [])[0]["_id"]


@vcr.use_cassette("tests/test_base_client_usage_get_book_chapters.yaml")
def test_base_client_usage_get_book_chapters(client):
    books_response = client.get_books(limit=1)
    for book in books_response.get("docs", []):
        book_chapters_data = client.get_book_chapters(book["_id"])
        assert len(book_chapters_data.get("docs", [])) > 0


@vcr.use_cassette("tests/test_base_client_usage_get_movies.yaml")
def test_base_client_usage_get_movies(client):
    limit = 5
    movies_response = client.get_movies(limit=limit)
    movies = movies_response.get("docs", [])
    assert len(movies) == limit
    for movie in movies:
        movie_data = client.get_movie(movie["_id"])
        movie_info = movie_data.get("docs", [])
        assert len(movie_info) == 1
        assert movie_info[0]["_id"] == movie["_id"]


@vcr.use_cassette("tests/test_base_client_usage_get_movie_quotes.yaml")
def test_base_client_usage_get_movie_quotes(client):
    movie_id = "5cd95395de30eff6ebccde5d"
    limit = 10
    quotes_response = client.get_movie_quotes(movie_id, limit=limit)
    quotes = quotes_response.get("docs", [])
    assert len(quotes) == limit
    assert quotes[0]["movie"] == movie_id


@vcr.use_cassette("tests/test_base_client_usage_get_characters.yaml")
def test_base_client_usage_get_characters(client):
    limit = 10
    characters_response = client.get_characters(limit=limit)
    characters = characters_response.get("docs", [])
    assert len(characters) == limit


@vcr.use_cassette("tests/test_base_client_usage_get_character.yaml")
def test_base_client_usage_get_character(client):
    character_id = "5cd99d4bde30eff6ebccfbbe"
    character_response = client.get_character(character_id)
    characters = character_response.get("docs", [])
    assert len(characters) == 1
    character = characters[0]
    assert character["_id"] == character_id
    assert character["gender"] == "Female"
    assert character["name"] == "Adanel"


@vcr.use_cassette("tests/test_base_client_usage_get_character_quotes.yaml")
def test_base_client_usage_get_character_quotes(client):
    character_id = "5cd99d4bde30eff6ebccfe9e"
    limit = 5
    character_quotes_response = client.get_character_quotes(character_id, limit=limit)
    quotes = character_quotes_response.get("docs", [])
    assert (len(quotes)) == limit


@vcr.use_cassette("tests/test_base_client_usage_get_quotes.yaml")
def test_base_client_usage_get_quotes(client):
    limit = 5
    quotes_response = client.get_quotes(limit=limit)
    quotes = quotes_response.get("docs", [])
    assert len(quotes) == limit


@vcr.use_cassette("tests/test_base_client_usage_get_chapters.yaml")
def test_base_client_usage_get_chapters(client):
    limit = 5
    chapters_response = client.get_chapters(limit=limit)
    chapters = chapters_response.get("docs", [])
    assert len(chapters) == limit


@vcr.use_cassette("tests/test_base_client_usage_get_chapter.yaml")
def test_base_client_usage_get_chapter(client):
    chapter_id = "6091b6d6d58360f988133b8f"
    chapter_response = client.get_chapter(chapter_id)
    chapters = chapter_response.get("docs", [])
    assert len(chapters) == 1
    chapter = chapters[0]
    assert chapter["_id"] == chapter_id
    assert chapter["chapterName"] == "A Conspiracy Unmasked"
