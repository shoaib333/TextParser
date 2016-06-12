# LineInfo class that will tokenize the console output into different categories
class LineInfo:
    def __init__(self, rawString="", date="", time="", time2="", type="", messageType="", messageInfoType="",
                 isMessageInfoTypePresent = True, message="", isLineParseable=True):
        self.rawLineString = rawString
        self.date = date  # data format is year-month-day
        self.time = time  # time format is hour, minute, seconds.mili seconds
        self.time2 = time2  # time2 not sure yet
        self.type = type  # type can be of three types i.e. INFO, DEBUG or ERROR
        self.messageType = messageType  # Type of message is e.g. cki mmi cmw etc
        self.messageInfoType = messageInfoType  # this belongs of atf or cmw or target type
        self.isMessageInfoTypePresent = isMessageInfoTypePresent
        self.message = message  # messge that is printed or the information that is being conveyed
        self.isLineParseable = isLineParseable


    def tokenizeData(self):
        print "tokenizing data"

        #TODO: checks needs to be places if the string is the same as the searched one
        #TODO: that means there is some error and the print is not the one we are looking at

        rawString = self.rawLineString#getting date

        splittedData =rawString.partition(' ')
        if splittedData[0] !=  rawString:

            self.date = splittedData[0]
            rawString = splittedData[2]
        else:
            print "string not found"
            self.isLineParseable = False #line can't be parsed
            return False
            #TODO: make a bool that will set to true when this happens


        splittedData = rawString.partition(' ')
        if splittedData[0] !=  rawString:
            self.time = splittedData[0]
            rawString = splittedData[2]
        else:
            print "string not found"
            #TODO: make a bool that will set to true when this happens
            self.isLineParseable = False #line can't be parsed
            return False

        #dump spaces
        splittedData = rawString.partition(':')
        if splittedData[0] !=  rawString:
            rawString = splittedData[2]
        else:
            print "string not found"
            #TODO: make a bool that will set to true when this happens
            self.isLineParseable = False #line can't be parsed
            return False

        splittedData = rawString.partition(':')
        if splittedData[0] !=  rawString:
            self.time2 = splittedData[0]
            rawString = splittedData[2]
        else:
            print "string not found"
            #TODO: make a bool that will set to true when this happens
            self.isLineParseable = False #line can't be parsed
            return False


        splittedData = rawString.partition(':')
        if splittedData[0] !=  rawString:
            self.type= splittedData[0]
            rawString = splittedData[2]
        else:
            print "string not found"
            #TODO: make a bool that will set to true when this happens
            self.isLineParseable = False #line can't be parsed
            return False


        splittedData = rawString.partition(':')
        if splittedData[0] !=  rawString:
            self.messageType = splittedData[0]
            rawString = splittedData[2]
        else:
            print "string not found"
            #TODO: make a bool that will set to true when this happens
            self.isLineParseable = False #line can't be parsed
            return False

        #dump spaces
        splittedData = rawString.partition(':')
        if splittedData[0] !=  rawString:
            rawString = splittedData[2]
        else:
            print "string not found"
            #TODO: make a bool that will set to true when this happens
            self.isLineParseable = False #line can't be parsed
            return False

        splittedData = rawString.partition(':')
        if splittedData[0] !=  rawString:
            self.messageInfoType = splittedData[0]
            rawString = splittedData[2]
        else:
            print "message Info Type not found"
            self.isMessageInfoTypePresent = False

        self.message = rawString
        self.remove_spaces()

        return True

    def remove_spaces(self):
        print "removing spaces"
        self.time.replace(' ','')
        self.date.replace(' ','')
        self.time2.replace(' ','')
        self.type.replace(' ','')
        self.messageType.replace(' ','')
        self.messageInfoType.replace(' ','')