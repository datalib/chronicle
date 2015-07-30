# HQuery

A REST API for fetching historical data, based on the
large, Wikipedia-sourced [historic-events] dataset,
made with the Flask framework.

### Endpoints

| Endpoint   | Method | Description |
|-----------:|:------:|:------------|
| `/v/query` |**POST**| Given a posted JSON query, respond with an array of rows. |
| `/v/<id>`  |**GET** | Return the row that matches the **id**. |
| `/v/`      |**GET** | Return the (static?) index page. |

### Row Schema

```
{
  "year": <integer>,
  "type": ["general" | "birth" | "death"],
  "date": [{"month": <integer>, "day": <integer>} | null],
  "desc": <string>
}
```

### Query Schema

```js
{
  "year": [start, end],  // inclusive
  "type": [t1, t2, ...],
  "date": [
    {"month": Number, "day": Number}, // start inclusive
    {"month": Number, "day": Number}, // end inclusive
  ]
}
```

[historic-events]: https://github.com/tuvalie/historic_events
