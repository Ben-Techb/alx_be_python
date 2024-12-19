Task = input("Enter the task description: ")
Priority = input("Enter the task priority (high, medium, low): ").lower()
Time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"The task '{Task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{Task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{Task}' is of LOW priority."
    case _:
        reminder = f"The task '{Task}' has an UNKNOWN priority."


if Time_bound == "yes":
    reminder += " It requires immediate attention today!"


print("\nReminder:")
print(reminder)
