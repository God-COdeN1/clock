import datetime
import os
import time
import csv
import keyboard
from colorama import init


def watch():
    while True:
        init()
        # if keyboard.is_pressed('c'):
        #     break
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        # os.system('cls' if os.name == 'nt' else 'clear')
        previous_data = []
        with open('cs/c.csv', 'r') as file:
            reader = csv.reader(file)
            previous_data = list(reader)
        if previous_data:
            previous_data[0] = [hour, minute]
        else:
            previous_data.append([hour, minute])
        with open('cs/c.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(previous_data)
        # print(f'Hours:{hour:02d} : minutes:{minute:02d}')
        # print("Hold c for disable")
        time.sleep(1)


def stopwatch():
    init()
    start_time = time.time()

    while True:
        if keyboard.is_pressed('s'):
            break
        now_time = time.time() - start_time
        hours = int(now_time // 86400)
        minutes = int(now_time // 60)
        seconds = int(now_time % 60)
        # os.system('cls' if os.name == 'nt' else 'clear')
        previous_data = []
        with open('cs/s.csv', 'r') as file:
            reader = csv.reader(file)
            previous_data = list(reader)
        if previous_data:
            previous_data[0] = [hours, minutes, seconds]
        else:
            previous_data.append([hours, minutes, seconds])
        with open('cs/s.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(previous_data)
        # print(f'Stopwatch: Hours:{hours:02d} : minutes:{minutes:02d} : seconds:{seconds:02d}')
        # print("Hold s for disable")
        time.sleep(1)
        if len(str(hours)) >= 24:
            return print("24 hours")

stopwatch()


with open('cs/s.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if 'a' in row:
            data = row['a']
            break

with open('file.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['A'] == '1':
            hours = int(row['B'])
            minutes = int(row['C'])
            seconds = 0
            break

if 'hours' in locals():
    print("Hour:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
