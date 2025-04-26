import tkinter as tk
from tkinter import messagebox

# Contact book class to manage contacts
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})

    def get_all_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]

    def update_contact(self, old_name, new_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact["name"] == old_name:
                contact["name"] = new_name
                contact["phone"] = new_phone
                contact["email"] = new_email
                contact["address"] = new_address
                return True
        return False

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact["name"] != name]


# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Input Error", "Name and phone number are required!")
        return

    contact_book.add_contact(name, phone, email, address)
    update_contact_list()
    clear_entries()

# Function to update the displayed contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contact_book.get_all_contacts():
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search contacts by name or phone
def search_contact():
    search_term = search_entry.get()
    if not search_term:
        messagebox.showwarning("Search Error", "Please enter a search term.")
        return

    results = contact_book.search_contact(search_term)
    contact_listbox.delete(0, tk.END)
    if results:
        for contact in results:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        contact_listbox.insert(tk.END, "No matching contacts found.")

# Function to delete a selected contact
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        contact_book.delete_contact(name)
        update_contact_list()

# Function to update a selected contact
def update_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if contact_book.update_contact(name, name, phone, email, address):
            update_contact_list()
            clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Update Error", "Failed to update contact.")

# Function to clear the input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x600")
root.config(bg="#f5f5f5")

# Create ContactBook object
contact_book = ContactBook()

# Title Label
title_label = tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"), fg="#333", bg="#f5f5f5")
title_label.pack(pady=20)

# Add Contact Section
add_contact_label = tk.Label(root, text="Add New Contact", font=("Arial", 14), fg="#333", bg="#f5f5f5")
add_contact_label.pack(pady=10)

name_label = tk.Label(root, text="Name:", font=("Arial", 12), fg="#333", bg="#f5f5f5")
name_label.pack()
name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

phone_label = tk.Label(root, text="Phone Number:", font=("Arial", 12), fg="#333", bg="#f5f5f5")
phone_label.pack()
phone_entry = tk.Entry(root, font=("Arial", 12), width=30)
phone_entry.pack(pady=5)

email_label = tk.Label(root, text="Email:", font=("Arial", 12), fg="#333", bg="#f5f5f5")
email_label.pack()
email_entry = tk.Entry(root, font=("Arial", 12), width=30)
email_entry.pack(pady=5)

address_label = tk.Label(root, text="Address:", font=("Arial", 12), fg="#333", bg="#f5f5f5")
address_label.pack()
address_entry = tk.Entry(root, font=("Arial", 12), width=30)
address_entry.pack(pady=5)

# Buttons for actions
add_button = tk.Button(root, text="Add Contact", font=("Arial", 12), bg="#4caf50", fg="white", activebackground="#45a045", command=add_contact)
add_button.pack(pady=10)

# Search Section
search_label = tk.Label(root, text="Search Contact (by Name or Phone):", font=("Arial", 12), fg="#333", bg="#f5f5f5")
search_label.pack(pady=10)
search_entry = tk.Entry(root, font=("Arial", 12), width=30)
search_entry.pack(pady=5)
search_button = tk.Button(root, text="Search", font=("Arial", 12), bg="#ff9800", fg="white", activebackground="#e67e22", command=search_contact)
search_button.pack(pady=10)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10, selectmode=tk.SINGLE)
contact_listbox.pack(pady=10)

# Buttons to update and delete contact
update_button = tk.Button(root, text="Update Contact", font=("Arial", 12), bg="#2196f3", fg="white", activebackground="#1976d2", command=update_contact)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", font=("Arial", 12), bg="#f44336", fg="white", activebackground="#e53935", command=delete_contact)
delete_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()