import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("StatPulse Pro | Ungrouped Data Analyzer")
window.geometry('1250x640')
window.config(bg="#f0f0f0")
# window.attributes('-alpha', 0.85)

def on_focus_in(event):
    window.attributes('-alpha', 0.90)  # Solid when you are working

def on_focus_out(event):
    window.attributes('-alpha', 0.80) # Slightly see-through when you click away

window.bind("<FocusIn>", on_focus_in)
window.bind("<FocusOut>", on_focus_out)

# --- 1. Create a Container for Canvas and Scrollbar ---
container = tk.Frame(window)
container.pack(fill="both", expand=True)

# --- 2. Create the Canvas ---
canvas = tk.Canvas(container, bg="#f0f0f0")
canvas.pack(side="top", fill="both", expand=True)

# --- 3. Create the Horizontal Scrollbar ---
h_scroll = tk.Scrollbar(container, orient="horizontal", command=canvas.xview)
h_scroll.pack(side="bottom", fill="x")

# Connect Canvas to Scrollbar
canvas.configure(xscrollcommand=h_scroll.set)

# --- 4. Create the Mainframe INSIDE the Canvas ---
# Note: We use canvas.create_window instead of .grid() for the mainframe
mainframe = tk.Frame(canvas, padx=20, pady=20)
canvas_frame = canvas.create_window((0, 0), window=mainframe, anchor="nw")

# --- 5. Update Scrollregion when mainframe size changes ---
def on_frame_configure(event):
    # Reset the scroll region to encompass the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))

mainframe.bind("<Configure>", on_frame_configure)

frame_style = {
    'highlightbackground': "#d1d1d1", # Subtle grey instead of harsh black
    'highlightthickness': 1,
    'padx': 10,
    'pady': 10,
}

head = tk.Label(mainframe, text="STATPULSE  ANALYSIS  ENGINE", font=('arial', 25, 'underline'), fg="#2c3e50")
head.grid(row=0, column=0, columnspan=6, pady=(0, 10))

inframe=tk.Frame(mainframe)
inframe.grid(row=1,column=0,sticky='nsew')

status_label = tk.Label(
    inframe,
    text="SYSTEM STATUS",
    font=('arial', 10, 'bold'),
    fg="#7f8c8d",
    bg=inframe['bg'] # Matches parent background
)
status_label.pack(pady=(5, 0))

state = tk.Entry(
    inframe,
    font=('arial', 18, 'bold'),
    width=12,
    justify='center',
    relief='flat',           # Removes the 90s sunken border
    bg='#ecf0f1',            # Soft gray background
    fg='#2c3e50',            # Professional dark text
    readonlybackground='#ecf0f1', # Ensures bg stays the same when locked
    highlightthickness=2,    # Add a thin professional border
    highlightbackground="#bdc3c7"
)
state.pack(ipady=5) # ipady makes the box taller/chunkier
state.config(state='readonly')

tk.Label(inframe,text="\nEnter Data Here :-  ", font=('arial', 14),fg="#333333").pack(side='left')

outbox = tk.Text(mainframe, font=('arial', 20), width=20, height=9,
                 undo=True,          # Enables Undo/Redo stack
                 autoseparators=True, # Saves "checkpoints" for undo
                 maxundo=50,         # Prevents using too much memory
                 padx=10, pady=10,   # Internal padding for text
                 relief='flat',      # Modern flat look
                 highlightthickness=2,
                 highlightbackground="#cccccc", # Gray border when idle
                 highlightcolor="#4a90e2")      # Blue border when typing
outbox.grid(row=2, column=0, padx=10, rowspan=3, sticky="nsew")

outerframe = tk.Frame(mainframe, **frame_style)
outerframe.grid(row=1, column=1,sticky='nsew')

rangetit = tk.Label(outerframe, text="Range :- ", font=('arial', 14),fg="#333333")
rangetit.grid(row=0, column=0, sticky='w')

range_val_label = tk.Label(outerframe, text='0.0', font=('arial', 14, 'bold'))
range_val_label.grid(row=0, column=1, sticky='w')

avg=tk.Label(outerframe,text="Average :- ", font=('arial', 14),fg="#333333")
avg.grid(row=1, column=0, sticky='w')

avg_val_label = tk.Label(outerframe, text='0.0', font=('arial', 14, 'bold'))
avg_val_label.grid(row=1, column=1, sticky='w')

tk.Label(outerframe,text="Mode :- ", font=('arial', 14),fg="#333333").grid(row=2, column=0, sticky='w')

mode_val_label = tk.Label(outerframe, text='0.0', font=('arial', 14, 'bold'))
mode_val_label.grid(row=2, column=1, sticky='w')

tk.Label(outerframe,text="Median :- ", font=('arial', 14),fg="#333333").grid(row=3, column=0, sticky='w')

median_val_label = tk.Label(outerframe, text='0.0', font=('arial', 14, 'bold'))
median_val_label.grid(row=3, column=1, sticky='w')

outerframe2 = tk.Frame(mainframe, **frame_style)
outerframe2.grid(row=2, column=1,sticky='nsew') # 'n' keeps it aligned to the top

tk.Label(outerframe2,text="Variance :- ", font=('arial', 14),fg="#333333").grid(row=0, column=0, sticky='w')

variance_val_label = tk.Label(outerframe2, text='0.0', font=('arial', 14, 'bold'))
variance_val_label.grid(row=0, column=1, sticky='w')

tk.Label(outerframe2,text="Variance :- ", font=('arial', 14),fg="#333333").grid(row=0, column=0, sticky='w')

variance_val_label = tk.Label(outerframe2, text='0.0', font=('arial', 14, 'bold'))
variance_val_label.grid(row=0, column=1, sticky='w')

tk.Label(outerframe2,text="Standard Deviation :- ", font=('arial', 14),fg="#333333").grid(row=1, column=0, sticky='w')

stdevi_val_label = tk.Label(outerframe2, text='0.0', font=('arial', 14, 'bold'))
stdevi_val_label.grid(row=1, column=1, sticky='w')

tk.Label(outerframe2,text="Mean Deviation :- ", font=('arial', 14),fg="#333333").grid(row=2, column=0, sticky='w')

mean_val_label = tk.Label(outerframe2, text='0.0', font=('arial', 14, 'bold'))
mean_val_label.grid(row=2, column=1, sticky='w')

tk.Label(outerframe2,text="Interquartile Range :- ", font=('arial', 14),fg="#333333").grid(row=3, column=0, sticky='w')

quarrange_val_label = tk.Label(outerframe2, text='0.0', font=('arial', 14, 'bold'))
quarrange_val_label.grid(row=3, column=1, sticky='w')

tk.Label(outerframe2,text="Quartile Deviation :- ", font=('arial', 14),fg="#333333").grid(row=4, column=0, sticky='w')

quardevi_val_label = tk.Label(outerframe2, text='0.0', font=('arial', 14, 'bold'))
quardevi_val_label.grid(row=4, column=1, sticky='w')

tk.Label(outerframe2,text="Quartile Deviation :- ", font=('arial', 14),fg="#333333").grid(row=4, column=0, sticky='w')

quardevi_val_label = tk.Label(outerframe2, text='0.0', font=('arial', 14, 'bold'))
quardevi_val_label.grid(row=4, column=1, sticky='w')

outerframe3 = tk.Frame(mainframe, **frame_style)
outerframe3.grid(row=1, column=2,sticky='nsew') # 'n' keeps it aligned to the top

tk.Label(outerframe3,text="Quartile ONE :- ", font=('arial', 14),fg="#333333").grid(row=0, column=0, sticky='w')

quarone_val_label = tk.Label(outerframe3, text='0.0', font=('arial', 14, 'bold'))
quarone_val_label.grid(row=0, column=1, sticky='w')

tk.Label(outerframe3,text="Quartile TWO :- ", font=('arial', 14),fg="#333333").grid(row=1, column=0, sticky='w')

quartwo_val_label = tk.Label(outerframe3, text='0.0', font=('arial', 14, 'bold'))
quartwo_val_label.grid(row=1, column=1, sticky='w')

