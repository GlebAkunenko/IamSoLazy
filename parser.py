import datetime as dt

with open('tasks.txt', 'r') as f:
    data = {}
    current_due = None
    for line in f.readlines():
        if line.isspace(): continue
        if line.startswith("!"):
            due = dt.datetime.fromisoformat(line[1:].strip())
            data[due] = []
            current_due = due
        else:
            data[current_due].append(line.strip())
