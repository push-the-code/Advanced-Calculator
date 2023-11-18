import math
from tkinter import *
from tkinter import ttk

switch1 = None
switch2 = None


def press(num):
    global exp
    exp += str(num)
    equation.set(exp)

def equal():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set("Error")
        exp = ""
        
def clear():
    global exp
    exp = ""
    equation.set("")


def back():
    global exp
    exp = exp[:-1]
    equation.set(exp)

def exiter():
    window.quit()
    window.destroy()

def scientific_tab():

    toplevel1 = Toplevel()
    toplevel1.geometry('400x550')
    toplevel1.minsize(400,550)
    toplevel1.maxsize(600,750)
    toplevel1.title("Scientific Calculator")

    toplevel1.columnconfigure(0,pad=1,weight=1)
    toplevel1.columnconfigure(1,pad=1,weight=1)
    toplevel1.columnconfigure(2,pad=1,weight=1)
    toplevel1.columnconfigure(3,pad=1,weight=1)
    toplevel1.columnconfigure(4,pad=1,weight=1)
    toplevel1.rowconfigure(0,pad=1,weight=1)
    toplevel1.rowconfigure(1,pad=1,weight=1)
    toplevel1.rowconfigure(2,pad=1,weight=1)
    toplevel1.rowconfigure(3,pad=1,weight=1)
    toplevel1.rowconfigure(4,pad=1,weight=1)
    toplevel1.rowconfigure(5,pad=1,weight=1)
    toplevel1.rowconfigure(6,pad=1,weight=1)
    toplevel1.rowconfigure(7,pad=1,weight=1)
    toplevel1.rowconfigure(8,pad=1,weight=1)
    toplevel1.rowconfigure(9,pad=1,weight=1)


    def one():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'1')
    def two():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'2')
    def three():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'3')
    def four():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'4')
    def five():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'5')
    def six():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'6')
    def seven():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'7')
    def eight():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'8')
    def nine():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'9')
    def zero():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.insert(pos,'0')
    def key_event(*args):
        if display2.get() == '0':
            display2.delete(0,'end')
    def add():
        pos = len(display2.get())
        display2.insert(pos,'+')
    def subtract():
        pos = len(display2.get())
        display2.insert(pos,'-')
    def multiply():
        pos = len(display2.get())
        display2.insert(pos,'*')
    def divide():
        pos = len(display2.get())
        display2.insert(pos,'/')
    def percent():
        pos = len(display2.get())
        display2.insert(pos,'%')
    def dot():
        if display2.get() == '':
            pos = len(display2.get())
            display2.insert(pos,'0.')
        else:
            pos = len(display2.get())
            display2.insert(pos,'.')
    def bracket1():
        pos = len(display2.get())
        display2.insert(pos,'(')
    def bracket2():
        pos = len(display2.get())
        display2.insert(pos,')')
    def expo():
        if display2.get() == '0':
            display2.delete(0,'end')
        pos = len(display2.get())
        display2.delete(0,'end')
        display2.insert(pos, str(math.e))
    def power():
        pos = len(display2.get())
        display2.insert(pos, '**')
    def power_two():
        pos = len(display2.get())
        display2.insert(pos, '**2')
    def factorial():
        try:
            exp = float(display2.get())
            exp = math.factorial(exp)
            display2.delete(0,'end')
            display2.insert(0, str(exp))
        except:
            display2.insert(0, math.factorial(0))
            display2.insert(0, 'fact(0)= ')
    def asinh():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.asinh(exp)
            elif switch2 is True:
                exp = math.asinh(math.radians(exp))
            else:
                exp = math.asinh(exp)
            display2.delete(0,'end')
            display2.insert(0, str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.asinh(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def acosh():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.acosh(exp)
            elif switch2 is True:
                exp = math.acosh(math.radians(exp))
            else:
                exp = math.acosh(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            display2.delete(0,'end')
            display2.insert(0,'Invalid Option')
            
    def atanh():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.atanh(exp)
            elif switch2 is True:
                exp = math.atanh(math.radians(exp))
            else:
                exp = math.atanh(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.atanh(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def sinh():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.sinh(exp)
            elif switch2 is True:
                exp = math.sinh(math.radians(exp))
            else:
                exp = math.sinh(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.sinh(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def cosh():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.cosh(exp)
            elif switch2 is True:
                exp = math.cosh(math.radians(exp))
            else:
                exp = math.cosh(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.cosh(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def tanh():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.tanh(exp)
            elif switch2 is True:
                exp = math.tanh(math.radians(exp))
            else:
                exp = math.tanh(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.tanh(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def asin():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.asin(exp)
            elif switch2 is True:
                exp = math.asin(math.radians(exp))
            else:
                exp = math.asin(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.asin(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def acos():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.acos(exp)
            elif switch2 is True:
                exp = math.acos(math.radians(exp))
            else:
                exp = math.acos(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.acos(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def atan():
        try:
            exp = float(display2.get())
            exp = math.atan(exp)
            if switch1 is True:
                exp = math.atan(exp)
            elif switch2 is True:
                exp = math.atan(math.radians(exp))
            else:
                exp = math.atan(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.atan(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def sin():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.sin(exp)
            elif switch2 is True:
                exp = math.sin(math.radians(exp))
            else:
                exp = math.sin(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.sin(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def cos():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.cos(exp)
            elif switch2 is True:
                exp = math.cos(math.radians(exp))
            else:
                exp = math.cos(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.cos(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def tan():
        try:
            exp = float(display2.get())
            if switch1 is True:
                exp = math.tan(exp)
            elif switch2 is True:
                exp = math.tan(math.radians(exp))
            else:
                exp = math.tan(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            if display2.get() == '':
                display2.delete(0,'end')
                display2.insert(0,math.tan(0))
            else:
                display2.delete(0,'end')
                display2.insert(0,'Invalid Option')
    def log():
        try:
            exp = float(display2.get())
            exp = math.log(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            display2.delete(0,'end')
            display2.insert(0,'Invalid Input')
    def log2():
        try:
            exp = float(display2.get())
            exp = math.log2(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            display2.delete(0,'end')
            display2.insert(0,'Invalid Input')
    def log10():
        try:
            exp = float(display2.get())
            exp = math.log10(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            display2.delete(0,'end')
            display2.insert(0,'Invalid Input')
    def ln():
        try:
            exp = float(display2.get())
            exp = math.log(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            display2.delete(0,'end')
            display2.insert(0,'Invalid Input')
    def sqrt():
        try:
            exp = float(display2.get())
            exp = math.sqrt(exp)
            display2.delete(0,'end')
            display2.insert(0,str(exp))
        except:
            display2.delete(0,'end')
            display2.insert(0,'Invalid Input')
    def pi():
        try:
            if display2.get() == '0':
                display2.delete(0,'end')
            pos = len(display2.get())
            display2.delete(0,'end')
            display2.insert(pos, str(math.pi))
        except:
            display2.delete(0,'end')
            display2.insert(0,str(math.pi))
            
    def sw1():
        global switch1
        if switch1 is None:
            switch1 = True
        else:
            switch1 = None
            
    def sw2():
        global switch2
        if switch2 is None:
            switch2 = True
        else:
            switch2 = None

    def clear(*args):
        display2.delete(0,'end')
    def backspace(*args):
        pos = len(display2.get())
        disp = str(display2.get())
        display2.delete(0,'end')
        display2.insert(0, disp[:pos-1])
    def equal(*args):
        try:
            exp = display2.get()
            exp = eval(exp)
            display2.delete(0,'end')
            display2.insert(0, exp)
        except:
            display2.delete(0,'end')
            display2.insert(0,' ')
    def key(*args):
        if display2.get() == '0':
            display2.delete(0,'end')

    def enter1(e):
        sin['background'] = '#CFD8DC'
    def leave1(l):
        sin['background'] = 'SystemButtonFace'
    def enter2(e):
        cos['background'] = '#CFD8DC'
    def leave2(l):
        cos['background'] = 'SystemButtonFace'
    def enter3(e):
        tan['background'] = '#CFD8DC'
    def leave3(l):
        tan['background'] = 'SystemButtonFace'
    def enter4(e):
        log['background'] = '#CFD8DC'
    def leave4(l):
        log['background'] = 'SystemButtonFace'
    def enter5(e):
        rad['background'] = '#CFD8DC'
    def leave5(l):
        rad['background'] = 'SystemButtonFace'
    def enter6(e):
        a_sin['background'] = '#CFD8DC'
    def leave6(l):
        a_sin['background'] = 'SystemButtonFace'
    def enter7(e):
        a_cos['background'] = '#CFD8DC'
    def leave7(l):
        a_cos['background'] = 'SystemButtonFace'
    def enter8(e):
        a_tan['background'] = '#CFD8DC'
    def leave8(l):
        a_tan['background'] = 'SystemButtonFace'
    def enter9(e):
        log2['background'] = '#CFD8DC'
    def leave9(l):
        log2['background'] = 'SystemButtonFace'
    def enter10(e):
        deg['background'] = '#CFD8DC'
    def leave10(l):
        deg['background'] = 'SystemButtonFace'
    def enter11(e):
        sin_h['background'] = '#CFD8DC'
    def leave11(l):
        sin_h['background'] = 'SystemButtonFace'
    def enter12(e):
        cos_h['background'] = '#CFD8DC'
    def leave12(l):
        cos_h['background'] = 'SystemButtonFace'
    def enter13(e):
        tan_h['background'] = '#CFD8DC'
    def leave13(l):
        tan_h['background'] = 'SystemButtonFace'
    def enter14(e):
        log10['background'] = '#CFD8DC'
    def leave14(l):
        log10['background'] = 'SystemButtonFace'
    def enter15(e):
        pi['background'] = '#CFD8DC'
    def leave15(l):
        pi['background'] = 'SystemButtonFace'
    def enter16(e):
        a_sin_h['background'] = '#CFD8DC'
    def leave16(l):
        a_sin_h['background'] = 'SystemButtonFace'
    def enter17(e):
        a_cos_h['background'] = '#CFD8DC'
    def leave17(l):
        a_cos_h['background'] = 'SystemButtonFace'
    def enter18(e):
        a_tan_h['background'] = '#CFD8DC'
    def leave18(l):
        a_tan_h['background'] = 'SystemButtonFace'
    def enter19(e):
        l_n['background'] = '#CFD8DC'
    def leave19(l):
        l_n['background'] = 'SystemButtonFace'
    def enter20(e):
        square['background'] = '#CFD8DC'
    def leave20(l):
        square['background'] = 'SystemButtonFace'
    def enter21(e):
        clear['background'] = '#CFD8DC'
    def leave21(l):
        clear['background'] = 'SystemButtonFace'
    def enter22(e):
        percent['background'] = '#CFD8DC'
    def leave22(l):
        percent['background'] = 'SystemButtonFace'
    def enter23(e):
        backspace['background'] = '#CFD8DC'
    def leave23(l):
        backspace['background'] = 'SystemButtonFace'
    def enter24(e):
        power2['background'] = '#CFD8DC'
    def leave24(l):
        power2['background'] = 'SystemButtonFace'
    def enter25(e):
        divide['background'] = '#CFD8DC'
    def leave25(l):
        divide['background'] = 'SystemButtonFace'
    def enter26(e):
        seven['background'] = '#CFD8DC'
    def leave26(l):
        seven['background'] = 'SystemButtonFace'
    def enter27(e):
        eight['background'] = '#CFD8DC'
    def leave27(l):
        eight['background'] = 'SystemButtonFace'
    def enter28(e):
        nine['background'] = '#CFD8DC'
    def leave28(l):
        nine['background'] = 'SystemButtonFace'
    def enter29(e):
        factorial['background'] = '#CFD8DC'
    def leave29(l):
        factorial['background'] = 'SystemButtonFace'
    def enter30(e):
        multiply['background'] = '#CFD8DC'
    def leave30(l):
        multiply['background'] = 'SystemButtonFace'
    def enter31(e):
        four['background'] = '#CFD8DC'
    def leave31(l):
        four['background'] = 'SystemButtonFace'
    def enter32(e):
        five['background'] = '#CFD8DC'
    def leave32(l):
        five['background'] = 'SystemButtonFace'
    def enter33(e):
        six['background'] = '#CFD8DC'
    def leave33(l):
        six['background'] = 'SystemButtonFace'
    def enter34(e):
        powerx['background'] = '#CFD8DC'
    def leave34(l):
        powerx['background'] = 'SystemButtonFace'
    def enter35(e):
        subtract['background'] = '#CFD8DC'
    def leave35(l):
        subtract['background'] = 'SystemButtonFace'
    def enter36(e):
        one['background'] = '#CFD8DC'
    def leave36(l):
        one['background'] = 'SystemButtonFace'
    def enter37(e):
        two['background'] = '#CFD8DC'
    def leave37(l):
        two['background'] = 'SystemButtonFace'
    def enter38(e):
        three['background'] = '#CFD8DC'
    def leave38(l):
        three['background'] = 'SystemButtonFace'
    def enter39(e):
        expo['background'] = '#CFD8DC'
    def leave39(l):
        expo['background'] = 'SystemButtonFace'
    def enter40(e):
        add['background'] = '#CFD8DC'
    def leave40(l):
        add['background'] = 'SystemButtonFace'
    def enter41(e):
        dot['background'] = '#CFD8DC'
    def leave41(l):
        dot['background'] = 'SystemButtonFace'
    def enter42(e):
        zero['background'] = '#CFD8DC'
    def leave42(l):
        zero['background'] = 'SystemButtonFace'
    def enter43(e):
        bracket1['background'] = '#CFD8DC'
    def leave43(l):
        bracket1['background'] = 'SystemButtonFace'
    def enter44(e):
        bracket2['background'] = '#CFD8DC'
    def leave44(l):
        bracket2['background'] = 'SystemButtonFace'
    def enter45(e):
        equal['background'] = '#CFD8DC'
    def leave45(l):
        equal['background'] = 'SystemButtonFace'
        

    display2 = Entry(toplevel1,validatecommand='%i',font="Ariel 20",relief=SUNKEN,borderwidth=7,justify=RIGHT)
    display2.grid(row=0,columnspan=5,ipady=20, sticky='nsew')
    display2.focus()
    display2.bind('<Return>',equal)
    display2.bind('<Escape>',clear)
    display2.bind('<BackSpace>',backspace)
    display2.bind('<Key-0>',key)
    display2.bind('<Key-1>',key)
    display2.bind('<Key-2>',key)
    display2.bind('<Key-4>',key)
    display2.bind('<Key-5>',key)
    display2.bind('<Key-6>',key)
    display2.bind('<Key-8>',key)
    display2.bind('<Key-9>',key)
    display2.bind('<Key-.>',key)
    

    sin = Button(toplevel1,text='sin',font='Ariel 16',relief=GROOVE,command=sin)
    sin.grid(row=1,column=0,ipady=10,sticky='nsew')
    sin.bind("<Enter>",enter1)
    sin.bind("<Leave>",leave1)
    
    cos = Button(toplevel1,text='cos',font='Ariel 16',relief=GROOVE,command=cos)
    cos.grid(row=1,column=1,ipady=10,sticky='nsew')
    cos.bind("<Enter>",enter2)
    cos.bind("<Leave>",leave2)
    
    tan = Button(toplevel1,text='tan',font='Ariel 16',relief=GROOVE,command=tan)
    tan.grid(row=1,column=2,ipady=10,sticky='nsew')
    tan.bind("<Enter>",enter3)
    tan.bind("<Leave>",leave3)
    
    log = Button(toplevel1,text='log',font='Ariel 16',relief=GROOVE,command=log)
    log.grid(row=1,column=3,ipady=10,sticky='nsew')
    log.bind("<Enter>",enter4)
    log.bind("<Leave>",leave4)
    
    rad = Checkbutton(toplevel1,text='RAD',font='Ariel 16',relief=GROOVE,command=sw1)
    rad.grid(row=1,column=4,ipady=10,sticky='nsew')
    rad.bind("<Enter>",enter5)
    rad.bind("<Leave>",leave5)

    a_sin = Button(toplevel1,text='sin⁻¹',font='Ariel 16',relief=GROOVE,command=asin)
    a_sin.grid(row=2,column=0,ipady=10,sticky='nsew')
    a_sin.bind("<Enter>",enter6)
    a_sin.bind("<Leave>",leave6)
    
    a_cos = Button(toplevel1,text='cos⁻¹',font='Ariel 16',relief=GROOVE,command=acos)
    a_cos.grid(row=2,column=1,ipady=10,sticky='nsew')
    a_cos.bind("<Enter>",enter7)
    a_cos.bind("<Leave>",leave7)
    
    a_tan = Button(toplevel1,text='tan⁻¹',font='Ariel 16',relief=GROOVE,command=atan)
    a_tan.grid(row=2,column=2,ipady=10,sticky='nsew')
    a_tan.bind("<Enter>",enter8)
    a_tan.bind("<Leave>",leave8)
    
    log2 = Button(toplevel1,text='log2',font='Ariel 16',relief=GROOVE,command=log2)
    log2.grid(row=2,column=3,ipady=10,sticky='nsew')
    log2.bind("<Enter>",enter9)
    log2.bind("<Leave>",leave9)
    
    deg = Checkbutton(toplevel1,text='DEG',font='Ariel 16',relief=GROOVE,command=sw2)
    deg.grid(row=2,column=4,ipady=10,sticky='nsew')
    deg.bind("<Enter>",enter10)
    deg.bind("<Leave>",leave10)

    sin_h = Button(toplevel1,text='sinh',font='Ariel 16',relief=GROOVE,command=sinh)
    sin_h.grid(row=3,column=0,ipady=10,sticky='nsew')
    sin_h.bind("<Enter>",enter11)
    sin_h.bind("<Leave>",leave11)
    
    cos_h = Button(toplevel1,text='cosh',font='Ariel 16',relief=GROOVE,command=cosh)
    cos_h.grid(row=3,column=1,ipady=10,sticky='nsew')
    cos_h.bind("<Enter>",enter12)
    cos_h.bind("<Leave>",leave12)
    
    tan_h = Button(toplevel1,text='tanh',font='Ariel 16',relief=GROOVE,command=tanh)
    tan_h.grid(row=3,column=2,ipady=10,sticky='nsew')
    tan_h.bind("<Enter>",enter13)
    tan_h.bind("<Leave>",leave13)
    
    log10 = Button(toplevel1,text='log10',font='Ariel 16',relief=GROOVE,command=log10)
    log10.grid(row=3,column=3,ipady=10,sticky='nsew')
    log10.bind("<Enter>",enter14)
    log10.bind("<Leave>",leave14)
    
    pi = Button(toplevel1,text='π',font='Ariel 16',relief=GROOVE,command=pi)
    pi.grid(row=3,column=4,ipady=10,sticky='nsew')
    pi.bind("<Enter>",enter15)
    pi.bind("<Leave>",leave15)

    a_sin_h = Button(toplevel1,text='sinh⁻¹',font='Ariel 16',relief=GROOVE,command=asinh)
    a_sin_h.grid(row=4,column=0,ipady=10,sticky='nsew')
    a_sin_h.bind("<Enter>",enter16)
    a_sin_h.bind("<Leave>",leave16)
    
    a_cos_h = Button(toplevel1,text='cosh⁻¹',font='Ariel 16',relief=GROOVE,command=acosh)
    a_cos_h.grid(row=4,column=1,ipady=10,sticky='nsew')
    a_cos_h.bind("<Enter>",enter17)
    a_cos_h.bind("<Leave>",leave17)
    
    a_tan_h = Button(toplevel1,text='tanh⁻¹',font='Ariel 16',relief=GROOVE,command=atanh)
    a_tan_h.grid(row=4,column=2,ipady=10,sticky='nsew')
    a_tan_h.bind("<Enter>",enter18)
    a_tan_h.bind("<Leave>",leave18)
    
    l_n = Button(toplevel1,text='ln',font='Ariel 16',relief=GROOVE,command=ln)
    l_n.grid(row=4,column=3,ipady=10,sticky='nsew')
    l_n.bind("<Enter>",enter19)
    l_n.bind("<Leave>",leave19)
    
    
    square = Button(toplevel1,text='√',font='Ariel 16',relief=GROOVE,command=sqrt)
    square.grid(row=4,column=4,ipady=10,sticky='nsew')
    square.bind("<Enter>",enter20)
    square.bind("<Leave>",leave20)

    clear = Button(toplevel1,text=chr(67),font='Ariel 16',relief=GROOVE,command=clear)
    clear.grid(row=5,column=0,ipady=10,sticky='nsew')
    clear.bind("<Enter>",enter21)
    clear.bind("<Leave>",leave21)
    
    percent = Button(toplevel1,text='%',font='Ariel 16',relief=GROOVE,command=percent)
    percent.grid(row=5,column=1,ipady=10,sticky='nsew')
    percent.bind("<Enter>",enter22)
    percent.bind("<Leave>",leave22)
    
    backspace = Button(toplevel1,text='⌫',font='Ariel 16',relief=GROOVE,command=backspace)
    backspace.grid(row=5,column=2,ipady=10,sticky='nsew')
    backspace.bind("<Enter>",enter23)
    backspace.bind("<Leave>",leave23)
    
    power2 = Button(toplevel1,text='x²',font='Ariel 16',relief=GROOVE,command=power_two)
    power2.grid(row=5,column=3,ipady=10,sticky='nsew')
    power2.bind("<Enter>",enter24)
    power2.bind("<Leave>",leave24)
    
    divide = Button(toplevel1,text='÷',font='Ariel 18',relief=GROOVE,command=divide)
    divide.grid(row=5,column=4,ipady=10,sticky='nsew')
    divide.bind("<Enter>",enter25)
    divide.bind("<Leave>",leave25)

    seven = Button(toplevel1,text='7',font='Ariel 16',relief=GROOVE,command=seven)
    seven.grid(row=6,column=0,ipady=10,sticky='nsew')
    seven.bind("<Enter>",enter26)
    seven.bind("<Leave>",leave26)
    
    eight = Button(toplevel1,text='8',font='Ariel 16',relief=GROOVE,command=eight)
    eight.grid(row=6,column=1,ipady=10,sticky='nsew')
    eight.bind("<Enter>",enter27)
    eight.bind("<Leave>",leave27)
    
    nine = Button(toplevel1,text='9',font='Ariel 16',relief=GROOVE,command=nine)
    nine.grid(row=6,column=2,ipady=10,sticky='nsew')
    nine.bind("<Enter>",enter28)
    nine.bind("<Leave>",leave28)
    
    factorial = Button(toplevel1,text='!',font='Ariel 16',relief=GROOVE,command=factorial)
    factorial.grid(row=6,column=3,ipady=10,sticky='nsew')
    factorial.bind("<Enter>",enter29)
    factorial.bind("<Leave>",leave29)
    
    multiply = Button(toplevel1,text='×',font='Ariel 18',relief=GROOVE,command=multiply)
    multiply.grid(row=6,column=4,ipady=10,sticky='nsew')
    multiply.bind("<Enter>",enter30)
    multiply.bind("<Leave>",leave30)

    four = Button(toplevel1,text='4',font='Ariel 16',relief=GROOVE,command=four)
    four.grid(row=7,column=0,ipady=10,sticky='nsew')
    four.bind("<Enter>",enter31)
    four.bind("<Leave>",leave31)
    
    five = Button(toplevel1,text='5',font='Ariel 16',relief=GROOVE,command=five)
    five.grid(row=7,column=1,ipady=10,sticky='nsew')
    five.bind("<Enter>",enter32)
    five.bind("<Leave>",leave32)
    
    six = Button(toplevel1,text='6',font='Ariel 16',relief=GROOVE,command=six)
    six.grid(row=7,column=2,ipady=10,sticky='nsew')
    six.bind("<Enter>",enter33)
    six.bind("<Leave>",leave33)
    
    powerx = Button(toplevel1,text='^',font='Ariel 16',relief=GROOVE,command=power)
    powerx.grid(row=7,column=3,ipady=10,sticky='nsew')
    powerx.bind("<Enter>",enter34)
    powerx.bind("<Leave>",leave34)
    
    subtract = Button(toplevel1,text='-',font='Ariel 18',relief=GROOVE,command=subtract)
    subtract.grid(row=7,column=4,ipady=10,sticky='nsew')
    subtract.bind("<Enter>",enter35)
    subtract.bind("<Leave>",leave35)

    one = Button(toplevel1,text='1',font='Ariel 16',relief=GROOVE,command=one)
    one.grid(row=8,column=0,ipady=10,sticky='nsew')
    one.bind("<Enter>",enter36)
    one.bind("<Leave>",leave36)
    
    two = Button(toplevel1,text='2',font='Ariel 16',relief=GROOVE,command=two)
    two.grid(row=8,column=1,ipady=10,sticky='nsew')
    two.bind("<Enter>",enter37)
    two.bind("<Leave>",leave37)
    
    three = Button(toplevel1,text='3',font='Ariel 16',relief=GROOVE,command=three)
    three.grid(row=8,column=2,ipady=10,sticky='nsew')
    three.bind("<Enter>",enter38)
    three.bind("<Leave>",leave38)
    
    expo = Button(toplevel1,text='e⨯',font='Ariel 16',relief=GROOVE,command=expo)
    expo.grid(row=8,column=3,ipady=10,sticky='nsew')
    expo.bind("<Enter>",enter39)
    expo.bind("<Leave>",leave39)
    
    add = Button(toplevel1,text='+',font='Ariel 18',relief=GROOVE,command=add)
    add.grid(row=8,column=4,ipady=10,sticky='nsew')
    add.bind("<Enter>",enter40)
    add.bind("<Leave>",leave40)

    dot = Button(toplevel1,text='•',font='Ariel 16',relief=GROOVE,command=dot)
    dot.grid(row=9,column=0,ipady=10,sticky='nsew')
    dot.bind("<Enter>",enter41)
    dot.bind("<Leave>",leave41)
    
    zero = Button(toplevel1,text='0',font='Ariel 16',relief=GROOVE,command=zero)
    zero.grid(row=9,column=1,ipady=10,sticky='nsew')
    zero.bind("<Enter>",enter42)
    zero.bind("<Leave>",leave42)
    
    bracket1 = Button(toplevel1,text='(',font='Ariel 16',relief=GROOVE,command=bracket1)
    bracket1.grid(row=9,column=2,ipady=10,sticky='nsew')
    bracket1.bind("<Enter>",enter43)
    bracket1.bind("<Leave>",leave43)
    
    bracket2 = Button(toplevel1,text=')',font='Ariel 16',relief=GROOVE,command=bracket2)
    bracket2.grid(row=9,column=3,ipady=10,sticky='nsew')
    bracket2.bind("<Enter>",enter44)
    bracket2.bind("<Leave>",leave44)
    
    equal = Button(toplevel1,text='=',font='Ariel 18',relief=GROOVE,command=equal)
    equal.grid(row=9,column=4,ipady=10,sticky='nsew')
    equal.bind("<Enter>",enter45)
    equal.bind("<Leave>",leave45)

    toplevel1.mainloop()

def  length_converter():
    toplevel2 = Toplevel()
    toplevel2.title("Length Conversion")
    toplevel2.resizable(width='false', height='false')
    factors = {'nmi':1852, 'mi':1609.34, 'yd':0.9144, 'ft':0.3048, 'in':0.0254, 'km':1000, 'm':1, 'cm':0.01, 'mm':0.001, 'dm':0.1, 'mim':0.000001, 'nm':0.000000001, 'pm':0.000000000001}
    ids = {'Decimeter':'dm', 'Millimeter':'mm', 'Kilometer':'km', 'Meter':'m','Centimeter':'cm', 'Micrometer':'mim', 'Nanometer':'nm', 'Picometer':'pm', 'Yard':'yd', 'Nautical Mile':'nmi', 'Foot':'ft', 'Mile':'mi', 'Inch':'in'}
    
    def enter7(e):
        seven['background'] = '#CFD8DC'
    def leav7(e):
        seven['background'] = 'SystemButtonFace'
    def enter8(e):
        eight['background'] = '#CFD8DC'
    def leav8(e):
        eight['background'] = 'SystemButtonFace'
    def enter9(e):
        nine['background'] = '#CFD8DC'
    def leav9(e):
        nine['background'] = 'SystemButtonFace'
    def enterBS(e):
        backspace['background'] = '#CFD8DC'
    def leavBS(e):
        backspace['background'] = 'SystemButtonFace'
    def enter4(e):
        four['background'] = '#CFD8DC'
    def leav4(e):
        four['background'] = 'SystemButtonFace'
    def enter5(e):
        five['background'] = '#CFD8DC'
    def leav5(e):
        five['background'] = 'SystemButtonFace'
    def enter6(e):
        six['background'] = '#CFD8DC'
    def leav6(e):
        six['background'] = 'SystemButtonFace'
    def enterC(e):
        clear['background'] = '#CFD8DC'
    def leavC(e):
        clear['background'] = 'SystemButtonFace'
    def enter1(e):
        one['background'] = '#CFD8DC'
    def leav1(e):
        one['background'] = 'SystemButtonFace'
    def enter2(e):
        two['background'] = '#CFD8DC'
    def leav2(e):
        two['background'] = 'SystemButtonFace'
    def enter3(e):
        three['background'] = '#CFD8DC'
    def leav3(e):
        three['background'] = 'SystemButtonFace'
    def enterDt(e):
        dot['background'] = '#CFD8DC'
    def leavDt(e):
        dot['background'] = 'SystemButtonFace'
    def enter00(e):
        zeroZ['background'] = '#CFD8DC'
    def leav00(e):
        zeroZ['background'] = 'SystemButtonFace'
    def enter0(e):
        zero['background'] = '#CFD8DC'
    def leav0(e):
        zero['background'] = 'SystemButtonFace'
    def enterEq(e):
        equal['background'] = '#CFD8DC'
    def leavEq(e):
        equal['background'] = 'SystemButtonFace'
        
    def seven():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'7')
    def eight():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'8')
    def nine():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'9')
    def backspace(*args):
        pos = len(display1.get())
        val = str(display1.get())
        display1.delete(0,'end')
        display1.insert(0,val[:pos-1])
    def four():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'4')
    def five():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'5')
    def six():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'6')
    def clear(*args):
        display1.delete(0,'end')
        display2.delete(0,'end')
    def one():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'1')
    def two():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'2')
    def three():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'3')
    def dot():
        if display.get()=="":
            pos = len(display.get())
            display.insert(pos,'0.')
        else:
            pos = len(display.get())
            display.insert(pos,'.')
    def zeroZ():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'00')
    def zero():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'0')
    def convert(amount, fromV, toV):
        if fromV != 'm':
            amount = amount*factors[fromV]
            return amount/factors[toV]
        else:
            return amount/factors[toV]
    def equal():
        try:
            amount = float(display1.get())
        except ValueError:
            out_amount.set('Invalid Input')
            return None
        if in_unit.get() == 'Select a unit' or out_unit.get() == 'Select a unit':
            out_amount.set('Please choose a unit')
            return None
        else:
            fromV = ids[in_unit.get()]
            toV = ids[out_unit.get()]
            out_amount.set(convert(amount, fromV, toV))
    def key(*args):
        if display.get() == '0':
            display.delete(0,'end')

    in_amount = StringVar()
    in_amount.set('')
    out_amount = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    
    display1 = Entry(toplevel2, textvariable=in_amount, validatecommand=('%i'),font="Ariel 20",relief=SUNKEN,borderwidth=5,justify=RIGHT)
    display1.grid(row=0,columnspan=5,ipady=10,sticky='nsew')
    display1.bind("<Key-0>",key)
    display1.bind("<Key-1>",key)
    display1.bind("<Key-2>",key)
    display1.bind("<Key-3>",key)
    display1.bind("<Key-4>",key)
    display1.bind("<Key-5>",key)
    display1.bind("<Key-6>",key)
    display1.bind("<Key-7>",key)
    display1.bind("<Key-8>",key)
    display1.bind("<Key-9>",key)
    display1.bind('Key-.',key)
    display1.bind('<Return>',equal)
    display1.bind('<Escape>',clear)
    display1.bind('<BackSpace>',backspace)
    display1.focus()

    fromVal = ttk.OptionMenu(toplevel2, in_unit,  '', 'Decimeter', 'Millimeter', 'Kilometer', 'Meter', 'Centimeter', 'Micrometer', 'Nanometer', 'Picometer', 'Yard', 'Nautical Mile', 'Foot', 'Mile', 'Inch')
    fromVal.grid(row=1, columnspan=4, sticky='nsew')
    fromVal.config(in_unit.set('Select a unit'))
    
    display2 = Entry(toplevel2, textvariable=out_amount, state='readonly', validatecommand=("%i"),font="Ariel 20",relief=SUNKEN,borderwidth=5,justify=RIGHT)
    display2.grid(row=2,columnspan=4,ipady=10,sticky='nsew')

    toVal = ttk.OptionMenu(toplevel2, out_unit, '', 'Decimeter', 'Millimeter', 'Kilometer', 'Meter', 'Centimeter', 'Micrometer', 'Nanometer', 'Picometer', 'Yard', 'Nautical Mile', 'Foot', 'Mile', 'Inch')
    toVal.grid(row=3, columnspan=4, sticky='nsew')
    toVal.config(out_unit.set('Select a unit '))
    
    seven = Button(toplevel2, text="7", command=seven, font="Ariel 17",relief=GROOVE)
    seven.grid(row=4, column=0, ipadx=7, ipady=10,sticky="nsew")
    seven.bind("<Enter>",enter7)
    seven.bind("<Leave>",leav7)

    eight = Button(toplevel2, text="8", command=eight, font="Ariel 17",relief=GROOVE)
    eight.grid(row=4, column=1, ipadx=7, ipady=10,sticky="nsew")
    eight.bind("<Enter>",enter8)
    eight.bind("<Leave>",leav8)

    nine = Button(toplevel2, text="9", command=nine, font="Ariel 17",relief=GROOVE)
    nine.grid(row=4, column=2, ipadx=7, ipady=10,sticky="nsew")
    nine.bind("<Enter>",enter9)
    nine.bind("<Leave>",leav9)

    backspace = Button(toplevel2, text="⌫", command=backspace, font="Ariel 14", relief=GROOVE)
    backspace.grid(row=4, column=3, ipadx=8, ipady=10,sticky="nsew")
    backspace.bind("<Enter>",enterBS)
    backspace.bind("<Leave>",leavBS)

    four = Button(toplevel2, text="4", command=four, font="Ariel 17",relief=GROOVE)
    four.grid(row=5, column=0, ipadx=7, ipady=10,sticky="nsew")
    four.bind("<Enter>",enter4)
    four.bind("<Leave>",leav4)

    five = Button(toplevel2, text="5", command=five, font="Ariel 17",relief=GROOVE)
    five.grid(row=5, column=1, ipadx=7, ipady=10,sticky="nsew")
    five.bind("<Enter>",enter5)
    five.bind("<Leave>",leav5)

    six = Button(toplevel2, text="6", command=six, font="Ariel 17",relief=GROOVE)
    six.grid(row=5, column=2, ipadx=7, ipady=10,sticky="nsew")
    six.bind("<Enter>",enter6)
    six.bind("<Leave>",leav6)

    clear = Button(toplevel2, text=chr(67), command=clear, font="Ariel 14", relief=GROOVE)
    clear.grid(row=5, column=3, ipadx=8, ipady=10,sticky="nsew")
    clear.bind("<Enter>",enterC)
    clear.bind("<Leave>",leavC)

    one = Button(toplevel2, text="1", command=one, font="Ariel 17", relief=GROOVE)
    one.grid(row=6, column=0, ipadx=7, ipady=10, sticky="nsew")
    one.bind("<Enter>",enter1)
    one.bind("<Leave>",leav1)

    two = Button(toplevel2, text="2", command=two, font="Ariel 17", relief=GROOVE)
    two.grid(row=6, column=1, ipadx=7, ipady=10, sticky="nsew")
    two.bind("<Enter>",enter2)
    two.bind("<Leave>",leav2)

    three = Button(toplevel2, text="3", command=three, font="Ariel 17", relief=GROOVE)
    three.grid(row=6, column=2, ipadx=7, ipady=10, sticky="nsew")
    three.bind("<Enter>",enter3)
    three.bind("<Leave>",leav3)

    dot = Button(toplevel2,text='•',font='Ariel 17',relief=GROOVE,command=dot)
    dot.grid(row=7,column=2, ipadx=7, ipady=10,sticky='nsew')
    dot.bind("<Enter>",enterDt)
    dot.bind("<Leave>",leavDt)

    zeroZ = Button(toplevel2,text='00',font='Ariel 15',relief=GROOVE,command=zeroZ)
    zeroZ.grid(row=7,column=0, ipadx=7, ipady=10,sticky='nsew')
    zeroZ.bind("<Enter>",enter00)
    zeroZ.bind("<Leave>",leav00)

    zero = Button(toplevel2,text='0',font='Ariel 17',relief=GROOVE,command=zero)
    zero.grid(row=7,column=1, ipadx=7, ipady=10,sticky='nsew')
    zero.bind("<Enter>",enter0)
    zero.bind("<Leave>",leav0)
    
    equal = Button(toplevel2,text='=',font='Ariel 17',relief=GROOVE,command=equal)
    equal.grid(row=7,column=3, ipadx=7, ipady=10,sticky='nsew')
    equal.bind("<Enter>",enterEq)
    equal.bind("<Leave>",leavEq)
    
    toplevel2.mainloop()
    
def  area_converter():
    toplevel3 = Toplevel()
    toplevel3.resizable(width='false', height='false')
    toplevel3.title("Area Conversion")
    
    factors = {'sq_m':1, 'sq_dm':0.01, 'sq_cm':0.0001, 'sq_km':1000000, 'sq_mm':0.000001, 'ar':100, 'hec':10000, 'sq_mi':2590000.0, 'sq_rd':25.292827712845468, 'sq_yd':0.8361204013377926, 'sq_ft':0.0929022668153103, 'sq_in':0.0006451612903225806, 'acr':4046.944556859571024}
    ids = {'Square Meter':'sq_m', 'Square Decimeter':'sq_dm', 'Square Centimeter':'sq_cm', 'Square Centimeter':'sq_cm', 'Square Kilometer':'sq_km', 'Square Millimeter':'sq_mm', 'Are':'ar', 'Hectare':'hec', 'Square Miles':'sq_mi', 'Square Rod':'sq_rd', 'Square Yard':'sq_yd', 'Square Foot':'sq_ft', 'Square Inch':'sq_in', 'Acre':'acr'}

    in_amount = StringVar()
    in_amount.set('')
    out_amount = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()

    def enter7(e):
        seven['background'] = '#CFD8DC'
    def leav7(e):
        seven['background'] = 'SystemButtonFace'
    def enter8(e):
        eight['background'] = '#CFD8DC'
    def leav8(e):
        eight['background'] = 'SystemButtonFace'
    def enter9(e):
        nine['background'] = '#CFD8DC'
    def leav9(e):
        nine['background'] = 'SystemButtonFace'
    def enterBS(e):
        backspace['background'] = '#CFD8DC'
    def leavBS(e):
        backspace['background'] = 'SystemButtonFace'
    def enter4(e):
        four['background'] = '#CFD8DC'
    def leav4(e):
        four['background'] = 'SystemButtonFace'
    def enter5(e):
        five['background'] = '#CFD8DC'
    def leav5(e):
        five['background'] = 'SystemButtonFace'
    def enter6(e):
        six['background'] = '#CFD8DC'
    def leav6(e):
        six['background'] = 'SystemButtonFace'
    def enterC(e):
        clear['background'] = '#CFD8DC'
    def leavC(e):
        clear['background'] = 'SystemButtonFace'
    def enter1(e):
        one['background'] = '#CFD8DC'
    def leav1(e):
        one['background'] = 'SystemButtonFace'
    def enter2(e):
        two['background'] = '#CFD8DC'
    def leav2(e):
        two['background'] = 'SystemButtonFace'
    def enter3(e):
        three['background'] = '#CFD8DC'
    def leav3(e):
        three['background'] = 'SystemButtonFace'
    def enterDt(e):
        dot['background'] = '#CFD8DC'
    def leavDt(e):
        dot['background'] = 'SystemButtonFace'
    def enter00(e):
        zeroZ['background'] = '#CFD8DC'
    def leav00(e):
        zeroZ['background'] = 'SystemButtonFace'
    def enter0(e):
        zero['background'] = '#CFD8DC'
    def leav0(e):
        zero['background'] = 'SystemButtonFace'
    def enterEq(e):
        equal['background'] = '#CFD8DC'
    def leavEq(e):
        equal['background'] = 'SystemButtonFace'

    def seven():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'7')
    def eight():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'8')
    def nine():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'9')
    def backspace(*args):
        pos = len(display1.get())
        val = str(display1.get())
        display1.delete(0,'end')
        display1.insert(0,val[:pos-1])
    def four():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'4')
    def five():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'5')
    def six():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'6')
    def clear(*args):
        display1.delete(0,'end')
        display2.delete(0,'end')
    def one():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'1')
    def two():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'2')
    def three():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'3')
    def dot():
        if display1.get()=="":
            pos = len(display.get())
            display.insert(pos,'0.')
        else:
            pos = len(display.get())
            display.insert(pos,'.')
    def zeroZ():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'00')
    def zero():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'0')
    def convert(amount, fromV, toV):
        if fromV != 'sq_m':
            amount = amount*factors[fromV]
            return amount/factors[toV]
        else:
            return amount/factors[toV]
    def equal():
        try:
            amount = float(display1.get())
        except ValueError:
            out_amount.set('Invalid Input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amount.set('Please choose a unit')
            return None
        else:
            fromV = ids[in_unit.get()]
            toV = ids[out_unit.get()]
            out_amount.set(convert(amount, fromV, toV))
    def key(*args):
        if display.get() == '0':
            display.delete(0,'end')
    
    display1 = Entry(toplevel3, textvariable=in_amount, validatecommand=('%i'),font="Ariel 20", relief=SUNKEN, borderwidth=5, justify=RIGHT)
    display1.grid(row=0,columnspan=5,ipady=10,sticky='nsew')
    display1.bind("<Key-0>",key)
    display1.bind("<Key-1>",key)
    display1.bind("<Key-2>",key)
    display1.bind("<Key-3>",key)
    display1.bind("<Key-4>",key)
    display1.bind("<Key-5>",key)
    display1.bind("<Key-6>",key)
    display1.bind("<Key-7>",key)
    display1.bind("<Key-8>",key)
    display1.bind("<Key-9>",key)
    display1.bind('Key-.',key)
    display1.bind('<Return>',equal)
    display1.bind('<Escape>',clear)
    display1.bind('<BackSpace>',backspace)
    display1.focus()

    fromVal = ttk.OptionMenu(toplevel3, in_unit, '', 'Square Decimeter', 'Square Centimeter', 'Square Kilometer', 'Square Meter', 'Square Millimeter', 'Are', 'Hectare', 'Square Miles', 'Square Rod', 'Square Yard', 'Square Foot', 'Square Inch', 'Acre')
    fromVal.grid(row=1, columnspan=4, sticky='nsew')
    fromVal.config(in_unit.set('Select a unit'))

    display2 = Entry(toplevel3, textvariable=out_amount, state='readonly', validatecommand=("%i"),font="Ariel 20", relief=SUNKEN, borderwidth=5,justify=RIGHT)
    display2.grid(row=2,columnspan=4,ipady=10,sticky='nsew')

    toVal = ttk.OptionMenu(toplevel3, out_unit, '', 'Square Decimeter', 'Square Centimeter', 'Square Kilometer', 'Square Meter', 'Square Millimeter', 'Are', 'Hectare', 'Square Miles', 'Square Rod', 'Square Yard', 'Square Foot', 'Square Inch', 'Acre')
    toVal.grid(row=3, columnspan=4, sticky='nsew')
    toVal.config(out_unit.set('Select a unit'))

    seven = Button(toplevel3, text="7", command=seven, font="Ariel 17",relief=GROOVE)
    seven.grid(row=4, column=0, ipadx=7, ipady=10,sticky="nsew")
    seven.bind("<Enter>",enter7)
    seven.bind("<Leave>",leav7)

    eight = Button(toplevel3, text="8", command=eight, font="Ariel 17",relief=GROOVE)
    eight.grid(row=4, column=1, ipadx=7, ipady=10,sticky="nsew")
    eight.bind("<Enter>",enter8)
    eight.bind("<Leave>",leav8)

    nine = Button(toplevel3, text="9", command=nine, font="Ariel 17",relief=GROOVE)
    nine.grid(row=4, column=2, ipadx=7, ipady=10,sticky="nsew")
    nine.bind("<Enter>",enter9)
    nine.bind("<Leave>",leav9)

    backspace = Button(toplevel3, text="⌫", command=backspace, font="Ariel 14", relief=GROOVE)
    backspace.grid(row=4, column=3, ipadx=8, ipady=10,sticky="nsew")
    backspace.bind("<Enter>",enterBS)
    backspace.bind("<Leave>",leavBS)

    four = Button(toplevel3, text="4", command=four, font="Ariel 17",relief=GROOVE)
    four.grid(row=5, column=0, ipadx=7, ipady=10,sticky="nsew")
    four.bind("<Enter>",enter4)
    four.bind("<Leave>",leav4)

    five = Button(toplevel3, text="5", command=five, font="Ariel 17",relief=GROOVE)
    five.grid(row=5, column=1, ipadx=7, ipady=10,sticky="nsew")
    five.bind("<Enter>",enter5)
    five.bind("<Leave>",leav5)

    six = Button(toplevel3, text="6", command=six, font="Ariel 17",relief=GROOVE)
    six.grid(row=5, column=2, ipadx=7, ipady=10,sticky="nsew")
    six.bind("<Enter>",enter6)
    six.bind("<Leave>",leav6)

    clear = Button(toplevel3, text=chr(67), command=clear, font="Ariel 14", relief=GROOVE)
    clear.grid(row=5, column=3, ipadx=8, ipady=10,sticky="nsew")
    clear.bind("<Enter>",enterC)
    clear.bind("<Leave>",leavC)

    one = Button(toplevel3, text="1", command=one, font="Ariel 17", relief=GROOVE)
    one.grid(row=6, column=0, ipadx=7, ipady=10, sticky="nsew")
    one.bind("<Enter>",enter1)
    one.bind("<Leave>",leav1)

    two = Button(toplevel3, text="2", command=two, font="Ariel 17", relief=GROOVE)
    two.grid(row=6, column=1, ipadx=7, ipady=10, sticky="nsew")
    two.bind("<Enter>",enter2)
    two.bind("<Leave>",leav2)

    three = Button(toplevel3, text="3", command=three, font="Ariel 17", relief=GROOVE)
    three.grid(row=6, column=2, ipadx=7, ipady=10, sticky="nsew")
    three.bind("<Enter>",enter3)
    three.bind("<Leave>",leav3)

    dot = Button(toplevel3,text='•',font='Ariel 17',relief=GROOVE,command=dot)
    dot.grid(row=7,column=2, ipadx=7, ipady=10,sticky='nsew')
    dot.bind("<Enter>",enterDt)
    dot.bind("<Leave>",leavDt)

    zeroZ = Button(toplevel3,text='00',font='Ariel 15',relief=GROOVE,command=zeroZ)
    zeroZ.grid(row=7,column=0, ipadx=7, ipady=10,sticky='nsew')
    zeroZ.bind("<Enter>",enter00)
    zeroZ.bind("<Leave>",leav00)

    zero = Button(toplevel3,text='0',font='Ariel 17',relief=GROOVE,command=zero)
    zero.grid(row=7,column=1, ipadx=7, ipady=10,sticky='nsew')
    zero.bind("<Enter>",enter0)
    zero.bind("<Leave>",leav0)
    
    equal = Button(toplevel3,text='=',font='Ariel 17',relief=GROOVE,command=equal)
    equal.grid(row=7,column=3, ipadx=7, ipady=10,sticky='nsew')
    equal.bind("<Enter>",enterEq)
    equal.bind("<Leave>",leavEq)
    
    toplevel3.mainloop()

def weight_converter():
    toplevel6 = Toplevel()
    toplevel6.title("Weight Conversion")
    toplevel6.resizable(width='false', height='false')

    factors = {'tn':1000000, 'qnt':100000, 'kg':1000, 'hg':100, 'dg':10, 'g':1, 'deg':0.1, 'cg':0.01, 'mg':0.001, 'mig':0.000001, 'ng':0.000000001, 'ct':0.2, 'lb':453.592374495299}
    ids = {'Ton':'tn', 'Quintal':'qnt', 'Carat':'ct', 'Pound':'lb', 'Kilogram':'kg', 'Hectagram':'hg', 'Decagram':'dg', 'Gram':'g', 'Decigram':'deg', 'Centigram':'cg', 'Milligram':'mg', 'Microgram':'mig', 'Nanogram':'ng'}

    def enter7(e):
        seven['background'] = '#CFD8DC'
    def leav7(e):
        seven['background'] = 'SystemButtonFace'
    def enter8(e):
        eight['background'] = '#CFD8DC'
    def leav8(e):
        eight['background'] = 'SystemButtonFace'
    def enter9(e):
        nine['background'] = '#CFD8DC'
    def leav9(e):
        nine['background'] = 'SystemButtonFace'
    def enterBS(e):
        backspace['background'] = '#CFD8DC'
    def leavBS(e):
        backspace['background'] = 'SystemButtonFace'
    def enter4(e):
        four['background'] = '#CFD8DC'
    def leav4(e):
        four['background'] = 'SystemButtonFace'
    def enter5(e):
        five['background'] = '#CFD8DC'
    def leav5(e):
        five['background'] = 'SystemButtonFace'
    def enter6(e):
        six['background'] = '#CFD8DC'
    def leav6(e):
        six['background'] = 'SystemButtonFace'
    def enterC(e):
        clear['background'] = '#CFD8DC'
    def leavC(e):
        clear['background'] = 'SystemButtonFace'
    def enter1(e):
        one['background'] = '#CFD8DC'
    def leav1(e):
        one['background'] = 'SystemButtonFace'
    def enter2(e):
        two['background'] = '#CFD8DC'
    def leav2(e):
        two['background'] = 'SystemButtonFace'
    def enter3(e):
        three['background'] = '#CFD8DC'
    def leav3(e):
        three['background'] = 'SystemButtonFace'
    def enterDt(e):
        dot['background'] = '#CFD8DC'
    def leavDt(e):
        dot['background'] = 'SystemButtonFace'
    def enter00(e):
        zeroZ['background'] = '#CFD8DC'
    def leav00(e):
        zeroZ['background'] = 'SystemButtonFace'
    def enter0(e):
        zero['background'] = '#CFD8DC'
    def leav0(e):
        zero['background'] = 'SystemButtonFace'
    def enterEq(e):
        equal['background'] = '#CFD8DC'
    def leavEq(e):
        equal['background'] = 'SystemButtonFace'

    def seven():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'7')
    def eight():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'8')
    def nine():
        if  display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'9')
    def backspace(*args):
        pos = len(display1.get())
        val = str(display1.get())
        display1.delete(0,'end')
        display1.insert(0,val[:pos-1])
    def four():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'4')
    def five():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'5')
    def six():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'6')
    def clear(*args):
        display1.delete(0,'end')
        display2.delete(0,'end')
    def one():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'1')
    def two():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'2')
    def three():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'3')
    def dot():
        if display.get()=="":
            pos = len(display.get())
            display.insert(pos,'0.')
        else:
            pos = len(display.get())
            display.insert(pos,'.')
    def zeroZ():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'00')
    def zero():
        if display1.get() == '0':
            display1.delete(0,'end')
        pos = len(display1.get())
        display1.insert(pos,'0')
    def convert(amount, fromV, toV):
        if fromV != 'g':
            amount = amount*factors[fromV]
            return amount/factors[toV]
        else:
            return amount/factors[toV]
    def equal():
        try:
            amount = float(display1.get())
        except ValueError:
            out_amount.set('Invalid Input')
            return None
        if in_unit.get() == 'Select a unit' or out_unit.get() == 'Select a unit':
            out_amount.set('Please choose a unit')
            return None
        else:
            fromV = ids[in_unit.get()]
            toV = ids[out_unit.get()]
            out_amount.set(convert(amount, fromV, toV))
    def key(*args):
        if display.get() == '0':
            display.delete(0, 'end')

    in_amount = StringVar()
    in_amount.set('')
    out_amount = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    
    display1 = Entry(toplevel6, textvariable=in_amount, validatecommand=('%i'),font="Ariel 20",relief=SUNKEN,borderwidth=5,justify=RIGHT)
    display1.grid(row=0,columnspan=5,ipady=10,sticky='nsew')
    display1.bind("<Key-0>",key)
    display1.bind("<Key-1>",key)
    display1.bind("<Key-2>",key)
    display1.bind("<Key-3>",key)
    display1.bind("<Key-4>",key)
    display1.bind("<Key-5>",key)
    display1.bind("<Key-6>",key)
    display1.bind("<Key-7>",key)
    display1.bind("<Key-8>",key)
    display1.bind("<Key-9>",key)
    display1.bind('Key-.',key)
    display1.bind('<Return>',equal)
    display1.bind('<Escape>',clear)
    display1.bind('<BackSpace>',backspace)
    display1.focus()

    fromVal = ttk.OptionMenu(toplevel6, in_unit, '', 'Kilogram', 'Hectagram', 'Decagram', 'Gram', 'Decigram', 'Centigram', 'Milligram', 'Microgram', 'Nanogram', 'Carat', 'Pound', 'Ton', 'Quintal')
    fromVal.grid(row=1, columnspan=4, sticky='nsew')
    fromVal.config(in_unit.set('Select a unit'))

    display2 = Entry(toplevel6, textvariable=out_amount, state='readonly', validatecommand=('%i'), font='Ariel 20', relief=SUNKEN, borderwidth=5, justify=RIGHT)
    display2.grid(row=2, columnspan=4, ipady=10, sticky='nsew')

    toVal = ttk.OptionMenu(toplevel6, out_unit, '', 'Kilogram', 'Hectagram', 'Decagram', 'Gram', 'Decigram', 'Centigram', 'Milligram', 'Microgram', 'Nanogram', 'Carat', 'Pound', 'Ton', 'Quintal')
    toVal.grid(row=3, columnspan=4, sticky='nsew')
    toVal.config(out_unit.set('Select a unit'))

    seven = Button(toplevel6, text="7", command=seven, font="Ariel 17",relief=GROOVE)
    seven.grid(row=4, column=0, ipadx=7, ipady=10,sticky="nsew")
    seven.bind("<Enter>",enter7)
    seven.bind("<Leave>",leav7)

    eight = Button(toplevel6, text="8", command=eight, font="Ariel 17",relief=GROOVE)
    eight.grid(row=4, column=1, ipadx=7, ipady=10,sticky="nsew")
    eight.bind("<Enter>",enter8)
    eight.bind("<Leave>",leav8)

    nine = Button(toplevel6, text="9", command=nine, font="Ariel 17",relief=GROOVE)
    nine.grid(row=4, column=2, ipadx=7, ipady=10,sticky="nsew")
    nine.bind("<Enter>",enter9)
    nine.bind("<Leave>",leav9)

    backspace = Button(toplevel6, text="⌫", command=backspace, font="Ariel 14", relief=GROOVE)
    backspace.grid(row=4, column=3, ipadx=8, ipady=10,sticky="nsew")
    backspace.bind("<Enter>",enterBS)
    backspace.bind("<Leave>",leavBS)

    four = Button(toplevel6, text="4", command=four, font="Ariel 17",relief=GROOVE)
    four.grid(row=5, column=0, ipadx=7, ipady=10,sticky="nsew")
    four.bind("<Enter>",enter4)
    four.bind("<Leave>",leav4)

    five = Button(toplevel6, text="5", command=five, font="Ariel 17",relief=GROOVE)
    five.grid(row=5, column=1, ipadx=7, ipady=10,sticky="nsew")
    five.bind("<Enter>",enter5)
    five.bind("<Leave>",leav5)

    six = Button(toplevel6, text="6", command=six, font="Ariel 17",relief=GROOVE)
    six.grid(row=5, column=2, ipadx=7, ipady=10,sticky="nsew")
    six.bind("<Enter>",enter6)
    six.bind("<Leave>",leav6)

    clear = Button(toplevel6, text=chr(67), command=clear, font="Ariel 14", relief=GROOVE)
    clear.grid(row=5, column=3, ipadx=8, ipady=10,sticky="nsew")
    clear.bind("<Enter>",enterC)
    clear.bind("<Leave>",leavC)

    one = Button(toplevel6, text="1", command=one, font="Ariel 17", relief=GROOVE)
    one.grid(row=6, column=0, ipadx=7, ipady=10, sticky="nsew")
    one.bind("<Enter>",enter1)
    one.bind("<Leave>",leav1)

    two = Button(toplevel6, text="2", command=two, font="Ariel 17", relief=GROOVE)
    two.grid(row=6, column=1, ipadx=7, ipady=10, sticky="nsew")
    two.bind("<Enter>",enter2)
    two.bind("<Leave>",leav2)

    three = Button(toplevel6, text="3", command=three, font="Ariel 17", relief=GROOVE)
    three.grid(row=6, column=2, ipadx=7, ipady=10, sticky="nsew")
    three.bind("<Enter>",enter3)
    three.bind("<Leave>",leav3)

    dot = Button(toplevel6,text='•',font='Ariel 17',relief=GROOVE,command=dot)
    dot.grid(row=7,column=2, ipadx=7, ipady=10,sticky='nsew')
    dot.bind("<Enter>",enterDt)
    dot.bind("<Leave>",leavDt)

    zeroZ = Button(toplevel6,text='00',font='Ariel 15',relief=GROOVE,command=zeroZ)
    zeroZ.grid(row=7,column=0, ipadx=7, ipady=10,sticky='nsew')
    zeroZ.bind("<Enter>",enter00)
    zeroZ.bind("<Leave>",leav00)

    zero = Button(toplevel6,text='0',font='Ariel 17',relief=GROOVE,command=zero)
    zero.grid(row=7,column=1, ipadx=7, ipady=10,sticky='nsew')
    zero.bind("<Enter>",enter0)
    zero.bind("<Leave>",leav0)
    
    equal = Button(toplevel6,text='=',font='Ariel 17',relief=GROOVE,command=equal)
    equal.grid(row=7,column=3, ipadx=7, ipady=10,sticky='nsew')
    equal.bind("<Enter>",enterEq)
    equal.bind("<Leave>",leavEq)
    
    toplevel6.mainloop()
    
