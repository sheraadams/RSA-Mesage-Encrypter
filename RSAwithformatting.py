from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk

button_color = "#BB86FC" # lavender
box_color= "#03dbc5" # teal
button_text_color = "#000000"
back= "#1c1b1f"   # dark slate
text_color = "#BB86FC"  # lavender

# window dimensions and color
window = Tk()
window.geometry("720x1000")  # was 720 x 420
window.configure(bg=back)
window.title("RSA Encryption and Decryption Generator")

# Conversion functions
letter_to_number = lambda char: ord(char.lower()) - ord('a') + 1 if char.isalpha() else 32
number_to_letter = lambda num: chr(num + ord('a') - 1) if 1 <= num <= 26 else ' '
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

def encrypt():
    p, q, e = 3, 11, 3
    n, d = p * q, 10 - p

    message_input = uinput.get("1.0", "end-1c").lower()
    message_list = [str(letter_to_number(char)) for char in message_input]

    encrypted_list = [(int(i) ** e) % n for i in message_list]
    encrypted_list = ["{:02}".format(num) for num in encrypted_list]

    encrypted_str = str(encrypted_list).replace(" ", '').replace("'", "").replace("[", "").replace("]", "")

    entry4.delete("1.0", END)
    entry4.insert(END, encrypted_str)

# Decryption function
def decode():
    p, q, e = 3, 11, 3
    n, d = p * q, 10 - p

    word2 = uinput3.get("1.0", "end-1c").lower()
    decoded = word2.lower()

    for i in range(1, 10):
        decoded = decoded.replace(f'0{i}', str(i))

    decoded_temp = [int(item) for item in decoded.split(',') if item.isdigit()]

    dec_message = [(int(i) ** d) % n for i in decoded_temp]

    mapping = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 28: '.', 32: ' '
    }

    dec_message = [mapping[i] for i in dec_message if i in mapping]

    dec_str = ''.join(dec_message)

    chatb3.delete("1.0", END)
    chatb3.insert(END, dec_str)

# gui pack layout
path = '2lavender.png'
img= ImageTk.PhotoImage(Image.open(path))

# pack header image panel
panel = tk.Label(window, fg= back, image = img, borderwidth=0, highlightthickness=0)
panel.image = img
panel.pack()

# window to get input for number to assign to space
label4 = Label(window, bg= back, fg= text_color, font='Helvetica 10 bold', text="Assign space to a unique number (27-32)", pady=8)
label4.pack()

# value
uinput_value4 = StringVar(window)

# entry
uinput4 = Text(window, height=1, width=65, bg=box_color)
uinput4.pack()

# window to get input for number to assign to period
# label
label6 = Label(window, bg= back, fg= text_color, font='Helvetica 10 bold', text="Assign period (27-32)", pady=8)
label6.pack()

# entry value
uinput_value6 = StringVar(window)

#entry
uinput6 = Text(window, height=1, width=65, bg=box_color)
uinput6.pack()

# label enter message to encrypt
label3 = Label(window, bg= back, fg= text_color, font='Helvetica 10 bold', text="Encrypt: Enter a message to encrypt", pady=8)
label3.pack()

# value
uinput_value = StringVar(window)

# input window
uinput = Text(window, height=5, width=65, bg=box_color)
uinput.pack()

# text window for output message encrypted
label4 = Label(window, bg= back, fg= text_color, font='Helvetica 9 bold', text="Encrypted message:", pady=5)
label4.pack()

# output entry box
entry4 = Text(window, height=5, width=65, bg=box_color)
entry4.pack()

# labels
label2 = Label(window, bg= back, fg= text_color, font='Helvetica 9 bold', text="", pady=0)
label2.pack()

button02 = Button(window, bg= button_color, fg=button_text_color, height=1, width=10, text="Encrypt",command=lambda: encrypt())
button02.pack()

# window for text entry for message to decrypt
# label
label2 = Label(window, bg= back, fg= text_color, font='Helvetica 10 bold', text="Decrypt: Enter a message to decrypt", pady=8)
label2.pack()

#value
uinput_value3 = StringVar(window)

# entry box
uinput3 = Text(window, height=5, width=65, bg=box_color)
uinput3.pack()

# label
lab5 = Label(window, bg= back, fg= text_color, font='Helvetica 9 bold', text="Decrypted message:", pady=5)
lab5.pack()

# output entry box
chatb3 = Text(window, height=5,width=65, bg=box_color)
chatb3.pack()

#Label
lab6 = Label(window, bg= back, fg= box_color, font='Helvetica 9 bold', text="", pady=0)
lab6.pack()

# Decrypt button
button3 = Button(window, bg= button_color, fg=button_text_color, height=1, width=10, text="Decrypt",command=lambda: decode())
button3.pack()

# window for output comma to space
# label
label7 = Label(window, bg= back, fg= text_color, font='Helvetica 10 bold', text="To convert a comma separated string enter it below:", pady=8)
label7.pack()

uinput_value7 = StringVar(window)
uinput7 = Text(window, height=2.5, width=65, bg=box_color)
uinput7.pack()

# label
lab5 = Label(window, bg= back, fg= text_color, font='Helvetica 9 bold', text="Comma converted to space:", pady=5)
lab5.pack()

# window for output comma to space message
chatb4 = Text(window, height=2.5,width=65, bg=box_color)
chatb4.pack()

#label for spacing
lab9 = Label(window, bg= back, fg= text_color, font='Helvetica 9 bold', text="", pady=0)
lab9.pack()

# Comma to space button
button4 = Button(window, bg= button_color, fg=button_text_color, height=1, width=10, text="to Space",command=lambda: toSpace())
button4.pack()

# label
label1 = Label(window, bg= back, fg= text_color, font='Helvetica 10 bold', text="Using Key: p=3, q=11, e=3. Encryption: x^e %n Decryption: x^(10-e) %n", pady=5)
label1.pack()

window.mainloop()
start()
