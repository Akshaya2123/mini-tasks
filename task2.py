def print_name_pattern(name, choice):
    if choice == 1:
        # Right-angle triangle
        for i in range(1, len(name) + 1):
            print(name[:i])

    elif choice == 2:
        # Left-angle triangle
        for i in range(1, len(name) + 1):
            print(" " * (len(name) - i) + name[:i])

    elif choice == 3:
        # Pyramid
        for i in range(1, len(name) + 1):
            print(" " * (len(name) - i) + " ".join(name[:i]))

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")


# Input
name = input("Enter your name: ")

print("\nChoose a pattern:")
print("1. Right Angle")
print("2. Left Angle")
print("3. Pyramid")

choice = int(input("Enter your choice (1/2/3): "))

print("\nOutput:")
print_name_pattern(name, choice)