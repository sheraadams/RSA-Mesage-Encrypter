import statistics
from tkinter import*
import math
import tkinter as tk

from PIL import Image, ImageTk
import time
#colors
dpurple = "#C55FFC"
lpurple= "#EFDCF9"
dark= "#323E42"
purple= "#7954A1"
back = "#278ED5"
contrast = "#AFFF26"

# window dimesions and color
window = Tk()
window.geometry("720x1000")  # was 720 x 420
window.configure(bg=purple)
window.title("RSA Encryption and Decryption Generator")

def start():
    if __name__== '__main__':
        option = "menu"

def toSpace():
    # get input to convert comma to space
    toSpaceMessage = uinput7.get("1.0", "end-1c").lower()

    for i in range(len(toSpaceMessage)):
        toSpaceMessage= toSpaceMessage.replace(",", ' ')

    print(toSpaceMessage)
    chatb4.delete("1.0", END)
    chatb4.insert(END, toSpaceMessage)

# function to encode
def encrypt():

    # get input from textbox for value to assign to space
    space = uinput4.get("1.0", "end-1c").lower()
    # get input from textbox for value to assign to period
    period = uinput6.get("1.0", "end-1c").lower()


    # convert user input string to a digit
    if space.isdigit():
        int(space)
    if period.isdigit():
        int(period)

    notifyInvalid = ""
    # check that variable are unique
    if space == period:
        notifyInvalid = "Invalid input please assign space and period to unique values."

    chatb3.delete("1.0", END)
    chatb3.insert(END, notifyInvalid)

    # define variables
    p  = 3
    q = 11
    e = p
    p = int(p)
    q = int(q)
    e = int(e)
    n = p * q
    d = 10-p

    # get input from textbox and convert to list, print to console
    elmessage = uinput.get("1.0", "end-1c").lower()
    messagelist1 = list(elmessage)
    print(messagelist1)

    # convert alpha to numeric a = 1, b = 2 etc
    for i in range(len(messagelist1)):
        if messagelist1[i] == 'a':
            messagelist1[i] = '1'
        if messagelist1[i] == 'b':
            messagelist1[i] = '2'
        if messagelist1[i] == 'c':
            messagelist1[i] = '3'
        if messagelist1[i] == 'd':
            messagelist1[i] = '4'
        if messagelist1[i] == 'e':
            messagelist1[i] = '5'
        if messagelist1[i] == 'f':
            messagelist1[i] = '6'
        if messagelist1[i] == 'g':
            messagelist1[i] = '7'
        if messagelist1[i] == 'h':
            messagelist1[i] = '8'
        if messagelist1[i] == 'i':
            messagelist1[i] = '9'
        if messagelist1[i] == 'j':
            messagelist1[i] = '10'
        if messagelist1[i] == 'k':
            messagelist1[i] = '11'
        if messagelist1[i] == 'l':
            messagelist1[i] = '12'
        if messagelist1[i] == 'm':
            messagelist1[i] = '13'
        if messagelist1[i] == 'n':
            messagelist1[i] = '14'
        if messagelist1[i] == 'o':
            messagelist1[i] = '15'
        if messagelist1[i] == 'p':
            messagelist1[i] = '16'
        if messagelist1[i] == 'q':
            messagelist1[i] = '17'
        if messagelist1[i] == 'r':
            messagelist1[i] = '18'
        if messagelist1[i] == 's':
            messagelist1[i] = '19'
        if messagelist1[i] == 't':
            messagelist1[i] = '20'
        if messagelist1[i] == 'u':
            messagelist1[i] = '21'
        if messagelist1[i] == 'v':
            messagelist1[i] = '22'
        if messagelist1[i] == 'w':
            messagelist1[i] = '23'
        if messagelist1[i] == 'x':
            messagelist1[i] = '24'
        if messagelist1[i] == 'y':
            messagelist1[i] = '25'
        if messagelist1[i] == 'z':
            messagelist1[i] = '26'
        if messagelist1[i] == " ":
            messagelist1[i] = space
        if messagelist1[i] == '.':
            messagelist1[i] = period

    # print to console convert to string, strip commas and format appropriately
    print(messagelist1)
    print("messagelist1 string")
    tempmessagestr = str(messagelist1)
    print(tempmessagestr)
    print("temp message string")

    for i in range(len(tempmessagestr)):
        tempmessagestr= tempmessagestr.replace("'", ' ')
        tempmessagestr = tempmessagestr.replace(' ','')
        tempmessagestr = tempmessagestr.replace(' ', '')
        tempmessagestr = tempmessagestr.replace('[', '')
        tempmessagestr = tempmessagestr.replace(']', '')
    encrypted = list(tempmessagestr.split(","))
    print(encrypted)
    print("encrypted string")

    # evaluate string as numeric and make a list, then use RSA algorithm calculation on each element
    encrypt1 = [eval(i) for i in encrypted]
    for i in range(len(encrypt1)):
        encrypt1[i] = (encrypt1[i] ** e) % n

    # convert numeric to string and format single digits to be preceded by 0s
    en = [str(x) for x in encrypt1]


    en = str(encrypt1)
    print(en)

    # format and send encrypted and formatted message to the gui
    for i in range(len(en)):
        en = en.replace(" ", '')
        en = en.replace("'", "")
        en = en.replace(" ", "")
        en = en.replace("[", "")
        en = en.replace("]", "")

    entry4.delete("1.0", END)
    entry4.insert(END, en)

