from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

from Func import convertText
from HelperFunc import resource_path

try:
    import pyi_splash  # type: ignore
    pyi_splash.close()
except:
    pass

""" 
DOL: Wh, off wh, gy, sft, mod-hd, i/p.
DOLOMITE: White, off white, grey, soft, moderately hard, in part.
"""


def convertFromAbbr():
    text = txtBoxInput.get('1.0', END)
    txt = convertText(text, 'FROM_ABBR')
    # if isinstance(txt, bool):
    #     messagebox.showerror('Error', f'This is not a abbreviation click other button')
    #     txt = f'This is not a abbreviation click other button'
    if isinstance(txt, list):
        messagebox.showerror('Error', f'Please check this Word/s {txt}')
        txt = f'Please check this Word/s {txt}'
    addText(txt)


def convertToAbbr():
    text = txtBoxInput.get('1.0', END)
    txt = convertText(text, 'TO_ABBR')
    addText(txt)


def addText(txt):
    txtBoxOutput.delete('1.0', END)
    txtBoxOutput.insert(INSERT, txt)


root = Tk()

Button(root, text="From Abbr To Words", background='orange',
       command=convertFromAbbr).place(x=150, y=15)

Button(root, text="From Words To Abbr", background='orange',
       command=convertToAbbr).place(x=450, y=15)


group1 = LabelFrame(root, text="Text Input", padx=5,
                    pady=5, background='orange')
group1.place(x=20, y=55, width=660, height=20)

# Create the textbox
txtBoxInput = scrolledtext.ScrolledText(
    root, width=80, height=15, background='orange')
txtBoxInput.place(x=20, y=75)

group2 = LabelFrame(root, text="Text Output", padx=5,
                    pady=5, background='orange')
group2.place(x=20, y=330, width=660, height=20)

# Create the textbox
txtBoxOutput = scrolledtext.ScrolledText(
    root, width=80, height=15, background='orange')
txtBoxOutput.place(x=20, y=350)

madeWithLoveBy = Label(
    root, text='Made with ❤ by Mohamed Omar', background='orange', foreground='#000000',
    font=('monospace', 9, 'bold'))
madeWithLoveBy.place(x=490, y=595, width=190, height=20)

root.title('Litho_Abbr_Dict')
root.geometry('700x615')
root.configure(bg='#000')
root.resizable(False, False)
# Setting icon of master window
root.iconbitmap(resource_path('abbr.ico'))
# Start program
root.mainloop()
