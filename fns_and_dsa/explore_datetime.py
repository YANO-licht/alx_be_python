# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Obtain the current date and time
    current_date = datetime.now()
    # Format and print the current date and time in a readable format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date):
    # Prompt the user to enter a number of days
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date by adding the specified number of days to the current date
        future_date = current_date + timedelta(days=number_of_days)
        # Print the future date in a format like “YYYY-MM-DD”
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer value.")

def main():
    # Part 1: Display the Current Date and Time
    current_date = display_current_datetime()
    # Part 2: Calculate a Future Date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
