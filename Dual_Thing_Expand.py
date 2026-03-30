import tkinter as tk
from tkinter import *

win=tk.Tk()
win.title('Dual Thing Expand')
win.geometry('914x600')

def _on_mousewheel(event):
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

canvas = Canvas(win, bg='linen')
canvas.pack(side="left", fill="both", expand=True)

canvas.bind_all("<MouseWheel>", _on_mousewheel)

scrollbar = Scrollbar(win, orient="vertical", command=canvas.yview, width=30)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = Frame(canvas, bg='seashell')
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

label1=Label(scrollable_frame, text='Binomial Expressions Expander' , font=('arial',20,'underline'), bg='yellow' , fg='red')
label1.pack()

label2=Label(scrollable_frame, text='\n', font=('arial', 2), bg='lightblue')
label2.config(bg='seashell')
label2.pack()

label2=Label(scrollable_frame, text='Instructions To Use' , font=('arial',15,'underline'), fg='blue')
label2.config(bg='seashell')
label2.pack(anchor='w')

label3=Label(scrollable_frame, text="* You Can't Change X value here", font=('arial',12,'italic'), fg='green')
label3.config(bg='seashell')
label3.pack(anchor='w')

label4=Label(scrollable_frame, text="* As Below Example, You Can Only Change 3, 4 and 2 Only.", font=('arial',12,'italic'), fg='green')
label4.config(bg='seashell')
label4.pack(anchor='w')

label5=Label(scrollable_frame, text="* Format Should Same as Given Below.", font=('arial',12,'italic'), fg='green')
label5.config(bg='seashell')
label5.pack(anchor='w')

label6=Label(scrollable_frame, text='Example:- (4X+3)^2' , font=('arial',15,'bold'))
label6.config(bg='seashell')
label6.pack()

label7=Label(scrollable_frame, text='Enter Your Thing To Expand Here:-' , font=('arial',15,'underline'), fg='blue')
label7.config(bg='seashell')
label7.pack(anchor='w',pady=10)

def copy(event):
    event.widget.event_generate("<<Copy>>")

def paste(event):
    event.widget.event_generate("<<Paste>>")

entry1 = Entry(scrollable_frame, font=('arial', 15), width=30, justify='center', bg='powder blue')
entry1.pack(pady=10)


entry1.bind("<Control-c>", copy)
entry1.bind("<Control-v>", paste)

entry1.insert(0, '(aX+b)^n')

label8=Label(scrollable_frame, text="Here's Your Expanded Answer:- " , font=('arial',15,'underline'), fg='blue')
label8.config(bg='seashell')
label8.pack(anchor='w',pady=20)

text2=Text(scrollable_frame ,wrap="word" , height=8,font=('arial',15),bg='powder blue')
text2.pack(fill="both", expand=True,pady=2)

text3=Text(scrollable_frame ,wrap="word" , height=3,font=('arial',15),bg='powder blue')
text3.pack(fill="both", expand=True,pady=1)

def func(x):
    x=int(x)
    fact=1
    while x>0:
        fact=fact*x
        x=x-1
    return fact

def sg(n,r):
    n=int(n)
    r=int(r)
    # n=int(input('Enter Your Exponent? '))
    san=func(n)/(func(r)*func(n-r))
    return san

global string1
def thing(y,n):
    global string1
    keep=''
    r=0
    list2=[]
    po = str(entry1.get())
    for xp in po[1::1]:
        if xp.isdigit():
            keep = str(keep) + str(xp)
        else:
            break
    while r<(n+1):
        y=int(y)
        y_value=y**r
        y_value=str(y_value)
        san2 = int(n) - int(r)
        if po[1].isalpha():
            string1='X^'+str(san2)
            string2 = string1 + ' x ' + y_value
            list2.append(string2)
        else:
            keep=int(keep)
            x_san=str(keep**san2)
            string11=x_san+' x '+'X^'+str(san2)
            string12=string11+' x '+y_value
            list2.append(string12)
        r=r+1
    return list2

def work(y,n):
    listdash=[]
    listdash2=[]
    c=0
    while c<(n+1):
        wo = int(sg(n, c))
        c=c+1
        listdash.append(wo)
    th=thing(y,n)
    c=0
    for y in listdash:
        listdash[c]='{'+str(listdash[c])+' x '+str(th[c])+'}'
        listdash2.append(listdash2)
        c=c+1
    list_new=[]
    for x in listdash:
        list_new.append(str(x) + ' + ')
    # print(listdash)
    list4last = list_new[-1]
    list4last = list4last.replace('+', '')
    list_new[-1] = list4last
    # print(list_new)
    expand=''
    for x in list_new:
        expand=expand+str(x)
    # print(listdash2)
    return expand

