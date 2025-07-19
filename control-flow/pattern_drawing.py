size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for i in range(1, int(size) + 1):
        print("*", end="")
    row += 1
    print("\n")


# for i in range(1, int(size) + 1):
#     for i in range(1, int(size) + 1):
#         print("*", end="")
#     print("\n")