tk.Label(outerframe3,text="Quartile THREE :- ", font=('arial', 14),fg="#333333").grid(row=2, column=0, sticky='w')

quarthree_val_label = tk.Label(outerframe3, text='0.0', font=('arial', 14, 'bold'))
quarthree_val_label.grid(row=2, column=1, sticky='w')

outerframe4 = tk.Frame(mainframe, **frame_style)
outerframe4.grid(row=2, column=2,sticky='nsew') # 'n' keeps it aligned to the top

# --- Decile Section ---
tk.Label(outerframe4, text="Find Decile (1-9):", font=('arial', 14,'underline'), fg="#333333").grid(row=1, column=0, sticky='w', pady=(10,0))
entry_decile = tk.Entry(outerframe4, font=('arial', 14, 'bold'), width=5, justify='center')
entry_decile.grid(row=1, column=1, pady=(10,0))

tk.Label(outerframe4, text="Decile Value:", font=('arial', 14)).grid(row=2, column=0, sticky='w')
decile_val_label = tk.Label(outerframe4, text='0.0', font=('arial', 14, 'bold'), fg="#2c3e50")
decile_val_label.grid(row=2, column=1, sticky='w')

# --- Percentile Section ---
tk.Label(outerframe4, text="Find Percentile (1-99):", font=('arial', 14,'underline'), fg="#333333").grid(row=3, column=0, sticky='w', pady=(10,0))
entry_percentile = tk.Entry(outerframe4, font=('arial', 14, 'bold'), width=5, justify='center')
entry_percentile.grid(row=3, column=1, pady=(10,0))

tk.Label(outerframe4, text="Percentile Value:", font=('arial', 14)).grid(row=4, column=0, sticky='w')
percentile_val_label = tk.Label(outerframe4, text='0.0', font=('arial', 14, 'bold'), fg="#2c3e50")
percentile_val_label.grid(row=4, column=1, sticky='w')


def decile_percentile():
    # Helper function to reset the status box to error
    def set_error(msg):
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, f"ERR: {msg}")
        state.config(fg="red")
        state.config(state='readonly')

    try:
        # 1. Process Decile
        d_idx = entry_decile.get().strip()
        if d_idx:
            val = float(d_idx)
            # Logic Limit: Deciles must be between 1 and 9
            if 1 <= val <= 9:
                res_d = get_position_value(val, 10)
                decile_val_label.config(text=f"{res_d}", fg="#2c3e50")
            else:
                set_error("D (1-9)")
                return # Stop the function here

        # 2. Process Percentile
        p_idx = entry_percentile.get().strip()
        if p_idx:
            val = float(p_idx)
            # Logic Limit: Percentiles must be between 1 and 99
            if 1 <= val <= 99:
                res_p = get_position_value(val, 100)
                percentile_val_label.config(text=f"{res_p}", fg="#2c3e50")
            else:
                set_error("P (1-99)")
                return

        # If we reached here without returning, the input was valid
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, "GOOD")
        state.config(fg="green")
        state.config(state='readonly')

    except ValueError:
        # This triggers if the user enters letters or symbols
        set_error("NUMBERS ONLY")
        decile_val_label.config(text="---", fg="red")
        percentile_val_label.config(text="---", fg="red")

# --- Calculate Button ---
# --- Styled Calculate Position Button ---
subbtn = tk.Button(
    outerframe4,
    text='CALCULATE POSITION',
    font=('arial', 11, 'bold'),
    bg="#34495e",            # Elegant dark blue-grey
    fg="white",
    activebackground="#1abc9c", # Changes to Turquoise when clicked
    activeforeground="white",
    relief="flat",           # Removes the old-school 3D border
    cursor="hand2",          # Hand icon on hover
    bd=0,
    command=decile_percentile
)
subbtn.grid(row=5, column=0, columnspan=2, padx=10,pady=5, sticky="ew", ipady=8)

# --- Hover Effects (The "Charm" logic) ---
def on_sub_enter(e):
    subbtn.config(bg="#2c3e50", fg="#1abc9c") # Darker background, bright text

def on_sub_leave(e):
    subbtn.config(bg="#34495e", fg="white")   # Back to original

