from datetime import datetime
from msvcrt import getch

class Stopwatch(object):
    def __init__(self):
        self.current = []
    def start(self):
        self.current.append(datetime.now())
    def lap(self):
        self.current.append(datetime.now())
    def stop(self):
        self.current.append(datetime.now())
        self.times = []
        for record in range(len(self.current) - 1):
            self.times.append(str(self.current[record + 1] - self.current[record]))
        self.times.append(str(self.current[-1] - self.current[0]))
        with open("python_hard_2_times.txt", "a+", encoding="utf-8") as file:
            for record in range(len(self.times)):
                if record == 0:
                    file.write("Started.\n")
                    print("Started.\n")
                elif record == len(self.times) - 1:
                    file.write("Stopped. Total time was " + self.times[record] + " seconds.\n")
                    print("Stopped. Total time was " + self.times[record] + " seconds.\n")
                else:
                    file.write("Lapped. Interval was " + self.times[record] + " seconds.\n")
                    print("Lapped. Interval was " + self.times[record] + " seconds.\n")
        self.current = []

def startwatch():
    stopwatch = Stopwatch()
    print("Please run in py.exe or cmd, not IDLE. If not, then use Ctrl+C to interrupt and do your own things.")
    print("Enter to start, l to lap and Space to stop.")
    while True:
        key = ord(getch())
        if key == 13:
            stopwatch.start()
        elif key == 108:
            stopwatch.lap()
        elif key == 32:
            stopwatch.stop()

if __name__ == "__main__":
    startwatch()
