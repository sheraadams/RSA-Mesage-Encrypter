
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

delay = 2

#colors
purple = "#C55FFC"
lpurple= "#EFDCF9"
dark= "#323E42"
dpurple= "#7954A1"
back = "#278ED5"
contrast = "#65FC6A"
window = Tk()
window.geometry("320x460")
window.configure(bg=purple)
window.title("Chat Support")

def chat():
    INPUT = uinput.get("1.0", "end-1c").lower().strip('\n')
    if (INPUT == "shop"):
        chatb.delete("1.0", END)
        chatb.insert(END, 'www.sheraadams.com')
    elif (INPUT == "returns"):
        chatb.delete("1.0", END)
        chatb.insert(END, 'Returns can be sent via\nUSPS to:\n\n6000^8 Infinity Dr.\n'
                          'Silicon Valley, CA\n00000\n\nTo speak with a customer '
                          'service representative\ncall: 800-0000-000')
    elif (INPUT == "contact"):
        chatb.delete("1.0", END)
        chatb.insert(END, '800-500-5000\n6000^8 Infinity Dr.\nSilicon Valley, CA\n00000')
    elif (INPUT == "help"):
        chatb.delete("1.0", END)
        chatb.insert(END, "To speak with a customer service representative\ncall: 800-000-0000")
    else:
        chatb.delete("1.0", END)
        chatb.insert(END,"How can I help you today?\nType 'quit' at anytime\nto quit.")

path = '2.png'
img= ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, fg= purple, image = img, borderwidth=0, highlightthickness=0)
panel.image = img
panel.pack()
lab = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Message from You:", pady=8)
lab.pack()
uinput_value = StringVar(window)
uinput = Text(window, height=5, width=25, bg=lpurple)
uinput.pack()
lab2 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Message from Support:", pady=8)
lab2.pack()
chatb = Text(window, height=10,width=25, bg=lpurple)
chatb.pack()
lab3 = Label(window, bg= purple, fg= lpurple, font='Helvetica 9 bold', text="Options: Shop, Help, Returns, Contact", pady=10)
lab3.pack()
button = Button(window, bg= dpurple, fg=lpurple, height=2, width=20, text="Send",command=lambda: chat())
button.pack()


window.mainloop()
