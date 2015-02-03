import wx

from Tkinter import *
from tkFileDialog import askopenfilename
import Tkinter as tk
import fbIO
import wx.lib.agw.hyperlink as hl
import chunk
import sys

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def upload(self, event, uname, pword):
        Tk().withdraw()
        filename=askopenfilename()

        fbIO.upload(filename, uname, pword)
        
    def basicGUI(self):
        
        #splash screen
        root = tk.Tk()

        root.overrideredirect(True)
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.1, height*0.1))

        image_file = "res/faceboxx_logo.gif"

        image = tk.PhotoImage(file=image_file)
        canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="black")
        canvas.create_image(width*0.5/2, height*0.5/2, image=image)
        canvas.pack()

        # show the splash screen for 3000 milliseconds then destroy
        root.after(3000, root.destroy)
        root.mainloop()

        #start application
        panel = wx.Panel(self)

        
        
        ## LOGIN DIALOGS ##
        getName = wx.TextEntryDialog(None, 'Enter Facebook Login')

        if getName.ShowModal()==wx.ID_OK:
            userName = getName.GetValue()

        getPass = wx.PasswordEntryDialog(None,'Enter Password')

        if getPass.ShowModal()==wx.ID_OK:
            passWord = getPass.GetValue()

        button=wx.Button(panel, label='New Upload',pos=(300,150),size=(80,30))
        self.Bind(wx.EVT_BUTTON, 
                    lambda event: self.upload(event, userName, passWord),
                    button)

        menuBar = wx.MenuBar()

        fileButton = wx.Menu()
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Exit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('res/sad_face.png'))
        fileButton.AppendItem(exitItem)

        menuBar.Append(fileButton, '&File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
      
        self.SetTitle('Faceboxx')
        self.Show(True)



        ## FILE HEADERS ##
        
        ### change to be hidden until file is uploaded/split? or just don't show at all?

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
        if indata: 
            i = 0
            names = indata[0]
            link = indata[0]
            position = [10, 40]
            shown = []
            #for k in xrange(len(indata[0])):
                #name = 'file' + str(i)
                #name = hl.HyperLinkCtrl(panel, -1, names[i], pos=position,
            # URL=link[i])
            if names[i][:-1] not in shown:
                                button=wx.Button(panel, label=names[i][:-1], pos=position,size=(80,30))
                                shown += names[i][:-1]
                                i += 1
                                position[1] += 30
                                self.Bind(wx.EVT_BUTTON, self.combine, button)

    def Quit(self, e):
        self.Close()
        sys.exit(0)
        
    def combine(self, event):
        # get label name
        # iterate through links and download each file with matching name
        # to name.zipdir/.
        # call joinFiles(name.zipiter, number of chunks)
        # call zipdecrypt(inputfile, password)
        return

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()
    return

main() 
