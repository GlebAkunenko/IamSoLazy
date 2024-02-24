from parser import data
from notion import push_task
from prettytable import PrettyTable

table = PrettyTable(field_names=['Task name', 'Due'])
for due in data:
    for task in data[due]:
        table.add_row((task, due))

print("These tasks will be added to the notion table:")
print(table)

print("\n")
ans = input("Is data correct? (yes for continue) ")
if not ans.lower().strip().startswith('y'):
    exit(0)

for due in data:
    for task in data[due]:
        if push_task(task, due):
            print(f"Task {task} has been uploaded")

print("All is done")