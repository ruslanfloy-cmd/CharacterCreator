import tkinter as tk
import os 
import Generator as gce
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


SAVE_DIRECTORY = 'SavedCharacters/'


root = tk.Tk()
root.title("CC Randomizer")
root.geometry("1280x720")

char_vars = {
    "name": tk.StringVar(),
    "gender": tk.StringVar(),
    "age": tk.IntVar(),
    "race": tk.StringVar(),
    "eyes": tk.StringVar(),
    "hair": tk.StringVar(),
    "height": tk.StringVar(),
    "body": tk.StringVar(),
    "traits": tk.StringVar(),
    "backstory": tk.StringVar()
}

def generateChar():
    global character
    character = gce.charGenerator()
    load_character_into_editor(character)

gif_file = "teto-kasane-teto.gif"
gif_image = Image.open(gif_file)
frames = gif_image.n_frames
photo_frames = [ImageTk.PhotoImage(file=gif_file, format=f"gif -index {i}") for i in range(frames)]

photo_frames = [ImageTk.PhotoImage(gif_image.copy().convert("RGBA"))]
try:
    while True:
        gif_image.seek(len(photo_frames))
        photo_frames.append(ImageTk.PhotoImage(gif_image.copy().convert("RGBA")))
except EOFError:
    pass  # reached end of GIF

gif_label = tk.Label(root)
gif_label.place(x=30, y=10)  # top-left corner

def animate(frame=0):
    gif_label.config(image=photo_frames[frame])
    frame = (frame + 1) % len(photo_frames)
    root.after(120, lambda: animate(frame))
animate()


def load_character_into_editor(character):
    char_vars["name"].set(character["name"])
    char_vars["gender"].set(character["gender"])
    char_vars["age"].set(character["age"])
    char_vars["race"].set(character["race"])
    char_vars["eyes"].set(character["eyes"])
    char_vars["height"].set(character["height"])
    char_vars["body"].set(character["body"])
    char_vars["hair"].set(character["hair"])
    char_vars["traits"].set(", ".join(character["traits"]))

    text_widget = char_vars["backstory_widget"]
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, character["backstory"])

def update_character_from_gui():
    global character

    character = {
        "name": char_vars["name"].get(),
        "gender": char_vars["gender"].get(),
        "age": int(char_vars["age"].get()),
        "race": char_vars["race"].get(),
        "eyes": char_vars["eyes"].get(),
        "hair": char_vars["hair"].get(),
        "height": char_vars["height"].get(),
        "body": char_vars["body"].get(),
        "traits": [t.strip() for t in char_vars["traits"].get().split(",")],
        "backstory": char_vars["backstory_widget"].get("1.0", tk.END).strip()
    }


def export_character_txt(filename="character.txt"):
    update_character_from_gui()
    if character is None:
        messagebox.showwarning("Save", "No character generated yet!")
        return
    os.makedirs(SAVE_DIRECTORY, exist_ok=True)

    filename = f"{character['name']}.txt"
    path = os.path.join(SAVE_DIRECTORY, filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write(gce.character_to_text(character))

    messagebox.showinfo("Saved", f"Character saved to:\n{path}")

def open_character_txt():
    filepath = filedialog.askopenfilename(
        title="Open character file",
        filetypes=[("Text files", "*.txt")]
    )

    if not filepath:  # Cancel
        return
    

    load_character_from_txt(filepath)
def load_character_from_txt(path):
    global character

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    character = gce.character_from_text(text)
    print(character)  # <-- check the keys
    load_character_into_editor(character)

def show_about():
    messagebox.showinfo("About", "This is a character creator randomizer with fantsy stuff and all made by ruslanfloy-cmd on GitHub")

def set_theme(theme):
    print(f"Theme set to: {theme}")

def set_language(language):
    print(f"Language set to: {language}")

def create_character_editor(parent):
    row = 0
    backstory_widget = None  # separate variable

    for field, var in char_vars.items():
        tk.Label(parent, text=field.capitalize()).pack(anchor="w", padx=5, pady=2)

        if field == "backstory":
            backstory_widget = tk.Text(parent, height=4, width=40)
            backstory_widget.pack(padx=5, pady=2)
        else:
            tk.Entry(parent, textvariable=var, width=40).pack(padx=5, pady=2)

        row += 1

    char_vars["backstory_widget"] = backstory_widget

def create_menu(root_window):
    
    menubar = tk.Menu(root_window)
    root_window.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open...", command=open_character_txt)
    file_menu.add_command(label="Save...", command= export_character_txt)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root_window.destroy)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)
    
    w = tk.Label(root, text='Character Creation')
    w.pack()
    button = tk.Button(root, text='Generate a Character!', width=25, command= generateChar)
    create_character_editor(root)
    button.pack()
    gif_label = tk.Label(root, image="")
    gif_label.pack()

create_menu(root)

root.mainloop()