subbtn.bind("<Enter>", on_sub_enter)
subbtn.bind("<Leave>", on_sub_leave)


outerframe6 = tk.Frame(mainframe, **frame_style)
outerframe6.grid(row=3, column=1,sticky='nsew') # 'n' keeps it aligned to the top

tk.Label(outerframe6,text="Enter Data Here To Find", font=('arial', 14,'underline'),fg="#333333").grid(row=0, column=0, sticky='w',columnspan=2)

tk.Label(outerframe6,text="Z-Index Value", font=('arial', 14,'underline'),fg="#333333").grid(row=1, column=0, sticky='ew',columnspan=2)

outerframe8 = tk.Frame(outerframe6)
outerframe8.grid(row=2, column=0, columnspan=2) # 'n' keeps it aligned to the top

tk.Label(outerframe8,text="Index :- ", font=('arial', 14),fg="#333333").grid(row=0, column=0)

entry_zval=tk.Entry(outerframe8, font=('arial', 14, 'bold'), width=4,justify='center')
entry_zval.grid(row=0, column=1)

tk.Label(outerframe6,text="Z-Index Value :- ", font=('arial', 14),fg="#333333").grid(row=3, column=0)

zval_label = tk.Label(outerframe6, text='0.0', font=('arial', 14, 'bold'))
zval_label.grid(row=3, column=1, sticky='w')


def calculate_single_z():
    try:
        # 1. Get the specific number the user is looking for
        target_val_str = entry_zval.get().strip()
        if not target_val_str:
            return  # Do nothing if empty

        target_val = float(target_val_str)

        # 2. Get the main dataset from your outbox
        string = outbox.get("1.0", "end-1c")
        data = [float(x.strip()) for x in string.split(',') if x.strip()]

        # 3. Validation: Is the number actually in our data?
        if target_val not in data:
            state.config(state='normal')
            state.delete(0, tk.END)
            state.insert(0, "NOT IN DATA")
            state.config(fg="orange")
            state.config(state='readonly')
            zval_label.config(text="ERROR", fg="red")
            return

        # 4. Calculate Mean and SD (Using your existing functions)
        aver = average()
        sd = standard_deviation()

        if sd == 0:
            zval_label.config(text="SD IS 0")
            return

        # 5. The Z-Score Formula: (x - mean) / sd
        z_score = (target_val - aver) / sd

        # 6. Success! Update the UI
        zval_label.config(text=f"{z_score:.4f}", fg="#27ae60")

        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, "GOOD")
        state.config(fg="green")
        state.config(state='readonly')

    except ValueError:
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, "INVALID NUM")
        state.config(fg="red")
        state.config(state='readonly')

# --- Styled Calculate Z-Index Button ---
subbtn2 = tk.Button(
    outerframe6,
    text='CALCULATE Z-INDEX',
    font=('arial', 11, 'bold'),
    bg="#e67e22",            # Deep Orange / Carrot color
    fg="white",
    activebackground="#d35400", # Darker orange when clicked
    activeforeground="white",
    relief="flat",           # Modern flat look
    cursor="hand2",
    bd=0,
    command=calculate_single_z
)
subbtn2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="ew", ipady=8)

# --- Hover Effects ---
def on_zbtn_enter(e):
    subbtn2.config(bg="#d35400") # Shifts to a richer shade on hover

def on_zbtn_leave(e):
    subbtn2.config(bg="#e67e22") # Back to base orange

subbtn2.bind("<Enter>", on_zbtn_enter)
subbtn2.bind("<Leave>", on_zbtn_leave)

outerframe7 = tk.Frame(mainframe, **frame_style)
outerframe7.grid(row=3, column=2,sticky='nsew') # 'n' keeps it aligned to the top

tk.Label(outerframe7,text="Coefficient of Variation :- ", font=('arial', 14),fg="#333333").grid(row=0, column=0)

coefvar_label = tk.Label(outerframe7, text='0.0', font=('arial', 14, 'bold'))
coefvar_label.grid(row=0, column=1, sticky='w')

tk.Label(outerframe7,text="Coefficient of Skewness :- ", font=('arial', 14),fg="#333333").grid(row=1, column=0)

