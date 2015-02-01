from Tkinter import *
import webbrowser

url = 'http://www.sampleurl.com'

root = Tk()
frame = Frame(root)
frame.pack()

def OpenUrl():
    webbrowser.open_new(url)

button = Button(frame, text="CLICK", command=OpenUrl)

button.pack()
root.mainloop()
