import tkinter as tk
from tkinter import *

win=tk.Tk()
win.title('Calculator')
win.geometry('1200x600')
win.config(bg='#ffe4c4')

win.attributes('-alpha', 0.8)  # 90% window transparency

def inverse():
    p=entry1.get()
    entry1.delete(0,'end')
    if p.isdigit():
        p=float(p)
        if p!=0:
            inv=(1/p)
        else:
            inv='Error'
    else:
        inv='Error'
    entry1.insert('end',inv)



import math

def calculate_ln():
    try:
        num = float(entry1.get())
        result = math.log(num)  # ln(x), where base is e
        entry1.delete(0, 'end')
        entry1.insert(0, str(result))
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "Error")


def factorial(x):
    p=1
    if x==0:
        fac=1
    elif x<0:
        fac='Error'
    else:
        while x>0:
            p=p*x
            x=x-1
        fac=p
    return fac

def button28():
    a=entry1.get()
    entry1.delete(0, tk.END)
    if a.isdigit():
        a=int(a)
        ans=factorial(a)
        entry1.insert('end',ans)
    else:
        entry1.delete(0,tk.END)
        entry1.insert(0,'Error')

def ex(x):
    try:
        x = float(x)
        if x < 0:
            return 'Error'
        result = sum((x ** ij) / factorial(ij) for ij in range(10))
        return result
    except ValueError:
        return 'Error'



def button23():
    k=entry1.get()
    entry1.delete(0,tk.END)
    ans=ex(k)
    entry1.insert(0,ans)

def C():
    entry1.delete(0,'end')
    entry1.insert('end','0')

def press_1():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '1')
    else:
        entry1.insert('end', '1')

def press_2():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '2')
    else:
        entry1.insert('end', '2')

def press_3():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '3')
    else:
        entry1.insert('end', '3')

def press_4():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '4')
    else:
        entry1.insert('end', '4')

def press_5():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '5')
    else:
        entry1.insert('end', '5')

def press_6():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '6')
    else:
        entry1.insert('end', '6')

def press_7():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '7')
    else:
        entry1.insert('end', '7')

def press_8():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '8')
    else:
        entry1.insert('end', '8')

def press_9():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '9')
    else:
        entry1.insert('end', '9')

def press_0():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '0')
    else:
        entry1.insert('end', '0')

def press_00():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '00')
    else:
        entry1.insert('end', '00')

def press_dot():
    current = entry1.get()
    if current == '0':  # if only a zero is present
        entry1.delete(0, 'end')
        entry1.insert(0, '0.')
    else:
        entry1.insert('end', '.')

def cuberoot():
    h=entry1.get()
    entry1.delete(0,'end')
    if h.isdigit():
        h=int(h)
        entry1.delete(0,tk.END)
        cubrt=h**(1/3)
        entry1.insert('end',cubrt)
    else:
        entry1.insert('end', 'Error')

def squareroot():
    h=entry1.get()
    entry1.delete(0, 'end')
    if h.isdigit():
        h=int(h)
        entry1.delete(0,tk.END)
        sqrt=h**(1/2)
        entry1.insert('end',sqrt)
    else:
        entry1.insert('end', 'Error')

def delete_last_character():
    current_text = entry1.get()
    if current_text:  # check if it's not empty
        entry1.delete(0, 'end')  # clear the Entry
        entry1.insert(0, current_text[:-1])  # insert all but the last character

def evaluate_expression():
    f=entry1.get()
    entry1.delete(0,tk.END)
    # Replace 'x' with '*' for proper multiplication syntax
    expr = f.replace('x', '*')
    expr = expr.replace('mod','%')
    expr = expr.replace('quo','//')
    expr = expr.replace('^', '**')
    expr = expr.replace('and','&')
    expr = expr.replace('or', '|')
    expr = expr.replace('xor', '^')
    expr = expr.replace('AND','and')
    expr = expr.replace('OR', 'or')
    expr = expr.replace('NOT', 'not')

    try:
        result = eval(expr)
        entry1.insert('end',result)
    except Exception as e:
        entry1.insert('end', 'Error')
        return f"Error: {e}"

