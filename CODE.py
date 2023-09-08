import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get("1.0", tk.END))
            screen.delete("1.0", tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            screen.delete("1.0", tk.END)
            screen.insert(tk.END, "Error")

    elif text == "C":
        screen.delete("1.0", tk.END)

    else:
        screen.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.geometry("400x500")
root.title("Simple Calculator")

# Create the display screen
screen = tk.Text(root, font=("Helvetica", 20), height=1)
screen.pack(fill=tk.BOTH, expand=True)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 20), height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
