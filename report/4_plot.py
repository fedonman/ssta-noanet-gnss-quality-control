#!/usr/bin/env python
import glob
import math
import matplotlib.pyplot as plt
import datetime as dt

def convert_snr(r):
    SNR = [(),(25, 26), (26, 28), (28, 32), (32, 36), (36, 39), (39, 42), (42, 45), (45, 48), ()]
    b = math.floor(r)
    if b == 0:
        return 25
    elif b == 9:
        return 49
    else: 
        return SNR[b][0] + ((SNR[b][1] - SNR[b][0]) * (r - b))

input_directory = "reports/"
output_direcory = "plots/"

years = ["08", "09", "10", "11", "12", "13", "14", "15", "16", "17"]
reports = []

for i in years:
    for r in sorted(glob.glob(input_directory + "*" + i + "S")):
        reports.append(r)

M1 = []
M2 = []
S1 = []
S2 = []

base = dt.date(2008, 6, 17)
dates = [base + dt.timedelta(days=x) for x in range(0, len(reports))]

for report in reports:
    with open(report, encoding='utf-8') as f:
        for line in f:
            if line.startswith('Moving average MP12'):
                splitted = line.split(':')
                M1.append(float(splitted[1].replace('m', '').strip()))
                continue
            if line.startswith('Moving average MP21'):
                splitted = line.split(':')
                M2.append(float(splitted[1].replace('m', '').strip()))
                continue
            if line.startswith('Mean S1'):
                splitted = line.split(':')
                S1.append(convert_snr(float(splitted[1].strip().split(' ')[0].strip())))
                continue
            if line.startswith('Mean S2'):
                splitted = line.split(':')
                S2.append(convert_snr(float(splitted[1].strip().split(' ')[0].strip())))
                continue

fig, ax = plt.subplots()
plt.xlabel('Time (year)')
plt.ylabel('Multipath (m)')
ax.plot(dates, M1, 'r+', label='MP1 KLOK')
ax.plot(dates, M2, 'gx', label='MP2 KLOK')
legend = ax.legend(loc='upper right', numpoints=1)
plt.show()

fig, ax = plt.subplots()
plt.xlabel('Time (year)')
plt.ylabel('Mean SNR (dBHz)')
ax.plot(dates, S1, 'r+', label='SN1 KLOK')
ax.plot(dates, S2, 'gx', label='SN2 KLOK')
legend = ax.legend(loc='upper right', numpoints=1)
plt.show()
