import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox

class FileExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("File Explorer")
        self.geometry("600x400")

        # Create buttons
        self.open_file_button = tk.Button(self, text="Open File", command=self.open_file)
        self.open_file_button.pack(side=tk.TOP, fill=tk.X)

        self.open_directory_button = tk.Button(self, text="Open Directory", command=self.open_directory)
        self.open_directory_button.pack(side=tk.TOP, fill=tk.X)

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(side=tk.TOP, fill=tk.X)

        # Create a Listbox to display directory contents
        self.file_listbox = Listbox(self, selectmode=tk.SINGLE)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.file_listbox.yview)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Selected File", file_path)

    def open_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.list_directory_contents(directory_path)

    def list_directory_contents(self, directory_path):
        self.file_listbox.delete(0, tk.END)  # Clear the listbox
        try:
            for item in os.listdir(directory_path):
                self.file_listbox.insert(tk.END, item)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = FileExplorer()
    app.mainloop()
