from Tkinter import *

class popupWindow(object):
    def __init__(self,master, text="None", isTextFieldRequired = FALSE):
        top=self.top=Toplevel(master)

        self.lableMessage=Label(top,text=text)
        self.lableMessage.grid(row=0, column=0)
        self.lableMessage.pack()
        self.textFieldRequired = isTextFieldRequired
        # Text input field is required enable this
        if isTextFieldRequired == TRUE:
            self.e=Entry(top)
            self.e.pack()

        self.buttonOk=Button(top,text='Ok',command=self.cleanup, width = 20)
        self.buttonOk.grid(row=3, column=1)
        self.buttonOk.pack()

        # can't be maximize
        top.resizable(width=False, height=False)

        self.center()

    # function that will make the window appear to the center of the screen
    def center(self):
        self.top.update_idletasks()
        w = self.top.winfo_screenwidth()
        h = self.top.winfo_screenheight()
        size = tuple(int(_) for _ in self.top.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2

        self.top.geometry("%dx%d+%d+%d" % (size + (x, y-200)))

    def cleanup(self):
        if self.textFieldRequired == TRUE:
            #To get the value of the text field
            self.value=self.e.get()

        self.top.destroy()