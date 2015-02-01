# splash Screen

import Tkinter as tk

root = tk.Tk()

root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.1, height*0.1))

image_file = "faceboxx_logo.gif"

image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="black")
canvas.create_image(width*0.5/2, height*0.5/2, image=image)
canvas.pack()

# show the splash screen for 3000 milliseconds then destroy
root.after(3000, root.destroy)
root.mainloop()

