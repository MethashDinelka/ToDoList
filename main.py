import customtkinter as tk
from datetime import datetime
import webbrowser
import os
import sys

def resource_path(relative_path):
    """ Get the absolute path to the resource, whether in development or in PyInstaller bundle """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = tk.CTk()

def submit():
    task1 = entry1.get()
    task2 = entry2.get()
    task3 = entry3.get()
    task4 = entry4.get()
    task5 = entry5.get()

    temxt = f"""Date & Time : {current_datetime}
Tasks       :

01. {task1}
02. {task2}
03. {task3}
04. {task4}
05. {task5}"""

    label_submit.configure(text="Details Submitted Successfully!")

    rootx = tk.CTk()
    width, height = 700, 500

    display_width = rootx.winfo_screenwidth()
    display_height = rootx.winfo_screenheight()
    left = int((display_width / 2) - (width / 2))
    top = int((display_height / 2) - (height / 2))

    rootx.title("To-Do List")
    rootx.iconbitmap(resource_path("icon.ico"))
    rootx.configure(fg_color="light yellow")
    rootx.geometry(f"{width}x{height}+{left}+{top}")
    rootx.resizable(False, False)

    labelx = tk.CTkLabel(rootx,text=temxt,text_color="black", font=("Times New Roman", 20))
    labelx.pack(pady=10)

    labely = tk.CTkLabel(rootx, text="To-Do List (Version 1.0) All Right Reverved BY Methash Dinelka©", text_color="red", font=("Times New Roman", 20))
    labely.pack(pady=10)

    web_button = tk.CTkButton(rootx,text="WebSite",text_color="blue",fg_color="light blue",height=60,width=250,font=("Times New Roman",45),command=lambda :webbrowser.open("http://methash-dinelka.blogspot.com/"))
    web_button.pack(pady=10)

    git_button = tk.CTkButton(rootx,text="Github",text_color="blue",fg_color="light blue",height=60,width=250,font=("Times New Roman",45),command=lambda :webbrowser.open("https://github.com/MethashDinelka"))
    git_button.pack(pady=10)

    close_button = tk.CTkButton(rootx,text="Close",text_color="white",fg_color="red",height=60,width=250,font=("Times New Roman",45),command=lambda :rootx.destroy())
    close_button.pack(pady=10)

    rootx.mainloop()


width, height = 900, 750

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int((display_width / 2) - (width / 2))
top = int((display_height / 2) - (height / 2))

root.title("To-Do List")
root.iconbitmap(resource_path("icon.ico"))
root.configure(fg_color="light yellow")
root.geometry(f"{width}x{height}+{left}+{top}")
#root.resizable(False, False)
timen = datetime.now()
current_datetime = timen.strftime("%Y-%m-%d")

frame = tk.CTkFrame(root,fg_color="transparent",border_color="black",border_width=100)
frame.pack()

label = tk.CTkLabel(frame,text="To-Do List 1.0v",font=("Kristen ITC",95),text_color="red")
label.pack()

label2 = tk.CTkLabel(root,text="Methash Dinelka © - Software Development",font=("Times New Roman",20),text_color="black")
label2.pack(pady=20)

label3 = tk.CTkLabel(root,text="Enter Your Tasks inside Spaces Below.",font=("Aerial",40),text_color="Blue")
label3.pack(pady=10)

entry1 = tk.CTkEntry(root,placeholder_text="Enter Task 01",width=600,height=30,fg_color="light green",placeholder_text_color="black",text_color="black")
entry1.pack(pady=10)

entry2 = tk.CTkEntry(root,placeholder_text="Enter Task 02",width=600,height=30,fg_color="light green",placeholder_text_color="black",text_color="black")
entry2.pack(pady=10)

entry3 = tk.CTkEntry(root,placeholder_text="Enter Task 03",width=600,height=30,fg_color="light green",placeholder_text_color="black",text_color="black")
entry3.pack(pady=10)

entry4 = tk.CTkEntry(root,placeholder_text="Enter Task 04",width=600,height=30,fg_color="light green",placeholder_text_color="black",text_color="black")
entry4.pack(pady=10)

entry5 = tk.CTkEntry(root,placeholder_text="Enter Task 05",width=600,height=30,fg_color="light green",placeholder_text_color="black",text_color="black")
entry5.pack(pady=20)

button = tk.CTkButton(root,text="Submit",text_color="red",fg_color="yellow",height=60,width=250,font=("Times New Roman",45),command=submit)
button.pack(pady=10)

label_submit = tk.CTkLabel(root,text_color="black",font=("Times New Roman",25),text=" ")
label_submit.pack(pady=10)

close_button = tk.CTkButton(root, text="Close", text_color="white", fg_color="red", height=60, width=250,font=("Times New Roman", 45), command=lambda: root.destroy())
close_button.pack(pady=10)

root.mainloop()