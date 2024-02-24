from parser import data
from notion import push_task


for due in data:
    for task in data[due]:
        push_task(task, due)
        # print(task, due)

for due in data:
    for task in data[due]:
        push_task(task, due)
        # print(task, due)