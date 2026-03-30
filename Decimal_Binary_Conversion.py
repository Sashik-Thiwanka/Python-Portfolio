from tkinter import *

win=Tk()
win.geometry('600x625')
win.title('Deicimal Binary Conversion - Sri Lanka Presents')
win.config(bg='seashell')

label=Label(win, text='Decimal Binary Conversion', font=('arial',25,"underline"))
label.config(bg='orange')
label.pack(pady=10)

label3=Label(win, text='\n', font=('arial',1))
label3.config(bg='seashell')
label3.pack()

label4=Label(win, text='* When You Enter a Number & Convert Will Automatically Clear and You Will Get Output..', font=('arial',10))
label4.configure(bg='yellow')
label4.pack(padx=7)

label89=Label(win, text='Warning = These are 8 Bit Deals...', font=('arial',10))
label89.configure(bg='pink')
label89.pack(padx=7)

label3=Label(win, text='\n', font=('arial',5))
label3.config(bg='seashell')
label3.pack()

label2=Label(win, text='Enter Your Decimal Or Binary Number Here :-', font=('arial',12))
label2.pack(anchor='w')

# def limit_text_length(event):            #for Enter a limit in textbox
#     content = textbox1.get("1.0", "end-1c")
#     if len(content) >= 8 and event.keysym not in ("BackSpace", "Delete", "Left", "Right"):
#         return "break"  # Prevent typing but allow deletion/movement
#     return None

# def on_key(event):
#     global key_count
#     key_count += 1
#     textbox3.delete(1.0,'end')
#     textbox3.insert(1.0,'Key Count = '+ str(key_count))
#     textbox4.delete(1.0, 'end')
#     textbox5.delete(1.0, 'end')
#     # print(f"Key pressed: {event.keysym}, Count: {key_count}")

# count1=Text(win, height=1, width=10)
# count1.pack(padx=2, pady=2)
# count1.insert('1.0','count')
# count1.tag_configure("center", justify="center")
# count1.tag_add("center", "1.0", "end")

def count_key(key):
    wp=textbox1.get(1.0,'end-1c')
    count1.delete(1.0,'end')
    count1.tag_configure("center", justify="center")
    count1.tag_add("center", "1.0", "end")
    if len(wp)==0:
        count1.insert(1.0, 'Count : 0')
    else:
        count1.insert(1.0,'Count : '+str(len(wp)+1))

key_count=0
textbox1=Text(win,height=1 , width=50 , font=('arial',13), bg='yellow' , fg='red')
textbox1.bind("<Key>",count_key)
textbox1.pack(padx=2,pady=2)

# textbox1.bind("<Key>", limit_text_length)  # Bind key press event
# text_widget.unbind("<Key>")

# textbox1.insert(1.0,'0')

count1=Text(win, height=1, width=10)
count1.pack(padx=2, pady=2)
count1.insert('1.0','count')
count1.tag_configure("center", justify="center")
count1.tag_add("center", "1.0", "end")

status=Text(win, height=1, width=10)
status.pack(padx=2, pady=2)
status.insert('1.0','status')
status.tag_configure("center", justify="center")
status.tag_add("center", "1.0", "end")

label5=Label(win, text='\n', font=('arial',1))
label5.config(bg='seashell')
label5.pack()

label4=Label(win, text="Here's your Decimal or Binary Number:- ", font=('arial',12))
label4.pack(anchor='w')

# label3=Label(win, text='\n', font=('arial',12))
# label3.pack()

textbox3=Text(win,height=1 , width=50 ,bg='lightblue', font=('arial',13))
textbox3.pack(padx=2,pady=2)
textbox3.insert('1.0','Normal Binary')
textbox3.config(state='normal')

textbox4=Text(win,height=1 , width=50 ,bg='lightblue', font=('arial',13))
textbox4.pack(padx=2,pady=2)
textbox4.insert('1.0','8 Bit Ones Complement')
textbox4.config(state='normal')

