words = input().split()
print_list = [word for word in words if len(word) % 2 == 0]

print("\n".join(print_list))
