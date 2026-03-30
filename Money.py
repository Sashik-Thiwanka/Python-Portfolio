def moneyshow(value):
    notes = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
    result = {}

    for note in notes:
        # Calculate how many notes fit
        count = value // note
        # Assign the count (will be 0 if value < note)
        result[note] = count
        # Update the remaining value
        value %= note

    return result


from datetime import datetime


def addlist(tot):
    notes = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]

    # Get current date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Using 'with' ensures the file closes correctly even if an error occurs
    with open('Bill.txt', 'a') as file:
        file.write("-" * 40 + "\n")
        file.write(f"Date/Time: {now}\n")
        file.write(f"Total Expenditure: {tot}\n")
        file.write("Payment Breakdown:\n")

        local = moneyshow(tot)

        for x in notes:
            if x in local:
                file.write(f"\t{x:>4} Notes ->> {local[x]}\n")

        file.write("\n")

def abovesub():
    p=entry1.get()
    if p.isdigit():
        pnew='Rs '+str(p)+'.00'
        lab = 'You Have ' + str(pnew) + " With You, Let's See What is Happening\n\n"
        text1.insert(1.0, lab)
        value.config(text=pnew)
    elif p[-3]=='.':
        mid=p[-4::-1]
        midrup=mid[-1::-1]
        mident = p[-1:-3:-1]
        mident = mident[::-1]
        if midrup.isdigit():
            if mident.isdigit():
                pnew='Rs '+str(midrup)+'.'+str(mident)
                value.config(text=pnew)
                lab='You Have '+str(pnew)+" With You, Let's See What is Happening\n\n "
                text1.insert(1.0,lab)
            else:
                value.config(text='Not Valid')
        else:
            value.config(text='Not Valid')
    else:
        value.config(text='Not Valid')


def notemanage():
    p = entry2.get()

    # Validation & Variable Assignment
    try:
        mark = int(float(p))
    except ValueError:
        text1.insert(1.0, 'Sorry, that expenditure amount is invalid.\n\n')
        return

    diction = moneyshow(mark)
    addlist(mark)
    text1.insert(1.0, f'You Spent Rs.{mark}.00\n\n')

    # Calculate Balance
    try:
        current_text = value.cget("text")
        # Extract numbers only
        current_num = int(''.join(filter(str.isdigit, current_text.split('.')[0])))
        final_value = current_num - mark
        value.config(text=f'Rs {final_value}.00')
    except:
        final_value = 0

    if final_value < 0:
        text1.insert(1.0, "Very Sorry. You Have To Apply For a Bank Loan\n\n")
        value.config(fg='red')
        # Reset labels and STOP
        for lbl in [label5000, label1000, label500, label100, label50, label20, label10, label5, label2, label1]:
            lbl.config(text='0')
        return  # Important to stop here

    # Update Cumulative Totals
    # Dictionary mapping to prevent the label1/label2 mixup
    label_map = {
        5000: label5000, 1000: label1000, 500: label500, 100: label100,
        50: label50, 20: label20, 10: label10, 5: label5, 2: label2, 1: label1
    }

    for note, lbl in label_map.items():
        current_val = int(lbl.cget("text"))
        new_total = current_val + diction.get(note, 0)
        lbl.config(text=str(new_total))

def clearall():
    text1.delete(1.0,tk.END)
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    value.config(text='Rs 0.00', fg='green')

def clear():
    entry2.delete(0,tk.END)


import tkinter as tk
# from tkinter import ttk

window = tk.Tk()
window.geometry('700x575')
window.title('Money Pocket Managing Simple APP')

# --- Header Section ---
header_frame = tk.Frame(window)
header_frame.pack(fill='x', pady=20, padx=20)

tk.Label(header_frame, text='Initial Amount:', font=('arial', 12, 'bold')).grid(row=0, column=0, sticky='w')
entry1 = tk.Entry(header_frame, font=('arial', 15), width=20)
entry1.grid(row=0, column=1, padx=10)

tk.Button(header_frame, text='SET INITIAL', bg='#4CAF50', fg='white',
          font=('arial', 10, 'bold'), width=15,command=abovesub).grid(row=0, column=2, padx=5)

tk.Button(header_frame, text='CLEAR ALL', bg='red', fg='white',
          font=('arial', 10, 'bold'), width=15,command=clearall).grid(row=0, column=3, padx=5)

