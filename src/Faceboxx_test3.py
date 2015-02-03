import wx
import wx.lib.agw.hyperlink as hl
import fbIO

from Tkinter import *
from tkFileDialog import askopenfilename




class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def upload(self, event):
        Tk().withdraw()
        filename=askopenfilename()

        ### REPLACE WITH UPLOAD CODE ###
        
        ### filename is set, need to send to fbIO.py with fb credentials
        
        print(filename)

    def basicGUI(self):

        panel = wx.Panel(self)

        
        
        ## LOGIN DIALOGS ##
        getName = wx.TextEntryDialog(None, 'Enter Facebook Login')

        if getName.ShowModal()==wx.ID_OK:
            userName = getName.GetValue()

        getPass = wx.PasswordEntryDialog(None,'Enter Password')

        if getPass.ShowModal()==wx.ID_OK:
            passWord = getPass.GetValue()

        ## REPLACE WITH FB LOGIN CODE ##
        
        ### need to send userName, passWord to fbIO.py
        
        print(userName)
        print(passWord)
        ## REPLACE WITH FB LOGIN CODE ##


        button=wx.Button(panel, label='New Upload',pos=(300,150),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.upload, button)

        menuBar = wx.MenuBar()

        fileButton = wx.Menu()
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Exit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('sad_face.png'))
        fileButton.AppendItem(exitItem)
        #need to add way to kill process, fully close file?

        menuBar.Append(fileButton, '&File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
      
        self.SetTitle('Faceboxx')
        self.Show(True)



        ## FILE HEADERS ##
        
        ### change to be hidden until file is uploaded/split

        Text1 = wx.StaticText(panel, -1, 'Filename', (10,10))
        Text1.SetForegroundColour('black')

        Text2 = wx.StaticText(panel, -1, '#Files', (80,10))
        Text2.SetForegroundColour('#black')

        Text3 = wx.StaticText(panel, -1, 'Filesize(mb)', (130,10))
        Text3.SetForegroundColour('#black')

        Text4 = wx.StaticText(panel, -1, 'Date Uploaded', (210,10))
        Text4.SetForegroundColour('#black')

        ## FILE LIST ##

        indata = fbIO.link_name_map()
        i = 0
        names = indata[0]
        link = indata[1]
        position = [10,40]
        for k in xrange(len(indata[0])):
            name = 'file' + str(i)
            name = hl.HyperLinkCtrl(panel, -1, names[i], pos= position,
                                  URL=link[i])
            position[1] += 30
            i += 1
            
    '''



        self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        
        ### hyperlinks to each individual file after upload
        
        file1 = wx.HyperlinkCtrl(self, wx.ID_ANY, 'Filename1', 'www.google.com', (10,40),
              wx.DefaultSize, wx.HL_DEFAULT_STYLE, wx.HyperlinkCtrlNameStr)
        #sizer.Add(file1, 0, wx.ALL, 10)
        
        #self.Bind(wx.EVT_HYPERLINK_LEFT, self.OnLink)
        #file1.SetColours("BLUE", "BLUE", "BLUE")


        fileNum1 = wx.StaticText(panel, -1, '5', (80,40))
        Text1.SetForegroundColour('black')

        fileSize1 = wx.StaticText(panel, -1, '48.67', (130,40))
        Text1.SetForegroundColour('black')

        dateUpload1 = wx.StaticText(panel, -1, '2015-02-01 02:24:15', (210,40))
        Text1.SetForegroundColour('black')

        file2 = hl.HyperLinkCtrl(panel, -1, 'Filename2', pos=(10,70),
                                  URL="http://www.wxpython.org/")

        fileNum2 = wx.StaticText(panel, -1, '12', (80,70))
        Text1.SetForegroundColour('black')

        fileSize2 = wx.StaticText(panel, -1, '136.23', (130,70))
        Text1.SetForegroundColour('black')

        dateUpload2 = wx.StaticText(panel, -1, '2015-02-01 02:26:34', (210,70))
        Text1.SetForegroundColour('black')
    '''
    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

    
main()
        