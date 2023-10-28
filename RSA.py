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
window = Tk()
window.geometry("620x620")  # was 720 x 420
window.configure(bg=purple)
window.title("RSA Encryption and Decryption Generator")

def start():
    if __name__== '__main__':
        option = "menu"

# function to encode
def encrypt():
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
    messageInput = uinput.get("1.0", "end-1c").lower()
    messagelist = list(messageInput)
    print(messagelist)

    # convert alpha to numeric a = 1, b = 2 etc
    for i in range(len(messagelist)):
        if messagelist[i] == 'a':
            messagelist[i] = '1'
        if messagelist[i] == 'b':
            messagelist[i] = '2'
        if messagelist[i] == 'c':
            messagelist[i] = '3'
        if messagelist[i] == 'd':
            messagelist[i] = '4'
        if messagelist[i] == 'e':
            messagelist[i] = '5'
        if messagelist[i] == 'f':
            messagelist[i] = '6'
        if messagelist[i] == 'g':
            messagelist[i] = '7'
        if messagelist[i] == 'h':
            messagelist[i] = '8'
        if messagelist[i] == 'i':
            messagelist[i] = '9'
        if messagelist[i] == 'j':
            messagelist[i] = '10'
        if messagelist[i] == 'k':
            messagelist[i] = '11'
        if messagelist[i] == 'l':
            messagelist[i] = '12'
        if messagelist[i] == 'm':
            messagelist[i] = '13'
        if messagelist[i] == 'n':
            messagelist[i] = '14'
        if messagelist[i] == 'o':
            messagelist[i] = '15'
        if messagelist[i] == 'p':
            messagelist[i] = '16'
        if messagelist[i] == 'q':
            messagelist[i] = '17'
        if messagelist[i] == 'r':
            messagelist[i] = '18'
        if messagelist[i] == 's':
            messagelist[i] = '19'
        if messagelist[i] == 't':
            messagelist[i] = '20'
        if messagelist[i] == 'u':
            messagelist[i] = '21'
        if messagelist[i] == 'v':
            messagelist[i] = '22'
        if messagelist[i] == 'w':
            messagelist[i] = '23'
        if messagelist[i] == 'x':
            messagelist[i] = '24'
        if messagelist[i] == 'y':
            messagelist[i] = '25'
        if messagelist[i] == 'z':
            messagelist[i] = '26'
        if messagelist[i] == ' ':
            messagelist[i] = '32'
        if messagelist[i] == '.':
            messagelist[i] = '28'

    # print to console convert to string, strip commas and format appropriately
    print(messagelist)
    print("messagelist string")
    tempmessagestr = str(messagelist)
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
    encryptlist = [eval(i) for i in encrypted]
    for i in range(len(encryptlist)):
        encryptlist[i] = (encryptlist[i] ** e) % n

    # convert numeric to string and format single digits to be preceded by 0's
    for i in range(len(encryptlist)):
        encryptlist[i] = "{:02}".format(encryptlist[i])

    en = str(encryptlist)
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

# function to decodedpt
def decode():
    # get input from the gui text entry box
    word2 = uinput3.get("1.0", "end-1c").lower()
    decoded = word2.lower()

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
    for i in range(len(decoded)):
        decoded = decoded.replace('01', '1')
        decoded = decoded.replace('02', '2')
        decoded = decoded.replace('03', '3')
        decoded = decoded.replace('04', '4')
        decoded = decoded.replace('05', '5')
        decoded = decoded.replace('06', '6')
        decoded = decoded.replace('07', '7')
        decoded = decoded.replace('08', '8')
        decoded = decoded.replace('09', '9')
    decmessage = []
    decodedtemp = [int(item) for item in decoded.split(',') if item.isdigit()]

    # iterate through list applying rsa decryption algorithm and append decrypted elements to new list
    for i in decodedtemp:
        i = (i ** d) % n
        print(i, end=', ')
        decmessage.append(i)

    # iterate through list and assign numeric to alpha 1=a, b =2 etc
    mapping = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 28: '.', 32: ' '
    }

    for i in range(len(decmessage)):
        if decmessage[i] in mapping:
            decmessage[i] = mapping[decmessage[i]]
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


# logo optional
#path = '2.png'
#img= ImageTk.PhotoImage(Image.open(path))
#panel = tk.Label(window, fg= purple, image = img, borderwidth=0, highlightthickness=0)
#panel.image = img
#panel.pack()

label1 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Key: p=3, q=11, e=3. Encryption: x^e %n Decryption: x^(10-e) %n", pady=5)
label1.pack()
label3 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Encrypt: Enter a message to encrypt", pady=8)
label3.pack()
uinput_value = StringVar(window)
uinput = Text(window, height=5, width=65, bg=lpurple)
uinput.pack()

label4 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Encrypted message:", pady=5)
label4.pack()
entry4 = Text(window, height=5, width=65, bg=lpurple)
entry4.pack()
label2 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="", pady=0)
label2.pack()
button02 = Button(window, bg= dpurple, fg=lpurple, height=1, width=10, text="Encrypt",command=lambda: encrypt())
button02.pack()


label2 = Label(window, bg= purple, fg= contrast, font='Helvetica 10 bold', text="Decrypt: Enter a message to decrypt", pady=8)
label2.pack()
uinput_value3 = StringVar(window)
uinput3 = Text(window, height=5, width=65, bg=lpurple)
uinput3.pack()
lab5 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Decrypted message:", pady=5)
lab5.pack()
chatb3 = Text(window, height=5,width=65, bg=lpurple)

chatb3.pack()
lab6 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="", pady=0)
lab6.pack()
button3 = Button(window, bg= dpurple, fg=lpurple, height=1, width=10, text="Decrypt",command=lambda: decode())
button3.pack()


window.mainloop()
start()