coefsk_label = tk.Label(outerframe7, text='0.0', font=('arial', 14, 'bold'))
coefsk_label.grid(row=1, column=1, sticky='w')

tk.Label(outerframe7, text='\n', font=('arial', 5, 'bold')).grid(row=2, column=1, sticky='w')

def mode():
    string = outbox.get("1.0", "end-1c")
    data = [x.strip() for x in string.split(',') if x.strip()]
    if not data:
        print("No data found")
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        return 0
    counts = [data.count(x) for x in data]
    max_count_index = counts.index(max(counts))
    # print('Mode is:', data[max_count_index])
    mode_val_label.config(text=str(data[max_count_index]))
    return data[max_count_index]

def range():
    string = outbox.get("1.0", "end-1c")
    data = [int(x.strip()) for x in string.split(',') if x.strip()]
    if not data:
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        return
    maximum = max(data)
    minimum = min(data)
    result = maximum - minimum
    range_val_label.config(text=str(result))
    # print('Range is:', result)

def median():
    string = outbox.get("1.0", "end-1c")
    data = sorted([int(x.strip()) for x in string.split(',') if x.strip()])
    if not data:
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        return
    n = len(data)
    if n % 2 != 0:
        res = data[n // 2]
    else:
        mid1 = data[n // 2 - 1]
        mid2 = data[n // 2]
        res = (mid1 + mid2) / 2
    median_val_label.config(text=str(res))
    # print('Median is:', res)


def average():
    string = outbox.get("1.0", "end-1c")
    data = [int(x.strip()) for x in string.split(',') if x.strip()]
    if not data:
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        # print("No data to calculate!")
        return
    avg = sum(data) / len(data)
    avg_val_label.config(text=f"{avg:.4f}")
    # print('Average is:', avg)
    return avg

def variance():
    string = outbox.get("1.0", "end-1c")
    data = [int(x.strip()) for x in string.split(',') if x.strip()]
    total=0
    aver=average()
    for x in data:
        mid=int(x)-aver
        midnext=mid**2
        total+=midnext
    var=total/len(data)
    variance_val_label.config(text=f"{var:.4f}")
    # print('Variance is:',var)
    return var

def standard_deviation():
    var = variance()
    st_devi = var ** 0.5
    # print('Standard Deviation:', st_devi)
    stdevi_val_label.config(text=f"{st_devi:.4f}")
    return st_devi

def mean_deviation():
    string = outbox.get("1.0", "end-1c")
    data = [int(x.strip()) for x in string.split(',') if x.strip()]
    if not data:
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        return 0
    aver = average()  # Ensure your average() function returns a value!
    total = 0
    for x in data:
        # Use abs() to ensure we get the POSITIVE distance
        distance = abs(x - aver)
        total += distance
    md = total / len(data)
    # print("Mean Deviation:", md)
    mean_val_label.config(text=f"{md:.4f}")
    return md


# Change 'state' to 'denominator' in the header
def get_position_value(value, denominator):
    string = outbox.get("1.0", "end-1c")

    # We use a try/except here just in case the data in the outbox is messy
    try:
        data = sorted([int(x.strip()) for x in string.split(',') if x.strip()])
    except ValueError:
        data = []

    if not data:
        # Now 'state' correctly refers to your Global Entry Box
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        return 0

    n = len(data)

    # Use 'denominator' here instead of 'state'
    pos = (n + 1) * (int(value) / int(denominator))

    index = int(pos) - 1
    index = max(0, min(index, len(data) - 1))

    result_value = data[index]
    return result_value

def quartile_deviation():
    # 1. Fetch values
    q1 = get_position_value(1, 4)
    q3 = get_position_value(3, 4)

    # 2. Refined Check:
    # We check if they are numbers AND if they aren't the 'Error 0'
    # provided by get_position_value when the outbox is empty.
    if (isinstance(q1, (int, float)) and isinstance(q3, (int, float))) and (q1 != 0 or q3 != 0):
        qd = (q3 - q1) / 2
        quardevi_val_label.config(text=f"{qd:.4f}", fg="black")
        return qd
    else:
        # This is now reachable if data is missing or invalid
        quardevi_val_label.config(text="ERROR", fg="red")
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'DATA ERROR')
        state.config(state='readonly', fg="red")
        return None

def coefficient_of_variation():
    sd = standard_deviation()
    aver = average()
    if aver == 0:
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        # print("Mean is 0; CV is undefined.")
        return 0
    cv = (float(sd) / float(aver)) * 100
    # print(f"Coefficient of Variation: {cv:.2f}%")
    coefvar_label.config(text=f"{cv:.4f}")
    return cv

def coefficient_of_skewness():
    aver = average()
    mo = mode()
    sd = standard_deviation()
    if sd == 0:
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')
        return 0
    cs = (float(aver) - float(mo)) / float(sd)
    # print(f"Coefficient of Skewness: {cs:.4f}")
    coefsk_label.config(text=f"{cs:.4f}")
    return cs

def interquartile_range():
    try:
        # Assuming get_position_value returns a float/int
        q1_val = get_position_value(1, 4)
        q3_val = get_position_value(3, 4)

        # Calculate using floats to keep decimals
        iqr = float(q3_val) - float(q1_val)

        # Update your UI label (from your previous code)
        quarrange_val_label.config(text=f"{iqr:.4f}")

        return iqr

    except Exception as e:
        # print(f"Error calculating IQR: {e}")
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')


def quartiles():
    try:
        # Get values - assuming these return numbers
        Q1 = get_position_value(1, 4)
        Q2 = get_position_value(2, 4)
        Q3 = get_position_value(3, 4)

        # Update labels with consistent 4-decimal precision
        quarone_val_label.config(text=f"{Q1:.4f}")
        quartwo_val_label.config(text=f"{Q2:.4f}")
        quarthree_val_label.config(text=f"{Q3:.4f}")

    except Exception as e:
        # If get_position_value fails (e.g. empty data), show error
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(state='readonly')


def calculate_z_scores():
    # 1. Clear existing data immediately (keeping header and separator)
    # This prevents old results from staying if the new calculation fails
    z_listbox.delete(2, tk.END)

    # 2. Get and clean data
    string = outbox.get("1.0", "end-1c")
    try:
        data = [float(x.strip()) for x in string.split(',') if x.strip()]
    except ValueError:
        data = []

    if not data:
        # Use your state box to show error
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, 'ERROR')
        state.config(fg="red", state='readonly')
        z_listbox.insert(tk.END, "Check Input Data!")
        return

    # 3. Get Mean and SD (These must return values!)
    aver = average()
    sd = standard_deviation()

    # Handle the math error where SD is 0 (all numbers are the same)
    if sd == 0:
        z_listbox.insert(tk.END, "SD is 0 - No Variation")
        return

    # 4. Calculate and Insert with "Alignment Charm"
    for x in data:
        z = (x - aver) / sd

        # PRO TIP: Use :<+10.2f to force the + or - sign.
        # This keeps the column perfectly straight even with negative numbers!
        display_text = f"{x:<12} | {z:<+10.2f}"

        z_listbox.insert(tk.END, display_text)

        # Optional: Add a subtle color to the text if it's an outlier (Z > 3 or Z < -3)
        if abs(z) > 3:
            z_listbox.itemconfig(tk.END, {'fg': 'red'})


def add_shortcuts(widget):
    # Undo & Redo
    widget.bind("<Control-z>", lambda e: widget.edit_undo())
    widget.bind("<Control-y>", lambda e: widget.edit_redo())

    # Copy, Paste, Cut (Standard behavior)
    widget.bind("<Control-c>", lambda e: widget.event_generate("<<Copy>>"))
    widget.bind("<Control-v>", lambda e: widget.event_generate("<<Paste>>"))
    widget.bind("<Control-x>", lambda e: widget.event_generate("<<Cut>>"))
    widget.bind("<Control-a>", lambda e: select_all(widget))

def select_all(widget):
    widget.tag_add("sel", "1.0", "end")
    return "break"  # Prevents default behavior

# Call the function
add_shortcuts(outbox)

# Create the menu
context_menu = tk.Menu(outbox, tearoff=0, font=('arial', 10))
context_menu.add_command(label="Undo", command=lambda: outbox.edit_undo())
context_menu.add_command(label="Redo", command=lambda: outbox.edit_redo())
context_menu.add_separator()
context_menu.add_command(label="Cut", command=lambda: outbox.event_generate("<<Cut>>"))
context_menu.add_command(label="Copy", command=lambda: outbox.event_generate("<<Copy>>"))
context_menu.add_command(label="Paste", command=lambda: outbox.event_generate("<<Paste>>"))
context_menu.add_separator()
context_menu.add_command(label="Clear All", command=lambda: outbox.delete("1.0", tk.END))

# Function to show menu on right click
def show_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

outbox.bind("<Button-3>", show_menu) # <Button-3> is right-click

outbox.config(bg="#f9f9f9", fg="#333333", insertbackground="black")


def final():
    # 1. Visual Feedback: Disable button and change color while processing
    mainbutton.config(text="CALCULATING...", state="disabled", bg="#95a5a6")
    mainbutton.update_idletasks()

    string = outbox.get("1.0", "end-1c")

    try:
        # 2. Data Cleaning & Validation
        # Using float allows for more flexible data input
        data = [float(x.strip()) for x in string.split(',') if x.strip()]

        if not data:
            raise ValueError("No numbers found")

        # 3. Update Status to GOOD using your charm design
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, "✔ GOOD")
        state.config(fg="#27ae60", highlightbackground="#27ae60")
        state.config(state='readonly')

        # 4. Run the calculation chain
        # Note: Some functions rely on others, so the order is fine
        range()
        average()
        mode()
        median()
        variance()
        standard_deviation()
        mean_deviation()
        quartile_deviation()
        coefficient_of_variation()
        coefficient_of_skewness()
        interquartile_range()
        quartiles()
        calculate_z_scores()

    except Exception as e:
        # 5. Universal Error Handling
        # This catches letters, empty boxes, or math errors (like division by zero)
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, "✘ ERROR")
        state.config(fg="#e74c3c", highlightbackground="#e74c3c")
        state.config(state='readonly')

        # Optional: Print the specific error to console for debugging
        print(f"System Error: {e}")

    finally:
        # 6. Reset the button state no matter what happens
        mainbutton.config(text="CALCULATE\nALL STATS", state="normal", bg="#27ae60")

