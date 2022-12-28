first_string = str(input())
second_string = str(input())

def index_of_the_first(first_string):
    return ord(first_string)

def index_of_the_second(second_string):
    return  ord(second_string)

print_list = []
for i in range(index_of_the_first(first_string) + 1, index_of_the_second(second_string)):
    print_list.append(chr(i))

index_of_the_first(first_string)
index_of_the_second(second_string)

print(" ".join(print_list))