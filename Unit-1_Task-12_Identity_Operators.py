list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(f"list_a is list_b: {list_a is list_b}")          # True
print(f"list_a is list_c: {list_a is list_c}")          # False
print(f"list_a is not list_c: {list_a is not list_c}")  # True
print(f"list_a is not list_b: {list_a is not list_b}")  # False