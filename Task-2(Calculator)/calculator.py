#Task 2 - Calculator App
import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("285x320")
        self.root.configure(bg="#7F00FF") 
        self.init_widgets()

    def init_widgets(self):
        self.display_var = tk.StringVar()
        self.display_var.set("")
        self.display_entry = tk.Entry(self.root, textvariable=self.display_var, font=("Roboto", 18,"bold"), bg="#FFF", 
                                      fg="#0C0C0C", bd=0, justify="right")
        self.display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            ("7", 1, 0, 1, 1), ("8", 1, 1, 1, 1), ("9", 1, 2, 1, 1), ("/", 1, 3, 1, 1),
            ("4", 2, 0, 1, 1), ("5", 2, 1, 1, 1), ("6", 2, 2, 1, 1), ("*", 2, 3, 1, 1),
            ("1", 3, 0, 1, 1), ("2", 3, 1, 1, 1), ("3", 3, 2, 1, 1), ("-", 3, 3, 1, 1),
            ("C", 4, 0, 1, 1), ("0", 4, 1, 1, 1), (".", 4, 2, 1, 1), ("+", 4, 3, 1, 1),
            ("=", 5, 0, 4, 4) 
        ]

        for (text, row, column, rowspan, columnspan) in buttons:
            if text == "=":
                button = tk.Button(self.root, text=text, font=("Roboto", 14), bg="#FF7C01", fg="#FFF", bd=0, 
                                   command=lambda t=text: self.on_button_click(t), height=1)
                button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5, sticky="nsew")
            elif text == "C": 
                button = tk.Button(self.root, text=text, font=("Roboto", 14), bg="#FF0000", fg="#FFF", bd=0, 
                                   command=lambda t=text: self.on_button_click(t))
                button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5, sticky="nsew")
            else:
                button = tk.Button(self.root, text=text, font=("Roboto", 14), bg="#FDFDFD", fg="#0C0C0C", bd=0,
                                    command=lambda t=text: self.on_button_click(t))
                button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5, sticky="nsew")

        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

    def on_button_click(self, text):
        current_display = self.display_var.get()

        if text == "C":
            self.display_var.set("")
            self.display_entry.config(fg="#0C0C0C") 
        elif text == "=":
            try:
                result = eval(current_display)
                self.display_var.set(result)
                self.display_entry.config(fg="#0C0C0C") 
            except SyntaxError:
                self.display_var.set("SYNTAX ERROR")
                self.display_entry.config(fg="red") 
        else:
            self.display_var.set(current_display + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
