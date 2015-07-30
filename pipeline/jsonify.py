import sys
import csv
import json


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


def parse_row(row):
    if len(row) == 3:
        row.insert(1, "1")
    year, type_, date_info, text = row
    type_ = TYPE_INDEX[int(type_)]
    month = None
    day = None

    if date_info != 'circa':
        parts = date_info.split()
        month = MONTH_INDEX[parts[0]]
        if len(parts) == 2:
            day = int(parts[1])

    return {
        'date': {'year': int(year),
                 'month': month,
                 'day': day},
        'type': type_,
        'desc': text,
        }


def main():
    reader = csv.reader(
        sys.stdin,
        delimiter='\t',
        quoting=csv.QUOTE_NONE,
    )
    for item in reader:
        sys.stdout.write(json.dumps(parse_row(item)))
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()
