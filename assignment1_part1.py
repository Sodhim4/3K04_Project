from tkinter import *
import random
import time
import tkinter as tk
from random import randrange
import functools
from tkinter import messagebox

def open_new_user_page():
    def submit():
        username = username_entry.get()
        password = password_entry.get()
        # Add code to validate the username and password here

    new_user_window = Toplevel(window)
    new_user_window.title("New User Login Page")
    new_user_window.geometry("800x600")
    new_user_window.configure(bg="white")
    
    # Add widgets and content for the New User Login Page here
    username_label = Label(new_user_window, text="Name:", font=("Arial", 16))
    username_label.pack(pady=10)
    
    username_entry = Entry(new_user_window, font=("Arial", 16))
    username_entry.pack(pady=5)
    
    password_label = Label(new_user_window, text="Password:", font=("Arial", 16))
    password_label.pack(pady=10)
    
    password_entry = Entry(new_user_window, show="*", font=("Arial", 16))
    password_entry.pack(pady=5)

    enter_button = Button(new_user_window, text="Enter", bg="green", fg="white", font=("Arial bold", 16), command=submit)
    enter_button.pack(pady=10)

def open_existing_user_page():
    def submit():
        username = username_entry.get()
        password = password_entry.get()
        # Add code to validate the username and password here

    existing_user_window = Toplevel(window)
    existing_user_window.title("Existing User Login Page")
    existing_user_window.geometry("800x600")
    existing_user_window.configure(bg="white")
    
    # Add widgets and content for the Existing User Login Page here
    username_label = Label(existing_user_window, text="Name:", font=("Arial", 16))
    username_label.pack(pady=10)
    
    username_entry = Entry(existing_user_window, font=("Arial", 16))
    username_entry.pack(pady=5)
    
    password_label = Label(existing_user_window, text="Password:", font=("Arial", 16))
    password_label.pack(pady=10)
    
    password_entry = Entry(existing_user_window, show="*", font=("Arial", 16))
    password_entry.pack(pady=5)

    enter_button = Button(existing_user_window, text="Enter", bg="green", fg="white", font=("Arial bold", 16), command=submit)
    enter_button.pack(pady=10)

def win():
    frame = Toplevel(window)
    frame.title("Login For New User")
    frame.geometry("1920x1080")  # Fixed the geometry specification
    frame.configure(bg="black")

window = Tk()
window.title("Start Menu")
window.geometry("1280x1024")
window.configure(bg="gray")

# Add a welcome label with a larger font size and move it down
welcome_label = Label(window, text="Welcome to Pacemaker Project", bg="gray", fg="black", font=("Arial bold", 60))
welcome_label.pack(pady=50)
welcome_label.place(x=220, y=150)

# Make buttons smaller and center them at the bottom
button1 = Button(window, text="New User Login", bg="white", fg="black", font=("Arial bold", 30), command=open_new_user_page)
button1.place(x=750, y=400)

button2 = Button(window, text="Existing User Login", bg="white", fg="black", font=("Arial bold", 30), command=open_existing_user_page)
button2.place(x=705, y=525)

window.mainloop()