"""
def  temp_converter():
    toplevel7 = Toplevel()
    
    toplevel7.title("Temperature Conversion")
    toplevel7.mainloop()

def  volume_converter():
    toplevel4 = Toplevel()
    toplevel4.geometry("400x550")
    toplevel4.title("Volume Conversion")
    toplevel4.mainloop()

def  speed_converter():
    toplevel5 = Toplevel()
    toplevel5.geometry("400x550")
    toplevel5.title("Speed Conversion")
    toplevel5.mainloop()

def  power_converter():
    toplevel8 = Toplevel()
    toplevel8.geometry("400x550")
    toplevel8.title("Power Conversion")
    toplevel8.mainloop()

def  pressure_converter():
    toplevel9 = Toplevel()
    toplevel9.geometry("400x550")
    toplevel9.title("Pressure Conversion")
    toplevel9.mainloop()
"""


window = Tk()
window.title("Calculator")
window.geometry("315x460")
window.resizable(width=False,height=False)
window.minsize(315,460)

window.columnconfigure(0, pad=1, weight=1)
window.columnconfigure(1, pad=1, weight=1)
window.columnconfigure(2, pad=1, weight=1)
window.columnconfigure(3, pad=1, weight=1)
window.rowconfigure(0, pad=1, weight=0)
window.rowconfigure(1, pad=1, weight=1)
window.rowconfigure(2, pad=1, weight=1)
window.rowconfigure(3, pad=1, weight=1)
window.rowconfigure(4, pad=1, weight=1)
window.rowconfigure(5, pad=1, weight=1)

