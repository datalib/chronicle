# HQuery

A REST API for fetching historical data, based on the
large, Wikipedia-sourced [historic-events] dataset,
made with the Flask framework.

### Endpoints

| Endpoint   | Method | Description |
|-----------:|:------:|:------------|
| `/v/query` |**POST**| Given a posted JSON query, respond with an array of events. |
| `/v/<id>`  |**GET** | Return the row that matches the **id**. |
| `/v/`      |**GET** | Return the (static?) index page. |


### Schema

Let `<date>` be an Object of:

    {
      "year":  <int>,
      "month": [<int> | null],
      "day":   [<int> | null]
    }

The `month` and `day` keys can be null because some
events have unknown dates; then we can define the
**Event Schema**, which is the schema for each event
object returned.

    {
      "type": ["general" | "birth" | "death"],
      "desc": <string>,
      "date": <date>
    }

The **Query Schema**:

    {
      "type": [<string>...],
      "desc": <regex>,
      "start": <date>,
      "end": <date>
    }

[historic-events]: https://github.com/tuvalie/historic_events
