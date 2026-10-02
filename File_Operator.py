
import os
from datetime import datetime
class JournalManager:

    def __init__(self):
        self.filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "journal.txt"
        )

    # 1. Add a new journal entry
    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{date_time}]\n{entry}\n\n")

            print("Entry added successfully!")

        except OSError as e:
            print("Error: Unable to write to the journal file.", e)

    # 2. View all journal entries
    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read().strip()

            if data:
                print("\nYour Journal Entries:")
                print("------------------------------")
                print(data)
            else:
                print("No journal entries found. Start by adding a new entry!")

        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")

        except PermissionError:
            print("Error: Permission denied!")

    # 3. Search for an entry
    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ")

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read().strip()

            entries = data.split("\n\n") if data else []
            found = False

            for entry in entries:
                if keyword.lower() in entry.lower():
                    if not found:
                        print("\nMatching Entries:")
                        print("------------------------------")

                    print(entry)
                    found = True

            if not found:
                print(f"No entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied!")

    # 4. Delete all entries
    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        confirm = input(
            "Are you sure you want to delete all entries? (yes/no): "
        )

        if confirm.strip().lower() == "yes":
            try:
                with open(self.filename, "w", encoding="utf-8") as file:
                    file.write("")

                print("All journal entries have been deleted.")

            except OSError as e:
                print("Error: Unable to delete entries.", e)

        else:
            print("Deletion cancelled.")

    # 5. Exit program
    def exit_program(self):
        print("Thank you for using Personal Journal Manager. Goodbye!")
        raise SystemExit


# Main Program
journal = JournalManager()

while True:
    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    print("\nUser Input:")

    try:
        choice = int(input())

        if choice == 1:
            journal.add_entry()

        elif choice == 2:
            journal.view_entries()

        elif choice == 3:
            journal.search_entry()

        elif choice == 4:
            journal.delete_entries()

        elif choice == 5:
            journal.exit_program()

        else:
            print("Invalid option. Please select a valid option from the menu.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    except Exception as e:
        print("Error:", e)