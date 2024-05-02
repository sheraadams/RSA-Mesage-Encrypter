from tkinter import Tk, Label, Text, Button, END

# Color dictionary
colors = {
    "button_color": "#BB86FC", # lavender
    "bg_color": "#1c1b1f",  # dark slate
    "box_color": "#03dbc5", # teal
    "button_text_color": "#000000",  # black
    "text_color": "#BB86FC" # lavender
}

window = Tk()
window.geometry("620x620")
window.configure(bg=colors["bg_color"])
window.title("RSA Encryption and Decryption Generator")

# Conversion functions
letter_to_number = lambda char: ord(char.lower()) - ord('a') + 1 if char.isalpha() else 32
number_to_letter = lambda num: chr(num + ord('a') - 1) if 1 <= num <= 26 else ' '

# Encryption function
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

# GUI elements
label1 = Label(window, bg=colors["bg_color"], fg=colors["text_color"], font='Helvetica 10 bold',
               text="Key: p=3, q=11, e=3. Encryption: x^e %n Decryption: x^(10-e) %n", pady=5)
label1.pack()

label3 = Label(window, bg=colors["bg_color"], fg=colors["text_color"], font='Helvetica 10 bold', text="Encrypt: Enter a message to encrypt", pady=8)
label3.pack()

uinput = Text(window, height=5, width=65, bg=colors["box_color"])
uinput.pack()

label4 = Label(window, bg=colors["bg_color"], fg=colors["button_text_color"], font='Helvetica 9 bold', text="Encrypted message:", pady=5)
label4.pack()

entry4 = Text(window, height=5, width=65, bg=colors["box_color"])
entry4.pack()

button02 = Button(window, bg=colors["button_color"], fg=colors["button_text_color"], height=1, width=10, text="Encrypt", command=encrypt)
button02.pack()

label2 = Label(window, bg=colors["bg_color"], fg=colors["text_color"], font='Helvetica 10 bold', text="Decrypt: Enter a message to decrypt", pady=8)
label2.pack()

uinput3 = Text(window, height=5, width=65, bg=colors["box_color"])
uinput3.pack()

lab5 = Label(window, bg=colors["bg_color"], fg=colors["button_text_color"], font='Helvetica 9 bold', text="Decrypted message:", pady=5)
lab5.pack()

chatb3 = Text(window, height=5, width=65, bg=colors["box_color"])
chatb3.pack()

button3 = Button(window, bg=colors["button_color"], fg=colors["button_text_color"], height=1, width=10, text="Decrypt", command=decode)
button3.pack()

window.mainloop()
