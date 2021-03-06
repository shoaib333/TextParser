from Tkinter import *
import tkFileDialog
from LineInfo import *
from  grammar import *
from textWindow import *

#pass/fail enums
TC_FAIL = -1
TC_PASS = 1

#Parser Grammar
g = grammar()
grammar = g.grammar

#Function to calculate file length
def file_len(fname):                                    #calculate number of lines in the file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#Function to load the log file, and populate then contents in the array
def load_file_as_array(self = None, fname=""):                       #load file line by line into object
    if fname == "":                                     # if no file name is present return failure
        txtWindow = popupWindow(self.master, "No file is Selected, kindly Select a file")
        self.master.wait_window(txtWindow.top)
        print "No file is selected"
        return TC_FAIL

    file_length = file_len(fname)# calculate file length
    lineInfoLists = [LineInfo() for x in range(file_length)]# creating list of line objects

    f = open(fname)                                     # open log file
    count = 0

    while open(fname):                                  # start loading file
        for lineInfoLists[count].rawLineString in f:    #fill raw data in to the class object

            if count >= file_length:                    # guard check
                print "File data exceeded"
                break
            status = lineInfoLists[count].tokenizeData()#tokenize received string line
            if status == False:
                print "Line could not be parsed, as format did not match"
            count = count +1

        break#all of the file is traversed
    f.close()    #all of the data is parsed in the objects, close the file

    return lineInfoLists

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Parser")
        #setting window to screen size
        self.master.geometry('{}x{}'.format(self.winfo_screenwidth(),self.winfo_screenheight()))
        self.master.rowconfigure(100, weight=1)
        self.master.columnconfigure(100, weight=1)
        self.grid(sticky=W + E + N + S)
        self.enteredFilter = 'None'     # To store the filter string
        self.data = 'None'              # Variable to store the parsed log file

        #Create a Frame placeholder that will hold all other frames
        self.mainFrame = Frame(self.master, width = (self.winfo_screenwidth()-50), height = (self.winfo_screenheight()-50))
        self.mainFrame.grid()
        self.mainFrame.config(relief = RIDGE, borderwidth=2)
        # self.mainFrame.pack_configure(side = LEFT, expand = True)

        # crete menu frame that will hold all the buttons
        self.createMenuFrame()

        # crete text frame that will control Text gui
        self.createTextFrame()

    # Create a menu frame this section contains all of the gui control
    def createMenuFrame(self):

        self.menuFrame = Frame(self.mainFrame, width=60, height=20)
        self.menuFrame.pack_configure(side="left")
        self.menuFrame.grid(row=0, column=0)  # Place it on the top left corner
        self.menuFrame.config(relief=RIDGE, borderwidth = 2)
        # Add button to load file to parse
        self.button = Button(self.menuFrame, text="Browse File to Parse", command=self.load_file, width=20)
        self.button.grid(row=0, column=0)

        # Add button to load file to parse
        self.button = Button(self.menuFrame, text="Browse schema", command=self.load_schema, width=20)
        self.button.grid(row=0, column=1)

        # Add button to store the filtered file on drive
        self.button = Button(self.menuFrame, text="Generate File", command=self.generateFile, width=20)
        self.button.grid(row=0, column=2)

        # Text label for Filter
        self.filterlable = Label(self.menuFrame, text="Filter")
        self.filterlable.grid(row=1, column=0)

        # Displaying input field where user can enter filter strings
        vcmd = self.master.register(self.validate)  # We have to wrap the command
        self.entry = Entry(self.menuFrame, validate="key", validatecommand=(vcmd, '%P'), width=20)
        self.entry.pack(side="left")
        self.entry.grid(row=1, column=1)

        self.button = Button(self.menuFrame, text="Apply Filter", command=self.ApplyFilter, width=20)
        self.button.grid(row=1, column=2)

    # This section contains text field gui control
    def createTextFrame(self):

        # TEXT FRAME
        self.textFrame = Frame(self.mainFrame, width=500, height=100)
        self.textFrame.pack(fill="both", expand=True)
        self.textFrame.grid(row=01, column=01)
        self.textFrame.config(relief=RIDGE, borderwidth = 2)
        # ensure a consistent GUI size
        # self.textFrame.grid_propagate(False)

        # implement stretchability
        self.textFrame.grid_rowconfigure(0, weight=1)
        self.textFrame.grid_columnconfigure(0, weight=1)

        # Create A Text Widget

        self.txt = Text(self.textFrame, borderwidth=3, relief="sunken", width=150, height=45)
        self.txt.config(font=("consolas", 12), undo=True, wrap=NONE)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        Yscrollb = Scrollbar(self.textFrame, command=self.txt.yview)
        Yscrollb.grid(row=0, column=1, sticky='nsew')

        Xscrollb = Scrollbar(self.textFrame, command=self.txt.xview, orient=HORIZONTAL)
        Xscrollb.grid(row=1, column=0, sticky='nsew')

        self.txt.config(xscrollcommand=Xscrollb.set, yscrollcommand=Yscrollb.set)


    def generateFile(self):
        filteredString = self.parseFilterString()

        if filteredString == "":
            txtWindow = popupWindow(self.master, "No filter string is entered \n kindly enter a filter string")
            self.master.wait_window(txtWindow.top)
            print "No filter is entered"
            return
        file =  tkFileDialog.asksaveasfile(filetypes=(("text files", "*.txt"), ("All files", "*.*")))
        #TODO: here parse the string according to the filter output the file

        #write data in the file
        v = open(file.name,'w')
        count = len(self.data)
        for i in range(0, count-2):
            for j in range(1, len(filteredString)):

                #TODO: chcek this out!... if re.match(self.data[i].rawLineString, filteredString[j]) != None:
                tempString = self.data[i].rawLineString
                tempFilter = filteredString[j]
                tempString = tempString.upper()
                tempFilter = tempFilter.upper()
                if tempString.find(tempFilter) != -1:
                    print "Raw Data:"+ self.data[i].rawLineString
                    v.writelines(self.data[i].rawLineString)
                    break
        v.close()

    def ApplyFilter(self):

        print "Applying the entered filter to the loaded file"
        filteredString = self.parseFilterString()

        if filteredString == "":
            txtWindow = popupWindow(self.master, "No filter string is entered \n kindly enter a filter string")
            self.master.wait_window(txtWindow.top)
            print "No filter string is entered"
            # TODO: print the dialog box, with the message
            return

        self.txt.config(state=NORMAL)
        self.txt.delete("1.0",END)
        self.txt.config(state=DISABLED)
        # write data in the file
        count = len(self.data)
        for i in range(0, count-2):
            for j in range(1, len(filteredString)):
                #TODO: chcek this out!... if re.match(self.data[i].rawLineString, filteredString[j]) != None:
                tempString = self.data[i].rawLineString
                tempFilter = filteredString[j]
                tempString = tempString.upper()
                tempFilter = tempFilter.upper()
                if tempString.find(tempFilter) != -1:
                    self.txt.config(state=NORMAL)
                    self.txt.insert(END, self.data[i].rawLineString)
                    self.txt.config(state=DISABLED)
                    break
        #data is printed on the text view container

    def parseFilterString(self):
        rawString = self.enteredFilter              #getting filtered

        if rawString == "":
            txtWindow = popupWindow(self.master, "No filter string is entered \n kindly enter a filter string")
            self.master.wait_window(txtWindow.top)

            print "No filter string is entered"
            return ""

        filteredString = ['']

        splittedData = rawString.partition(',')
        if splittedData[0] != rawString:
            filteredString[0] = splittedData[0]
            rawString = splittedData[2]

        while rawString != ';':
            splittedData =rawString.partition(',')
            if splittedData[0] != rawString:
                filteredString.append(splittedData[0])
                rawString = splittedData[2]
            else:
                splittedData =rawString.partition(';')
                filteredString.append(splittedData[0])
                break

        return filteredString

    def validate(self, new_text):
        if not new_text:                        # the field is being cleared
            self.enteredFilter = 'None'
            return True
        try:
            self.enteredFilter = str(new_text)
            return True
        except ValueError:
            return False

    def load_file(self):                        # load file to be parsed
        # setting the types of the files that can be loaded
        fname = tkFileDialog.askopenfilename(filetypes=(("text files", "*.txt"), ("All files", "*.*")))

        try:
            print("""here it comes: self.settings["template"].set(fname)""")
            print "file name is " + str(fname)
        except:  # <- naked except is a bad idea
            tkFileDialog.showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return

        if fname == "":  # if no file name is present return failure
            txtWindow = popupWindow(self.master, "No file is Selected, kindly Select a file")
            self.master.wait_window(txtWindow.top)
            print "No file is selected"
            return

        data = load_file_as_array(self, fname)           # load file and copy lines into objects

        if data != TC_FAIL:
            self.data = data
        else:
            txtWindow = popupWindow(self.master, "ERROR: Data could not be loaded from the file")
            self.master.wait_window(txtWindow.top)
            print "Data could not be loaded from the file"

        print "printed"
        return

    def load_schema(self):
        fname = tkFileDialog.askopenfilename(filetypes=(("text files", "*.txt"),
                                                        ("XML files", "*.xml"),
                                                        ("All files", "*.*")))
        if fname:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
                print "file name is " + str(fname)
            except:  # <- naked except is a bad idea
                tkFileDialog.showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return

if __name__ == "__main__":
    Parser = MyFrame()

    Parser.mainloop()