def subtraction():
    if entry1.get()=='0':
        entry1.delete(0,tk.END)
        entry1.insert('end','-')
    else:
        entry1.insert('end', '-')

def addition():
    if entry1.get()=='0':
        entry1.delete(0,tk.END)
        entry1.insert('end','+')
    else:
        entry1.insert('end', '+')

def multiplication():
    if entry1.get()=='0':
        entry1.delete(0,tk.END)
        entry1.insert('end','x')
    else:
        entry1.insert('end', 'x')

def division():
    if entry1.get() == '0':
        entry1.delete(0, tk.END)
        entry1.insert('end', '/')
    else:
        entry1.insert('end', '/')

def expo2():
    c = entry1.get()
    try:
        x = float(c)
        ex2 = x ** 2
        entry1.delete(0, 'end')  # Clear the entry
        entry1.insert(0, str(ex2))  # Insert the squared result
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "Error")

def expo3():
    c = entry1.get()
    try:
        x = float(c)
        ex3 = x ** 3
        entry1.delete(0, 'end')  # Clear the entry
        entry1.insert(0, str(ex3))  # Insert the squared result
    except ValueError:
        entry1.delete(0, 'end')
        entry1.insert(0, "Error")

def memory_add():
    with open('memory.txt', 'a') as f:
        f.write(entry1.get() + '\n')

def delete_previous_line():
    try:
        with open('memory.txt', 'r') as f:
            lines = f.readlines()

        if len(lines) < 2:
            entry1.delete(0, 'end')
            entry1.insert(0, "Error")
            return

        # Remove the second-to-last line
        del lines[-2]

        with open('memory.txt', 'w') as f:
            f.writelines(lines)

        entry1.delete(0, 'end')
        entry1.insert(0, "Done")
    except FileNotFoundError:
        entry1.delete(0, 'end')
        entry1.insert(0, "Error")
    except Exception as e:
        entry1.delete(0, 'end')
        entry1.insert(0, f"Error: {e}")

