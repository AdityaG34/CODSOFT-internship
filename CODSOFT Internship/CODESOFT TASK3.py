#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

# Function to generate a random password
def generate_password(length):
    # Define character sets for different complexity levels
    lower_chars = string.ascii_lowercase  # Lowercase letters
    upper_chars = string.ascii_uppercase  # Uppercase letters
    digits = string.digits  # Numbers
    special_chars = string.punctuation  # Special characters

    # Combine character sets based on desired complexity
    complexity = input("Enter complexity (low/medium/high): ").lower()
    if complexity == "low":
        characters = lower_chars + digits
    elif complexity == "medium":
        characters = lower_chars + upper_chars + digits
    elif complexity == "high":
        characters = lower_chars + upper_chars + digits + special_chars
    else:
        print("Invalid complexity level. Using medium complexity.")
        characters = lower_chars + upper_chars + digits

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function
def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer for password length.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()


# In[ ]:




