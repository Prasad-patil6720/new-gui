import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        file_name.set(file_path)
        text_widget.delete(1.0, tk.END)  # Clear previous text in the Text widget
        text_widget.insert(tk.END, f"Selected File: {file_path}")

# Create the main window
root = tk.Tk()
root.title("File Browser")

# Variable to store the selected file name
file_name = tk.StringVar()

# Create and configure the widgets
label = tk.Label(root, text="Selected File:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, textvariable=file_name, state='readonly', width=40)
entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=1, column=0, columnspan=2, pady=10)

# Single-line Text widget to display information
text_widget = tk.Text(root, height=1, width=50)
text_widget.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
