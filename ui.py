import tkinter as tk
import file_parse

# creates instance of tkinter library
root = tk.Tk()
# sets default size of window
root.geometry("720x450")


''' FUNCTION DEFINITIONS FOR UI '''


# shows frame from downloads folder
def show_frame(frame):
    frame.tkraise()
# filler function to show that the button has been pressed
def button_clicked(file): 
    print(file, " clicked")


# parses downloads folder
def parse_downloads():
    old_files = file_parse.clean_dir("C:\\Users\\Scott's PC\\Documents\\Call Of Duty Black Ops Cold War")
        # old_files = file_parse.clean_dir("/")
        # print(len(old_files))
    # for file in old_files():
    #     # creates button for each 
    #     next_button = tk.Button(root,text=file, command=button_clicked(file))
    return old_files

def parse_desktop():
    old_files = file_parse.clean_dir("")

def parse_documents():
    old_files = file_parse.clean_dir("/Users/ryancarney/Documents")





''' UI DISPLAY '''

# home_frame = tk.Frame(root)
# home_frame.pack(fill=tk.BOTH, expand=True)

# downloads_button = tk.Button(home_frame, text="Clean Downloads", command=parse_downloads, width=10, height=3)
# desktop_button = tk.Button(home_frame, text="Clean Desktop", command=parse_desktop, width=10, height=3)
# documents_button = tk.Button(home_frame, text="Clean Documents", command=parse_documents, width=10, height=3)

for i in range(5):
    for j in range(1):
        button_text = f"Button {i*3 + j + 1}"
        button = tk.Button(root, text=button_text, width=100, height=3)
        button.grid(row=i, column=j, padx=5, pady=5)


# Packing frame

# downloads_button.pack(pady=15)
# desktop_button.pack(pady=15)
# documents_button.pack(pady=15)

root.mainloop()

