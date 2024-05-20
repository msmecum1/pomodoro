import random
import time
import os
import winsound
import tkinter as tk
from tkinter import messagebox

# Global variable to control the timer loop
running = False

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
    print("Pomodoro completed!")
    play_sound()  # Play a sound when the timer is completed
    break_timer(5)  # Start a break timer for 5 minutes after the Pomodoro timer completes

def play_sound():
    # Choose the appropriate command based on the operating system
    if os.name == 'nt':  # For Windows
        for _ in range(5):  # Repeat the beep 5 times
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:  # For macOS or Linux
        os.system("afplay /System/Library/Sounds/Ping.aiff")

def break_timer(minutes):
    global running
    running = True
    print("Break time starts now!")
    play_sound()  # Play a sound when break time starts
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
    print("Quit being lazy and go back to work!")
    break_label.config(text="")  # Clear break label
    timer_label.config(text="")  # Clear timer label
    root.update()  # Update the Tkinter window

def start_pomodoro():
    global running
    running = True
    if main_quest_options or side_mission_options:
        if start_pomodoro_btn["text"] == "Start Pomodoro":
            selected_task = select_random_task()
            if selected_task:
                task_label.config(text=f"Let's get going with: {selected_task}")
                start_pomodoro_btn.config(text="Stop Pomodoro", command=stop_pomodoro)
                pomodoro_timer(25)  # Start the Pomodoro timer (25 minutes)
        else:
            stop_pomodoro()
    else:
        messagebox.showwarning("Warning", "Please add main quests or side missions first!")

def stop_pomodoro():
    global running
    running = False
    start_pomodoro_btn.config(text="Start Pomodoro", command=start_pomodoro)
    task_label.config(text="")

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

def select_random_task():
    if not main_quest_options and not side_mission_options:
        return None

    task_list = main_quest_options + side_mission_options
    return random.choice(task_list)

root = tk.Tk()
root.title("Productivity App")

# Main quest section
main_quest_label = tk.Label(root, text="Main Quests:")
main_quest_label.grid(row=0, column=0, padx=5, pady=5)

main_quest_entry = tk.Entry(root, width=30)
main_quest_entry.grid(row=1, column=0, padx=5, pady=5)

add_main_quest_btn = tk.Button(root, text="Add", command=add_main_quest)
add_main_quest_btn.grid(row=1, column=1, padx=5, pady=5)

remove_main_quest_btn = tk.Button(root, text="Remove", command=remove_main_quest)
remove_main_quest_btn.grid(row=1, column=2, padx=5, pady=5)

main_quest_listbox = tk.Listbox(root, height=5, width=50)
main_quest_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Side mission section
side_mission_label = tk.Label(root, text="Side Missions:")
side_mission_label.grid(row=3, column=0, padx=5, pady=5)

side_mission_entry = tk.Entry(root, width=30)
side_mission_entry.grid(row=4, column=0, padx=5, pady=5)

add_side_mission_btn = tk.Button(root, text="Add", command=add_side_mission)
add_side_mission_btn.grid(row=4, column=1, padx=5, pady=5)

remove_side_mission_btn = tk.Button(root, text="Remove", command=remove_side_mission)
remove_side_mission_btn.grid(row=4, column=2, padx=5, pady=5)

side_mission_listbox = tk.Listbox(root, height=5, width=50)
side_mission_listbox.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Pomodoro timer section
timer_label = tk.Label(root, text="", font=("Arial", 24))
timer_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

task_label = tk.Label(root, text="", font=("Arial", 16))
task_label.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

break_label = tk.Label(root, text="", font=("Arial", 16))
break_label.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

start_pomodoro_btn = tk.Button(root, text="Start Pomodoro", command=start_pomodoro)
start_pomodoro_btn.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

main_quest_options = []
side_mission_options = []

root.mainloop()
    
    #cd source/repos/productive
    