menubar = Menu(window)

option = Menu(menubar,tearoff=0)
option.add_command(label="Scientific",command=scientific_tab)
option.add_separator()
option.add_command(label="Exit",command=exiter)
menubar.add_cascade(label="Option",menu=option)

converter = Menu(menubar, tearoff=0)
converter.add_command(label="Length",command=length_converter)
converter.add_command(label="Area",command=area_converter)
converter.add_command(label="Weight",command=weight_converter)
"""
converter.add_command(label="Volume",command=volume_converter)
converter.add_command(label="Speed",command=speed_converter)
converter.add_command(label="Temperature",command=temp_converter)
converter.add_command(label="Power",command=power_converter)
converter.add_command(label="Pressure",command=pressure_converter)
"""
menubar.add_cascade(label="Converter",menu=converter)

window.config(menu=menubar)

def one():
    if display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'1')
def two():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'2')
def three():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'3')
def four():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'4')
def five():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'5')
def six():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'6')
def seven():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'7')
def eight():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'8')
def nine():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'9')
def zero():
    if  display.get() == '0':
        display.delete(0,'end')
    pos = len(display.get())
    display.insert(pos,'0')
def add():
    pos = len(display.get())
    display.insert(pos,'+')
def subtract():
    pos = len(display.get())
    display.insert(pos,'-')
