import tkinter as tk
import file_parse

# creates instance of tkinter library
root = tk.Tk()
# sets default size of window
root.geometry("400x300")


''' FUNCTION DEFINITIONS FOR UI '''


# shows frame from downloads folder
def show_frame(frame):
    frame.tkraise()
# filler function to show that the button has been pressed
def button_clicked(file): 
    print(file, " clicked")


# parses downloads folder
def parse_downloads():
    old_files = file_parse.clean_dir("/Users/ryancarney/Downloads")
    for file in old_files():
        # creates button for each 
        next_button = tk.Button(root,text=file, command=button_clicked(file))

def parse_desktop():
    old_files = file_parse.clean_dir("/Users/ryancarney/Desktop")

def parse_documents():
    old_files = file_parse.clean_dir("/Users/ryancarney/Documents")





''' UI DISPLAY '''

home_frame = tk.Frame(root)
home_frame.pack(fill=tk.BOTH, expand=True)

downloads_button = tk.Button(root, text="Clean Downloads", command=parse_downloads, width=10, height=3)
desktop_button = tk.Button(root, text="Clean Desktop", command=parse_desktop, width=10, height=3)
documents_button = tk.Button(root, text="Clean Documents", command=parse_documents, width=10, height=3)



# Packing frame

downloads_button.pack(home_frame=tk.CENTER, pady=15)
desktop_button.pack(home_frame=tk.CENTER, pady=15)
documents_button.pack(home_frame=tk.CENTER, pady=15)

root.mainloop()