# Create the button with a modern look
mainbutton = tk.Button(
    outerframe7,
    text='CALCULATE\nALL STATS',
    border=0,                  # We'll use highlight instead of old-school borders
    bg='#27ae60',              # A nice "Success" Green
    fg='white',                # High contrast text
    font=('arial', 16, 'bold'),
    padx=20,
    activebackground='#2ecc71', # Brightens when clicked
    activeforeground='white',
    cursor='hand2',            # Changes cursor to a hand for "clickability"
    command=final
)
mainbutton.grid(row=3, column=0, columnspan=2, pady=20, padx=10, sticky="nsew")

def on_enter(e):
    # 'raised' makes it look 3D, 'bg' changes the color
    mainbutton.config(bg='#2ecc71', relief='raised')

def on_leave(e):
    # 'flat' or 'groove' returns it to normal
    mainbutton.config(bg='#27ae60', relief='flat')

mainbutton.bind("<Enter>", on_enter)
mainbutton.bind("<Leave>", on_leave)


# def final():
#     # Change button text to show it's working
#     mainbutton.config(text="CALCULATING...", state="disabled", bg="#95a5a6")
#     mainbutton.update_idletasks()  # Force UI to update immediately
#
#     # ... your existing logic from the previous step ...
#     # (The try/except block we wrote earlier)
#
#     # After calculations are done, reset the button
#     mainbutton.config(text="CALCULATE\nALL STATS", state="normal", bg="#27ae60")