def read_last_line():
    try:
        with open('memory.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1].strip()
                entry1.delete(0, 'end')
                entry1.insert(0, last_line)
            else:
                entry1.delete(0, 'end')
                entry1.insert(0, "Error")
    except FileNotFoundError:
        entry1.delete(0, 'end')
        entry1.insert(0, "Error")

po = 0.0

def M_add():
    global po
    try:
        k = float(entry1.get())
        po += k
    except ValueError:
        entry1.delete(0, tk.END)
        entry1.insert('end', "Error")

def M_subtract():
    global po
    try:
        k = float(entry1.get())
        po -= k
    except ValueError:
        entry1.delete(0, tk.END)
        entry1.insert('end', "Error")

def M_show():
    global po
    entry1.delete(0, tk.END)
    entry1.insert('end', str(po))


def Mapankaya():
    try:
        k = entry1.get()
        entry1.delete(0, tk.END)
        if k and k[0] == '-':
            k = k[1:]
        entry1.insert('end', k)
    except IndexError:
        entry1.delete(0, tk.END)
        entry1.insert('end', "Error")

def fi():
    k = (22 / 7)
    k = str(k)
    k=k[0:6]
    if entry1.get()=='0':
        entry1.delete(0, tk.END)
        entry1.insert('end', k)
    else:
        entry1.insert('end', k)


def bracket():
    text = entry1.get()
    # Count the number of opening and closing brackets
    open_count = text.count('(')
    close_count = text.count(')')

    # Decide what to insert based on the balance
    if open_count <= close_count:
        entry1.insert('end', '(')
    else:
        entry1.insert('end', ')')

def mod():
    entry1.insert('end','mod')

def quo():
    entry1.insert('end','quo')

def exponent():
    if entry1.get!='':
        entry1.insert('end', '^(')
    else:
        entry1.delete(0,'end')
        entry1.insert('end', 'Error')

def exponent_inv():
    if entry1.get!='':
        entry1.insert('end', '^(1/')
    else:
        entry1.delete(0,'end')
        entry1.insert('end', 'Error')

def ex10():
    entry1.insert('end','10^(')

def decimal_to_binary():
    n=entry1.get()
    entry1.delete(0,tk.END)

    n=int(n)
    if n>0:
        n=str(bin(n))
        k=n[2:]
        zeros_0=''
        if len(k)<8:
            for g in range (8-len(k)):
                zeros_0=zeros_0+'0'
            k=zeros_0+str(k)
            entry1.insert('end', k)
            # print('Binary Number is',k)

        else:
        # print("Sorry Bro, We are Still in 8 bits, but I will give your Num")
            # print('Binary Number is', n[2:])
            entry1.insert('end', n[2:])
    elif n<0:
        h=bin(n)
        if len(h[3:])>8:
            entry1.insert('end', 'Error')
                # print("Sorry Bro, We are Still in 8 bits, very sorry")
        else:
            ons=''
            list=[]
            for x in h[3:]:
                if x=='1':
                    list.append(0)
                else:
                    list.append(1)
            for y in list[0:]:
                ons=ons+str(y)

            zeros=''
            if len(ons)<8:
                for x in range (8-len(ons)):
                    zeros=zeros+'1'
                ons=str(zeros)+str(ons)
                entry1.configure(font=('arial', 40))
                entry1.insert('end','Ones:'+ons)
                # print('Ones Complement is',ons)

            else:
                entry1.configure(font=('arial', 40))
                entry1.insert('end','Ones:'+ons)

                # print('Ones Complement is: ',ons)

            list2=[]
            for k in ons:
                list2.append(k)
            g=-1
            while list2[g]=='1':
                list2[g]='0'
                g=g-1
            list2[g]='1'
            twos_str=''
            for m in list2:
                twos_str=twos_str+m
            entry1.insert('end', '   twos:'+twos_str)

            # print('Twos Complement Number is',twos_str)
    else:
        entry1.configure(font=('arial', 40))
        entry1.insert('end','00000000')
        # print('Binary Number is: '+'00000000')

def convert():
    if v.get()==0:
        decimal_to_binary()
    elif v.get()==1:
        entry1.delete(0,tk.END)
        entry1.insert('end', 'Still Developing')
    else:
        entry1.insert('end', 'Error')

def bin_and():
    entry1.insert('end', ' and ')

def bin_or():
    entry1.insert('end', ' or ')

def bin_xor():
    entry1.insert('end', ' xor ')

def left_shift():
    entry1.insert('end',' << ')

def right_shift():
    entry1.insert('end', ' >> ')

def l_and():
    entry1.insert('end', ' AND ')

def l_or():
    entry1.insert('end', ' OR ')

def l_not():
    entry1.insert('end', ' NOT ')

def Tr():
    if entry1.get()!='0':
        entry1.insert('end', ' True ')
    else:
        entry1.delete(0,tk.END)
        entry1.insert('end', ' True ')

def Fl():
    if entry1.get() != '0':
        entry1.insert('end', ' False ')
    else:
        entry1.delete(0, tk.END)
        entry1.insert('end', ' False ')

for i in range(12):
    win.grid_rowconfigure(i, weight=1)

for i in range(6):
    win.grid_columnconfigure(i, weight=1)

frame1=Frame(win)
frame1.grid(row=0, column=0, columnspan=12, sticky='nsew', padx=5, pady=5)
for i in range(12):
    frame1.grid_columnconfigure(i, weight=1)
for i in range(12):
    frame1.grid_rowconfigure(i, weight=1)

entry1=Entry(frame1,font=('Helvetica',60),justify='right',bg='#d0f0c0')
entry1.grid(row=0,column=0,columnspan=12,sticky='nsew')
entry1.insert(0,'0')

def on_focus_in(event):
    if entry1.get() == placeholder:
        entry1.delete(0, 'end')
        entry1.config(fg='black')

entry1.bind("<FocusIn>", on_focus_in)
# Disable keyboard input
entry1.bind("<Key>", lambda e: "break")
# Disable mouse interactions (left click, right click, double-click, etc.)
entry1.bind("<Button-1>", lambda e: "break")
entry1.bind("<Button-2>", lambda e: "break")
entry1.bind("<Button-3>", lambda e: "break")
entry1.bind("<Double-Button-1>", lambda e: "break")
entry1.bind("<B1-Motion>", lambda e: "break")  # Prevent dragging selection

def on_focus_out(event):
    if entry1.get() == '':
        entry1.insert(0, placeholder)
        entry1.config(fg='gray')

entry1.bind("<FocusOut>", on_focus_out)

placeholder='0'


frame_main=Frame(win)
frame_main.grid(row=1, column=0, columnspan=12, sticky='nsew', padx=5, pady=5)
for i in range(12):
    frame_main.grid_rowconfigure(i, weight=1)

for i in range(6):
    frame_main.grid_columnconfigure(i, weight=1)

frame2=Frame(frame_main)
frame2.grid(row=0,sticky='nsew',padx=10,pady=10,columnspan=6,column=0)
for i in range(6):  # or however many columns you want
    frame2.grid_columnconfigure(i, weight=1)
for i in range(8):  # maybe just a couple rows?
    frame2.grid_rowconfigure(i, weight=1)

but1=Button(frame2,text='Read',font=('Arial',20),width=15,height=1,border=5,command=read_last_line,bg="#f3e8ff")
but1.grid(row=0,column=0,sticky='nsew')

but2=Button(frame2,text='Save',font=('Arial',20),width=15,height=1,border=5,command=memory_add,bg="#f3e8ff")
but2.grid(row=0,column=1,sticky='nsew')

but3=Button(frame2,text='Delete',font=('Arial',20),width=15,height=1,border=5,command=delete_previous_line,bg="#f3e8ff")
but3.grid(row=0,column=2,sticky='nsew')

but4=Button(frame2,text='C',font=('Arial',20),width=15,height=1,border=5 ,command=C,bg="#f3e8ff")
but4.grid(row=0,column=3,sticky='nsew')

but5=Button(frame2,text='Back',font=('Arial',20),width=15,height=1,border=5,command=delete_last_character,bg="#f3e8ff")
but5.grid(row=0,column=4,sticky='nsew')

but6=Button(frame2,text='/',font=('Arial',20),width=15,height=1,border=5,command=division,bg="#ffeaea")
but6.grid(row=0,column=5,sticky='nsew')

#----------------------------------------------------------------------------

but7=Button(frame2,text='9',font=('Arial',20),width=15,height=1,border=5,command=press_9,bg='#ffeaea')
but7.grid(row=1,column=0,sticky='nsew')

but8=Button(frame2,text='8',font=('Arial',20),width=8,height=1,border=5,command=press_8,bg='#ffeaea')
but8.grid(row=1,column=1,sticky='nsew')

but9=Button(frame2,text='7',font=('Arial',20),width=8,height=1,border=5,command=press_7,bg='#ffeaea')
but9.grid(row=1,column=2,sticky='nsew')

but10=Button(frame2,text='x^2',font=('Arial',18),width=8,height=1,border=5,command=expo2,bg="#e6f0ff")
but10.grid(row=1,column=3,sticky='nsew')

but11=Button(frame2,text='x^3',font=('Arial',18),width=8,height=1,border=5,command=expo3,bg="#e6f0ff")
but11.grid(row=1,column=4,sticky='nsew')

but12=Button(frame2,text='X',font=('Arial',20),width=8,height=1,border=5,command=multiplication,bg="#ffeaea")
but12.grid(row=1,column=5,sticky='nsew')

#---------------------------------------------------------------------

but13=Button(frame2,text='6',font=('Arial',20),width=8,height=1,border=5,command=press_6,bg='#ffeaea')
but13.grid(row=2,column=0,sticky='nsew')

but14=Button(frame2,text='5',font=('Arial',20),width=8,height=1,border=5,command=press_5,bg='#ffeaea')
but14.grid(row=2,column=1,sticky='nsew')

but15=Button(frame2,text='4',font=('Arial',20),width=8,height=1,border=5,command=press_4,bg='#ffeaea')
but15.grid(row=2,column=2,sticky='nsew')

but16=Button(frame2,text='sqrt(x)',font=('Arial',15),width=8,height=1,border=5,command=squareroot,bg="#e6f0ff")
but16.grid(row=2,column=3,sticky='nsew')

but17=Button(frame2,text='cubert(x)',font=('Arial',15),width=8,height=1,border=5,command=cuberoot,bg="#e6f0ff")
but17.grid(row=2,column=4,sticky='nsew')

but18=Button(frame2,text='-',font=('Arial',20),width=8,height=1,border=5,command=subtraction,bg="#ffeaea")
but18.grid(row=2,column=5,sticky='nsew')

#------------------------------------------------------------------

but19=Button(frame2,text='3',font=('Arial',20),width=8,height=1,border=5,command=press_3,bg='#ffeaea')
but19.grid(row=3,column=0,sticky='nsew')

but20=Button(frame2,text='2',font=('Arial',20),width=8,height=1,border=5,command=press_2,bg='#ffeaea')
but20.grid(row=3,column=1,sticky='nsew')

but21=Button(frame2,text='1',font=('Arial',20),width=8,height=1,border=5,command=press_1,bg='#ffeaea')
but21.grid(row=3,column=2,sticky='nsew')

but22=Button(frame2,text='1/x',font=('Arial',15),width=8,height=1,border=5,command=inverse,bg="#e6f0ff")
but22.grid(row=3,column=3,sticky='nsew')

but23=Button(frame2,text='e^(x)',font=('Arial',18),width=8,height=1,border=5,command=button23,bg="#e6f0ff")
but23.grid(row=3,column=4,sticky='nsew')

but24=Button(frame2,text='+',font=('Arial',20),width=8,height=1,border=5,command=addition,bg="#ffeaea")
but24.grid(row=3,column=5,sticky='nsew')

#-------------------------------------------------------------------------

but25=Button(frame2,text='0',font=('Arial',20),width=8,height=1,border=5,command=press_0,bg='#ffeaea')
but25.grid(row=4,column=0,sticky='nsew')

but26=Button(frame2,text='00',font=('Arial',20),width=8,height=1,border=5,command=press_00,bg='#ffeaea')
but26.grid(row=4,column=1,sticky='nsew')

but27=Button(frame2,text='.',font=('Arial',20),width=8,height=1,border=5,command=press_dot,bg='#ffeaea')
but27.grid(row=4,column=2,sticky='nsew')

but28=Button(frame2,text='x!',font=('Arial',20),width=8,height=1,border=5,command=button28,bg="#e6f0ff")
but28.grid(row=4,column=3,sticky='nsew')

but29=Button(frame2,text='ln(x)',font=('Arial',20),width=8,height=1,border=5,command=calculate_ln,bg="#e6f0ff")
but29.grid(row=4,column=4,sticky='nsew')

but30=Button(frame2,text='()',font=('Arial',20),width=8,height=1,border=5,command=bracket)
but30.grid(row=4,column=5,sticky='nsew')

#----------------------------------------------------------------------------------------------------------------------------

but31=Button(frame2,text='M+',font=('Arial',20),width=8,height=1,border=5,command=M_add,bg="#f3e8ff")
but31.grid(row=5,column=0,sticky='nsew')

but32=Button(frame2,text='M-',font=('Arial',20),width=8,height=1,border=5,command=M_subtract,bg="#f3e8ff")
but32.grid(row=5,column=1,sticky='nsew')

but33=Button(frame2,text='MR',font=('Arial',20),width=8,height=1,border=5,command=M_show,bg="#f3e8ff")
but33.grid(row=5,column=2,sticky='nsew')

but34=Button(frame2,text='|x|',font=('Arial',20),width=8,height=1,border=5, command=Mapankaya,bg="#e6f0ff")
but34.grid(row=5,column=3,sticky='nsew')

but35=Button(frame2,text='π',font=('Arial',20),width=8,height=1,border=5,command=fi,bg="#e6f0ff")
but35.grid(row=5,column=4,sticky='nsew')

but36=Button(frame2,text='=',font=('Arial',35),width=8,height=1,border=5,command=evaluate_expression,bg='yellow')
but36.grid(row=5,column=5,sticky='nsew',rowspan=2)

#------------------------------------------------------------------------------------------------------------------------

but37=Button(frame2,text='Mod',font=('Arial',20),width=8,height=1,border=5,command=mod,bg="#e6f0ff")
but37.grid(row=6,column=0,sticky='nsew')

but38=Button(frame2,text='Quo',font=('Arial',20),width=8,height=1,border=5,command=quo,bg="#e6f0ff")
but38.grid(row=6,column=1,sticky='nsew')

but39=Button(frame2,text='x^(1/y)',font=('Arial',18),width=8,height=1,border=5,command=exponent_inv,bg="#e6f0ff")
but39.grid(row=6,column=2,sticky='nsew')

but40=Button(frame2,text='x^(y)',font=('Arial',18),width=8,height=1,border=5,command=exponent,bg="#e6f0ff")
but40.grid(row=6,column=3,sticky='nsew')

but41=Button(frame2,text='10^(x)',font=('Arial',18),width=8,height=1,border=5,command=ex10,bg="#e6f0ff")
but41.grid(row=6,column=4,sticky='nsew')
#----------------------------------------------------------------------------------------------------------------

frame3=Frame(frame_main)
frame3.grid(row=0, column=7, padx=5, pady=5,sticky='nsew',columnspan=5)

for i in range(50):
    frame3.grid_rowconfigure(i,weight=1)
for i in range(6):
    frame3.grid_columnconfigure(i,weight=1)

# spacer = Label(frame3, text="", height=2)
# spacer.grid(row=0, column=0)

label1=Label(frame3,text='Bitwise Arithmetics',font=('Arial',18,'underline'))
label1.grid(row=0 ,sticky='nsew',columnspan=5)

but42=Button(frame3,text='and',font=('Arial',18),border=5,bg="#e6f0ff",command=bin_and)
but42.grid(row=1,column=0,sticky='nsew')

but43=Button(frame3,text='or',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=bin_or)
but43.grid(row=1,column=1,sticky='nsew')

but44=Button(frame3,text='xor',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=bin_xor)
but44.grid(row=1,column=2,sticky='nsew')

but45=Button(frame3,text='()',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=bracket)
but45.grid(row=1,column=3,sticky='nsew')

but46=Button(frame3,text='<<',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=left_shift)
but46.grid(row=2,column=0,sticky='nsew')

but45=Button(frame3,text='>>',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=right_shift)
but45.grid(row=2,column=1,sticky='nsew')

but52=Button(frame3,text='True',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=Tr)
but52.grid(row=2,column=2,sticky='nsew')

but53=Button(frame3,text='False',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=Fl)
but53.grid(row=2,column=3,sticky='nsew')

#---------------------------------------------------------------------------------------------------------------
spacer = Label(frame3, text="", height=2)
spacer.grid(row=3, column=0)

frame4=Frame(frame3)
frame4.grid(row=5, column=0, padx=5, pady=5,sticky='nsew',columnspan=5)

for i in range(12):
    frame4.grid_rowconfigure(i,weight=1)
for i in range(6):
    frame4.grid_columnconfigure(i,weight=1)

v=IntVar()
Radiobutton(frame4, text='Decimal to Binary conversion  |' ,variable=v,value=0,font=('Arial',12)).grid(row=0, column=0,sticky='nsew')
Radiobutton(frame4, text='Binary to Decimal conversion' ,variable=v,value=1 ,font=('Arial',12)).grid(row=0, column=3,sticky='nsew')

#-------------------------------------------------------------------------------------------------------------

frame5=Frame(frame3)
frame5.grid(row=4, column=0, padx=5, pady=5,sticky='nsew',columnspan=5)

for i in range(12):
    frame5.grid_rowconfigure(i,weight=1)
for i in range(6):
    frame5.grid_columnconfigure(i,weight=1)

label2=Label(frame5,text='Binary Decimal Conversion',font=('Arial',18,'underline'))
label2.grid(row=0 ,sticky='nsew',columnspan=5)

but48=Button(frame4,text='Convert',font=('Arial',18),border=5,bg="#e6f0ff",width=7,command=convert)
but48.grid(row=3,column=0,sticky='ew',columnspan=4)

#---------------------------------------------------------------------------------------------------------------

spacer = Label(frame3, text="", height=2)
spacer.grid(row=6, column=0)

frame6=Frame(frame3)
frame6.grid(row=7, column=0, padx=5, pady=5,sticky='nsew',columnspan=5)
#
for i in range(12):
    frame6.grid_rowconfigure(i,weight=1)
for i in range(6):
    frame6.grid_columnconfigure(i,weight=1)

label3=Label(frame6,text='Logical Arithmetic',font=('Arial',18,'underline'))
label3.grid(row=1 ,sticky='nsew',columnspan=5)

but49=Button(frame6,text='AND',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=l_and)
but49.grid(row=2,column=0,sticky='ew')

but50=Button(frame6,text='OR',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=l_or)
but50.grid(row=2,column=1,sticky='ew')

but51=Button(frame6,text='NOT',font=('Arial',18),border=5,bg="#e6f0ff",width=8,command=l_not)
but51.grid(row=2,column=2,sticky='ew')

for i in range(6):  # Assuming 6 columns inside the frame
    frame4.grid_columnconfigure(i, weight=1)
    frame5.grid_columnconfigure(i, weight=1)
    frame6.grid_columnconfigure(i, weight=1)

# frame4.config(highlightbackground="red", highlightthickness=2)
# frame5.config(highlightbackground="red", highlightthickness=2)
# frame6.config(highlightbackground="red", highlightthickness=2)

# ---------------------------------------------------------------------------------------------------------------
def animate_equal():
    # Simulate button press
    but36.config(relief='sunken')
    win.after(50, lambda: but36.config(relief='raised'))
    evaluate_expression()  # Call the actual function

win.bind('<Return>', lambda e: animate_equal())

button_map = {
    '0': but25,
    '1': but21,
    '2': but20,
    '3': but19,
    '4': but15,
    '5': but14,
    '6': but13,
    '7': but9,
    '8': but8,
    '9': but7
}

def on_key_press(event):
    key = event.char
    keysym = event.keysym

    allowed_keys = set(button_map.keys())  # '0' to '9'

    if keysym == 'Return':
        animate_equal()
        return

    if keysym == 'BackSpace':
        entry1.delete(len(entry1.get()) - 1, tk.END)
        animate_button(but5)
        return

    if key in allowed_keys:
        if entry1.get() == "0":
            entry1.delete(0, tk.END)
        entry1.insert(tk.END, key)
        animate_button(button_map[key])
        return

    # Handle normal brackets
    if key in ('(', ')'):
        entry1.insert(tk.END, key)


def animate_button(button):
    original_color = button.cget("background")
    button.config(background="orange")
    button.after(200, lambda: button.config(background=original_color))

win.bind("<Key>", on_key_press)

win.mainloop()

#cd C:\Users\Sashik_Thiwanka\PycharmProjects\Python Self Practising
#pyinstaller --onefile --windowed --icon=icon.ico Calculator.py