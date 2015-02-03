import wx

from Tkinter import *
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

        top = Tk()
        top.wm_title('Faceboxx')
        L1 = Label(top, text="User Name")
        L1.grid(row=0, column=0)
        E1 = Entry(top, bd = 5)
        E1.grid(row=0, column=1)
        L1 = Label(top, text="Password")
        L1.grid(row=1, column=0)
        E2 = Entry(top, bd = 5, show="*")
        E2.grid(row=1, column=1)

        def ok():
            username = E1.get()
            password = E2.get()
            top.destroy()
            ### USE VARS TO ACCESS FACEBOOK HERE ##
            return username, password
        
        MyButton1 = Button(top, text="Submit", width=10, command= ok)
        MyButton1.grid(row=3, column=1)

        top.mainloop()

        button=wx.Button(panel, label='Upload',pos=(300,10),size=(70,25))
        self.Bind(wx.EVT_BUTTON,self.upload, button)

        menuBar = wx.MenuBar()

        fileButton = wx.Menu()
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Exit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('sad_face.png'))
        fileButton.AppendItem(exitItem)

        menuBar.Append(fileButton, '&File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
      
        self.SetTitle('Faceboxx')
        self.Show(True)



        

        Text1 = wx.StaticText(panel, -1, 'File1', (10,10))
        Text1.SetForegroundColour('#67cddc')
        Text1.SetBackgroundColour('black')

        Text2 = wx.StaticText(panel, -1, 'File2', (10,40))
        Text2.SetForegroundColour('#67cddc')
        Text2.SetBackgroundColour('black')

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()



main()
