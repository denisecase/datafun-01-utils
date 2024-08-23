'''
Module: Stellar Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

When we work hard to write useful code, we want it to be reusable.

A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.

Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it on my machine or in an online interpreter to make sure this simple version runs correctly before continuing.
'''

#####################################
# Declare a variable named byline.
#####################################

byline: str = 'Byline for all my analytics projects'

#####################################
# Define a main() function for my module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print my byline variable to the console.
# Add a type hint to indicate that this function doesn't return anything when called (that is, it has a Python type of None).
# It doesn't need any additional information passed in, so there's nothing needed inside the parentheses.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    # Indent everything after the colon when defining a function.
    # Start with a docstring whenever declaring a function.
    # Provide the indented statements below.
    print(byline)

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

# This part ensures that the main function runs when we execute the script.
# It's a standard practice in Python, so you don't need to change anything here.

if __name__ == '__main__':
    # Call my main function by writing the function name immediately followed by open & close parentheses.
    # Indent everything after the colon above.
    main()
