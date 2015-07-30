import sys
import sqlite3
import json
from datetime import date


CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS history (
    id    INTEGER PRIMARY KEY,
    desc  TEXT,
    type  TEXT,
    year  INTEGER,
    month INTEGER,
    day   INTEGER
);
'''


def main():
    conn = sqlite3.connect('history.db')
    with conn:
        conn.execute(CREATE_TABLE)
        for index, line in enumerate(sys.stdin, 1):
            datum = json.loads(line)
            row = [
                index,
                datum['desc'],
                datum['type'],
                datum['date']['year'],
                datum['date']['month'],
                datum['date']['day'],
            ]
            conn.execute(
                'INSERT INTO history VALUES (?,?,?,?,?,?)',
                row
                )
        conn.commit()


if __name__ == '__main__':
    main()
