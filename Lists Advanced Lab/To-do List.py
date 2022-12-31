numbers_list = []
task_list = []
print_list = []
while True:
    current_input = str(input())
    if current_input == "End":
        break
    current_input = current_input.split("-")
    numbers_list.append(int(current_input.pop(0)))
    task_list.append(current_input.pop())

for i in range(0, max(numbers_list)):
    print_list.append("")

for i in range(0, len(numbers_list)):
    current_index = numbers_list[i] - 1
    current_task = task_list[i]
    print_list[current_index] = current_task

while '' in print_list:
    print_list.remove('')

print(print_list)
