# daily_reminder.py

# Prompt user for task details
Task = input("Enter the task description: ")
Priority = input("Enter the task priority (high, medium, low): ").lower()
Time_Bound = input("Is the task time-bound? (yes or no): ").lower()

# Process task and provide customized reminder
match Priority:
    case "high":
        reminder = f"The task '{Task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{Task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{Task}' is of LOW priority."
    case _:
        reminder = f"The task '{Task}' has an UNKNOWN priority."

# Modify the reminder based on time sensitivity
if Time_Bound == "yes":
    reminder += " It requires immediate attention today!"

# Output the customized reminder
print("\nReminder:")
print(reminder)
