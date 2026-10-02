# File_Operator

* **Author:** Drashti Vasani

---

## 📌 Project Description

Personal Journal Manager is a menu-driven Python application that allows users to add, view, search, and delete personal journal entries. Each entry is saved in a text file with the current date and time.

---

## ✨ Features

* **Add a New Entry:** Saves journal text with a timestamp.
* **View All Entries:** Displays all saved journal entries.
* **Search for an Entry:** Searches entries using a keyword or date.
* **Delete All Entries:** Deletes all entries after user confirmation.
* **Exit:** Terminates the program with a goodbye message.

---

## 🛠️ Technologies Used

* Python
* `os` module
* `datetime` module
* File Handling
* Object-Oriented Programming
* Exception Handling
* Conditional Statements and Loops

---

## 📂 Project Structure

```text

File_Operator/
│
├── File_Operator.py
├── journal.txt
├── file_operator.png
└── README.md

```

---

**Note:** The `journal.txt` file is created automatically when the first journal entry is saved.

---

## ▶️ How to Run

1. Install Python on your computer.
2. Save the program as `File_Operator.py`.
3. Open the project folder in VS Code.
4. Open the terminal and run:

```bash
python File_Operator.py
```

---

## 💻 Sample Output

### 1. Add a New Entry — Python

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
1
Enter your journal entry: python
Entry added successfully!
```

### 2. Add a New Entry — SQL

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
1
Enter your journal entry: sql
Entry added successfully!
```

### 3. View All Entries

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
2

Your Journal Entries:
------------------------------
[2026-10-01 20:47:12]
python

[2026-10-01 20:47:16]
sql
```

### 4. Search for an Entry

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
3
Enter a keyword or date to search: python

Matching Entries:
------------------------------
[2026-10-01 20:47:12]
python
```

### 5. Delete All Entries

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
4
Are you sure you want to delete all entries? (yes/no): yes
All journal entries have been deleted.
```

### 6. Exit Program

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
5
Thank you for using Personal Journal Manager. 
Goodbye!
```

---


## 📚 Concepts Used

* **Class and Object:** Uses the `JournalManager` class to organize journal operations.
* **Constructor:** Initializes the journal file path.
* **File Handling:** Uses append (`"a"`), read (`"r"`), and write (`"w"`) modes.
* **Date and Time:** Uses `datetime.now()` and `strftime()` to record timestamps.
* **OS Module:** Manages the file path and checks file existence.
* **Exception Handling:** Handles invalid input, missing files, permission errors, and file operation errors.
* **Loops and Conditions:** Uses `while`, `if`, `elif`, and `else` to control the menu.
* **String Methods:** Uses `strip()` and `lower()` for input processing and case-insensitive searching.

---

## 🎯 Learning Outcomes

* Understand Python file handling.
* Practice Object-Oriented Programming.
* Work with date and time.
* Implement keyword-based searching.
* Handle invalid inputs and file errors.
* Build a menu-driven console application.

---



## 📝 Conclusion

The Personal Journal Manager demonstrates how Python can be used to create a simple journal application with file storage, timestamps, search functionality, and deletion options.

---

                                                            ⭐ **Thank you** ⭐

---