# OK...this time I will give it a GUI from tkinter

import platform
import secrets
import random
import tkinter as tk
import bleach


# if using python version 3.6 or later, use secrets module for randomizations
# otherwise use random module...get python version

z = platform.python_version()

# list of basic special chars to choose from, modify if needed
clist = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# extended list of special chars to choose from, modify if needed
eclist = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
          '<', '>', '/', ':', '{', '}', '|', '_', '+', '-',
          '=', ',', '.', '~', '`']


def strPart(numChar, name, color):

    # pull first numChar characters from name string
    # adding filler '#' if needed
    a = list(name)
    while len(a) < numChar:
        a.append('#')
    if len(a) > numChar:
        a = a[:numChar]

    # pull first numChar characters from color string
    # adding filler '#' if needed
    b = list(color)
    while len(b) < numChar:
        b.append("#")
    if len(b) > numChar:
        b = b[:numChar]

    # make the first char of color string capital
    b[0] = b[0].upper()

    return a, b


def digPart(num1, num2):

    # include this part if not done so already...
    # import platform, secrets, random
    # z = platform.python_version()

    if z > '3.5':
        # get random int from num1 to num2
        x = str(secrets.choice(range(num1, num2)))
    else:
        # get random int from num1 to num2
        x = str(random.randrange(num1, num2))

    return x


def CharPass(name, color, numChar, num1, num2):
    # code will take 2 strings from user via GUI...
    # their last name and least favorite color
    # will derive a chosen length password from first 'numChar' letters of
    # last name, first 'numChar' letters of least favorite color
    # ('#' for filler if needed), randomly chosen number(s) between
    # num1 and num2 and 2 or 5 randomly chosen special characters
    # from clist/eclist

    # split passowrd
    pass1 = ''
    pass2 = ''

    # get string parts of password
    pass1, pass2 = strPart(numChar, name, color)

    # get int part of passowrd
    if num1 > 10000:
        rnum1 = digPart(num1, num2)
        rnum2 = digPart(num1, num2)

        # add int parts to passowrd halves
        pass2.append(rnum2)
        pass1.append(rnum1)

        # choose special chars and add to password parts
        x = random.choice(eclist)
        x1 = random.choice(eclist)
        y = random.choice(eclist)
        y1 = random.choice(eclist)
        z1 = random.choice(eclist)

        pass1.append(y)
        pass1.append(y1)
        pass2.append(x)
        pass2.append(x1)
        pass2.append(z1)

    else:
        rnum = digPart(num1, num2)

        # add int part to 2nd half of password
        pass2.append(rnum)

        # choose special chars and add to password parts
        x = random.choice(clist)
        y = random.choice(clist)
        pass1.append(y)
        pass2.append(x)

    return pass1, pass2


def eightCharPass(name, color):

    numChar = 2
    num1 = 10
    num2 = 100
    pass1, pass2 = CharPass(name, color, numChar, num1, num2)

    # join password halves and convert to string
    x = pass1 + pass2
    y = ''
    y = y.join(x)

    # output to GUI
    output_field.insert(0, y)


def twelveCharPass(name, color):

    numChar = 4
    num1 = 10
    num2 = 100
    pass1, pass2 = CharPass(name, color, numChar, num1, num2)

    # join password halves and convert to string
    x = pass1 + pass2
    y = ''
    y = y.join(x)

    # output to GUI
    output_field.insert(0, y)


def fourteenCharPass(name, color):

    numChar = 4
    num1 = 1000
    num2 = 10000
    pass1, pass2 = CharPass(name, color, numChar, num1, num2)

    # join password halves and convert to string
    x = pass1 + pass2
    y = ''
    y = y.join(x)

    # output to GUI
    output_field.insert(0, y)


def twentyfiveCharPass(name, color):

    numChar = 5
    num1 = 10001
    num2 = 100000
    pass1, pass2 = CharPass(name, color, numChar, num1, num2)

    # join password halves and convert to string
    x = pass1 + pass2
    y = ''
    y = y.join(x)

    # output to GUI
    output_field.insert(0, y)