# function to decrypt
def decode():

    # get input from textbox for value to assign to space
    space = uinput4.get("1.0", "end-1c").lower()
    # get input from textbox for value to assign to period
    period = uinput6.get("1.0", "end-1c").lower()

    if space.isdigit():
        int(space)
    if period.isdigit():
        int(period)

    notifyInvalid = ""
    # check that values are unique
    if space == period:
        notifyInvalid = "Invalid input please assign space and period to unique values."

    chatb3.delete("1.0", END)
    chatb3.insert(END, notifyInvalid)


    # get input from the gui text entry box
    word2 = uinput3.get("1.0", "end-1c").lower()
    decry = word2.lower()

    # initialize variables
    p  = 3
    q = 11
    e = p
    p = int(p)
    q= int(q)
    e = int(e)
    n = p * q
    d = 10-p

    # remove leading zeros and evaluate as digits
    for i in range(len(decry)):
        decry = decry.replace('01', '1')
        decry = decry.replace('02', '2')
        decry = decry.replace('03', '3')
        decry = decry.replace('04', '4')
        decry = decry.replace('05', '5')
        decry = decry.replace('06', '6')
        decry = decry.replace('07', '7')
        decry = decry.replace('08', '8')
        decry = decry.replace('09', '9')
    decmessage = []

    decry2 = [int(item) for item in decry.split(',') if item.isdigit()]

    # iterate through list applying rsa decryption algorithm and append decrypted elements to new list
    for i in decry2:
        i = (i ** d) % n
        print(i, end=', ')
        decmessage.append(i)
    # iterate through list and assign numeric to alpha 1=a, b =2 etc
    for i in range(len(decmessage)):
        if decmessage[i] == 1:
            decmessage[i] = 'a'
        if decmessage[i] == 2:
            decmessage[i] = 'b'
        if decmessage[i] == 3:
            decmessage[i] = 'c'
        if decmessage[i] == 4:
            decmessage[i] = 'd'
        if decmessage[i] == 5:
            decmessage[i] = 'e'
        if decmessage[i] == 6:
            decmessage[i] = 'f'
        if decmessage[i] == 7:
            decmessage[i] = 'g'
        if decmessage[i] == 8:
            decmessage[i] = 'h'
        if decmessage[i] == 9:
            decmessage[i] = 'i'
        if decmessage[i] == 10:
            decmessage[i] = 'j'
        if decmessage[i] == 11:
            decmessage[i] = 'k'
        if decmessage[i] == 12:
            decmessage[i] = 'l'
        if decmessage[i] == 13:
            decmessage[i] = 'm'
        if decmessage[i] == 14:
            decmessage[i] = 'n'
        if decmessage[i] == 15:
            decmessage[i] = 'o'
        if decmessage[i] == 16:
            decmessage[i] = 'p'
        if decmessage[i] == 17:
            decmessage[i] = 'q'
        if decmessage[i] == 18:
            decmessage[i] = 'r'
        if decmessage[i] == 19:
            decmessage[i] = 's'
        if decmessage[i] == 20:
            decmessage[i] = 't'
        if decmessage[i] == 21:
            decmessage[i] = 'u'
        if decmessage[i] == 22:
            decmessage[i] = 'v'
        if decmessage[i] == 23:
            decmessage[i] = 'w'
        if decmessage[i] == 24:
            decmessage[i] = 'x'
        if decmessage[i] == 25:
            decmessage[i] = 'y'
        if decmessage[i] == 26:
            decmessage[i] = 'z'
        if decmessage[i] == int(space):
            decmessage[i] = " "
        if decmessage[i] == int(period):
            decmessage[i] = "."
    j = 1
    decstr = str(decmessage)


    # strip unwanted characters
    while j == 1:
        for character in decstr:
            decstr = decstr.strip(',')
            decstr = decstr.strip('""')
        j -= 1

    for i in range(len(decstr)):
        decstr = decstr.replace(" ", '')
        decstr = decstr.replace(',', '*')
        decstr = decstr.replace("'", "")
        decstr = decstr.replace(" ", "")

    for i in range(len(decstr)):
        decstr = decstr.replace('{}', ' ')
        decstr = decstr.replace('**', ' ')
        decstr = decstr.replace('*', '')
        decstr = decstr.replace('[', '')
        decstr = decstr.replace(']', '')

    # send formatted decrypted plain english message to giu
    chatb3.delete("1.0", END)
    chatb3.insert(END, decstr)


