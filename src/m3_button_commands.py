import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

window = tk.Tk()
window.title("Form")

bg_color = "white"  
fg_color = "black"  

window.configure(background=bg_color)

fields = [
    ("Name", 30),
    ("Address Line 1", 40),
    ("Address Line 2", 40),
    ("City", 30),
    ("State", 5),
    ("Zip Code", 10),
    ("Phone Number", 15),
    ("Email Address", 30)
]

entries = []

frame = tk.Frame(window, bg=bg_color)
frame.pack(padx=10, pady=10)

for field_name, field_width in fields:
    label = tk.Label(frame, text=field_name, bg=bg_color, fg=fg_color)
    label.grid(sticky="w", pady=2)
    entry = tk.Entry(frame, width=field_width)
    entry.grid(sticky="we", pady=2)
    entries.append(entry)

def print_form():
    for entry in entries:
        print(entry.get())
submit_button = tk.Button(window, text="Submit", bg="pink", fg="white", width=20, command=print_form)
submit_button.place(relx=0.5, rely=1.0, anchor="s", y=-10)

window.mainloop()
###############################################################################
# DONE: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
submit_button = tk.Button(window, text="Submit", bg="pink", fg="white", width=20, command=print_form)
submit_button.place(relx=0.5, rely=1.0, anchor="s", y=-10)