textbox5=Text(win,height=1 , width=50 ,bg='lightblue', font=('arial',13))
textbox5.pack(padx=2,pady=2)
textbox5.insert('1.0','8 Bit Twos Complement')
textbox5.config(state='normal')

def on_button_press():
    print("Button Pressed!")

global ab, ji
k=''
def decimal_to_binary():
    status.delete('1.0','end')
    textbox3.delete('1.0', 'end')
    textbox4.delete('1.0', 'end')
    textbox5.delete('1.0', 'end')
    global k
    w = textbox1.get('1.0', 'end-1c')
    for x in w:
        if x.isalpha():
            k = 'e'
            break
        else:
            k = 'g'
    if k == 'g':
        w = int(w)
        func1(w)
    else:
        status.delete(1.0,'end')
        status.insert(1.0,'Error')
        textbox3.insert(1.0,' Please Enter Numbers Only')

    abc=''
    w = textbox1.get('1.0', 'end-1c')
    for x in w:
        if x.isalpha():
            abc = 'Error'
        else:
            abc = 'good'

    status.delete(1.0,'end')
    status.insert(1.0, abc)
    status.tag_configure("center", justify="center")
    status.tag_add("center", "1.0", "end")

    if abc=='Error':
        textbox3.insert(1.0,'You have Entered Letters')
        textbox4.insert(1.0,'Why This Bro...')
        textbox5.insert(1.0,'Are You OK ?..')

# def func2():
#     # status.delete(1.0, 'end')
#     textbox3.delete(1.0, 'end')
#     textbox4.delete(1.0, 'end')
#     textbox5.delete(1.0, 'end')

def func3():
    status.tag_configure("center", justify="center")
    status.tag_add("center", "1.0", "end")

v = IntVar()
Radiobutton(win, text='Decimal to Binary', variable=v, value=1, font=('Arial',14), height=1, width=20).pack()
Radiobutton(win, text='Binary to Decimal', variable=v, value=0, font=('Arial',14), height=1, width=20).pack()

label6=Label(win,text='-----------------------------------------------' ,bg='seashell')
label6.pack()

label7=Label(win,text='Change This if Only You Entered Ones or Twos Complement', bg='pink' ,font=('arial',10,'underline'))
label7.pack()

ij = IntVar()
RB1=Radiobutton(win, text='For Normal Binary Number', variable=ij , value=0, font='Arial', bg='lightgreen')
RB1.pack()
RB2=Radiobutton(win, text='Press This If Entered Ones', variable=ij , value=1, font='Arial' , bg='lightgreen')
RB2.pack()
RB3=Radiobutton(win, text='Press This If Entered Twos', variable=ij , value=2, font='Arial', bg='lightgreen')
RB3.pack()

