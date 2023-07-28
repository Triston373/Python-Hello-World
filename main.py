# Lab written by Triston Oswald, deviation from tutorials given
# from Programming with Mosh here: https://www.youtube.com/watch?v=_uQrJ0TkZlc

# Print statement
print("Triston Oswald")

# Create integer variable (store value "10" in memory)
price = 10
# Update price value to be 30
price += 20
# Define floating point value
rating = 3.3
# String variable
name = 'Triston'
# Boolean variable (note: boolean values are case-sensitive)
boolean = False

print(price)
print(rating)
print(name)
print(boolean)

# Ask for user input, print statement and wait for user to type in terminal.
# Stores input in variable
user_name = input('What is your name? ')
user_color = input('What color is your favorite? ')
# Concatenate string variables to print on one line
print('Hello, ' + user_name + '! Your favorite color is ' + user_color)

# Example of type casting from string to int
birth_year = input('What is your birth year? ')
print(type(birth_year))
age = 2023 - int(birth_year)
print(age)

# Print statement multiplier
print('x5 ' * 5)
# ASCII art
print("""\
                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /
                    """)