def buttonpress():
    text2.delete('1.0','end')
    text3.delete('1.0','end')
    p=entry1.get()
    p=str(p)
    if p[0]!='(':
        text2.insert('1.0','Your Structure is Incorrect. Please Check Again')
    else:
        if '(' in p and ')' in p and '^' in p:
            string6=''
            string7=''
            string9=''
            c=-1
            for xu in p[-1::-1]:
                xa=''
                if xu=='^':
                    xa=xa+str(xu)
                    break
                else:
                    string6 = string6 + str(xu)
                c=c-1
            # print(string6)
            n0=int(string6[::-1])
            st=''
            xa=int(c-2)
            for xb in p[xa::-1]:
                if xb=='+':
                    st='g'
                    break
                elif xb=='-':
                    string9='-'
                    # print('minus added')
                    st='g'
                    break
                else:
                    if xb.isdigit():
                        string7=string7+str(xb)
                        st='g'
                    else:
                        st='b'
                        break
            if st=='g':
                string11=string9+string7
                # print(string9)
                # print(string11)
                # ready=
                y0=int(string11[:])

                answer=work(y0,n0)
                answer=str(answer)
                answer=answer.strip('X^0')
                text2.insert('1.0','How I Got:-  '+answer)
                answer=str(answer)
                t=solve(answer)
                text3.insert('1.0','Real Answer is:-  '+t)
                history(t)
                readme()
            else:
                text2.insert('1.0', 'Your Entered Structure is Incorrect. Please Check Again...')

        else:
            text2.insert(1.0,'Your Entered Structure is Incorrect. Please Check Again')


def solve(name):
    list2red=[]
    name=name.split('+')
    for x in name:
        x = x.strip('{} ').strip()
        parts = [p.strip() for p in x.split('x')]
        num_product = 1
        x_part = ''
        for part in parts:
            if '^' in part.lower():
                x_part = part  # Preserve the X^n part
            else:
                num_product *= int(part)
        list2red.append(f'{num_product} {x_part}')

    final_expression = ' + '.join(list2red)
    final_expression=str(final_expression)
    final_expression=final_expression.strip('X^0')
    Finally=fix_polynomial(final_expression)
    return Finally

def fix_polynomial(expression):
    return expression.replace(" + -", " - ")

Button1=Button(scrollable_frame,text='Click Here', command=buttonpress , width=15 ,height=1, border=12 ,bg='lightgreen',font=('arial',15,'italic'))
Button1.pack(pady=15)

label8=Label(scrollable_frame, text='Designed By Sashik Thiwanka', font=('arial',15,'italic'))
label8.pack(anchor='se')

from datetime import datetime

def history(tone):
    if tone!='':
        today = datetime.now().strftime('%Y-%m-%d')
        # Path to your text file
        file_path = 'History.txt'

        # Write the date to the file
        with open(file_path, 'a') as file:
            file.write(f'Date: {today}\n')
            file.write('entry1.get()'+'\t-->\t\t'+tone+'\n\n')

import textwrap

def readme():
    # file_path = 'Read_me.txt'
    # with open(file_path, 'w') as file:
    content='''Binomial Expression Expander
    📌 Overview
    This Python project expands binomial expressions of the form (a + b)^n into their full expanded polynomial using the binomial theorem. It's designed to handle both symbolic and numeric inputs, making it a useful tool for students, teachers, and math enthusiasts.
    
    
    🚀 Features
    - Supports expressions with variables (e.g. x, y, etc.)
    - Accepts both positive integers and symbolic exponents
    - Offers step-by-step breakdown (optional)
    - GUI (Tkinter-based) version and/or CLI version
    - Exports results to a text file
    - Includes error handling for invalid inputs
    
    
    🛠️ How It Works
    This tool uses the binomial theorem:
    
    (a + b)^n = Σ (n choose k) * a^(n-k) * b^k
    
    Each term is calculated by computing combinations (nCk) using Python’s built-in math.comb() (Python 3.8+) or a custom function.
    
    
    📁 Output Example
    For input (x+2)^3, output will be:
    
    x^3 + 3x^2*2 + 3x*2^2 + 2^3
    = x^3 + 6x^2 + 12x + 8
    
    
    📚 Math Behind It
    This project is inspired by the classical Binomial Theorem, taught in algebra and combinatorics. It also showcases the beauty of mathematical patterns when coded into logic.
    
    
    ✅ To-Do / Improvements
    - Add support for fractional exponents
    - Latex-style output formatting
    - Multivariable expansion
    - Integration with SymPy for symbolic math
    
    
    👨‍💻 Author
    Sashik
    Python enthusiast | GUI design explorer | Math logic tinkerer
    Made with 💡 and a touch of code magic
    '''
    # wrapped_text = textwrap.fill(content, width=1600)

    with open('Read_Me.txt', 'w', encoding='utf-8') as file:
        file.write(content)

win.mainloop()