def func1(n):
    if v.get()==1:
        if n>0:
            n=str(bin(n))
            kg=n[2:]
            zeros_0=''
            if len(kg)<8:
                for g in range (8-len(kg)):
                    zeros_0=zeros_0+'0'
                kg=zeros_0+str(kg)
                g='Your Binary Number is:  '+kg
                textbox3.delete(1.0,'end')
                textbox4.delete(1.0,'end')
                textbox5.delete(1.0,'end')
                # textbox3.config(state='normal')
                textbox3.insert(1.0,g)
                # print(g)

            else:
                # print("Sorry Bro, We are Still in 8 bits, but I will give your Num")
                la="Sorry Bro, We are Still in 8 Bits, But I Will Give Your Num"
                textbox3.insert(1.0, la)
                lb='Binary Number is: '+ n[2:]
                textbox3.delete(1.0,'end')
                textbox4.delete(1.0,'end')
                textbox5.delete(1.0,'end')
                textbox3.insert(1.0,la)
                textbox4.insert(1.0, lb)
                textbox5.insert(1.0,'Next Time Try to Give 8 Bit Number')
        elif n<0:
            h=bin(n)
            zeros_1=''
            for n in range(8 - len(h[3:])):
                zeros_1 = zeros_1 + '0'
            lh='Binary Number is:- '+zeros_1+str(h[3:])
            textbox3.delete(1.0, 'end')
            textbox4.delete(1.0, 'end')
            textbox5.delete(1.0, 'end')
            textbox3.insert(1.0, lh)
            if len(h[3:])>8:
                status.delete(1.0,'end')
                status.insert(1.0,'Error')
                func3()
                # print("Sorry Bro, We are Still in 8 bits, very sorry")
                lc="Sorry Bro, We are Still in 8 bits"
                textbox3.delete(1.0,'end')
                textbox4.delete(1.0,'end')
                textbox5.delete(1.0,'end')
                textbox3.insert(1.0, lc)
                textbox4.insert(1.0,'Very Sorry')
            else:
                ons=''
                list6=[]
                for x in h[3:]:
                    if x=='1':
                        list6.append(0)
                    else:
                        list6.append(1)
                for y in list6[0:]:
                    ons=ons+str(y)

                zeros=''
                if len(ons)<8:
                    for x in range (8-len(ons)):
                        zeros=zeros+'1'
                    ons=str(zeros)+str(ons)
                    print('Ones Complement is',ons)
                    ld='Ones Complement is: '+ons
                    textbox3.delete(1.0, 'end')
                    textbox4.delete(1.0, 'end')
                    textbox5.delete(1.0, 'end')
                    textbox3.insert(1.0, ld)

                else:
                    # print('Ones Complement is:- ',ons)
                    le='Ones Complement is: '+ str(ons)
                    textbox3.delete(1.0, 'end')
                    # textbox4.delete(1.0, 'end')
                    # textbox5.delete(1.0, 'end')
                    textbox4.insert(1.0, le)

                list2=[]
                for kn in ons:
                    list2.append(kn)
                g=-1
                while list2[g]=='1':
                    list2[g]='0'
                    g=g-1
                list2[g]='1'
                twos_str=''
                for m in list2:
                    twos_str=twos_str+m
                # print('Twos Complement Number is',twos_str)
                # textbox3.delete(1.0,'end')
                # textbox4.delete(1.0,'end')
                textbox5.delete(1.0,'end')
                lf='Twos Complement Number is: '+twos_str
                textbox4.insert(1.0, lf)
        else:
            # print('Binary Number is:- '+'00000000')
            lg='Binary Number is: '+'00000000'
            textbox3.insert(1.0, lg)

    elif v.get()==0:
        count1.delete(1.0,'end')
        status.delete('1.0','end')
        if ij.get()==0:
            if n>0:
                st=''
                list5=[]
                for x in str(n):
                    if x.isdigit():
                        if x!='0':
                            if x!='1':
                                st='bad'
                                status.delete(1.0,'end')
                                status.insert(1.0, 'Error')
                                func3()
                                textbox3.delete(1.0, 'end')
                                textbox4.delete(1.0, 'end')
                                textbox5.delete(1.0, 'end')
                                textbox3.insert(1.0,'Insert Only Ones & Zeros')
                                break
                            else:
                                st='good'
                                # status.insert(1.0, 'good')
                        else:
                            st='good'
                            # status.insert(1.0, 'good')
                            break
                    else:
                        st='bad'
                        status.delete(1.0,'end')
                        status.insert(1.0, 'Error')
                        func3()
                        textbox3.delete(1.0, 'end')
                        textbox4.delete(1.0, 'end')
                        textbox5.delete(1.0, 'end')
                        textbox3.insert(1.0,'Please Enter Numbers Only')
                        textbox4.insert(1.0,"Don't You have a Brain To Understand")
                        textbox5.insert(1.0,'That These are Numbers')

                # status.insert(1.0, str(st))
                if st=='good':
                    for i in str(n):
                        list5.append(i)
                    value_list=[]
                    x=0
                    for b in list5:
                        if b=='1':
                            e=(len(list5)-1)-x
                            binary= 2**e
                            value_list.append(binary)
                        x = x + 1
                    tot=0
                    for ju in value_list:
                        tot=tot+int(ju)
                    ly='Your Decimal Number is: '+str(tot)
                    textbox3.delete(1.0, 'end')
                    textbox4.delete(1.0, 'end')
                    textbox5.delete(1.0, 'end')
                    textbox3.insert(1.0,ly)

            elif n==0:
                status.delete(1.0,'end')
                status.config(state='normal')
                status.insert(1.0,'Error')
                print('Not Bad')
                textbox3.insert(1.0,'Your Decimal Number is : 0')

            else:
                textbox3.insert(1.0,'Please Insert Positive Numbers')
                status.delete(1.0, 'end')
                status.insert(1.0, 'Error')
            status.insert(1.0,'Not Bad')
        elif ij.get()==1:
            if n>0:
                list0=[]
                zeros_1=''
                n = str(n)
                # print([n])
                if len(n)<=8:
                    for g in range (8-len(n)):
                        zeros_1=zeros_1+'0'
                    n=zeros_1+str(n)
                else:
                    status.delete(1.0, 'end')
                    status.insert(1.0, 'Error')
                    func3()
                    textbox3.delete(1.0,'end')
                    textbox4.delete(1.0,'end')
                    textbox5.delete(1.0,'end')
                    te10='Sorry Bro We are Dealing With 8 Bits'
                    te11='You Know This Is 8 Bit Deals'
                    te12='So The First Bit Should 1'
                    textbox3.insert(1.0, te10)
                    textbox4.insert(1.0, te11)
                    textbox5.insert(1.0, te12)


                if n[0]=='1':
                    if len(n)<=8:
                        print(n)
                        for x in n:
                            if x=='1':
                                list0.append(x)
                                # sto='good'
                            elif x=='0':
                                list0.append(x)
                                # sto='good'
                            else:
                                # sto='bad'
                                status.delete(1.0,'end')
                                status.insert(1.0, 'Error')
                                func3()
                                textbox3.delete(1.0, 'end')
                                textbox4.delete(1.0, 'end')
                                textbox5.delete(1.0, 'end')
                                textbox3.insert(1.0,'Please Enter Ones & Zeros')
                                break
                        # print(list0)
                        list2=[]
                        # list0[0]=-127
                        po=7
                        for x in list0:
                            go= int(x) * 2**int(po)
                            po=po-1
                            list2.append(go)
                        list2[0]=-127
                        tot=0
                        for to in list2:
                            tot=tot+to
                        te9 = 'Decimal Number of Your Ones Complement is: '
                        te10 = 'here: ' + str(tot)
                        textbox3.delete(1.0,'end')
                        textbox4.delete(1.0,'end')
                        textbox5.delete(1.0,'end')
                        textbox3.insert(1.0, te9)
                        textbox4.insert(1.0, te10)

                    else:
                        textbox3.delete(1.0, 'end')
                        textbox4.delete(1.0, 'end')
                        textbox5.delete(1.0, 'end')
                        status.delete(1.0,'end')
                        textbox3.insert(1.0,'Sorry Bro')
                        status.insert(1.0,'Error')
                        textbox4.insert(1.0, 'Here We are Dealing With 8 Bits')

                else:
                    # print('please enter valid ones complement')
                    te6='Please Enter Valid Ones Complement'
                    te7='You Know This Is 8 Bit Deals'
                    te8='So The First bit Should 1'
                    textbox3.delete(1.0,'end')
                    textbox4.delete(1.0,'end')
                    textbox5.delete(1.0,'end')
                    textbox3.insert(1.0, te6)
                    textbox4.insert(1.0, te7)
                    textbox5.insert(1.0, te8)
                    status.delete(1.0,'end')
                    status.insert(1.0, 'Error')
                    func3()
                    #here we are dealing with 8bits bro
                    # first bit should one

            elif n==0:
                textbox3.insert(1.0,'Please Insert Valid Ones Complement')
                textbox4.insert(1.0,'First Bit Should 1')
                status.delete(1.0, 'end')
                status.insert(1.0, 'Error')

            else:
                textbox3.insert(1.0,'Please Enter Positive Numbers')
                status.delete(1.0, 'end')
                status.insert(1.0, 'Error')

        elif ij.get()==2:
            twos=''
            zeros_6=''
            list7=[]
            n=str(n)
            if len(n) <= 8:
                for g in range(8 - len(n)):
                    zeros_6 = zeros_6 + '0'
                twos = zeros_6 + str(n)
            # print(twos)
            else:
                te9='Sorry Bro, We are Dealing With 8 Bits'
                textbox3.delete(1.0,'end')
                textbox4.delete(1.0,'end')
                textbox5.delete(1.0,'end')
                textbox3.insert(1.0,te9)
                status.delete(1.0,'end')
                status.insert(1.0, 'Error')
                func3()
            if twos[0]=='1':
                for x in n:
                    if x=='1':
                        list7.append(x)
                        # sto='good'
                    elif x=='0':
                        list7.append(x)
                        # sto='good'
                    else:
                        # sto='bad'
                        textbox3.delete(1.0, 'end')
                        textbox4.delete(1.0, 'end')
                        textbox5.delete(1.0, 'end')
                        textbox3.insert(1.0,'Enter Only Ones & Zeros')
                        status.delete(1.0, 'end')
                        status.insert(1.0, 'Error')
                        func3()
                        break
                    # print(list7)
                list8=[]
                pib = 7
                for xox in list7:
                    go = int(xox) * 2 ** int(pib)
                    pib = pib - 1
                    list8.append(go)
                list8[0] = -128
                # print(list8)
                tota = 0
                for to in list8:
                    tota = tota + to
                te4='Decimal Number of Your Twos Complement is: '
                te5='Here: '+str(tota)
                textbox3.delete(1.0,'end')
                textbox4.delete(1.0,'end')
                textbox5.delete(1.0,'end')
                textbox3.insert(1.0, te4)
                textbox4.insert(1.0, te5)

            else:
                te1='Please Enter Valid Twos Complement'
                te2='You Know This Is 8 Bit Deals'
                te3='So the First Bit Should be 1'
                status.delete(1.0, 'end')
                textbox3.delete(1.0,'end')
                textbox4.delete(1.0,'end')
                textbox5.delete(1.0,'end')
                textbox3.insert(1.0, te1)
                textbox4.insert(1.0, te2)
                textbox5.insert(1.0, te3)
                status.insert(1.0, 'Error')
                func3()
                # first bit should one

            # list_dash=[]
            # for x in str(n):
            #     list_dash.append(str(x))
            # print(list_dash)
            # g = -1
            # while list_dash[g] == '0':
            #     list_dash[g] = '1'
            #     g = g - 1
            #     print(g)
            # list_dash[g] ='0'
            # print(list_dash)

    else:
        lz='Please Choose What You Want Below'
        textbox3.delete(1.0, 'end')
        textbox4.delete(1.0, 'end')
        textbox5.delete(1.0, 'end')
        textbox3.insert(1.0,lz)

# sts=func1() and decimal_to_binary()

button1=Button(win,text='Click Here To Convert', height=2 , width=35 ,font=('arial',12) , border=12 ,command=decimal_to_binary) #command=decimal_to_binary
button1.pack()

# win.bind("<Return>", lambda event: decimal_to_binary())

final_label=Label(win, text='Designed By Sashik Thiwanka', font=('Sans',10))
final_label.pack(anchor='e')

# def generate_readme():
#     content = """# My Tkinter App
# This is a simple GUI application to do Binary to Decimal or Decimal to Binary conversion.
# ## Features
# - Interactive UI
# - Customizable Widgets
# - Easy to Use
#
# ## Instructions
# - Always Follow Application rules and then,
#   application will work correctly
# """
#     with open("README.md", "w") as file:
#         file.write(content)
#     print("README.md created successfully!")

win.mainloop()