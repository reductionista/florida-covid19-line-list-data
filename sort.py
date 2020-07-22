#!/usr/bin/env python3
#
# Sort Florida line list data available at (click Download → Spreadsheet):
# https://open-fdoh.hub.arcgis.com/datasets/florida-covid19-case-line-data
#
# Direct link: https://opendata.arcgis.com/datasets/37abda537d17458bae6677b8ab75fcb9_0.csv

import sys, csv

def sort(fname):
    arr = []
    first = True
    for l in csv.reader(open(fname)):
        if first:
            l[0] = l[0].replace('\ufeff', '')
            offset_objectid = l.index('ObjectId')
            first = False
        for (i, _) in enumerate(l):
            if l[i].endswith('+00'):
                l[i] = l[i][:-3]
        del(l[offset_objectid])
        arr.append(l)
    arr = sorted(arr)
    wr = csv.writer(sys.stdout, lineterminator='\n')
    for l in arr:
        wr.writerow(l)

def main():
    if len(sys.argv) < 2:
        raise Exception('Usage: sort.py <csvfile>')
    sort(sys.argv[1])

if __name__ == '__main__':
    main()
