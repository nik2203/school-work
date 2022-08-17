from tkinter import *
from tkinter import Button, Label, messagebox as mb


root=Tk()
root.title('Sample Programs')

'''
myCanvas=Canvas(root, bg = 'purple', height=250, width=300)
coord=10,50,240,210
arc=myCanvas.create_arc(coord, start=0, extent =120, fill='pink')
myCanvas.pack()

var1=IntVar()
myC1=Checkbutton(root,text='Male',variable=var1)
myC1.grid(row=0,column=0,rowspan=2,columnspan=2,sticky=W,padx=40,pady=20)
var2=IntVar()
myC2=Checkbutton(root,text='Female',variable=var2)
myC2.grid(row=2,column=0,rowspan=2,columnspan=2,sticky=W,padx=40,pady=20)

def answer():
    if mb.askyesno('Answer','Is 2020 a leap year?'):
        mb.showinfo('Answer','Correct')
        exit()
    else:
        mb.showinfo('Answer','Incorrect')
def callback():
    if mb.askyesno('Verify','Really quit?'):
        mb.showinfo('Quit','Goodbye')
        exit()
    else:
        mb.showinfo('No','GOod choice')

label=Label(root,text='Would you like to answer a question?')
b1=Button(root,text='Answer',command=answer,padx=40,pady=20).pack(fill=None)
b2=Button(root,text='Quit',command=callback,padx=40,pady=20).pack(fill=None)
'''
frame=Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
r


root.mainloop()