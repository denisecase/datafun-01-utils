'''  ITERATION 2

Module: Stellar Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this second iteration, add a function that returns the byline as a string.

I'll create a function named get_byline().
It'll return my byline to whatever calls the get_byline() function. 
   
I'll update the main() function to use the new get_byline() function. 

Same conditional boilerplate at the end. 

I'll test this version before adding more code that shows:
- my ability to declare variables of different types
- my ability to use Python to calculate basic descriptive statistics. '''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Stellar Analytics: Delivering Professional Insights'

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