def multiply():
    pos = len(display.get())
    display.insert(pos,'*')
def divide():
    pos = len(display.get())
    display.insert(pos,'/')
def percent():
    pos = len(display.get())
    display.insert(pos,'%')
def dot():
    if display.get()=="":
        pos = len(display.get())
        display.insert(pos,'0.')
    else:
        pos = len(display.get())
        display.insert(pos,'.')
def clear(*args):
    display.delete(0,'end')
def backspace(*args):
    pos = len(display.get())
    val = str(display.get())
    display.delete(0,'end')
    display.insert(0,val[:pos-1])
def equal(*args):
    try:
        exp = display.get()
        exp = eval(exp)
        display.delete(0,'end')
        display.insert(0,exp)
    except:
        display.delete(0,'end')
        display.insert(0,' ')        
def key(*args):
    if display.get() == '0':
        display.delete(0,'end')

def enter1(e):
    clear['background'] = '#CFD8DC'
def enter2(e):
    percent['background'] = '#CFD8DC'
def enter3(e):
    backspace['background'] = '#CFD8DC'
def enter4(e):
    divide['background'] = '#CFD8DC'
def enter5(e):
    seven['background'] = '#CFD8DC'
def enter6(e):
    eight['background'] = '#CFD8DC'
def enter7(e):
    nine['background'] = '#CFD8DC'
