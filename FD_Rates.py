import tkinter as tk
import calendar
from tkinter import *

win=tk.Tk()
win.geometry('659x628')
win.title('FIXED DEPOSIT RATES')
win.configure(borderwidth=2 , background='#657383')

main_frame=Frame(win,bg='#2F3E46')
main_frame.grid()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def setting():
    p = entry1.get()
    q = entry2.get()
    try:
        p = float(p)
        q = float(q)
        label6.config(text='Good', fg='green')
        annual = p * (q / 100)

    except ValueError:
        if not is_number(entry1.get()):
            label6.config(text='Please Insert Numbers to Value', fg='red')
        elif not is_number(entry2.get()):
            label6.config(text='Please Insert Numbers to Percentage', fg='red')
        else:
            label6.config(text='Invalid Input', fg='red')
    return annual

def third_line():
    if v.get()==0:
        annual_rate()
    elif v.get()==1:
        t1=setting()*2
        label12.configure(text=t1)
        # label6.config(text=third_line(), fg='Black',bg='white')
        label11.configure(text='Two Year INT')
    elif v.get()==2:
        t1 = setting()*3
        label12.configure(text=t1)
        # label6.config(text=third_line(), fg='Black', bg='white')
        label11.configure(text='Three Year INT')
    elif v.get()==3:
        t1 = setting()*4
        label12.configure(text=t1)
        # label6.config(text=third_line(), fg='Black', bg='white')
        label11.configure(text='Four Year INT')
    elif v.get() == 4:
        t1 = setting()*5
        label12.configure(text=t1)
        # label6.config(text=third_line(), fg='Black', bg='white')
        label11.configure(text='Five Year INT')
    else:
        label6.configure(text='Please Select Above Year', fg='red')

def exit_app():
    win.destroy()

def reset_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label6.config(text="Good",fg='green')
    label12.config(text="Annual_rate")
    label10.config(text="Three-Month_rate")
    label8.config(text="One-Month_rate")


def annual_rate():
    t=setting()
    # label6.config(text=third_line(), fg='Black', bg='white')
    label12.configure(text=t)

def thr_month():
    r=setting()/4
    # label6.config(text=third_line(), fg='Black', bg='white')
    label10.configure(text=r)

def one_month():
    s=setting()/12
    # label6.config(text=third_line(), fg='Black', bg='white')
    label8.configure(text=s)

frame1=tk.Frame(main_frame,bg="#D8D5E1", padx=5, pady=5)
frame1.grid(padx=20, pady=20,row=0,sticky='ew')

label1=Label(frame1,text='Fixed Deposit Rates', font=('arial',27,'underline') , bg='#D8D5E1')
label1.pack(anchor="center", padx=5, pady=5)

frame10=Frame(main_frame,background='#657383')
frame10.grid(row=2)

label101=Label(frame10,text='Opened Month as num:   ',font=('arial',10,'italic'),bg='#D8D5E1')
label101.pack(side='left')

entry102=Entry(frame10,width=3,font=('arial',10),justify='center')
entry102.pack(side='left')

label103=Label(frame10,text='     ', bg='#2F3E46')
label103.pack(side='left')

label104=Label(frame10,text='Opened date as num:   ',font=('arial',10,'italic'),bg='#D8D5E1')
label104.pack(side='left')

entry105=Entry(frame10,width=3,font=('arial',10),justify='center')
entry105.pack(side='left')

label106=Label(frame10,text='     ', bg='#2F3E46')
label106.pack(side='left')

label107=Label(frame10,text='Time Period:   ',font=('arial',10,'italic'),bg='#D8D5E1')
label107.pack(side='left')

entry108=Entry(frame10,width=3,font=('arial',10),justify='center')
entry108.pack(side='left')

label109=Label(frame10,text='    ', bg='#2F3E46')
label109.pack(side='left')

label110=Label(frame10,text='Year:   ',font=('arial',10,'italic'),bg='#D8D5E1')
label110.pack(side='left')

entry111=Entry(frame10,width=5,font=('arial',10),justify='center')
entry111.pack(side='left')

frame2=tk.Frame(main_frame,bg='#2F3E46')
frame2.grid(row=3,sticky='ew',pady=20,padx=20)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)

