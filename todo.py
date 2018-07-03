# Todo List with Python and Tkinter
# Created by Dan Dumitrache - http://saigon.ro
# Python 2.7.15rc1

import Tkinter
import random
import tkMessageBox



# Creates the root window
root = Tkinter.Tk()



# Changes the default root window
root.geometry("530x420")
root.configure(bg="white", padx=20, pady=20)
root.title("Dan & Emma To Do List")



# Create an empty list
tasks = []



# For testing use a default list
tasks = ["Learn HTML5", "Check out CSS4", "Build something with Tkinter", "Prime thing to do", "Google staff", "Vue.js should be checked"]



# Creates functions
def update_listbox():
	# Clear the current list
	clear_listbox()
	# Populate the listbox
	for task in tasks:
		lb_tasks.insert("end", task)

def clear_listbox():
	lb_tasks.delete(0, "end")

def add_task():
	# Gets the task to add from the txt_input box
	task = txt_input.get()
	# Makes sure the task is not empty
	if task != "":
		# Appends the task to the list of tasks
		tasks.append(task)
		# Updates the listbox
		update_listbox()
	# If the task is empty then tells the user
	else:
		lbl_display["text"] = "Please enter a task!"
	# Clears the input box
	txt_input.delete(0, "end")

def del_all():
	# Creates a confirmation box
	confirmed = tkMessageBox.askyesno("Please Confirm", "Do you really want to delete all of the tasks?")
	if confirmed == True:
		# Make the tasks to be global
		global tasks
		# Clear all the tasks
		tasks = []
		# Update the listbox
		update_listbox()

def del_one():
	# Gets the text of the currently selected task
	task = lb_tasks.get("active")
	# Check if it is in the list
	if task in tasks:
		tasks.remove(task)
	# Updates the list box
	update_listbox()

def sort_asc():
	# Sorts the list ascending (from A to Z)
	tasks.sort()
	# After sorting ascending, updates the list
	update_listbox()

def sort_desc():
	# Sorts the list descending (from Z to A)
	# Sorts ascending the reverses
	tasks.sort()
	tasks.reverse()
	# After sorting descending, updates the list
	update_listbox()

def choose_random():
	# Chooses a random task
	task = random.choice(tasks)
	# Updates the display label
	lbl_display["text"] = task

def show_number_of_tasks():
	# Gets the number of tasks
	number_of_tasks = len(tasks)
	# Creates and formats the message
	msg = "Number of tasks: %s" %number_of_tasks
	# Displays the message
	lbl_display["text"] = msg





# =============== Creates the lables =================
lbl_title = Tkinter.Label(root, text="To Do App", bg="white", font=('Verdana', 14, 'bold'))
lbl_title.grid(row=0, column=0, pady=(0, 15))

lbl_display = Tkinter.Label(root, text="", bg="white", fg="red")
lbl_display.grid(row=0, column=1)



# =============== Creates the input box =================
txt_input = Tkinter.Entry(root, width=35)
txt_input.grid(row=1, column=1)



# =============== Creates the buttons =================
btn_add_task = Tkinter.Button(root, text="Add Task", fg="green", bg="white", width=15, command=add_task)
btn_add_task.grid(row=1, column=0, padx=20, pady=(0, 15))

btn_del_all = Tkinter.Button(root, text="Delete All", fg="red", bg="white", width=15, command=del_all)
btn_del_all.grid(row=2, column=0)

btn_del_one = Tkinter.Button(root, text="Delete Selected", fg="red", bg="white", width=15, command=del_one)
btn_del_one.grid(row=3, column=0, pady=(0, 15))

btn_sort_asc = Tkinter.Button(root, text="Sort A-Z", fg="black", bg="white", width=15, command=sort_asc)
btn_sort_asc.grid(row=4, column=0)

btn_sort_desc = Tkinter.Button(root, text="Sort Z-A", fg="black", bg="white", width=15, command=sort_desc)
btn_sort_desc.grid(row=5, column=0, pady=(0, 15))

btn_choose_random = Tkinter.Button(root, text="Choose Random", fg="black", bg="white", width=15, command=choose_random)
btn_choose_random.grid(row=6, column=0)

btn_number_of_tasks = Tkinter.Button(root, text="Number of Tasks", fg="black", bg="white", width=15, command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7, column=0)

btn_exit = Tkinter.Button(root, text="Exit", fg="red", bg="white", width=15, command=exit)
btn_exit.grid(row=8, column=0, pady=(15, 0))




# =============== Creates the List Box =================
lb_tasks = Tkinter.Listbox(root, width=35)
lb_tasks.grid(row=2, column=1, rowspan=10)




# =============== Starts the main events loop =================
root.mainloop()
