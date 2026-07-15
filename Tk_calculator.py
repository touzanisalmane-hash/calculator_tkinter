import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")


def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(value))


def clear_display():
    display.delete(0, tk.END)


def calculate_result():
    expression = display.get()

    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Div by 0")

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "C":
        btn = tk.Button(
            window,
            text=text,
            font=("Arial", 18),
            command=clear_display
        )
    else:
        btn = tk.Button(
            window,
            text=text,
            font=("Arial", 18),
            command=lambda t=text: button_click(t)
        )

    btn.grid(row=row, column=col, sticky="nsew")

equals_button = tk.Button(
    window,
    text="=",
    font=("Arial", 18),
    bg="lightblue",
    command=calculate_result
)
equals_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()