def enter8(e):
    multiply['background'] = '#CFD8DC'
def enter9(e):
    four['background'] = '#CFD8DC'
def enter10(e):
    five['background'] = '#CFD8DC'
def enter11(e):
    six['background'] = '#CFD8DC'
def enter12(e):
    subtract['background'] = '#CFD8DC'
def enter13(e):
    one['background'] = '#CFD8DC'
def enter14(e):
    two['background'] = '#CFD8DC'
def enter15(e):
    three['background'] = '#CFD8DC'
def enter16(e):
    add['background'] = '#CFD8DC'
def enter17(e):
    dot['background'] = '#CFD8DC'
def enter18(e):
    zero['background'] = '#CFD8DC'
def enter19(e):
    equals['background'] = '#CFD8DC'

    
def leav1(e):
    clear['background'] = 'SystemButtonFace'
def leav2(e):
    percent['background'] = 'SystemButtonFace'
def leav3(e):
    backspace['background'] = 'SystemButtonFace'
def leav4(e):
    divide['background'] = 'SystemButtonFace'
def leav5(e):
    seven['background'] = 'SystemButtonFace'
def leav6(e):
    eight['background'] = 'SystemButtonFace'
def leav7(e):
    nine['background'] = 'SystemButtonFace'
def leav8(e):
    multiply['background'] = 'SystemButtonFace'
