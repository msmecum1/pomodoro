import random
import time
import os
import winsound

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Pomodoro completed!")
    play_sound()  # Play a sound when the timer is completed

def play_sound():
    # Choose the appropriate command based on the operating system
    if os.name == 'nt':  # For Windows
        for _ in range(5):  # Repeat the beep 5 times
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:  # For macOS or Linux
        os.system("afplay /System/Library/Sounds/Ping.aiff")  # Adjust the path and sound file name as necessary

def main():
    print("Welcome to the Quest Generator!")
    
    # Options for main quest and side mission
    main_quest_options = [
        "change of core doc",
        "loss of core doc",
        "Appraisal Journal",
        "Search Article",
		"Add Key Role"
    ]

    side_mission_options = [
        "JM",
        "School",
        "Clean Emails and Schedules",
        "ASP Course",
    ]

    # Ask the user to choose between main quest and side mission
    user_choice = input("Choose your adventure:\n1. Main Quest\n2. Side Mission\nEnter 1 or 2: ")

    if user_choice == "1":
        quest = random.choice(main_quest_options)
        print(f"Your main quest is: {quest}. Get working on it!")
    elif user_choice == "2":
        mission = random.choice(side_mission_options)
        print(f"Your side mission is: {mission}. Get working on it!")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    start_pomodoro = input("Start Pomodoro timer? (yes/no): ")
    if start_pomodoro.lower() == "yes":
        pomodoro_timer(25)  # 25 minutes for a Pomodoro timer
    else:
        print("No Pomodoro timer started. Get working!")

if __name__ == "__main__":
    main()