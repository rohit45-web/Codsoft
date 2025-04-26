import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(password_length_entry.get())
        
        
        if length < 1:
            raise ValueError("Password length must be at least 1 character.")
        
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for i in range(length))
       
        password_display.config(text=password)
    
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

def copy_to_clipboard():
    password = password_display.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("460x400") 
root.resizable(False, False)  
root.configure(background='silver') 

title_label = tk.Label(root, text="Password Generator", font=("Algerian", 20, "bold"), fg="#2b2b2b", bg="silver")
title_label.place(x=80, y=20)

instructions_label = tk.Label(root, text="Enter the desired password length:", font=("Calibri", 16, "bold"), fg="#555", bg="silver")
instructions_label.place(x=90, y=80)

password_length_entry = tk.Entry(root, font=("Calibri", 16, "bold"), width=10, justify="center", bd=2, relief="solid")
password_length_entry.place(x=165, y=120)

generate_button = tk.Button(root, text="Generate Password", font=("Calibri", 16, "bold"), bg="darkgreen", fg="white", activebackground="#45a045", activeforeground="white", bd=0, padx=10, pady=5, command=generate_password)
generate_button.place(x=130, y=170)

password_display = tk.Label(root, text="", font=("Calibri", 16, "bold"), fg="purple", bg="silver", wraplength=400, anchor="center")
password_display.place(x=30, y=220, width=390)


copy_button = tk.Button(root, text="Copy to Clipboard", font=("Calibri", 16, "bold"), bg="navy", fg="white", activebackground="#1e88e5", activeforeground="white", bd=0, padx=10, pady=5, command=copy_to_clipboard)
copy_button.place(x=140, y=280)

root.mainloop()