# --- Balance Display ---
balance_frame = tk.Frame(window, relief='groove', borderwidth=2)
balance_frame.pack(fill='x', padx=20, pady=10)

tk.Label(balance_frame, text='CURRENT BALANCE:', font=('arial', 14)).pack(side='left', padx=10, pady=10)
value = tk.Label(balance_frame, text='0.00', fg='green', font=('arial', 20, 'bold'))
value.pack(side='left', padx=10)

# --- Spenditure Input ---
input_frame = tk.LabelFrame(window, text=" Add Expenditure ", font=('arial', 10, 'italic'))
input_frame.pack(fill='x', padx=20, pady=10)

tk.Label(input_frame, text='Enter Amount:', font=('arial', 12)).grid(row=0, column=0, padx=10, pady=20)
entry2 = tk.Entry(input_frame, font=('arial', 15), width=20)
entry2.grid(row=0, column=1, padx=10)

tk.Button(input_frame, text='SUBMIT', bg='#2196F3', fg='white', width=10,command=notemanage).grid(row=0, column=2, padx=5)
tk.Button(input_frame, text='CLEAR', bg='#f44336', fg='white', width=10,command=clear).grid(row=0, column=3, padx=5)

# --- History and Denominations Section ---
# Split the bottom into two columns
bottom_container = tk.Frame(window)
bottom_container.pack(fill='both', expand=True, padx=20, pady=10)

# Left: Log/Text Area
history_frame = tk.Frame(bottom_container)
history_frame.pack(side='left', fill='both', expand=True)

tk.Label(history_frame, text="Transaction Log", font=('arial', 11, 'bold')).pack(anchor='w')
text1 = tk.Text(history_frame, width=40, font=('arial', 11), bg='#f9f9f9')
text1.pack(fill='both', expand=True, pady=5)

# Right: Denomination Calculator
calc_frame = tk.LabelFrame(bottom_container, text=" Payment Suggestion ", padx=10)
calc_frame.pack(side='right', fill='y', padx=(20, 0))

# 5000 Label
tk.Label(calc_frame, text="5000 >>>", font=('arial', 12)).grid(row=0, column=0, sticky='e', pady=2)
label5000 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label5000.grid(row=0, column=1, padx=10)

# 1000 Label
tk.Label(calc_frame, text="1000 >>>", font=('arial', 12)).grid(row=1, column=0, sticky='e', pady=2)
label1000 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label1000.grid(row=1, column=1, padx=10)

# 500 Label
tk.Label(calc_frame, text="500 >>>", font=('arial', 12)).grid(row=2, column=0, sticky='e', pady=2)
label500 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label500.grid(row=2, column=1, padx=10)

# ... (Repeat this pattern for 100, 50, 20, 10, 5, 2, 1) ...
# For the sake of brevity, ensure you change the row index (row=3, row=4, etc.) for each one.

tk.Label(calc_frame, text="100 >>>", font=('arial', 12)).grid(row=3, column=0, sticky='e', pady=2)
label100 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label100.grid(row=3, column=1, padx=10)


tk.Label(calc_frame, text="50 >>>", font=('arial', 12)).grid(row=4, column=0, sticky='e', pady=2)
label50 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label50.grid(row=4, column=1, padx=10)

tk.Label(calc_frame, text="20 >>>", font=('arial', 12)).grid(row=5, column=0, sticky='e', pady=2)
label20 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label20.grid(row=5, column=1, padx=10)

tk.Label(calc_frame, text="10 >>>", font=('arial', 12)).grid(row=6, column=0, sticky='e', pady=2)
label10 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label10.grid(row=6, column=1, padx=10)


tk.Label(calc_frame, text="5 >>>", font=('arial', 12)).grid(row=7, column=0, sticky='e', pady=2)
label5 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label5.grid(row=7, column=1, padx=10)

tk.Label(calc_frame, text="2 >>>", font=('arial', 12)).grid(row=8, column=0, sticky='e', pady=2)
label2 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label2.grid(row=8, column=1, padx=10)

tk.Label(calc_frame, text="1 >>>", font=('arial', 12)).grid(row=9, column=0, sticky='e', pady=2)
label1 = tk.Label(calc_frame, text='0', font=('arial', 12, 'bold'), width=5, anchor='w')
label1.grid(row=9, column=1, padx=10)

window.mainloop()