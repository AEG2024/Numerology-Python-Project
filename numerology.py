import tkinter as tk
from tkinter import messagebox


# Function to sum the digits of a number
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        if digit.isdigit():  # Ensure we're only summing digits
            total += int(digit)
    return total


# Function to reduce a number to a single digit
def reduce_to_single_digit(num):
    while num > 9:
        num = sum_of_digits(num)
    return num


# Dictionary to map letters to numbers
letter_to_number = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 2,
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 1,
    "T": 2,
    "U": 3,
    "V": 4,
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}

# List of vowels
vowels = {"A", "E", "I", "O", "U"}

life_path_descriptions = {
    1: "Life Path 1: You are a natural leader, ambitious, and driven.",
    2: "Life Path 2: You are a peacemaker, diplomatic, and cooperative.",
    3: "Life Path 3: You are creative, expressive, and love to communicate.",
    4: "Life Path 4: You are hardworking, practical, and disciplined.",
    5: "Life Path 5: You are adventurous, freedom-loving, and dynamic.",
    6: "Life Path 6: You are caring, nurturing, and responsible.",
    7: "Life Path 7: You are introspective, analytical, and spiritual.",
    8: "Life Path 8: You are ambitious, materialistic, and goal-oriented.",
    9: "Life Path 9: You are compassionate, humanitarian, and idealistic.",
}

expression_descriptions = {
    1: "Expression 1: You are a self-starter, innovative, and confident.",
    2: "Expression 2: You are a team player, diplomatic, and cooperative.",
    3: "Expression 3: You are expressive, artistic, and full of energy.",
    4: "Expression 4: You are disciplined, practical, and grounded.",
    5: "Expression 5: You are versatile, energetic, and love change.",
    6: "Expression 6: You are nurturing, responsible, and community-oriented.",
    7: "Expression 7: You are introspective, thoughtful, and spiritual.",
    8: "Expression 8: You are driven, ambitious, and business-minded.",
    9: "Expression 9: You are compassionate, broad-minded, and humanitarian.",
}

soul_urge_descriptions = {
    1: "Soul Urge 1: You have a deep desire to lead and assert your individuality.",
    2: "Soul Urge 2: You have a deep desire for harmony and partnership.",
    3: "Soul Urge 3: You have a deep desire to express yourself creatively.",
    4: "Soul Urge 4: You have a deep desire for stability and security.",
    5: "Soul Urge 5: You have a deep desire for freedom and adventure.",
    6: "Soul Urge 6: You have a deep desire to care for others and create a loving, harmonious environment.",
    7: "Soul Urge 7: You have a deep desire for knowledge and spiritual connection.",
    8: "Soul Urge 8: You have a deep desire for success and material achievement.",
    9: "Soul Urge 9: You have a deep desire to help others and make the world a better place.",
}

# Personality Number Descriptions
personality_descriptions = {
    1: "Personality 1: You are independent, self-reliant, and assertive. You often take the lead and enjoy being in control.",
    2: "Personality 2: You are gentle, cooperative, and sensitive. You have a calming presence and are a good listener.",
    3: "Personality 3: You are sociable, expressive, and creative. You love to engage with others and often have a playful nature.",
    4: "Personality 4: You are practical, disciplined, and reliable. You value order and structure in your life.",
    5: "Personality 5: You are adventurous, curious, and adaptable. You thrive on change and new experiences.",
    6: "Personality 6: You are nurturing, caring, and family-oriented. You prioritize your loved ones and enjoy creating harmony.",
    7: "Personality 7: You are introspective, analytical, and contemplative. You seek knowledge and enjoy spending time alone.",
    8: "Personality 8: You are ambitious, confident, and goal-oriented. You have strong leadership qualities and are driven to succeed.",
    9: "Personality 9: You are compassionate, humanitarian, and idealistic. You care deeply about others and strive to make a positive impact.",
}


# Function to calculate the Expression Number
def calculate_expression_number(full_name):
    full_name = full_name.upper()
    total = 0
    for letter in full_name:
        if (
            letter.isalpha() and letter in letter_to_number
        ):  # Ignore non-alphabet characters
            total += letter_to_number[letter]
    return reduce_to_single_digit(total)


