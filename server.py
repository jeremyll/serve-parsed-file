from flask import Flask, request, render_template
from parsers import parse_file, make_groupings


FILE_PATH = 'Canadian Candidates Social Media Ad Spend.csv'


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    sort_by = request.args.get('sort_by', None)
    print(sort_by)

    rows = parse_file(FILE_PATH)
    headers = rows[0].keys()

    groupings = make_groupings(rows)

    return render_template(
        'table.html',
        rows=rows, headers=headers,
        groupings=groupings
    )

