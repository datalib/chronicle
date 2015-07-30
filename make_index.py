import sqlite3
import csv


MONTH_INDEX = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}
TYPE_INDEX = {
    1: 'general',
    2: 'birth',
    3: 'death',
}

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS history
(
    row   INTEGER PRIMARY KEY,
    year  INTEGER,
    type  SYMBOL,
    month INTEGER,
    day   INTEGER,
    text  TEXT
)
'''

INSERT_TEMPLATE = 'INSERT INTO history VALUES (?,?,?,?,?,?)'


def parse_row(row):
    print(row)
    if len(row) == 3:
        row.insert(1, "1")
    year, type_, date, text = row
    type_ = TYPE_INDEX[int(type_)]
    month = None
    day = None

    if date != 'circa':
        parts = date.split()
        month = MONTH_INDEX[parts[0]]
        if len(parts) == 2:
            day = int(parts[1])

    return [year, type_, month, day, text.decode('utf-8')]


def main():
    conn = sqlite3.connect('history.db')
    conn.execute(CREATE_TABLE)
    with conn:
        with open('historic_events/historic_events.tsv') as handle:
            reader = csv.reader(
                handle,
                delimiter='\t',
                quoting=csv.QUOTE_NONE,
                )
            for row_id, row in enumerate(reader, 1):
                conn.execute(
                    INSERT_TEMPLATE,
                    [row_id] + parse_row(row),
                    )
        conn.commit()

if __name__ == '__main__':
    main()