def selection():

    # clear output
    output_field.delete(0, 'end')

    # get length choice from radio buttons
    choice = var.get()

    # get name and color, sanitize user input
    name = bleach.clean(name_field.get()[0:30])
    color = bleach.clean(color_field.get()[0:20])

    if choice == 1:
        eightCharPass(name, color)
    elif choice == 2:
        twelveCharPass(name, color)
    elif choice == 3:
        fourteenCharPass(name, color)
    elif choice == 4:
        twentyfiveCharPass(name, color)


# Driver code
if __name__ == '__main__':

    # create window in tkinter
    window = tk.Tk()
    window.title('Generate a strong password!!!')

    # create frames and labels within for GUI objects

    # header
    frame1 = tk.Frame(master=window, width=550, height=80, borderwidth=1,
                      bg='blue')
    frame1.pack()

    label1 = tk.Label(master=frame1, text='Generate a Strong Password...',
                      bg='blue', fg='white', font=('New Times Roman', 20))
    label1.place(x=25, y=20)

    # last name field
    frame2 = tk.Frame(master=window, width=550, height=80, borderwidth=1,
                      bg='alice blue')
    frame2.pack()

    label2 = tk.Label(master=frame2, text='Please enter your last name',
                      font=('New Times Roman', 13), fg='gray', bg='alice blue')
    label2.place(x=25, y=10)

    name_field = tk.Entry(master=frame2, font=('New Times Roman', 15),
                          width=45, bd=0)
    name_field.place(x=25, y=40)

    # least favorite color field
    frame3 = tk.Frame(master=window, width=550, height=70,
                      borderwidth=1, bg='alice blue')
    frame3.pack()

    label3 = tk.Label(master=frame3,
                      text='Please enter your least favorite color',
                      font=('New Times Roman', 13), fg='gray', bg='alice blue')
    label3.place(x=25, y=10)

    color_field = tk.Entry(master=frame3, font=('New Times Roman', 15),
                           width=45, bd=0)
    color_field.place(x=25, y=40)

    # radio buttons
    frame4 = tk.Frame(master=window, width=550, height=90,
                      borderwidth=1, bg='alice blue')
    frame4.pack()

    label4 = tk.Label(master=frame4, text='Choose length of passowrd',
                      font=('New Times Roman', 13), fg='gray', bg='alice blue')
    label4.place(x=25, y=10)

    var = tk.IntVar()

    rbox1 = tk.Radiobutton(master=frame4, text='8', variable=var, value=1,
                           height=2, width=10, bg='alice blue',
                           activebackground='alice blue')
    rbox1.place(x=25, y=45)

    rbox2 = tk.Radiobutton(master=frame4, text='12', variable=var, value=2,
                           height=2, width=10, bg='alice blue',
                           activebackground='alice blue')
    rbox2.place(x=135, y=45)

    rbox3 = tk.Radiobutton(master=frame4, text='14', variable=var, value=3,
                           height=2, width=10, bg='alice blue',
                           activebackground='alice blue')
    rbox3.place(x=245, y=45)

    rbox4 = tk.Radiobutton(master=frame4, text='25', variable=var, value=4,
                           height=2, width=10, bg='alice blue',
                           activebackground='alice blue')
    rbox4.place(x=355, y=45)

    # generate button
    frame5 = tk.Frame(master=window, width=550, height=120, borderwidth=1,
                      bg='alice blue')
    frame5.pack()

    button1 = tk.Button(master=frame5, text='Generate Password', bg='blue',
                        fg='white', font=('New Times Roman', 20), bd=2,
                        activebackground='alice blue', width=32, height=2,
                        command=selection)
    button1.place(x=14, y=18)

    # output
    frame6 = tk.Frame(master=window, width=550, height=150, borderwidth=1,
                      bg='alice blue')
    frame6.pack()

    label6 = tk.Label(master=frame6, text='Password Generated',
                      font=('New Times Roman', 13), fg='gray', bg='alice blue')
    label6.place(x=25, y=1)

    output_field = tk.Entry(master=frame6, font=('New Times Roman', 15),
                            width=45, bd=0)
    output_field.place(x=25, y=30)

    window.mainloop()
