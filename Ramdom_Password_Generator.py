import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Variables for GUI elements
        self.length_var = tk.IntVar(value=12)
        self.use_letters_var = tk.BooleanVar(value=True)
        self.use_numbers_var = tk.BooleanVar(value=True)
        self.use_symbols_var = tk.BooleanVar(value=True)

        # Advanced: Exclude similar characters (e.g., 'I', 'l', '1', 'O', '0')
        self.exclude_similar_var = tk.BooleanVar(value=True)

        # Create GUI elements
        ttk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(root, textvariable=self.length_var, width=5).grid(row=0, column=1, padx=10, pady=10)

        ttk.Checkbutton(root, text="Include Letters", variable=self.use_letters_var).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Checkbutton(root, text="Include Numbers", variable=self.use_numbers_var).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Checkbutton(root, text="Include Symbols", variable=self.use_symbols_var).grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        # Advanced: Checkbox to exclude similar characters
        ttk.Checkbutton(root, text="Exclude Similar Characters", variable=self.exclude_similar_var).grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        ttk.Button(root, text="Generate Password", command=self.generate_password).grid(row=5, column=0, columnspan=2, pady=10)

        # Display generated password
        self.password_var = tk.StringVar()
        ttk.Label(root, text="Generated Password:").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(root, textvariable=self.password_var, state="readonly", width=30).grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        # Clipboard button
        ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        use_letters = self.use_letters_var.get()
        use_numbers = self.use_numbers_var.get()
        use_symbols = self.use_symbols_var.get()
        exclude_similar = self.exclude_similar_var.get()

        if not (use_letters or use_numbers or use_symbols):
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        # Advanced: Exclude similar characters
        if exclude_similar:
            chars_to_exclude = 'Il1O0'
        else:
            chars_to_exclude = ''

        characters = self.get_valid_characters(use_letters, use_numbers, use_symbols, chars_to_exclude)

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def get_valid_characters(self, use_letters, use_numbers, use_symbols, chars_to_exclude):
        all_characters = ''

        if use_letters:
            all_characters += string.ascii_letters
        if use_numbers:
            all_characters += string.digits
        if use_symbols:
            all_characters += string.punctuation

        # Remove excluded characters
        characters = ''.join(c for c in all_characters if c not in chars_to_exclude)

        return characters

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()


