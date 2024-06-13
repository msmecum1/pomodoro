import random
import time
import os
import winsound
import tkinter as tk
from tkinter import messagebox

# Global variables
running = False
round_count = 0
main_quest_options = []
side_mission_options = []

# Motivational quotes
motivational_quotes = [
    "I'm a driver I'm a winner",
    "Everyone wanted a piece of my shit",
    "surrender is death, and death is for pussies.",
    "My ass is a fucking champion.",
    "I'm the man who has the ball. I'm the man you can throw it faster than fuck."
]

def get_motivational_quote():
    return random.choice(motivational_quotes)

def pomodoro_timer(minutes):
    global running
    running = True
    seconds = int(minutes * 60)
    while seconds and running:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        timer_label.config(text=timer)  # Update timer label
        root.update()  # Update the Tkinter window
        time.sleep(1)
        seconds -= 1
    if running:
        pomodoro_completed()

def pomodoro_completed():
    global round_count
    round_count += 1
    round_count_label.config(text=f"Rounds: {round_count}")
    play_sound()  # Play a sound when the timer is completed
    break_timer(5)  # Start a break timer for 5 minutes after the Pomodoro timer completes

def play_sound():
    if os.name == 'nt':  # For Windows
        for _ in range(5):  # Repeat the beep 5 times
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:  # For macOS or Linux
        os.system("afplay /System/Library/Sounds/Ping.aiff")

def break_timer(minutes):
    global running
    running = True
    break_label.config(text="Break Time")  # Update break label
    root.update()  # Update the Tkinter window
    seconds = int(minutes * 60)
    while seconds and running:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        timer_label.config(text=timer)  # Update timer label
        root.update()  # Update the Tkinter window
        time.sleep(1)
        seconds -= 1
    if running:
        break_completed()

def break_completed():
    play_sound()  # Play a sound when break time is over
    break_label.config(text="")  # Clear break label
    timer_label.config(text="")  # Clear timer label
    root.update()  # Update the Tkinter window

def start_pomodoro():
    global running
    running = True
    if main_quest_options or side_mission_options:
        if start_pomodoro_btn["text"] == "WHERE DO WE GO FROM HERE":
            selected_task = select_random_task()
            if selected_task:
                task_label.config(text=f"Let's get going with: {selected_task}")
                start_pomodoro_btn.config(text="Stop Pomodoro", command=stop_pomodoro)
                if selected_task in main_quest_options:
                    pomodoro_timer(25)  # Start the Pomodoro timer (25 minutes)
                else:
                    pomodoro_timer(10)  # Start the side mission timer (10 minutes)
        else:
            stop_pomodoro()
    else:
        messagebox.showwarning("Warning", "Please add main quests or side missions first!")

def stop_pomodoro():
    global running
    running = False
    start_pomodoro_btn.config(text="WHERE DO WE GO FROM HERE", command=start_pomodoro)
    task_label.config(text="")

def select_random_task():
    all_tasks = main_quest_options + side_mission_options
    return random.choice(all_tasks) if all_tasks else None

def add_main_quest():
    user_input = main_quest_entry.get()
    if user_input:
        main_quest_options.append(user_input)
        main_quest_entry.delete(0, tk.END)
        update_lists()

def add_side_mission():
    user_input = side_mission_entry.get()
    if user_input:
        side_mission_options.append(user_input)
        side_mission_entry.delete(0, tk.END)
        update_lists()

def remove_main_quest():
    selected = main_quest_listbox.curselection()
    if selected:
        main_quest_options.pop(selected[0])
        update_lists()

def remove_side_mission():
    selected = side_mission_listbox.curselection()
    if selected:
        side_mission_options.pop(selected[0])
        update_lists()

def update_lists():
    main_quest_listbox.delete(0, tk.END)
    side_mission_listbox.delete(0, tk.END)
    for quest in main_quest_options:
        main_quest_listbox.insert(tk.END, quest)
    for mission in side_mission_options:
        side_mission_listbox.insert(tk.END, mission)

