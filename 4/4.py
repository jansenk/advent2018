import re
t = '[1518-02-06 23:52] Guard #3109 begins shift'
et = '\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] (?P<message>.*)'
bt = 'Guard \#(?P<id>\d*?) begins shift'


class GuardEntry:
    def __init__(self, line):
        self.line = line
        entrymatch = re.match(et, line)
        entrydict = entrymatch.groupdict()
        self.year = int(entrydict["year"])
        self.month = int(entrydict["month"])
        self.day = int(entrydict["day"])
        self.hour = int(entrydict["hour"])
        self.minute = int(entrydict["minute"])
        self.guardEvent = False
        self.sleepEvent = False
        self.wakeEvent = False
        message = entrydict["message"]
        if message.find("Guard") != -1:
            self.guardEvent = True
            guardMatch = re.search(bt, message)
            self.guardId = int(guardMatch.group("id"))
        elif message.find("asleep") != -1:
            self.sleepEvent = True
        elif message.find("wakes") != -1:
            self.wakeEvent = True
        else:
            raise Exception("I've discovered a message I can't parse: %s" % message)

    def __lt__(self, other):
        if self.year < other.year:
            return True
        if self.month < other.month:
            return True
        if self.day < other.day:
            return True
        if self.hour < other.hour:
            return True
        if self.minute < other.minute:
            return True
        return False


entries = [GuardEntry(l.strip()) for l in open("test.txt", "r")]
entries = sorted(entries)

for entry in entries:
    print(entry.line)

