import wx

from Tkinter import Tk
from tkFileDialog import askopenfilename




class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def upload(self, event):
        ### UPLOAD CODE ###
        Tk().withdraw()
        filename=askopenfilename()
        print(filename)

    def basicGUI(self):

        
        panel = wx.Panel(self)
        
        button=wx.Button(panel, label='Upload',pos=(300,10),size=(70,25))
        self.Bind(wx.EVT_BUTTON,self.upload, button)

        menuBar = wx.MenuBar()

        fileButton = wx.Menu()
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Exit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('res/sad_face.png'))
        fileButton.AppendItem(exitItem)

        menuBar.Append(fileButton, '&File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is your Facebook Login?', 'Facebook Login', 'login')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()

        passBox = wx.TextEntryDialog(None, 'What is your Facebook password?', 'Facebook Password', 'password')

        if passBox.ShowModal()==wx.ID_OK:
            password = passBox.GetValue()

        self.SetTitle('Faceboxx - ' +userName)
        self.Show(True)


        ### INSERT FILE LISTING CODE HERE ###

        Text1 = wx.StaticText(panel, -1, 'Login ='+userName, (10,10))
        Text1.SetForegroundColour('#67cddc')
        Text1.SetBackgroundColour('black')

        Text2 = wx.StaticText(panel, -1, 'Password ='+password, (10,40))
        Text2.SetForegroundColour('#67cddc')
        Text2.SetBackgroundColour('black')

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()



main()
