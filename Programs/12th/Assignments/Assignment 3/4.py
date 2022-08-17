from tkinter import messagebox

root=tk.Tk()
can=tk.Canvas(root,width=300,height=300)
can.pack()

def ex():
    warning=tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if warning=='yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
        
btn=tk.Button(root, text='Exit Application',command=ex,bg='brown',fg='white')
can.create_window(150, 150, window=btn)
  
root.mainloop()
