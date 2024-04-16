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
    break_timer(5)  # Start a break timer for 5 minutes after the Pomodoro timer completes

def play_sound():
    # Choose the appropriate command based on the operating system
    if os.name == 'nt':  # For Windows
        for _ in range(5):  # Repeat the beep 5 times
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:  # For macOS or Linux
        os.system("afplay /System/Library/Sounds/Ping.aiff")  

def break_timer(minutes):
    print("Break time starts now!")
    play_sound()  # Play a sound when break time starts
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    play_sound()  # Play a sound when break time is over
    print("quit being lazy and go back to work!")

def main():
    print("I see you need to get some work done")
    
    while True:  # Loop until the user types "quit"
        # Options for main quest and side mission
        main_quest_options = [
            "change of Doc",
            "Loss of Doc",
            "Add Key Role",
            "Change of Key Role",
            "Gain of Position",
            "Change of Position",

        ]

        side_mission_options = [
            "School project",
            "cloud compliance",
            "Design Workout Program",
            "C# Master class",
            "Clean",
            
        ]

        # Ask the user to choose between main quest and side mission
        user_choice = input("WHERE DO WE GO FROM HERE i'm feeling it:\n1. Main Quest\n2. Side Mission\nEnter 1 or 2 (or type 'quit' to exit): ")

        if user_choice.lower() == "quit":
            print("Exiting program...")
            break  # Exit the loop and end the program
        elif user_choice == "1":
            quest = random.choice(main_quest_options)
            print(f"Your main quest is: {quest}. Get working on it!")
        elif user_choice == "2":
            mission = random.choice(side_mission_options)
            print(f"Your side mission is: {mission}. Get working on it!")
        else:
            print("Invalid choice. Please enter 1, 2, or 'quit'.")
            continue  # Restart the loop

        start_pomodoro = input("Start Pomodoro timer? (yes/no): ")
        if start_pomodoro.lower() == "yes":
            pomodoro_timer(25)  # 25 minutes for a Pomodoro timer
        else:
            print("No Pomodoro timer started. Get working!")

if __name__ == "__main__":
    main() 
