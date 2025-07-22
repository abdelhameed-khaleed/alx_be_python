from time import sleep


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        # display_menu()
        choice = input(
            "Enter your choice: add/remove/view/exit:").strip().lower()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item is not None and item != "":
                shopping_list.append(item)
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item:
                if item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print(f"Item '{item}' not found in the list.")
        elif choice == '3':
            for i in shopping_list:
                print(f"- {i} \n")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    sleep(1)


if __name__ == "__main__":
    main()