def leav9(e):
    four['background'] = 'SystemButtonFace'
def leav10(e):
    five['background'] = 'SystemButtonFace'
def leav11(e):
    six['background'] = 'SystemButtonFace'
def leav12(e):
    subtract['background'] = 'SystemButtonFace'
def leav13(e):
    one['background'] = 'SystemButtonFace'
def leav14(e):
    two['background'] = 'SystemButtonFace'
def leav15(e):
    three['background'] = 'SystemButtonFace'
def leav16(e):
    add['background'] = 'SystemButtonFace'
def leav17(e):
    dot['background'] = 'SystemButtonFace'
def leav18(e):
    zero['background'] = 'SystemButtonFace'
def leav19(e):
    equals['background'] = 'SystemButtonFace'
    

display = Entry(window,validatecommand=('%i', '%P','%v', '%V', '%W'),state="normal",font="Ariel 33",relief=SUNKEN,borderwidth=8,justify=RIGHT)
display.grid(row=0, columnspan=4, ipady=10, sticky="nsew")
display.bind('<Return>',equal)
display.bind('<Escape>',clear)
display.bind('<BackSpace>',backspace)
display.bind('<Key-0>',key)
display.bind('<Key-1>',key)
display.bind('<Key-2>',key)
display.bind('<Key-4>',key)
display.bind('<Key-5>',key)
display.bind('<Key-6>',key)
display.bind('<Key-8>',key)
display.bind('<Key-9>',key)
display.bind('<Key-.>',key)
display.focus()


