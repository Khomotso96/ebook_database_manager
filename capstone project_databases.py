import sqlite3

# create a connection to the database.
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# create the book table if it doesn't exist.
cursor.execute('''
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER
)
''')

# check if the book table is empty.
cursor.execute('SELECT COUNT(*) FROM book')
result = cursor.fetchone()
if result[0] == 0:
    # insert initial data into the table.
    cursor.executemany('''
    INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)
    ''', [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ])

    conn.commit()
    print("Initial books inserted successfully.")
else:
    print("Book table already contains data. Skipping initial insertion.")

# function to add a new book.
def add_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    qty = int(input("Enter quantity: "))
    cursor.execute('INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', (id, title, author, qty))
    conn.commit()
    print("Book added successfully!")

# function to update book information.
def update_book():
    id = int(input("Enter book ID to update: "))
    new_qty = int(input("Enter new quantity: "))
    cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (new_qty, id))
    conn.commit()
    print("Book information updated successfully!")

# function to delete a book.
def delete_book():
    id = int(input("Enter book ID to delete: "))
    cursor.execute('DELETE FROM book WHERE id = ?', (id,))
    conn.commit()
    print("Book deleted successfully!")

# function to search for a book.
def search_book():
    keyword = input("Enter title or author to search: ")
    cursor.execute('SELECT * FROM book WHERE title LIKE ? OR author LIKE ?', ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()
    if books:
        print("Search results:")
        for book in books:
            print(book)
    else:
        print("Book not found.")

# main program loop for the menu.
while True:
    print("\nBookstore Menu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_book()
    elif choice == '0':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# close the connection to the database.
conn.close()