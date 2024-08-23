'''
Module: Stellar Analytics - Reusable Module for Our Data Analytics Projects

This module provides a simple, reusable foundation for analytics projects. 
We will learn how to declare variables, format strings, and create a basic function.
We'll also introduce and use optional type hints to make our code clearer.
'''

#####################################
# Import Modules
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing two modules:
# - `statistics`: This gives us tools to calculate things like averages.
# - `math`: This provides common math functions (like pi), though we won't use it much here.

import statistics
import math  # You can remove this if you don't need it, but it's good practice to see how imports work.

#####################################
# Declare Global Variables with Type Hints
#####################################

# Global variables are variables we can use anywhere in our code.
# Type hints show what type of value each variable should have.
# We'll practice declaring different types of variables here.

# Example of a string variable (a series of text characters).
company_name: str = 'Stellar Analytics Inc.'

# You try: Declare a string variable for the analyst's name.
analyst_name: str = 'Jane Doe'

# Example of an integer variable (a whole number).
count_active_projects: int = 5

# You try: Declare an integer variable for years in operation.
years_in_operation: int = 10

# Example of a boolean variable (True or False value).
has_international_presence: bool = False

# You try: Declare a boolean variable for whether the company is profitable.
is_profitable: bool = True

# Example of a floating-point number (a number with a decimal).
average_client_satisfaction: float = 4.7

# You try: Declare a floating-point number for average project duration in months.
average_project_duration: float = 6.4

# Example of a list of strings (a collection of text items).
services_offered: list[str] = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]

# You try: Declare a list of strings for the regions covered.
regions_covered: list[str] = ["North America", "Europe", "Asia"]

# Example of a list of numbers (a collection of numeric items).
satisfaction_scores: list[float] = [4.8, 4.6, 4.9, 5.0, 4.7]

# You try: Declare a list of numbers for project durations in months.
project_durations: list[float] = [6.5, 7.2, 5.8, 6.0, 6.4]

#####################################
# Use Formatted Strings (f-strings)
#####################################

# We can combine variables into a string using f-strings, which makes it easy to format our messages.

# Example: Create a string that describes the number of active projects.
active_projects_string: str = f"Active Projects: {count_active_projects}"

# Example: Create a string that describes international presence.
international_presence_string: str = f"International Presence: {has_international_presence}"

# Example: Create a string that describes client satisfaction.
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"

#####################################
# Calculate Descriptive Statistics
#####################################

# Let's calculate some basic statistics using the `statistics` module and built-in Python functions.

# Find the smallest and largest project durations.
smallest_duration: float = min(project_durations)
largest_duration: float = max(project_durations)

# Calculate the total duration and the number of projects.
total_duration: float = sum(project_durations)
count_duration: int = len(project_durations)

# Calculate the mean (average), median, and standard deviation.
mean_duration: float = statistics.mean(project_durations)
median_duration: float = statistics.median(project_durations)
stdev_duration: float = statistics.stdev(project_durations)

#####################################
# Combine Statistics into a Formatted String
#####################################

# We can now create a string that combines all these statistics into a summary.
stats_string: str = f"""
Descriptive Statistics for Project Durations:
  Smallest Duration: {smallest_duration} months
  Largest Duration: {largest_duration} months
  Total Duration: {total_duration} months
  Number of Projects: {count_duration}
  Mean Duration: {mean_duration:.2f} months
  Median Duration: {median_duration} months
  Standard Deviation: {stdev_duration:.2f} months
"""

#####################################
# Declare a Byline with All the Information
#####################################

# Let's put everything together in a byline, which is a summary of all the important information.
byline: str = f"""
{company_name}
Analyst: {analyst_name}
{active_projects_string}
{international_presence_string}
{client_satisfaction_string}
Services Offered: {", ".join(services_offered)}
Regions Covered: {", ".join(regions_covered)}
{stats_string}
"""

#####################################
# Define a Main Function with a Type Hint
#####################################

# Now, we'll create a function called main. 
# A function is a block of code that performs a specific task. 
# This function will simply print our byline to the console.
# We can add a type hint to indicate that this function doesn't return anything (it returns None).

def main() -> None:
    # Print the byline to the console.
    print(byline)

#####################################
# Run the Main Function
#####################################

# This part ensures that the main function runs when we execute the script.
# It's a standard practice in Python, so you don't need to change anything here.

if __name__ == '__main__':
    main()