# gui pack layout
path = '2.png'
img= ImageTk.PhotoImage(Image.open(path))

# pack header image panel
panel = tk.Label(window, fg= purple, image = img, borderwidth=0, highlightthickness=0)
panel.image = img
panel.pack()

# window to get input for number to assign to space
label4 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Assign space to a unique number (27-32)", pady=8)
label4.pack()
# value
uinput_value4 = StringVar(window)
# entry
uinput4 = Text(window, height=1, width=65, bg=lpurple)
uinput4.pack()


# window to get input for number to assign to period
# label
label6 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Assign period (27-32)", pady=8)
label6.pack()
# entry value
uinput_value6 = StringVar(window)
#entry
uinput6 = Text(window, height=1, width=65, bg=lpurple)
uinput6.pack()

# label enter message to encrypt
label3 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Encrypt: Enter a message to encrypt", pady=8)
label3.pack()
# value
uinput_value = StringVar(window)
# input window
uinput = Text(window, height=5, width=65, bg=lpurple)
uinput.pack()


# text window for output message encrypted
label4 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Encrypted message:", pady=5)
label4.pack()
# output entry box
entry4 = Text(window, height=5, width=65, bg=lpurple)
entry4.pack()
# labels
label2 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="", pady=0)
label2.pack()
button02 = Button(window, bg= dpurple, fg=lpurple, height=1, width=10, text="Encrypt",command=lambda: encrypt())
button02.pack()


# window for text entry for message to decrypt
# label
label2 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Decrypt: Enter a message to decrypt", pady=8)
label2.pack()
#value
uinput_value3 = StringVar(window)
# entry box
uinput3 = Text(window, height=5, width=65, bg=lpurple)
uinput3.pack()
# label
lab5 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Decrypted message:", pady=5)
lab5.pack()
# output entry box
chatb3 = Text(window, height=5,width=65, bg=lpurple)
chatb3.pack()



#Label
lab6 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="", pady=0)
lab6.pack()
# Decrypt button
button3 = Button(window, bg= dpurple, fg=lpurple, height=1, width=10, text="Decrypt",command=lambda: decode())
button3.pack()


# window for output comma to space
# label
label7 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="To convert a comma separated string enter it below:", pady=8)
label7.pack()
uinput_value7 = StringVar(window)
uinput7 = Text(window, height=2.5, width=65, bg=lpurple)
uinput7.pack()
# label
lab5 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Comma converted to space:", pady=5)
lab5.pack()
# window for output comma to space message
chatb4 = Text(window, height=2.5,width=65, bg=lpurple)
chatb4.pack()
#label for spacing
lab9 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="", pady=0)
lab9.pack()
# Comma to space button
button4 = Button(window, bg= dpurple, fg=lpurple, height=1, width=10, text="to Space",command=lambda: toSpace())
button4.pack()


# label
label1 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Using Key: p=3, q=11, e=3. Encryption: x^e %n Decryption: x^(10-e) %n", pady=5)
label1.pack()


window.mainloop()
start()
