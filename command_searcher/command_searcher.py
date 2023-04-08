import os
import tkinter as tk
from tkinter import filedialog
import re

import re

def search_files(directory, keywords):
    """
    Search for files containing the given keywords in the directory and its subdirectories.
    """
    colors = ["white", "gray"]
    color_index = 0
    results.delete(0, tk.END)
    keyword_list = [k.strip() for k in keywords.split(",")] # Split keywords by comma and strip whitespace
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".txt"):
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f.readlines():
                        for keyword in keyword_list:
                            if keyword.startswith("/") and keyword.endswith("/"): # Check if keyword is a regex pattern
                                pattern = keyword[1:-1] # Remove the leading and trailing slashes
                                if re.search(pattern, line, re.IGNORECASE):
                                    # Split the filepath and line and insert them as separate lines in the Listbox
                                    filepath_line = f"{filepath}\n"
                                    line = f"{line}"
                                    results.insert(tk.END, filepath_line)
                                    results.itemconfig(tk.END, bg=colors[color_index % len(colors)])
                                    results.insert(tk.END, line)
                                    results.itemconfig(tk.END, bg=colors[color_index % len(colors)])
                                    color_index += 1
                            else: # Otherwise, do a regular keyword search
                                if keyword.lower() in line.lower():
                                    # Split the filepath and line and insert them as separate lines in the Listbox
                                    filepath_line = f"{filepath}\n"
                                    line = f"{line}"
                                    results.insert(tk.END, filepath_line)
                                    results.itemconfig(tk.END, bg=colors[color_index % len(colors)])
                                    results.insert(tk.END, line)
                                    results.itemconfig(tk.END, bg=colors[color_index % len(colors)])
                                    color_index += 1

def browse_directory():
    """
    Open a file dialog to select a directory to search.
    """
    global directory_entry
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def search():
    """
    Perform a search for the given keyword in the selected directory.
    """
    directory = directory_entry.get()
    keyword = keyword_entry.get()
    search_files(directory, keyword)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Text File Search")

    # Directory selection
    directory_label = tk.Label(root, text="Directory:", font=("Arial", 16))
    directory_label.pack()
    directory_entry = tk.Entry(root, font=("Arial", 14))
    directory_entry.pack(fill=tk.X, padx=10, pady=10, expand=True)
    browse_button = tk.Button(root, text="Browse...", font=("Arial", 14), command=browse_directory)
    browse_button.pack(padx=10, pady=10)

    # Keyword input
    keyword_label = tk.Label(root, text="Keyword:", font=("Arial", 16))
    keyword_label.pack()
    keyword_entry = tk.Entry(root, font=("Arial", 14))
    keyword_entry.pack(fill=tk.X, padx=10, pady=10, expand=True)

    # Search button
    search_button = tk.Button(root, text="Search", font=("Arial", 16), command=search)
    search_button.pack(padx=10, pady=10)

    # Results display
    results_frame = tk.Frame(root)
    results_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
    results_label = tk.Label(results_frame, text="Results:", font=("Arial", 16))
    results_label.pack()
    results_scrollbar = tk.Scrollbar(results_frame, orient=tk.HORIZONTAL)
    results_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    results_scrollbar_y = tk.Scrollbar(results_frame, orient=tk.VERTICAL)
    results_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    results = tk.Listbox(results_frame, font=("Arial", 14), width=70, height=20, xscrollcommand=results_scrollbar.set, yscrollcommand=results_scrollbar_y.set)
    results.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
    results_scrollbar.config(command=results.xview)
    results_scrollbar_y.config(command=results.yview)

    root.mainloop()
