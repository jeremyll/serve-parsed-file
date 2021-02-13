import csv
from itertools import groupby
from statistics import median


Header = str
FieldValue = str
MainRow = dict[Header, FieldValue]
MainRows = list[MainRow]

Average = float
Median = float
TotalSpend = float
Party = str
PartyStats = dict[Party, tuple[Average, Median, TotalSpend]]


def parse_file(path: str) -> MainRows:
    with open(path) as f:
        return list(csv.DictReader(f))


def make_groupings(rows: MainRows) -> PartyStats:
    stats = {}
    groups = groupby(rows, lambda x: x['Party'])
    for party, rows in groups:
        spend = [(int(r['Twitter Spend']) + int(r['Facebook Spend'])) for r in rows]
        totalSpend = sum(spend)
        averageSpend = totalSpend / len(spend)
        medianSpend = median(spend)
        stats[party] = (averageSpend, medianSpend, totalSpend)
    return stats

