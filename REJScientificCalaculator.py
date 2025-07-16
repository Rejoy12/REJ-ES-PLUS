import tkinter as tk
from tkinter import *
from tkinter import messagebox
from math import sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, log, sqrt, exp, pi, e, radians, degrees, factorial
import matplotlib.pyplot as plt
import numpy as np


root = Tk()
root.title("Rejoy ES Plus - Peak Innovation")
root.geometry("900x1200")
root.resizable(False, False)


expression = ""
input_text = StringVar()
theme_colors = {
    "bg": "#d0e8f2", 
    "button": "#ffffff",  
    "hover": "#b3d9ff",  
    "text": "#34558b", 
}
mode = "DEG"  


def button_click(item):
    """Handle button clicks to update the expression."""
    global expression
    expression += str(item)
    input_text.set(expression)

def button_clear():
    """Clear the input field."""
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    """Evaluate the current expression."""
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        history_listbox.insert(END, f"{expression} = {result}")
        expression = ""
    except Exception:
        input_text.set("Error")

def scientific_operation(op):
    """Perform scientific operations."""
    global expression, mode
    try:
        if not expression:
            input_text.set("Enter a value!")
            return
        value = eval(expression)
        if mode == "DEG":
            value = radians(value)
        if op == "sin":
            result = str(round(sin(value), 4))
        elif op == "cos":
            result = str(round(cos(value), 4))
        elif op == "tan":
            result = str(round(tan(value), 4))
        elif op == "sinh":
            result = str(round(sinh(value), 4))
        elif op == "cosh":
            result = str(round(cosh(value), 4))
        elif op == "tanh":
            result = str(round(tanh(value), 4))
        elif op == "sqrt":
            result = str(round(sqrt(value), 4))
        elif op == "log":
            result = str(round(log(value), 4))
        elif op == "fact":
            result = str(factorial(int(value)))
        input_text.set(result)
        history_listbox.insert(END, f"{op}({expression}) = {result}")
        expression = ""
    except Exception:
        input_text.set("Error")

def toggle_mode():
    """Switch between RAD and DEG modes."""
    global mode
    mode = "DEG" if mode == "RAD" else "RAD"
    mode_label.config(text=f"Mode: {mode}")

def clear_history():
    """Clear the history."""
    history_listbox.delete(0, END)

def plot_graph():
    """Plot the graph based on the given expression."""
    global expression
    try:
        
        x = np.linspace(-10, 10, 400)
        y = eval(expression.replace("x", "x"))
        plt.plot(x, y, label=f"y = {expression}")
        plt.title("Graph Plotting")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.grid()
        plt.legend()
        plt.show()
    except Exception:
        input_text.set("Error! Use 'x' in your equation.")

def about_app():
    """Show information about the app."""
    messagebox.showinfo("About", "Rejoy ES Plus - Developed by Rejoy.\nAdvanced scientific calculator with enhanced features.")


def apply_hover_effect(btn, color_on_hover, original_color):
    """Add hover effect to buttons."""
    btn.bind("<Enter>", lambda e: btn.config(bg=color_on_hover))
    btn.bind("<Leave>", lambda e: btn.config(bg=original_color))


menu_bar = Menu(root)
root.config(menu=menu_bar)


mode_menu = Menu(menu_bar, tearoff=0)
mode_menu.add_command(label="Toggle Mode (RAD/DEG)", command=toggle_mode)
menu_bar.add_cascade(label="Mode", menu=mode_menu)

history_menu = Menu(menu_bar, tearoff=0)
history_menu.add_command(label="Clear History", command=clear_history)
menu_bar.add_cascade(label="History", menu=history_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_app)
menu_bar.add_cascade(label="Help", menu=help_menu)


header_frame = Frame(root, bg=theme_colors["bg"])
header_frame.pack(fill=X)
header_label = Label(header_frame, text="Rejoy ES Plus", font=("Arial", 30, "bold"), bg=theme_colors["bg"], fg=theme_colors["text"])
header_label.pack(pady=10)


mode_label = Label(header_frame, text=f"Mode: {mode}", font=("Arial", 14), bg=theme_colors["bg"], fg=theme_colors["text"])
mode_label.pack()


input_frame = Frame(root, bg=theme_colors["bg"])
input_frame.pack(pady=10)
input_field = Entry(input_frame, textvariable=input_text, font=("Arial", 24), justify="right", bd=5, bg="#ffffff", fg=theme_colors["text"])
input_field.pack(ipady=10)


history_frame = Frame(root, bg=theme_colors["bg"])
history_frame.pack()
history_listbox = Listbox(history_frame, width=50, height=5, font=("Arial", 12), bg="#ffffff", fg=theme_colors["text"])
history_listbox.pack(pady=10)


scientific_frame = Frame(root, bg=theme_colors["bg"])
scientific_frame.pack(pady=10)

scientific_buttons = [
    ("sin", 0, 0), ("cos", 0, 1), ("tan", 0, 2), ("sinh", 0, 3),
    ("cosh", 1, 0), ("tanh", 1, 1), ("sqrt", 1, 2), ("log", 1, 3),
    ("Clear", 2, 0), ("Plot", 2, 1), ("Fact", 2, 2), ("=", 2, 3),
]

for text, row, col in scientific_buttons:
    btn = Button(
        scientific_frame, text=text, font=("Arial", 14), width=8, height=2,
        bg=theme_colors["button"], fg="black",
        command=lambda x=text: scientific_operation(x) if x != "Clear" and x != "=" and x != "Plot" and x != "Fact" else button_clear() if x == "Clear" else plot_graph() if x == "Plot" else scientific_operation("fact") if x == "Fact" else button_equal()
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    apply_hover_effect(btn, theme_colors["hover"], theme_colors["button"])


num_pad_frame = Frame(root, bg=theme_colors["bg"])
num_pad_frame.pack(pady=10)

num_buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 2), ("(", 3, 3)
]

for text, row, col in num_buttons:
    btn = Button(
        num_pad_frame, text=text, font=("Arial", 14), width=8, height=2,
        bg=theme_colors["button"], fg="black",
        command=lambda x=text: button_click(x)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    apply_hover_effect(btn, theme_colors["hover"], theme_colors["button"])

root.mainloop()
