# SDK Design

SDK built keeping two approaches in mind: 

    - the simple approach consist of using raw `dict` out of JSON data received
    from particular endpoint, accessed by dedicated client method. E.g.
    `get_books()` or `get_book("<id>")`.

    - the more advanced approach is recommended and provides ORM-like models to
    operate with response reuslts.

Essential part of SDK is API client module that provides methods to access
each API endpoint.

# Simple approach

Data directly available by calling client method that accessing appropriate
endpoint and fetching data using specifed filters.

# ORM-like approach

More advanced approach allows operating with API entities using defined models:
`Book`, `Movie`, `Character`, `Quote`, `Chapter`. 

Each model support building specific queries using filters, pagination, etc.
Please refer README.md for details.

Models also supporting relationships like `Book` instance will have 
`.get_chapters` method that returns `Chapter` instances related to particular
`Book` instance.
