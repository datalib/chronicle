# Chronicle

A REST API for fetching historical data, based on the
large, Wikipedia-sourced [historic-events] dataset,
made with the [Flask] framework and [Flask-Restless].

### Running

```sh
$ pip install -r requirements.txt
$ ./mkindex
$ python launch.py
```

### Endpoints

| Endpoint         | Method | Description |
|-----------------:|:------:|:------------|
| `/api/q?=<json>` |**GET**| Given a posted JSON query, respond with an array of events. |
| `/api/<id>`      |**GET** | Return the row that matches the **id**. |
| `/`              |**GET** | Return the (static?) index page. |

Note that because Chronicle uses Flask-Restless under the
hood, the `<json>` query is not the typical MongoDB syntax.
You may refer to the [query syntax] here.

### Schema

    {
      "id": <int>,
      "type": ["general" | "birth" | "death"],
      "desc": <string>,
      "date": {
        "year":  <int>,
        "month": [<int> | null],
        "day":   [<int> | null]
      }
    }

Sometimes the month/date fields can be null, this is
either because they are not available or the current
pipeline is not smart enough to extract it yet.

[historic-events]: https://github.com/tuvalie/historic_events
[Flask]: https://flask.pocoo.org
[Flask-Restless]: flask-restless.readthedocs.org/en/latest/
[query syntax]: http://flask-restless.readthedocs.org/en/latest/searchformat.html
