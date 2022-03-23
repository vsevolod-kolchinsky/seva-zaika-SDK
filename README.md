Welcome to Seva Zaika LOTR API SDK!

# Installing

FIXME

# Using

## Basic usage

## Getting list of books

```python
from seva_zaika_sdk import LotrApi

lotr = LotrApi(api_key="SECRET")

books = lotr.get_books()
for book in books.get("docs", []):
    print(f"{book}")

```

The result will be list of `dict` objects:

```
{'_id': '5cf5805fb53e011a64671582', 'name': 'The Fellowship Of The Ring'}
{'_id': '5cf58077b53e011a64671583', 'name': 'The Two Towers'}
{'_id': '5cf58080b53e011a64671584', 'name': 'The Return Of The King'}
```

## Advanced usage

### Getting list of Books and Chapters

```python
from seva_zaika_sdk import LotrApi

lotr = LotrApi(api_key="SECRET")

books = lotr.Book.query.limit(1).fetch()
for book in books:
    book_chapters = book.get_chapters()
    print(f"{book.name!r} chapters:")
    for num, chapter in enumerate(book_chapters, start=1):
        print(f"\t{num}. {chapter.name}")

```

The result will be list of native model entites:

```
'The Fellowship Of The Ring' chapters:
	1. A Long-expected Party
	2. The Shadow of the Past
	3. Three is Company
	4. A Short Cut to Mushrooms
	5. A Conspiracy Unmasked
	6. The Old Forest
	7. In the House of Tom Bombadil
	8. Fog on the Barrow-Downs
	9. At the Sign of The Prancing Pony
	10. Strider
	11. A Knife in the Dark
	12. Flight to the Ford
	13. Many Meetings
	14. The Council of Elrond
	15. The Ring Goes South
	16. A Journey in the Dark
	17. The Bridge of Khazad-dûm
	18. Lothlórien
	19. The Mirror of Galadriel
	20. Farewell to Lórien
	21. The Great River
	22. The Breaking of the Fellowship
```

### Getting list of Characters

```python

characters = lotr.Character.query.sort(name="desc").limit(10).fetch()
for character in characters:
    print(f"{character.name=}")

```

### Getting Character Quotes

```python

legolas = lotr.Character.query.filter(name="/legolas/i").fetch_one()
for quote in legolas.get_quotes():
    print(f"{legolas.name} said: {quote.dialog!r}")

```

#### Filtering Characters query

Supported kwarg modifiers are: 

* `__ne` - not equal,
* `__gt` - greater than,
* `__lt` – less than,
* `__gte` – greater or equal to, 
* `__lte` – less or equal to.

```python

not_legolas = lotr.Character.query.filter(name__ne="Legolas").fetch_one()
print(f"{not_legolas.name}")

```

### Getting filtered list of Movies

Get most awarded Movies:

```python

movies = lotr.Movie.query.filter(academy_award_wins__gt=10).fetch()

```

# Testing

FIXME
