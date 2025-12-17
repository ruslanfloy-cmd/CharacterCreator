import tkinter as tk
import Generator as gce
from tkinter import messagebox
from tkinter import *


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("CC GUI Demo")
    new_window.geometry("1280x720")

    create_menu(new_window)

def generateChar():
    character = gce.charGenerator()
    text = (
        f"Name: {character['name']}\n"
        f"Gender: {character['gender']}\n"
        f"Age: {character['age']}\n"
        f"Race: {character['race']}\n"
        f"Eyes: {character['eyes']}\n"
        f"Height: {character['height']}\n"
        f"Body: {character['body']}\n"
        f"Traits: {', '.join(character['traits'])}\n"
        f"Backstory: {character['backstory']}"
    )
    char_text.set(text)


def show_about():
    messagebox.showinfo("About", "This is a Tkinter Settings Menu Example.")

def set_theme(theme):
    print(f"Theme set to: {theme}")

def set_language(language):
    print(f"Language set to: {language}")

def create_menu(root_window):
    menubar = tk.Menu(root_window)
    root_window.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New...", command= open_new_window)
    file_menu.add_command(label="Open...", command=lambda: print("Option 2 selected"))
    file_menu.add_command(label="Save...", command=lambda: print("Option 3 selected"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root_window.destroy)

    settings_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Settings", menu=settings_menu)

    theme_menu = tk.Menu(settings_menu, tearoff=0)
    settings_menu.add_cascade(label="Theme", menu=theme_menu)

    theme_menu.add_command(label="Dark", command=lambda: set_theme("Dark"))
    theme_menu.add_command(label="Light", command=lambda: set_theme("Light"))

    language_menu = tk.Menu(settings_menu, tearoff=0)
    settings_menu.add_cascade(label="Language", menu=language_menu)

    language_menu.add_command(label="Russian", command=lambda: set_language("Russian"))
    language_menu.add_command(label="English", command=lambda: set_language("English"))

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)
    
    w = tk.Label(root, text='Character Creation')
    w.pack()
    button = tk.Button(root, text='Generate a Character!', width=25, command= generateChar)
    label = tk.Label(root, textvariable= char_text, justify="left")
    label.pack(pady=10)
    button.pack()

root = tk.Tk()
root.title("CC GUI Demo")
root.geometry("1280x720")
char_text = tk.StringVar(value="Click 'Generate' to create a character")
create_menu(root)

root.mainloop()
