import tkinter as tk
from tkinter import messagebox

# Store books
books = []

# Add book
def add_book():
    name = book_name.get()
    if name == "":
        messagebox.showerror("Error", "Enter book name")
    else:
        books.append({"name": name, "issued": False})
        messagebox.showinfo("Success", "Book Added Successfully")
        book_name.delete(0, tk.END)

# View books
def view_books():
    listbox.delete(0, tk.END)
    for book in books:
        status = "Issued" if book["issued"] else "Available"
        listbox.insert(tk.END, f"{book['name']} - {status}")

# Issue book
def issue_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a book")
        return

    index = selected[0]
    if books[index]["issued"]:
        messagebox.showerror("Error", "Already Issued")
    else:
        books[index]["issued"] = True
        messagebox.showinfo("Success", "Book Issued")

# Return book
def return_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a book")
        return

    index = selected[0]
    books[index]["issued"] = False
    messagebox.showinfo("Success", "Book Returned")

# Main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("500x500")
root.config(bg="#2c3e50")

# Title
title = tk.Label(root, text="Library Management System",
                 font=("Arial", 18, "bold"),
                 bg="#2c3e50", fg="white")
title.pack(pady=10)

# Entry
book_name = tk.Entry(root, font=("Arial", 12), width=30)
book_name.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack()

tk.Button(btn_frame, text="Add Book", width=12, bg="#27ae60", fg="white",
          command=add_book).grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="View Books", width=12, bg="#2980b9", fg="white",
          command=view_books).grid(row=0, column=1, padx=5, pady=5)

tk.Button(btn_frame, text="Issue Book", width=12, bg="#f39c12", fg="white",
          command=issue_book).grid(row=1, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Return Book", width=12, bg="#c0392b", fg="white",
          command=return_book).grid(row=1, column=1, padx=5, pady=5)

# Listbox
listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 11))
listbox.pack(pady=20)

# Run app
root.mainloop()