clear = Button(window, text=chr(67), command=clear, font="Ariel 17", relief=GROOVE)
clear.grid(row=1, column=0, ipadx=19, ipady=14,sticky="nsew")
clear.bind("<Enter>",enter1)
clear.bind("<Leave>",leav1)

percent = Button(window, text="%", command=percent, font="Ariel 17",relief=GROOVE)
percent.grid(row=1, column=1, ipadx=19, ipady=14,sticky="nsew")
percent.bind("<Enter>",enter2)
percent.bind("<Leave>",leav2)

backspace = Button(window, text="⌫", command=backspace, font="Ariel 17", relief=GROOVE)
backspace.grid(row=1, column=2, ipadx=19, ipady=14,sticky="nsew")
backspace.bind("<Enter>",enter3)
backspace.bind("<Leave>",leav3)

divide = Button(window, text="÷", command=divide, font="Ariel 17",relief=GROOVE)
divide.grid(row=1, column=3, ipadx=19, ipady=14,sticky="nsew")
divide.bind("<Enter>",enter4)
divide.bind("<Leave>",leav4)

seven = Button(window, text="7", command=seven, font="Ariel 17",relief=GROOVE)
seven.grid(row=2, column=0, ipadx=19, ipady=14,sticky="nsew")
seven.bind("<Enter>",enter5)
seven.bind("<Leave>",leav5)