def update_status(status_type):
    state.config(state='normal')
    state.delete(0, tk.END)

    if status_type == "GOOD":
        state.insert(0, "✔ GOOD")
        state.config(
            fg="#27ae60",  # Green Text
            highlightbackground="#27ae60",  # Green Border
            highlightcolor="#27ae60"
        )
    else:
        state.insert(0, "✘ ERROR")
        state.config(
            fg="#e74c3c",  # Red Text
            highlightbackground="#e74c3c",  # Red Border
            highlightcolor="#e74c3c"
        )

    state.config(state='readonly')  # Lock it back


outerframe9 = tk.Frame(mainframe, padx=20)
outerframe9.grid(row=1, column=3, rowspan=3, sticky='nsew')

tk.Label(outerframe9, text="All Individual Z-Scores",font=('arial', 16, 'underline')).pack(pady=(0, 10))

z_container = tk.Frame(outerframe9)
z_container.pack(fill='both', expand=True)

# 1. Create the Scrollbar
z_scroll = tk.Scrollbar(z_container)
z_scroll.pack(side='right', fill='y')

# 2. Create the Listbox
# We use a 'courier' font so the numbers align perfectly in columns
z_listbox = tk.Listbox(z_container, font=('courier', 12), width=30, height=20,
                       yscrollcommand=z_scroll.set)
