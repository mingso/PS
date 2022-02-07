import sys
import datetime

m, d = map(int, sys.stdin.readline().split())

date = datetime.datetime(2007, m, d)
print(date.strftime("%a").upper())