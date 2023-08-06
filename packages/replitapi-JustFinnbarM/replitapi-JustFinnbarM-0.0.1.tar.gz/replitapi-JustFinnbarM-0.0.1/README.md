# Replit API

## Database

Works exactly the same as the official implementation, but doesn't depend on Flask 1.1.2! See the official docs: https://replit-py.readthedocs.io/en/latest/api.html#module-replit.database

## Web scraper

```python
get_user_data(query, mode = "username")
```
`mode` - What to query by. Can be `"username"` or `"url"`.

`query` - The item to look for. Must be in format with the `mode`.

Returns: 
```python
LiteralObject({ # LiteralObject just behaves like a class for this purpose. Keys = Attributes.
    "favourite_langauges": [str(languages)],
    "cycles": int(cycles),
    "profile_picture": str(img_url)
  })
```

```python
get_repl_data(query, user = "", mode = "name")
```
`mode` - What to query by. Can be `"name"` or `"url"`.

`user` - Specifies the user to search for if the `mode` is `"name"`. Can be ommited if the `mode` is `"url"`.

`query` - The item to look for. Must be in format with the `mode`.

Returns: 
```python
LiteralObject({ # LiteralObject just behaves like a class for this purpose. Keys = Attributes.
    "favourite_langauges": [str(languages)],
    "cycles": int(cycles),
    "profile_picture": str(img_url)
  })
```

More to come!