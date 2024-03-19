#TASK 3 - Password Generator
import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("350x480")
        self.init_widgets()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

    def init_widgets(self):
        self.header_frame = tk.Frame(self.root, bg="#FF4331", pady=20)
        self.header_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.header_frame, text="Password Generator", font=("Roboto", 20, "bold"), bg="#FF4331", fg="white")
        self.title_label.pack(side=tk.TOP, padx=(20, 0))

        self.password_entry = tk.Entry(self.root, font=("Roboto", 20), bg="#444444", fg="white", bd=0)
        self.password_entry.pack(fill=tk.X, padx=20, pady=(20, 7), ipady=10)

        self.generate_button = tk.Button(self.root, text="Generate Password", font=("Nunito", 14, "bold"), bg="#222222", fg="white", bd=0, 
                                         command=self.generate_password)
        self.generate_button.pack(fill=tk.X, padx=20, pady=7)

        self.options_frame = tk.Frame(self.root, bg="#FF4331")
        self.options_frame.pack(fill=tk.X, padx=20)

        self.length_label = tk.Label(self.options_frame, text="Password Length", font=("Roboto", 14,"bold"), bg="#FF4331", fg="white")
        self.length_label.grid(row=0, column=0, padx=(5, 20))

        self.length_scale = tk.Scale(self.options_frame, from_=1, to=30, orient=tk.HORIZONTAL, bg="#FF4331", fg="white", bd=0, 
                                     highlightthickness=0,font=("Roboto", 10,"bold"))
        self.length_scale.set(8)
        self.length_scale.grid(row=0, column=1,pady=(5,20))

        self.uppercase_var = tk.IntVar()
        self.uppercase_check = tk.Checkbutton(self.options_frame, text="Include Uppercase", font=("Nunito", 14,"bold"), bg="#FF4331", 
                                              variable=self.uppercase_var)
        self.uppercase_check.grid(row=1, column=0, columnspan=2, pady=(10, 0))

        self.lowercase_var = tk.IntVar()
        self.lowercase_check = tk.Checkbutton(self.options_frame, text="Include Lowercase", font=("Nunito", 14,"bold"), bg="#FF4331", 
                                              variable=self.lowercase_var)
        self.lowercase_check.grid(row=2, column=0, columnspan=2)

        self.number_var = tk.IntVar()
        self.number_check = tk.Checkbutton(self.options_frame, text="Include Numbers", font=("Nunito", 14,"bold"), bg="#FF4331", 
                                           variable=self.number_var)
        self.number_check.grid(row=3, column=0, columnspan=2)

        self.symbol_var = tk.IntVar()
        self.symbol_check = tk.Checkbutton(self.options_frame, text="Include Symbols", font=("Nunito", 14,"bold"), bg="#FF4331", 
                                           variable=self.symbol_var)
        self.symbol_check.grid(row=4, column=0, columnspan=2)

        self.copy_button = tk.Button(self.root, text="Copy Password", font=("Nunito", 14, "bold"), bg="#222222", fg="white", bd=0, 
                                     command=self.copy_password)
        self.copy_button.pack(fill=tk.X, padx=20, pady=10)

    def generate_password(self):
        length = self.length_scale.get()
        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_numbers = self.number_var.get()
        include_symbols = self.symbol_var.get()

        chars = ''
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_lowercase:
            chars += string.ascii_lowercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += "!@#$%^&*=-_"
        if not chars:
            messagebox.showerror("Error", "Please select at least one option.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "Please generate a password first.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Success", "Password has been copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
