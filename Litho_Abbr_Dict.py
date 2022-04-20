from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import pyperclip

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


def selectAllTxtBoxInput(*event):
    txtBoxInput.tag_add(SEL, "1.0", END)
    txtBoxInput.mark_set(INSERT, "1.0")
    txtBoxInput.see(INSERT)

    return "break"


def selectAllTxtBoxOutput(*event):
    txtBoxOutput.tag_add(SEL, "1.0", END)
    txtBoxOutput.mark_set(INSERT, "1.0")
    txtBoxOutput.see(INSERT)

    return "break"


def paste(*event):
    text = txtBoxInput.selection_get(selection='CLIPBOARD')
    txtBoxInput.insert('insert', text)

    return "break"


def copy(*event):
    try:
        text = txtBoxInput.selection_get()
        text = txtBoxOutput.selection_get()
        pyperclip.copy(text)
    except TclError:
        pass
    return "break"


def cut(*event):
    txtBoxInput.clipboard_clear()
    text = txtBoxInput.get("sel.first", "sel.last")
    txtBoxInput.clipboard_append(text)
    txtBoxInput.delete("sel.first", "sel.last")

    return "break"


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
    txtBoxOutput.config(state='normal')
    txtBoxOutput.delete('1.0', END)
    txtBoxOutput.insert(INSERT, txt)
    txtBoxOutput.config(state='disabled')


root = Tk()

Button(root, text="From Abbr To Words", background='#ff6f00',
       command=convertFromAbbr).place(x=150, y=15)

Button(root, text="From Words To Abbr", background='#ff6f00',
       command=convertToAbbr).place(x=450, y=15)


group1 = LabelFrame(root, text="Text Input", padx=5,
                    pady=5, background='orange')
group1.place(x=20, y=55, width=660, height=20)

# Create the textbox
txtBoxInput = scrolledtext.ScrolledText(
    root, width=80, height=15, background='#ffc800')
txtBoxInput.place(x=20, y=75)

group2 = LabelFrame(root, text="Text Output", padx=5,
                    pady=5, background='orange')
group2.place(x=20, y=330, width=660, height=20)

# Create the textbox
txtBoxOutput = scrolledtext.ScrolledText(
    root, width=80, height=15, background='#ffc800')
txtBoxOutput.place(x=20, y=350)
txtBoxOutput.config(state='disabled')

madeWithLoveBy = Label(
    root, text='Made with ❤ by Mohamed Omar', background='orange', foreground='#000000',
    font=('monospace', 9, 'bold'))
madeWithLoveBy.place(x=490, y=595, width=190, height=20)

mInput = Menu(root, tearoff=0)
mInput.add_command(label="Select All", command=selectAllTxtBoxInput)
mInput.add_command(label="Copy", command=copy)
mInput.add_command(label="Cut", command=cut)
mInput.add_command(label="Paste", command=paste)

mOutput = Menu(root, tearoff=0)
mOutput.add_command(label="Select All", command=selectAllTxtBoxOutput)
mOutput.add_command(label="Copy", command=copy)


def do_popup_input(event):
    try:
        mInput.tk_popup(event.x_root, event.y_root)
    finally:
        mInput.grab_release()


def do_popup_output(event):
    try:
        mOutput.tk_popup(event.x_root, event.y_root)
    finally:
        mOutput.grab_release()


txtBoxInput.bind("<Button-3>", do_popup_input)
txtBoxOutput.bind("<Button-3>", do_popup_output)

root.title('Litho_Abbr_Dict')
root.geometry('700x615')
root.configure(bg='#000')
root.resizable(False, False)
# Setting icon of master window
root.iconbitmap(resource_path('abbr.ico'))
# Start program
root.mainloop()