# GUI setup
root = tk.Tk()
root.title("Pomodoro Timer")

# Create a main frame to hold all the widgets
main_frame = tk.Frame(root, borderwidth=2, highlightbackground="black")
main_frame.pack(fill="both", expand=True)


# Set the foreground color of the task label to red
task_label = tk.Label(root, text="", font=("Helvetica", 12), foreground="#FF0000")
task_label.pack()

# Set the border width to 2
root.config(highlightthickness=2, highlightbackground="black")

# Create a grid with 5 rows and 3 columns
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_rowconfigure(3, weight=1)
main_frame.grid_rowconfigure(4, weight=1)

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# Place the widgets in the grid
timer_label = tk.Label(main_frame, text="00:00", font=("Helvetica", 48))
timer_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

break_label = tk.Label(main_frame, text="", font=("Helvetica", 12))
break_label.grid(row=1, column=0, columnspan=3, sticky="nsew")

round_count_label = tk.Label(main_frame, text="Rounds: 0", font=("Helvetica", 12))
round_count_label.grid(row=2, column=0, columnspan=3, sticky="nsew")

start_pomodoro_btn = tk.Button(main_frame, text="WHERE DO WE GO FROM HERE", command=start_pomodoro, font=("Helvetica", 12))
start_pomodoro_btn.grid(row=3, column=0, sticky="nsew")

# Main quests
main_quest_frame = tk.Frame(main_frame)
main_quest_frame.grid(row=0, column=3, rowspan=5, sticky="nsew")

main_quest_label = tk.Label(main_quest_frame, text="Main Quests", font=("Helvetica", 12))
main_quest_label.pack()

main_quest_entry = tk.Entry(main_quest_frame)
main_quest_entry.pack()

main_quest_add_btn = tk.Button(main_quest_frame, text="Add Main Quest", command=add_main_quest)
main_quest_add_btn.pack()

main_quest_remove_btn = tk.Button(main_quest_frame, text="Remove Selected Main Quest", command=remove_main_quest)
main_quest_remove_btn.pack()

main_quest_listbox = tk.Listbox(main_quest_frame)
main_quest_listbox.pack()

# Side missions
side_mission_frame = tk.Frame(main_frame)
side_mission_frame.grid(row=0, column=4, rowspan=5, sticky="nsew")

side_mission_label = tk.Label(side_mission_frame, text="Side Missions", font=("Helvetica", 12))
side_mission_label.pack()

side_mission_entry = tk.Entry(side_mission_frame)
side_mission_entry.pack()

side_mission_add_btn = tk.Button(side_mission_frame, text="Add Side Mission", command=add_side_mission)
side_mission_add_btn.pack()

side_mission_remove_btn = tk.Button(side_mission_frame, text="Remove Selected Side Mission", command=remove_side_mission)
side_mission_remove_btn.pack()

side_mission_listbox = tk.Listbox(side_mission_frame)
side_mission_listbox.pack()

# Run the Tkinter event loop
root.mainloop()

# Define a function to play a sound when the timer is completed
def play_sound():
    if os.name == 'nt':  # For Windows
        for _ in range(5):  # Repeat the beep 5 times
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:  # For macOS or Linux
        os.system("afplay /System/Library/Sounds/Ping.aiff")

# Define a function to update the lists of main quests and side missions
def update_lists():
    main_quest_listbox.delete(0, tk.END)
    side_mission_listbox.delete(0, tk.END)
    for quest in main_quest_options:
        main_quest_listbox.insert(tk.END, quest)
    for mission in side_mission_options:
        side_mission_listbox.insert(tk.END, mission)

# Define a function to add a main quest
def add_main_quest():
    user_input = main_quest_entry.get()
    if user_input:
        main_quest_options.append(user_input)
        main_quest_entry.delete(0, tk.END)
        update_lists()

