from tkinter import *
from tkinter import messagebox

BG = "#7338a6"
FG = "white"
BG_TEXT = "black"
window = Tk()
window.title("To-Do List")
window.geometry("350x450")
window.config(bg=BG)

FONT_BIG = ("Arial", 15, "bold")
FONT_SMALL = ("Arial", 10, "bold")

def task_adding():
    task = main_entry.get()
    if task:
        main_list.insert(0, task)
        main_entry.delete(0, END)
        saving_tasks()
    else:
        messagebox.showerror(title="ERROR!",message="ENTER A TASK TO SAVE")


def delete_task():
    selected = main_list.curselection()
    if selected:
        main_list.delete(selected[0])
        saving_tasks()
    else:
        messagebox.showerror(title="ERROR!", message="CHOOSE A TASK TO DELETE")

def saving_tasks():
    with open("task.txt", "w") as listed_task:
        tasks = main_list.get(0, END)
        for n in tasks:
            listed_task.write(n + "\n")


def load_task():
    try:
        with open ("task.txt", "r") as listed_task:
            tasks = listed_task.readlines()
            for n in tasks:
                main_list.insert(0, n.strip())
    except FileNotFoundError:
        pass

lable = Label(text="To-Do List", font=("Arial", 30, "bold"), fg=FG, bg=BG)
lable.place(x=85, y=20)

main_entry = Entry(font=FONT_BIG, fg=BG_TEXT, width=25)
main_entry.place(x=40, y =80)

main_list = Listbox(font=FONT_SMALL, width=39, height=15)
main_list.place(x=40, y=120)

add_button = Button(command=task_adding, text="Add Task", font=FONT_BIG, fg=FG, bg="#06911f")
add_button.place(x=40, y=390)

del_button = Button(command=delete_task, text="Remove Task", font=FONT_BIG, fg=FG, bg="#96061c")
del_button.place(x=170, y=390)

load_task()
window.mainloop()