entry1=Entry(frame2,width=20, font=('arial',15),justify='center')
entry1.grid(row=0,column=0,sticky='w')

entry2=Entry(frame2,width=10, font=('arial',15),justify='center')
entry2.grid(row=0,column=1,sticky='e')
entry2.insert(0,6.5)

label2=Label(frame2, text='Please Enter Your Amount: Rs._' , font=('arial',10,'italic'), bg='#D8D5E1')
label2.grid(row=1,column=0,sticky='w',padx=6)

label3=Label(frame2, text='Annual Percentage: _%', font=('arial',10,'italic'), bg='#D8D5E1')
label3.grid(row=1,column=1,sticky='e',padx=6)

#------------------------------------------------------------------------------

def on_entry_click(event):
    if entry1.get() == placeholder_text:
        entry1.delete(0, "end")
        entry1.config(fg='black')

def on_focusout(event):
    if entry1.get() == '':
        entry1.insert(0, placeholder_text)
        entry1.config(fg='grey')

placeholder_text = "400000"
entry1.insert(0, placeholder_text)
entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focusout)

#------------------------------------------------------------------------------

linebreak='''---------------------------------------------------------------------------------------'''

frame3=tk.Frame(main_frame,bg='#2F3E46')
frame3.grid(padx=20,row=4,sticky='ew')

label4=Label(frame3, text=linebreak , font=('arial',15), bg='#2F3E46',fg='yellow')
label4.pack()

inner_frame = Frame(frame3, bg='#2F3E46')
inner_frame.pack()

label5 = Label(inner_frame, text='Status : ', font=('arial', 10), bg='#2F3E46', fg='white')
label5.pack(side='left', padx=5)

label6 = Label(inner_frame, text='Yet Good', font=('arial', 10), bg='yellow', fg='green',border=5 , borderwidth=5)
label6.pack(side='left', padx=5,pady=5)

frame6=Frame(main_frame, bg='#003366')
frame6.grid(row=5, sticky='ew',padx=20)
frame6.grid_columnconfigure(0,weight=1)

inner=Frame(frame6)
inner.pack()

v = IntVar()
options = ['1 Year', '2 Year', '3 Year', '4 Year', '5 Year']

for i, text in enumerate(options):
    frame = Frame(inner, bd=10, relief='groove')
    frame.pack(side='left',padx=6, pady=2)
    Radiobutton(
        frame,
        text=text,
        variable=v,
        value=i,
        font=('Arial', 10),
        height=1,
        width=5
    ).pack()

frame109=Frame(main_frame,bg='#003366')
frame109.grid(row=6, sticky='ew',padx=20)
frame109.grid_columnconfigure(0,weight=1)

label0=Label(frame109,text='Your Renewal Dates Will Show-Up Here', font=('arial', 10),bg='#D4af37')
label0.grid(row=0,sticky='ew',pady=6)

#------------------------------------------------------------------------------------------------

def setting3():
    pq = entry111.get()
    try:
        pq = float(pq)
        return pq

    except ValueError:
        if not is_number(entry111.get()):
            label6.config(text='Please Insert Numbers to Year', fg='red')
        else:
            label6.config(text='Invalid Input', fg='red')