# Function to calculate the Soul Urge Number with a detailed explanation
def calculate_soul_urge_number(full_name):
    full_name = full_name.upper()
    total = 0
    vowel_found = False  # Track if any vowel is found

    for letter in full_name:
        if letter in vowels:  # Sum only vowels
            total += letter_to_number[letter]
            vowel_found = True

    if not vowel_found:
        return (
            0,
            "The name you provided contains no vowels, which is why the Soul Urge Number is 0. "
            "The Soul Urge Number reflects your innermost desires and motivations, and since it is "
            "derived from vowels, a lack of vowels leads to a 0 result. You may want to reflect on "
            "how this unique characteristic of your name might influence your personal journey.",
        )

    return reduce_to_single_digit(total), ""


# Function to calculate the Personality Number
def calculate_personality_number(full_name):
    full_name = full_name.upper()
    total = 0
    for letter in full_name:
        if letter.isalpha() and letter not in vowels:  # Sum only consonants
            total += letter_to_number[letter]
    return reduce_to_single_digit(total)


# Function to calculate numerology numbers and show results
def calculate_numerology():
    full_name = name_entry.get()
    birthdate = birthdate_entry.get()

    # Validate birthdate input (must be 8 digits for MMDDYYYY format)
    if not birthdate.isdigit() or len(birthdate) != 8:
        messagebox.showerror(
            "Input Error", "Please enter a valid birthdate in MMDDYYYY format."
        )
        return

    # Perform the numerology calculations
    life_path_number = reduce_to_single_digit(sum_of_digits(birthdate))
    expression_number = calculate_expression_number(full_name)

    soul_urge_number, soul_urge_message = calculate_soul_urge_number(
        full_name
    )  # Updated calculation

    personality_number = calculate_personality_number(full_name)

    # Fetch descriptions from the dictionaries
    life_path_desc = life_path_descriptions.get(
        life_path_number, "No description available."
    )
    expression_desc = expression_descriptions.get(
        expression_number, "No description available."
    )
    soul_urge_desc = soul_urge_descriptions.get(
        soul_urge_number, "No description available."
    )
    personality_desc = personality_descriptions.get(
        personality_number, "No description available."
    )

    # Display results in a custom messagebox, including the soul urge message
    results = (
        f"Life Path Number: {life_path_number}\n{life_path_desc}\n\n"
        f"Expression Number: {expression_number}\n{expression_desc}\n\n"
        f"Soul Urge Number: {soul_urge_number}\n{soul_urge_desc}\n{soul_urge_message}\n\n"
        f"Personality Number: {personality_number}\n{personality_desc}"
    )
    custom_messagebox("Numerology Results", results)


# Custom messagebox function
def custom_messagebox(title, message):
    top = tk.Toplevel(root)
    top.title(title)
    top.geometry("600x800")
    top.configure(bg="#9370DB")  # Set background to light purple

    message_label = tk.Label(
        top,
        text=message,
        bg="#9370DB",
        fg="black",
        font=("Courier", 16),
        wraplength=300,
        justify="center",
    )
    message_label.pack(pady=20)

    close_button = tk.Button(
        top,
        text="Close",
        command=top.destroy,
        bg="white",
        fg="#4B0082",
        font=("Papyrus", 16),
    )
    close_button.pack(pady=10)


# Create the main window (define 'root' here)
root = tk.Tk()
root.title("Numerology Calculator")
root.geometry("600x500")
root.configure(bg="#4B0082")  # Indigo color for the window background

custom_font_title = ("Papyrus", 24, "bold")
custom_font_body = ("Courier", 20)

# Labels and entries for user input
name_label = tk.Label(
    root, text="Enter your full name:", bg="#4B0082", fg="white", font=custom_font_body
)
name_label.pack(pady=10)

name_entry = tk.Entry(root, font=custom_font_body, width=30)
name_entry.pack(pady=10)

birthdate_label = tk.Label(
    root,
    text="Enter your birthdate (MMDDYYYY):",
    bg="#4B0082",
    fg="white",
    font=custom_font_body,
)
birthdate_label.pack(pady=10)

birthdate_entry = tk.Entry(root, font=custom_font_body, width=30)
birthdate_entry.pack(pady=10)

# Button to calculate numerology
calculate_button = tk.Button(
    root,
    text="Reveal Your Numbers",
    command=calculate_numerology,
    bg="#9370DB",
    fg="white",
    font=custom_font_title,
)
calculate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