z_listbox.pack(side='left', fill='both', expand=True)

# 3. Link Scrollbar to Listbox
z_scroll.config(command=z_listbox.yview)

# Add a Header inside the listbox for clarity
z_listbox.insert(tk.END, f"{'Data (x)':<12} | {'Z-Score':<10}")
z_listbox.insert(tk.END, "-" * 28)

# Optional: Add a button to export or clear this specific list
tk.Button(outerframe9, text="Clear Z-List", font=('arial', 12,'bold'),border=3,
          command=lambda: z_listbox.delete(2, tk.END)).pack(pady=5)

def copy_all_results():
    try:
        # Gather data from all labels
        report_text = (
            "--- STATISTICAL REPORT ---\n"
            f"Mean: {avg_val_label.cget('text')}\n"
            f"Median: {median_val_label.cget('text')}\n"
            f"Mode: {mode_val_label.cget('text')}\n"
            f"Range: {range_val_label.cget('text')}\n"
            f"Variance: {variance_val_label.cget('text')}\n"
            f"Std Deviation: {stdevi_val_label.cget('text')}\n"
            f"Mean Deviation: {mean_val_label.cget('text')}\n"
            f"IQ Range: {quarrange_val_label.cget('text')}\n"
            f"Quartile Deviation: {quardevi_val_label.cget('text')}\n"
            f"Q1: {quarone_val_label.cget('text')} | Q2: {quartwo_val_label.cget('text')} | Q3: {quarthree_val_label.cget('text')}\n"
            f"Skewness: {coefsk_label.cget('text')}\n"
            f"Coeff. of Variation: {coefvar_label.cget('text')}\n"
            f"Decile Value: {decile_val_label.cget('text')}\n"
            f"Percentile Value: {percentile_val_label.cget('text')}\n"
            "--------------------------"
        )

        # THE FORCE STEPS:
        window.clipboard_clear()  # 1. Clear the system clipboard
        window.clipboard_append(report_text)  # 2. Append the text
        window.update()  # 3. Process the clipboard event IMMEDIATELY

        # Give a small visual hint in the status box too
        state.config(state='normal')
        state.delete(0, tk.END)
        state.insert(0, "COPIED!")
        state.config(state='readonly')

        messagebox.showinfo("Success", "Report copied to clipboard!")

    except Exception as e:
        messagebox.showerror("Error", f"Clipboard Error: {e}")


# Apply to your button (Make sure the button is in the right frame)
copy_btn = tk.Button(
    outerframe9,
    text="📋 COPY FULL REPORT",
    font=('arial', 12, 'bold'),
    bg="#2c3e50",            # Professional dark blue
    fg="white",
    relief="flat",
    cursor="hand2",
    command=copy_all_results
)
copy_btn.pack(pady=5, padx=20, fill='x', ipady=5)

# Optional: Add a hover effect to make it feel more "charming"
def on_copy_enter(e): copy_btn.config(bg="#34495e")
def on_copy_leave(e): copy_btn.config(bg="#2c3e50")
copy_btn.bind("<Enter>", on_copy_enter)
copy_btn.bind("<Leave>", on_copy_leave)

window.mainloop()