# Define a function to add a side mission
def add_side_mission():
    user_input = side_mission_entry.get()
    if user_input:
        side_mission_options.append(user_input)
        side_mission_entry.delete(0, tk.END)
        update_lists()

# Define a function to remove a main quest
def remove_main_quest():
    selected = main_quest_listbox.curselection()
    if selected:
        main_quest_options.pop(selected[0])
        update_lists()

# Define a function to remove a side mission
def remove_side_mission():
    selected = side_mission_listbox.curselection()
    if selected:
        side_mission_options.pop(selected[0])
        update_lists()

# Create the GUI widgets
task_label = tk.Label(root, text="", font=("Helvetica", 12), foreground="#FF0000")
task_label.pack()

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack()

break_label = tk.Label(root, text="", font=("Helvetica", 12))
break_label.pack()

round_count_label = tk.Label(root, text="Rounds: 0", font=("Helvetica", 12))
round_count_label.pack()

start_pomodoro_btn = tk.Button(root, text="WHERE DO WE GO FROM HERE", command=start_pomodoro, font=("Helvetica", 12))
start_pomodoro_btn.pack()

main_quest_frame = tk.Frame(root)
main_quest_frame.pack()

main_quest_label = tk.Label(main_quest_frame, text="Main Quests", font=("Helvetica", 12))
main_quest_label.pack()

main_quest_entry = tk.Entry(main_quest_frame)
main_quest_entry.pack()

main_quest_add_btn = tk.Button(main_quest_frame, text="Add Main Quest", command=add_main_quest)
main_quest_add_btn.pack()

main_quest_remove_btn = tk.Button(main_quest_frame, text="Remove Selected Main Quest", command=remove_main_quest)
main_quest_remove_btn.pack()

main_quest_listbox = tk.Listbox(main_quest_frame)
main_quest_listbox.pack()

side_mission_frame = tk.Frame(root)
side_mission_frame.pack()

side_mission_label = tk.Label(side_mission_frame, text="Side Missions", font=("Helvetica", 12))
side_mission_label.pack()

side_mission_entry = tk.Entry(side_mission_frame)
side_mission_entry.pack()

side_mission_add_btn = tk.Button(side_mission_frame, text="Add Side Mission", command=add_side_mission)
side_mission_add_btn.pack()

side_mission_remove_btn = tk.Button(side_mission_frame, text="Remove Selected Side Mission", command=remove_side_mission)
side_mission_remove_btn.pack()

side_mission_listbox = tk.Listbox(side_mission_frame)
side_mission_listbox.pack()

# Run the Tkinter event loop
root.mainloop()

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_data)
file_menu.add_command(label="Load", command=load_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_dialog)

# Run the Tkinter event loop
root.mainloop()

# Define a function to save the data
def save_data():
    with open("data.txt", "w") as file:
        file.write("Main Quests:\n")
        for quest in main_quest_options:
            file.write(quest + "\n")
        file.write("Side Missions:\n")
        for mission in side_mission_options:
            file.write(mission + "\n")

# Define a function to load the data
def load_data():
    try:
        with open("data.txt", "r") as file:
            data = file.read()
            main_quest_options.clear()
            side_mission_options.clear()
            for line in data.splitlines():
                if line.startswith("Main Quests:"):
                    continue
                elif line.startswith("Side Missions:"):
                    continue
                elif line:
                    if line in main_quest_options or line in side_mission_options:
                        continue
                    main_quest_options.append(line)
            for line in data.splitlines():
                if line.startswith("Side Missions:"):
                    continue
                elif line:
                    if line in main_quest_options or line in side_mission_options:
                        continue
                    side_mission_options.append(line)
    except FileNotFoundError:
        pass

# Define a function to display an about dialog
def about_dialog():
    messagebox.showinfo("About", "Pomodoro Timer v1.0\nCopyright (c) 2023\nAll rights reserved.")

# Run the script
if __name__ == "__main__":
    main()