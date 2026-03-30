def universal_to_decimal(anysys, number):
    # This string maps the character to its value based on its index
    glyphs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 1. Validate Base Range
    if not (2 <= anysys <= 36):
        print(f"Error: Base {anysys} is out of range. Please use a base between 2 and 36.")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return None

    number = str(number).upper()
    total = 0
    length = len(number)

    for i in range(length):
        char = number[i]

        # 2. Check if character exists in glyphs
        if char not in glyphs:
            print(f"Error: Invalid character '{char}' found. Use only 0-9 and A-Z.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

        value = glyphs.index(char)

        # 3. Check if digit is valid for the chosen base
        if value >= anysys:
            print(f"Error: Digit '{char}' is too large for base {anysys}.")
            print(f"In base {anysys}, the highest possible digit is '{glyphs[anysys - 1]}'.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

        # Calculate power (positional value)
        power = length - 1 - i
        total += value * (anysys ** power)

    return total


def x_to_the_power(con_base, decimal):
    # This string maps numbers to their character equivalents
    glyphs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # --- ERROR HANDLING ---
    # 1. Check if the base is valid (cannot be 0, 1, or negative)
    if con_base < 2:
        print(f"Error: Base {con_base} is invalid. The base must be 2 or greater.")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return None

    # 2. Check if the base exceeds our available characters (max 36)
    if con_base > 36:
        print(f"Error: Base {con_base} is too large. Maximum supported base is 36.")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return None

    # 3. Handle negative decimal inputs (not supported by this logic)
    if decimal < 0:
        print(f"Error: Input decimal {decimal} must be a non-negative integer.")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return None

    # --- CORE LOGIC ---
    if decimal == 0:
        return "0"

    # 1. GENERATE POWERS
    con_list = []
    exponent = 0
    while (con_base ** exponent) <= decimal:
        con_list.append(con_base ** exponent)
        exponent += 1
    con_list = con_list[::-1]

    # 2. CALCULATE DIGITS & CONVERT TO LETTERS
    result_string = ""
    remaining = decimal
    for power in con_list:
        digit = remaining // power

        # Double check that the digit doesn't break the glyph index
        if digit < len(glyphs):
            result_string += glyphs[digit]
        else:
            print(f"Error: Digit {digit} exceeds character map. Check logic.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

        remaining %= power

    return result_string

# octal to binary
def threebythree(octal):
    # 1. Input Type Validation
    # Ensure the input is something we can iterate over or convert to string
    try:
        string = str(octal)
    except Exception as e:
        print(f"Error: Could not convert input to string. {e}")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return None

    # 2. Empty Input Check
    if not string:
        print("Error: Input is empty.")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return ""

    things = []
    main = []

    for x in string:
        # 3. Handle non-digit characters (like decimals or letters)
        if not x.isdigit():
            print(f"Error: '{x}' is not a valid digit. Octal numbers only contain 0-7.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None  # Or you could use 'continue' to skip it

        x_int = int(x)

        # 4. Octal Range Validation (0-7)
        if x_int >= 8:
            print(f"Error: '{x_int}' is not an octal digit. Octal digits must be less than 8.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            # Note: The 'break' here would stop the whole process;
            # returning None makes it clear the conversion failed.
            return None

        things.append(x_int)

        # Call your previous function to get binary
        middle = x_to_the_power(2, x_int)

        # 5. Safety check for internal function return
        if middle is None:
            print(f"Error: Internal conversion failed for digit {x_int}.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

        # Pad with leading zeros to ensure 3-bit groups
        if len(middle) < 3:
            do = 3 - len(middle)
            for _ in range(do):
                middle = '0' + str(middle)

        for bit in middle:
            main.append(bit)

    # 6. Final Console Feedback
    print(f"Successfully converted octal {string} to binary list: {main}")


    final_string = ''
    for bit in main:
        final_string = final_string + str(bit)

    return final_string


def threeback(binary):
    # 1. Type Safety: Ensure we are working with a string
    binary = str(binary)

    # 2. Validation: Check if input is empty
    if not binary:
        print("Error: Input is empty. Please provide a binary string.")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return ""

    # 3. Validation: Ensure the string only contains 0s and 1s
    for char in binary:
        if char not in '01':
            print(f"Error: Invalid character '{char}' detected. Binary must only contain 0 and 1.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

    length = len(binary)
    original = length

    # Padding logic
    if length % 3 == 0:
        print('Confirmed: Input length is a multiple of 3.')
    else:
        print(f"Input length {original} is not a multiple of 3. Padding with leading zeros...")
        while length % 3:
            length += 1
        # No change to return, keeping logic as requested

    due = length - original
    for x in range(due):
        binary = "0" + binary

    items = []
    for x in binary:
        items.append(x)

    print(f"Processed bits: {items}")

    # Grouping into 3-bit chunks
    braked = ["".join(map(str, items[i:i + 3])) for i in range(0, len(items), 3)]
    print(f"Binary groups: {braked}")

    string = ''
    for x in braked:
        # 4. Conversion Check: Ensure universal_to_decimal succeeds
        # Using try/except in case the external function encounters a base error
        try:
            # Important: we pass x as a string to preserve leading zeros if needed
            converted_val = universal_to_decimal(2, x)
            if converted_val is None:
                print(f"Error: Conversion failed for group {x}.")
                status.config(state='normal', fg='red')
                status.delete(0, tk.END)
                status.insert(0, 'Error')
                status.config(state='readonly')
                return None
            string = string + str(converted_val)
        except Exception as e:
            print(f"Unexpected error during conversion of group {x}: {e}")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

    return string

# octal to binary
def fourbyfour(hex_string):
    # Mapping for all Hex digits to their 4-bit binary strings
    hex_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # 1. Check for empty input or None
    if hex_string is None or str(hex_string).strip() == "":
        print("Error: Input is empty. Please provide a hexadecimal string (e.g., '1A3F').")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return None

    # Clean the input: convert to string, remove spaces, and make uppercase
    hex_string = str(hex_string).strip().upper()
    binary_result = []

    print(f"Processing Hexadecimal input: {hex_string}")


    for char in hex_string:
        # 2. Detailed validation for each character
        if char not in hex_map:
            print(f"Error: '{char}' is not a valid hexadecimal digit.")
            print("Valid digits are 0-9 and A-F (or a-f).")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            # Returning None clearly signals the failure
            return None

        # Get the 4-bit string and convert to individual integers
        bits = hex_map[char]
        for bit in bits:
            binary_result.append(int(bit))

    # 3. Final construction of the string
    string = ''
    for x in binary_result:
        string += str(x)

    print(f"Success! Resulting Binary: {string}")
    return string


# Example: Hex 'A1' -> [1, 0, 1, 0, 0, 0, 0, 1]
# fourbyfour("A1")
#
def fourback(binary):
    # 1. Type and Content Validation
    binary = str(binary).strip()  # Clean whitespace

    if not binary:
        print("Error: Input is empty. Please provide a binary string (e.g., '1101').")
        status.config(state='normal', fg='red')
        status.delete(0, tk.END)
        status.insert(0, 'Error')
        status.config(state='readonly')
        return None

    # Check for invalid characters (must be only 0 or 1)
    for char in binary:
        if char not in '01':
            print(f"Error: Invalid character '{char}' detected. Binary strings only allow 0 and 1.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

    length = len(binary)

    # 2. PADDING logic (making it divisible by 4)
    if length % 4 != 0:
        due = 4 - (length % 4)
        print(f"Note: Binary length {length} is not divisible by 4. Adding {due} leading zero(s).")
        binary = ("0" * due) + binary
    else:
        print("Confirmed: Input length is already a multiple of 4.")

    # 3. GROUPING logic
    braked = [binary[i:i + 4] for i in range(0, len(binary), 4)]
    print(f"Binary Nibbles: {braked}")

    # 4. CONVERSION logic (Handling A-F)
    glyphs = "0123456789ABCDEF"
    hex_result = ""

    for group in braked:
        # Check if internal function is available
        try:
            decimal_val = universal_to_decimal(2, group)

            if decimal_val is None:
                print(f"Error: universal_to_decimal failed for group {group}.")
                status.config(state='normal', fg='red')
                status.delete(0, tk.END)
                status.insert(0, 'Error')
                status.config(state='readonly')
                return None

            # Use that decimal number to pick the right Hex character
            hex_result += glyphs[decimal_val]

        except NameError:
            print("Error: The function 'universal_to_decimal' is not defined.")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            status.config(state='normal', fg='red')
            status.delete(0, tk.END)
            status.insert(0, 'Error')
            status.config(state='readonly')
            return None

    print(f"Success! Final Hexadecimal: {hex_result}")
    return hex_result

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('Converter')
window.geometry('450x400')
window.resizable(False, False)

frame = Frame(window)
frame.pack(fill="both", expand=True, padx=20, pady=10)

# Centering columns
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

title = Label(frame, font=('arial', 18, 'bold'), text='NUMBER SYSTEM CONVERTER')
title.grid(row=0, columnspan=2, pady=(10, 20))

# Labels for selection
Label(frame, text="From:", font=('arial', 10, 'bold')).grid(row=1, column=0, sticky='w', padx=10)
Label(frame, text="To:", font=('arial', 10, 'bold')).grid(row=1, column=1, sticky='w', padx=10)

inbox = tk.Listbox(frame, selectmode=tk.SINGLE, font=('arial', 11), height=4, exportselection=0)
inbox.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')

outbox = tk.Listbox(frame, selectmode=tk.SINGLE, font=('arial', 11), height=4, exportselection=0)
outbox.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')

items = ["Decimal", "Binary", "Octal", "Hexa-Decimal"]
for item in items:
    inbox.insert(tk.END, item)
    outbox.insert(tk.END, item)

# Labels for Input/Output
Label(frame, text="Enter Number Here:", font=('arial', 11)).grid(row=3, column=0, pady=(20, 5))
Label(frame, text="Result Appears Here:", font=('arial', 11)).grid(row=3, column=1, pady=(20, 5))

input_entry = Entry(frame, font=('arial', 14), justify='center')
input_entry.grid(row=4, column=0, padx=10, pady=5, sticky='ew')

output_entry = Entry(frame, font=('arial', 14), justify='center', fg="blue")
output_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

status=Entry(frame,font=('arial',15), width=10)
status.grid(row=5,columnspan=2,pady=10)
status.insert(0,'State')

status.config(fg='blue', justify='center',state="readonly")


def finalcommand():
    output_entry.delete(0, tk.END)
    # Get user selections
    try:
        from_idx = inbox.curselection()[0]
        to_idx = outbox.curselection()[0]
    except IndexError:
        output_entry.insert(0, "Select Systems!")
        return
    val = input_entry.get().strip()
    if not val: return

    status.config(state='normal',fg='green')
    status.delete(0, tk.END)
    status.insert(0,'Good')
    status.config(state='readonly')

    if from_idx==0:
        if to_idx==0:
            output_entry.insert(0,val)
            status.config(state='normal', fg='green')
            status.delete(0, tk.END)
            status.insert(0, 'Very Funny')
            status.config(state='readonly')
        elif to_idx==1:
            mark=x_to_the_power(2,int(val))
            output_entry.insert(0,mark)
        elif to_idx==2:
            mark=x_to_the_power(8,int(val))
            output_entry.insert(0,mark)
        elif to_idx==3:
            mark=x_to_the_power(16,int(val))
            output_entry.insert(0,mark)
    elif from_idx==1:
        if to_idx==0:
            mark=universal_to_decimal(2,int(val))
            output_entry.insert(0,mark)
        elif to_idx==1:
            output_entry.insert(0, val)
            status.config(state='normal', fg='green')
            status.delete(0, tk.END)
            status.insert(0, 'Very Funny')
            status.config(state='readonly')
        elif to_idx==2:
            mark = threeback(int(val))
            if mark is not None:
                output_entry.insert(0, mark)
        elif to_idx==3:
            mark=fourback(int(val))
            output_entry.insert(0,mark)
    elif from_idx==2:
        if to_idx==0:
            mark=universal_to_decimal(8,int(val))
            output_entry.insert(0,mark)
        elif to_idx==1:
            mark=threebythree(int(val))
            output_entry.insert(0,mark)
        elif to_idx==2:
            status.config(state='normal', fg='green')
            status.delete(0, tk.END)
            status.insert(0, 'Very Funny')
            status.config(state='readonly')
            output_entry.insert(0,int(val))
        elif to_idx==3:
            mark1 = threebythree(val)  # Keep as string
            mark2 = fourback(mark1)  # Passes string to fourback
            output_entry.insert(0, mark2)
    elif from_idx==3:
        if to_idx==0:
            mark=universal_to_decimal(16,val)
            output_entry.insert(0,mark)
        elif to_idx==1:
            mark=fourbyfour(val)
            output_entry.insert(0,mark)
        elif to_idx==2:
            mark1=fourbyfour(val)
            mark2=threeback(mark1)
            output_entry.insert(0,mark2)
        elif to_idx==3:
            status.config(state='normal', fg='green')
            status.delete(0, tk.END)
            status.insert(0, 'Very Funny')
            status.config(state='readonly')
            output_entry.insert(0,val)

def clear():
    input_entry.delete(0,tk.END)
    output_entry.delete(0,tk.END)
    inbox.selection_clear(0, tk.END)
    outbox.selection_clear(0, tk.END)
    status.config(state='normal',fg='blue')
    status.delete(0, tk.END)
    status.insert(0,'State')
    status.config(state='readonly')

convert_btn = Button(frame, text="CONVERT", bg="green", fg="white", font=('arial', 12, 'bold'),
                    width=15, border=8,command=finalcommand)
convert_btn.grid(row=6, column=0, pady=30)

clear_btn = Button(frame, text="CLEAR", bg="green", fg="white", font=('arial', 12, 'bold'),
                    width=15, border=8,command=clear)
clear_btn.grid(row=6, column=1, pady=30)

window.mainloop()