import json
from colorama import Fore, Style, init
init(autoreset=True)
import time

print(Fore.MAGENTA + Style.BRIGHT + "\n🎉Welcome To Personal Library Manager!")

library = []    # Empty List to store books

# 1. Function to add a book
def add_book():
    title = input("\nEnter the book title: ").strip()
    author = input("Enter the author name: ").strip()
    
    # Handle year input errors
    while True:
        try:
            year = int(input("Enter the year of publication: "))
            if year <= 0:
                print("❌ Invalid input! Please enter a positive year greater than 0.")
                continue
            break   # When valid input entered, it will exit the loop
        except ValueError:
            print("❌ Invalid input! Please enter a valid year (numbers only).")

    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'

    # Check for duplicates (same title,, author, and year)
    for book in library:
        if (book['title'].lower() == title.lower() and book['author'].lower() == author.lower() and book['year'] == year):
            print("\n❌ This book already exists in your library.")
            return

   
    library.append({
        "title"           : title,
        "author"          : author,
        "year"            : year,
        "genre"           : genre,
        "read"            : read_status
    })
    print("\n✅ Book Added Successfully!")

# 2. Function to display all books
def display_books():
    if not library:
        print("\n❗ Your Library is empty.")
    else:
        print(f"\n📖 Available Book Details:")
        for index, book in enumerate(library, 1):
            print(Fore.GREEN + f"\n📘 Book {index}:")
            print(Fore.LIGHTWHITE_EX + f"""
Title           : {book['title']}, 
Author          : {book['author']}, 
Genre           : {book['genre']}, 
Year            : {book['year']},
Read Status     : {'📖 Read' if book['read'] else '⏳ Unread'}
""")

# 3. Function to search for a book
def search_book():
    query = input("\nEnter the book title, author or genre to search: ").strip().lower()
    found_books = [
        book for book in library 
        if query in book['title'].lower() 
        or query in book['author'].lower() 
        or query in book['genre'].lower()
        ]

    if found_books:
        print(f"\n🔍 Search Results: ")
        for book in found_books:
            print(f"""
Title: {book['title']},
Author: {book['author']},
Year: {book["year"]},
Genre: {book['genre']},
Read Status: {'Read' if book["read"] else 'Unread'}
""")
    else:
        print(f"\n❌ No books found matching '{query}'.")

# 4. Function to remove a book
def remove_book():
    title = input("\nEnter the book title to remove: ").strip()

    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"\n✅'{title}' has been removed from your library.")
            return
    print(f"\n❌ Book '{title}' not found in your library.")

# 5. Function to display library statistics
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("\n📊 Library Statistics: \nTotal books: 0\nPercentage Read: 0%")
        return
    
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100

    print(f"\n📊 Library Statistics: \nTotal Books: {total_books}\nPercentage Read: {percentage_read: .2f}%")


# Function to save library to a file
def save_library():
    print(Fore.YELLOW + "\nSaving Your Library...", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    with open("library.json", "w") as file:
        json.dump(library, file)
    print(Fore.GREEN + "\n💾 Library saved successfully!")

# Function to load library data from a file
def load_library():
    global library
    try:
        with open("library.json", "r") as file:
            library = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        library = []

# Load library data before running the menu
load_library()


# Function to show menu and handle user input
def menu():
    while True:
        print(Fore.YELLOW + Style.BRIGHT + "\n📚 Library Menu:" + Style.RESET_ALL)
        print(Fore.CYAN + "1. ➕ Add a Book" + Style.RESET_ALL)
        print(Fore.CYAN + "2. 💻 Display All Books" + Style.RESET_ALL)
        print(Fore.CYAN + "3. 🔍 Search for a Book" + Style.RESET_ALL)
        print(Fore.CYAN + "4. ❌ Remove a Book" + Style.RESET_ALL)
        print(Fore.CYAN + "5. 📊 Display Statistics" + Style.RESET_ALL)  
        print(Fore.CYAN + "6. 🚪 Exit" + Style.RESET_ALL)

        choice = input(Fore.LIGHTGREEN_EX + "Enter your choice (1-2-3...): " + Style.RESET_ALL)

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library() 
            print(Fore.CYAN + "\n📖 Thankyou for using the personal library manager!")
            print(Fore.MAGENTA + "✨ Have a great day!")
            break
        else:
            print("\n❌ Invalid choice! Please try again.\n")
        
# Run Menu
menu()

