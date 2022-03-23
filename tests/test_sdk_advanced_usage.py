import vcr


@vcr.use_cassette("tests/test_book_model.yaml")
def test_book_model(client):
    limit = 1
    books = client.Book.query.limit(limit).fetch()
    assert len(books) == limit

    book = client.Book.query.filter(name="The Fellowship Of The Ring").fetch_one()
    assert book._id == "5cf5805fb53e011a64671582"

    book = client.Book.query.filter(_id="5cf5805fb53e011a64671582").fetch_one()
    assert book.name == "The Fellowship Of The Ring"

    book_chapters = book.get_chapters()
    assert len(book_chapters) == 22


@vcr.use_cassette("tests/test_movie_model.yaml")
def test_movie_model(client):
    limit = 2
    movies = client.Movie.query.filter(academy_award_wins__gt=10).limit(limit).fetch()
    assert len(movies) == limit

    movie = client.Movie.query.filter(_id="5cd95395de30eff6ebccde5d").fetch_one()
    assert movie
    assert movie.name == "The Return of the King"

    movie_quotes = movie.get_quotes()
    assert len(movie_quotes) == 873


@vcr.use_cassette("tests/test_character_model.yaml")
def test_character_model(client):
    legolas = client.Character.query.filter(name="Legolas").fetch_one()
    assert legolas._id == "5cd99d4bde30eff6ebccfd81"

    legolas_again = client.Character.query.filter(
        _id="5cd99d4bde30eff6ebccfd81"
    ).fetch_one()
    assert legolas_again.name == "Legolas"

    character_quotes = legolas.get_quotes()
    assert len(character_quotes) == 55


@vcr.use_cassette("tests/test_quote_model.yaml")
def test_quote_model(client):
    limit = 5
    quotes = client.Quote.query.limit(limit).fetch()
    assert len(quotes) == limit

    quote = client.Quote.filter(_id="5cd96e05de30eff6ebcce7ec").fetch_one()
    assert quote.dialog == "Give us that! Deagol my love"


@vcr.use_cassette("tests/test_chapter_model.yaml")
def test_chapter_model(client):
    limit = 5
    chapters = client.Chapter.query.limit(limit).offset(limit).fetch()
    assert len(chapters) == limit

    chapter = client.Chapter.query.filter(_id="6091b6d6d58360f988133b91").fetch_one()
    assert chapter.name == "In the House of Tom Bombadil"


@vcr.use_cassette("tests/test_character_model_filters_and_sorting.yaml")
def test_character_model_filters_and_sorting(client):
    characters = client.Character.filter(name="/foot/i").sort(name="asc").fetch()
    assert len(characters) == 11
    first_character = characters[0]
    assert first_character._id == "5cd99d4bde30eff6ebccfe97"
    assert first_character.name == "Bodo Proudfoot"
