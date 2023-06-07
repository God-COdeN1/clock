import csv
import modul

watch_ = 1
stopwatch_ = None
while True:
    if watch_ == 1:
        modul.stopwatch()
        modul.read_stopwatch_data()

