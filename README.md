# Chronicle

A REST API for fetching historical data, based on the
large, Wikipedia-sourced [historic-events] dataset,
made with the [Flask] framework and [Flask-Restless].

| Endpoint               | Method | Description |
|-----------------------:|:------:|:------------|
| `/api/event?q=<json>`  |**GET** | Given a JSON query, respond with an array of events. |
| `/api/event/<id>`      |**GET** | Return the event that matches the **id**. |
| `/api/event`           |**GET** | Return all event objects. |
| `/`                    |**GET** | Return the (static?) index page. |

Note that because Chronicle uses Flask-Restless under the
hood, the `<json>` query is not the typical MongoDB syntax.
You may refer to the [query syntax] here. You might also
want to read up on the [request and responses] documentation
for an idea of how to better use the API.

### Schema

Note that this is the schema for *one* event object.
By default the endpoints return up to 30 events per
page- you may want to check out the [pagination]
format.

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

### Running

```sh
$ git clone --recursive git@github.com:datalib/chronicle.git
$ cd chronicle
$ pip install -r requirements.txt
$ ./mkindex
$ gunicorn chronicle.app:app
```

----------

`historic-events` is © Nolan Hemmatazad / Wikimedia Commons / [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/)

[historic-events]: https://github.com/tuvalie/historic_events
[Flask]: https://flask.pocoo.org
[Flask-Restless]: flask-restless.readthedocs.org/en/latest/
[query syntax]: http://flask-restless.readthedocs.org/en/latest/searchformat.html
[request and responses]: http://flask-restless.readthedocs.org/en/latest/requestformat.html
[pagination]: http://flask-restless.readthedocs.org/en/latest/requestformat.html#clientpagination