def setting2():
    p = entry102.get()
    q = entry105.get()
    r = entry108.get()
    try:
        p = int(p)
        q = int(q)
        r = int(r)
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if p<=12:
            if q<31:
                start_year = int(setting3())  # or any given starting year
                start_day = int(entry105.get())  # You can customize this if needed
                start_month = f"Deposit Start Month : {months[p - 1]}-{start_year}"
                end_dates = ''

                # Loop through months with step r
                for ij in range(0, 12, r):
                    month_index = (p - 1 + ij) % 12
                    year_offset = (p - 1 + ij) // 12
                    current_year = start_year + year_offset

                    # Format as "01-January-2025"
                    end_dates += f"{start_day:02d}-{months[month_index]}-{current_year}, "

                # Strip trailing comma and space
                formatted_dates = end_dates.strip().rstrip(',')

                # Update labels
                label6.configure(text=start_month, bg='white', fg='black')
                label0.configure(text=formatted_dates, fg='black')

                return formatted_dates


            elif q==31:
                start_year =int(setting3())

                start_month = 'Start Month :' + months[p - 1]
                i = 0
                added_months = []

                # Loop for up to 24 months max (two rounds), every r months
                while True:
                    month_index = (p - 1 + i) % 12
                    year_offset = (p - 1 + i) // 12
                    year = start_year + year_offset
                    month_number = month_index + 1

                    # Stop if we've reached one full year past the starting month
                    if year > start_year + 1 or (year == start_year + 1 and month_index >= p - 1):
                        break

                    max_day = calendar.monthrange(year, month_number)[1]
                    if q <= max_day:
                        label = f"{months[month_index]}-{q} ({year})"
                    else:
                        if month_index + 1 < 12:
                            next_month_index = month_index + 1
                            label = f"{months[next_month_index]}-1 ({year})"
                        else:
                            label = f"{months[0]}-1 ({year + 1})"  # Wrap to Jan next year

                    added_months.append(label)
                    i += r

                # Format the result
                k = ', '.join(added_months)
                label6.configure(text=start_month, bg='white', fg='black')
                # print("Extended 2-round output:", k)
                label0.configure(text=k , fg='black')

                return k

            else:
                label6.configure(text='Please Insert Valid Date', bg='white', fg='black')
        else:
                label6.configure(text='Please Insert Valid Month', bg='white', fg='black')

    except ValueError:
        if not is_number(entry102.get()):
            label6.config(text='Please Insert Numbers to Month', fg='red')
        elif not is_number(entry105.get()):
            label6.config(text='Please Insert Numbers to Date', fg='red')
        elif not is_number(entry108.get()):
            label6.config(text='Please Insert Numbers to Period', fg='red')
        else:
            label6.config(text='Invalid Input', fg='red')
        return None

#------------------------------------------------------------------------------------------------

button5=Button(frame109,text='Look Dates',border=5,command=setting2,font=('arial',10))
button5.grid(row=0,sticky='e',pady=6)

frame4=Frame(main_frame, bg='#003366')
frame4.grid(row=7, sticky='ew', padx=20)
frame4.grid_columnconfigure(0,weight=1)

label7=Label(frame4,text='1 Month Interest :', font=('arial', 10),bg='#D8D5E1')
label7.grid(row=0,sticky='w')

label8=Label(frame4,text='one_month_value', font=('arial', 10),bg='#D4af37')
label8.grid(row=0)

button1=Button(frame4,text='CLICK', font=('arial', 10),border=5, command=one_month)
button1.grid(row=0,sticky='e')

label9=Label(frame4,text='3 Month Interest :', font=('arial', 10),bg='#D8D5E1')
label9.grid(row=1,sticky='w',pady=25)

label10=Label(frame4,text='three-month_value', font=('arial', 10),bg='#D4af37')
label10.grid(row=1)

button2=Button(frame4,text='CLICK', font=('arial', 10),border=5,command=thr_month)
button2.grid(row=1,sticky='e')

label11=Label(frame4,text='Yearly Interest :', font=('arial', 10),bg='#D8D5E1')
label11.grid(row=2,sticky='w')

label12=Label(frame4,text='Above_Years_Values', font=('arial', 10),bg='#D4af37')
label12.grid(row=2,pady=5)

button3=Button(frame4,text='CLICK', font=('arial', 10),border=5,command=third_line)
button3.grid(row=2,sticky='e')

frame5=Frame(main_frame, bg='#2e8b57')
frame5.grid(row=8, sticky='ew',pady=5, padx=20)
frame5.grid_columnconfigure(0,weight=1)

label00=Label(frame5,text=linebreak, font=('arial', 15),bg='#2F3E46',fg='yellow')
label00.grid(row=0,pady=10)

button4=Button(frame5,text='Reset', font=('arial', 10),command=reset_fields,border=10)
button4.grid(row=1,sticky='w')

button4=Button(frame5,text='Exit', font=('arial', 10),command=exit_app , border=10)
button4.grid(row=1,sticky='e')

label13=Label(frame5,text='@All Rights Reserved', font=('arial', 10), bg='#2e8b57')
label13.grid(row=1,pady=5)

win.mainloop()