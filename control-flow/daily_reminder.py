# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
print("Reminder:", end=" ")

# Match Case based on priority
match priority:
    case 'high':
        print(f"'{task}' is a high priority task", end=" ")
    case 'medium':
        print(f"'{task}' is a medium priority task", end=" ")
    case 'low':
        print(f"'{task}' is a low priority task", end=" ")
    case _:
        print(f"'{task}' has an unrecognized priority level")

# Check if the task is time-bound
if time_bound == 'yes':
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")