eight = Button(window, text="8", command=eight, font="Ariel 17",relief=GROOVE)
eight.grid(row=2, column=1, ipadx=19, ipady=14,sticky="nsew")
eight.bind("<Enter>",enter6)
eight.bind("<Leave>",leav6)

nine = Button(window, text="9", command=nine, font="Ariel 17",relief=GROOVE)
nine.grid(row=2, column=2, ipadx=19, ipady=14,sticky="nsew")
nine.bind("<Enter>",enter7)
nine.bind("<Leave>",leav7)

multiply = Button(window, text="×", command=multiply, font="Ariel 17",relief=GROOVE)
multiply.grid(row=2, column=3, ipadx=19, ipady=14,sticky="nsew")
multiply.bind("<Enter>",enter8)
multiply.bind("<Leave>",leav8)

four = Button(window, text="4", command=four, font="Ariel 17",relief=GROOVE)
four.grid(row=3, column=0, ipadx=19, ipady=14,sticky="nsew")
four.bind("<Enter>",enter9)
four.bind("<Leave>",leav9)

five = Button(window, text="5", command=five, font="Ariel 17",relief=GROOVE)
five.grid(row=3, column=1, ipadx=19, ipady=14,sticky="nsew")
five.bind("<Enter>",enter10)
five.bind("<Leave>",leav10)

six = Button(window, text="6", command=six, font="Ariel 17",relief=GROOVE)
six.grid(row=3, column=2, ipadx=19, ipady=14,sticky="nsew")
six.bind("<Enter>",enter11)
six.bind("<Leave>",leav11)

subtract = Button(window, text="–", command=subtract, font="Ariel 17",relief=GROOVE)
subtract.grid(row=3, column=3, ipadx=19, ipady=14,sticky="nsew")
subtract.bind("<Enter>",enter12)
subtract.bind("<Leave>",leav12)

one = Button(window, text="1", command=one, font="Ariel 17",relief=GROOVE)
one.grid(row=4, column=0, ipadx=19, ipady=14,sticky="nsew")
one.bind("<Enter>",enter13)
one.bind("<Leave>",leav13)

two = Button(window, text="2", command=two, font="Ariel 17",relief=GROOVE)
two.grid(row=4, column=1, ipadx=19, ipady=14,sticky="nsew")
two.bind("<Enter>",enter14)
two.bind("<Leave>",leav14)

three = Button(window, text="3", command=three, font="Ariel 17",relief=GROOVE)
three.grid(row=4, column=2, ipadx=19, ipady=14,sticky="nsew")
three.bind("<Enter>",enter15)
three.bind("<Leave>",leav15)

add = Button(window, text="+", command=add, font="Ariel 17",relief=GROOVE)
add.grid(row=4, column=3, ipadx=19, ipady=14,sticky="nsew")
add.bind("<Enter>",enter16)
add.bind("<Leave>",leav16)

dot = Button(window, text="•", command=dot, font="Ariel 17",relief=GROOVE)
dot.grid(row=5, column=0, ipadx=19, ipady=14,sticky="nsew")
dot.bind("<Enter>",enter17)
dot.bind("<Leave>",leav17)

zero = Button(window, text="0",command=zero, font="Ariel 17",relief=GROOVE)
zero.grid(row=5, column=1, ipadx=19, ipady=14,sticky="nsew")
zero.bind("<Enter>",enter18)
zero.bind("<Leave>",leav18)

equals = Button(window, text="=", command=equal, font="Ariel 17", relief=GROOVE)
equals.grid(columnspan=6, row=5, column=2, ipadx=66, ipady=15,sticky="nsew")
equals.bind("<Enter>",enter19)
equals.bind("<Leave>",leav19)

window.mainloop()
