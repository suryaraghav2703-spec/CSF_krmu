import tkinter as tk
from tkinter import messagebox

# ---------------------------
# Simple GUI Calculator 
# ---------------------------

# Function to handle button clicks
def on_button_click(value):
    current_text = display.get()

    # If "C" (Clear) is pressed
    if value == "C":
        display.delete(0, tk.END)

    # If "=" is pressed, evaluate the expression
    elif value == "=":
        try:
            expression = display.get()
            result = eval(expression)  # Evaluate the math expression
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            display.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression!")
            display.delete(0, tk.END)

    # If "DEL" (backspace) is pressed
    elif value == "DEL":
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(0, current_text[:-1])  # Remove last character

    # Otherwise, just add the clicked button value to the display
    else:
        display.insert(tk.END, value)


# ---------------------------
# Main Window Setup
# ---------------------------

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)  # Fix the window size

# ---------------------------
# Display (Entry widget)
# ---------------------------

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# ---------------------------
# Button Layout
# ---------------------------

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("DEL", 5, 1), ("**", 5, 2), ("=", 5, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(
        root,
        text=text,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda t=text: on_button_click(t)
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Optional: Make all rows/columns expand equally (for better look)
for i in range(6):  # 0–5 rows
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 0–3 columns
    root.grid_columnconfigure(j, weight=1)

# ---------------------------
# Start the main event loop
# ---------------------------
root.mainloop()
