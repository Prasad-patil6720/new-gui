import tkinter as tk
from tkinter import *
from tkinter import filedialog





def main():
    def browse_file():
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            file_name.set(file_path)
            # text_widget.delete(1.0, tk.END)  # Clear previous text in the Text widget
            text_widget.insert(tk.END, f"Selected File: {file_path}\n")
            print(f"file path for iforMAC : {file_path}")
    def browse_file_enable():
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            file_name_enable.set(file_path)
            # text_widget.delete(1.0, tk.END)  # Clear previous text in the Text widget
            text_widget.insert(tk.END, f"Selected File: {file_path}\n")
            print(f"file path for Sheet Enable : {file_path}")
    # Create the main root
    root = tk.Tk()
    root.title("Folder Creation and Generating Documents")
    root.geometry("600x550")
    file_name=tk.StringVar()
    file_name_enable=tk.StringVar()
    

    # Create a label with the main heading, set its foreground color to red
    tk.Label(root, text="DSTO Automation Tool", font=("Times New Roman", 20), fg="red").grid(row=0,column=1,)


    label_file=tk.Label(root, text="InfoMAC Extract Sheet").grid(row=4, column=0, sticky="w",pady=10)
    label_button=tk.Button(root,text='Browse the File',command=browse_file).grid(row=4,column = 1,padx=100,pady=10)

    Field_frame=tk.Label(root, text="Field Selection Sheet").grid(row=5, column=0, sticky="w",pady=0)
    Field_button=tk.Button(root,text='Browse the File',command=browse_file_enable).grid(row=5,column = 1,padx=100,pady=0)

    # Field_frame=tk.Label(root, text="Field Selection Sheet").grid(row=5, column=0, sticky="w",pady=0)
    # Field_button=tk.Button(root,text='Browse the File',command=browse_file).grid(row=5,column = 1,padx=100,pady=0)

    application_frame=tk.Label(root, text="Application Enablement Sheet").grid(row=6, column=0, sticky="w",pady=10)
    application_button=tk.Button(root,text='Browse the File',command=browse_file).grid(row=6,column = 1,padx=100,pady=10)

    sharepath_frame=tk.Label(root, text="SharePath for generating Folders").grid(row=7, column=0, sticky="w",pady=10)
    sharepath_Entry=tk.Entry(root,textvariable = "name_var", font=('calibre',13,'normal')).grid(row=7, column=1, sticky="w",padx=100,pady=10)

    sharepath_documents=tk.Label(root, text="SharePath for generating Documents").grid(row=8, column=0, sticky="w",pady=10)
    sharepath_Entry_documents=tk.Entry(root,textvariable = "name_var", font=('calibre',13,'normal')).grid(row=8, column=1, sticky="w",padx=100,pady=10)


    create_folder=tk.Button(root,text='Create Folders',command=browse_file).grid(row=9,column = 0,padx=60,pady=10)
    Create_documents=tk.Button(root,text='Create Documents',command=browse_file).grid(row=9,column = 1,padx=80,pady=10)

    text_widget= tk.Text(root, bg="white", fg="black", font=("Helvetica", 12), height=10, width=40)   #.grid(row=10,column=1)
    text_widget.grid(row=10,column=1)

    # text_area = tk.Entry(root, bg="white",textvariable=file_name, fg="black", font=("Helvetica", 12)).grid(row=10,column=1)
    




    root.mainloop()

if __name__ == "__main__":
    main()