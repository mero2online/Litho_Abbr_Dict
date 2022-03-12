from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

from Func import convertText


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

Button(root, text="Convert From Abbr", background='#e00707',
       command=convertFromAbbr).grid(row=0, column=0, pady=5)

Button(root, text="Convert To Abbr", background='#e00707',
       command=convertToAbbr).grid(row=0, column=1, pady=5)


group1 = LabelFrame(root, text="Text Input", padx=5, pady=5)
group1.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=E+W+N+S)

# Create the textbox
txtBoxInput = scrolledtext.ScrolledText(group1, width=80, height=15)
txtBoxInput.grid(row=1, column=0, columnspan=2, sticky=E+W+N+S)

group2 = LabelFrame(root, text="Text Output", padx=5, pady=5)
group2.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=E+W+N+S)

# Create the textbox
txtBoxOutput = scrolledtext.ScrolledText(group2, width=80, height=15)
txtBoxOutput.grid(row=1, column=0, columnspan=2, sticky=E+W+N+S)

root.title('Litho_Abbr_Dict')
root.geometry('700x610')
root.configure(bg='#000')
root.resizable(False, False)
# Setting icon of master window
# root.iconbitmap(resource_path('las.ico'))
# Start program
root.mainloop()
