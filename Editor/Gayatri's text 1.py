import tkinter
from tkinter import *
import sys
import tkinter as ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import colorchooser
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
from tkinter.font import *
import tkinter.ttk as ttk

import datetime
import webbrowser
import os
import inspect
import importlib


file = None
def Quit():
    def opn():

        text.delete(1.0, END)

        global file
        file = open(askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*"),("Text files","*.txt"),("Python files","*.py") )))

        if file != '':
            x = str(file)
            y = x.split()[1]
            z = y.split("\'")[1]
            v=z.split("\\")[-1]
            t.title(os.path.basename(v)+"- Gayatri's text")
            txt = file.read()

            text.insert(INSERT, txt)
            file.close()
        else:

            pass

    def new_file():
        t.title("Untitled - Gayatri's text")

        text.delete(1.0,END)
        file=None

    def save():
        filename = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*"),("Text files","*.txt"),("Python files","*.py") ))

        if filename:
            alltext = text.get(1.0, END)

            f=open(filename, 'w')
            f.write(alltext)
            x = str(f)
            # print(x)
            # print(f)
            y = x.split()[1]
            z = y.split("/")[-1]
            # print("value of z=",z)
            # v = z.split("\\")
            # print("val of v=",v)
            # c=v.split("\\")
            # print("Value of c: ",c)

            t.title(z+"- Gayatri's text")




    def show():
        ab=Toplevel(t)
        ab.iconbitmap(r'C:\Users\user\Downloads\letter-g-icon-png-21704-Windows.ico')
        ab.title("Information")
        l=Label(ab,text="Gayatri's text\nauthor and developer-Gayatri(the decider)",fg="cyan",bg="grey",font=("Elephant",20))
        ab.geometry("580x90")
        l.pack()
        # showinfo("Gayatri's text","author and developer-Gayatri(the decider)")

    def normal():
        text.config(font=("Arial", 20))

    def bold():
        text.config(font=("Arial", 20, "bold"))

    def underline():
        text.config(font=("Arial", 20, "underline"))

    def italic():
        text.config(font=("Arial", 20, "italic"))

    def fontcolor():
        (triple, color) = askcolor()

        if color:
            text.config(foreground=color)

    def fontstyle():
        font=families("arial","helvetica")

        if font:
            text.config(font="font")

    def background():
        (triple, color) = askcolor()

        if color:
            text.config(background=color)

    def delete():
        MsgBox = messagebox.askquestion('Delete File', 'Are you sure you want to delete the file?',icon='warning')
        if MsgBox == 'yes':
            x = str(file)
            y = x.split()[1]
            t.destroy()

            y.split("\'")[1]
            os.remove(y.split("\'")[1])
            Quit()
            # os.remove(os.path.curdir)

        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')








    t=Toplevel()
    t.title("Untitled - Gayatri's Text")
    screenwidth=t.winfo_screenwidth()
    screenheight=t.winfo_screenheight()
    t.grid_rowconfigure(0,weight=1)
    t.grid_columnconfigure(0,weight=1)
    t.geometry('600x600')
    toolbaar = Frame(t, bd=2, relief=RAISED)

    img = Image.open(r"C:\Users\user\Desktop\new.jpg")
    photo1 = ImageTk.PhotoImage(img)
    new = Button(toolbaar, bd=5,bg="grey", width=22,height=22, relief=FLAT,image=photo1,command=new_file)
    new.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\open.jpg")
    photo2 = ImageTk.PhotoImage(img)
    open1=Button(toolbaar, bd=5,bg="grey", width=22,height=22, relief=FLAT,image=photo2,command=opn)
    open1.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\cut.jpg")
    photo3 = ImageTk.PhotoImage(img)
    cut=Button(toolbaar, bd=5,bg="grey", width=22,height=22, relief=FLAT,image=photo3,command=lambda :t.focus_get().event_generate("<<Cut>>"))
    cut.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\copy.png")
    photo4 = ImageTk.PhotoImage(img)
    copy = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo4,command=lambda: t.focus_get().event_generate("<<Copy>>"))
    copy.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\paste.jpg")
    photo5 = ImageTk.PhotoImage(img)
    paste = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo5,command=lambda: t.focus_get().event_generate("<<Paste>>"))
    paste.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\find.jpg")
    photo6 = ImageTk.PhotoImage(img)
    find = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo6)
    find.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\info.png")
    photo7 = ImageTk.PhotoImage(img)
    info1 = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo7)
    info1.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\undo.png")
    photo8 = ImageTk.PhotoImage(img)
    undo = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo8,command=lambda:t.focus_get().event_generate("<<Undo>>"))
    undo.pack(side=LEFT, padx=2, pady=2)

    img = Image.open(r"C:\Users\user\Desktop\redo.jpg")
    photo9 = ImageTk.PhotoImage(img)
    redo = Button(toolbaar, bd=5, bg="grey", width=22, height=22, relief=FLAT, image=photo9,command=lambda:t.focus_get().event_generate("<<Redo>>"))
    redo.pack(side=LEFT, padx=2, pady=2)


    toolbaar.pack(side=TOP, fill=X)

    text = Text(t,  font=("Arial", 20))

    scroll = Scrollbar(t, command=text.yview)

    scroll.config(command=text.yview)

    text.config(yscrollcommand=scroll.set,bg="white")

    scroll.pack(side=RIGHT, fill=Y)

    text.pack(side=TOP)

    t.iconbitmap(r'C:\Users\user\Downloads\letter-g-icon-png-21704-Windows.ico')
    # t.pack(fill=BOTH,expand=1)
    menu=Menu(t)
    t.config(menu=menu,bg="light grey")


    filemenu=Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New             ",accelerator='Ctrl+N',command=new_file)
    filemenu.add_command(label="Open            ",accelerator='Ctrl+O',command=opn)
    filemenu.add_command(label="Save            ",accelerator="Ctrl+S",command=save)
    filemenu.add_command(label="Close"           ,accelerator='Ctrl+W',command=t.quit)

    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=t.quit)

    editmenu=Menu(menu)
    menu.add_cascade(label="Edit",menu=editmenu)
    editmenu.add_command(label='Cut             ',accelerator='Ctrl+X',command=lambda :t.focus_get().event_generate("<<Cut>>"))
    editmenu.add_command(label='Copy            ',accelerator='Ctrl+C',command=lambda :t.focus_get().event_generate("<<Copy>>"))
    editmenu.add_command(label='Paste           ',accelerator='Ctrl+V',command=lambda :t.focus_get().event_generate("<<Paste>>"))
    editmenu.add_command(label='Delete'          ,accelerator='Ctrl+Alt+D',command=delete)
    editmenu.add_command(label='Undo'            ,accelerator='Ctrl+Z',command=lambda:t.focus_get().event_generate("<<Undo>>"))
    editmenu.add_command(label='Redo'           ,accelerator='Ctrl+Y',command=lambda :t.focus_get().event_generate("<<Redo>>"))

    formatmenu=Menu(menu)
    menu.add_cascade(label='Format',menu=formatmenu)
    formatmenu.add_checkbutton(label='Normal',command=normal)
    formatmenu.add_checkbutton(label='Bold',command=bold)
    formatmenu.add_checkbutton(label='Underline',command=underline)
    formatmenu.add_checkbutton(label='Italic',command=italic)
    formatmenu.add_separator()
    formatmenu.add_command(label='set font color',command=fontcolor)
    formatmenu.add_command(label='set font style',command=fontstyle)
    formatmenu.add_command(label='set background color',command=background)

    runmenu=Menu(menu)
    menu.add_cascade(label="Run",menu=runmenu)
    runmenu.add_command(label="Run...           F5")
    runmenu.add_separator()
    runmenu.add_command(label="Launch in firefox            Ctrl+alt+Shift+X")
    runmenu.add_command(label="Launch in Chrome             Ctrl+alt+Shift+R")

    helpmenu=Menu(menu)
    menu.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="About Gayatri's Text..",command=show)

    






    root.withdraw()
    mainloop()



def abc():
    print("Hello World!")


root=Tk()
style=ttk.Style(root)
root.title("Gayatri's Text")
root.config(bg="light grey")
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
root.geometry("600x600")
root.iconbitmap(r'C:\Users\user\Downloads\letter-g-icon-png-21704-Windows.ico')
# root.resizable("False","False")
im=Image.open(r"C:\Users\user\Desktop\gayu.jpg")
photo=ImageTk.PhotoImage(im)

# cv = Canvas()
# cv.config(width=600,height=600)
# cv.place( x=0,y=0,relwidth=1,relheight=1)


# cv.create_image(50, 50, image=photo)
l=Label(image=photo)
l.place(x=0,y=0,relwidth=1,relheight=1)

b=Button(l,justify=LEFT,bd=5,width=60,bg="grey",command=Quit)
img=Image.open(r"C:\Users\user\Desktop\jf.jpg")
photo2=ImageTk.PhotoImage(img)
b.config(image=photo2)
# cv.create_window(200,200,anchor="center",window=b)
b.pack()




root.mainloop()