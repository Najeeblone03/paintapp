from tkinter import *

root = Tk()
root.title("Paint App")
root.geometry("1100x600")

stroke_size = IntVar()
stroke_size.set(1)

stroke_color = StringVar()
stroke_color.set("black")

# Frame 1: Tools
frame1 = Frame(root, height=100, width=1100)
frame1.grid(row=0, column=0, sticky=NW)

# Tools frame
toolsFrame = Frame(frame1, height=100, width=100)
toolsFrame.grid(row=0, column=0)

def usepencil():
    stroke_color.set("black")
    canvas["cursor"] = "arrow"

def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = "dotbox"  # Fixed to use a string "dotbox"

pencilButton = Button(toolsFrame, text="Pencil", width=10, command=usepencil)
pencilButton.grid(row=0, column=0)

eraserButton = Button(toolsFrame, text="Eraser", width=10, command=useEraser)
eraserButton.grid(row=1, column=0)

toolslabel = Label(toolsFrame, text="Tools", width=10)
toolslabel.grid(row=2, column=0)

# Size Frame
sizeFrame = Frame(frame1, height=100, width=100)
sizeFrame.grid(row=0, column=1)

defaultButton = Button(sizeFrame, text="Default", width=10, command=usepencil)
defaultButton.grid(row=0, column=0)

options = [1, 2, 3, 4, 5, 10]

sizeList = OptionMenu(sizeFrame, stroke_size, *options)
sizeList.grid(row=1, column=0)

sizeLabel = Label(sizeFrame, text="Size", width=10)
sizeLabel.grid(row=2, column=0)

# Frame 2: Canvas
frame2 = Frame(root, height=500, width=1100, bg="yellow")
frame2.grid(row=1, column=0)

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)

# Variables for drawing
prevPoint = None

def paint(event):
    global prevPoint

    x, y = event.x, event.y

    if prevPoint:
        # Draw line between the previous point and current point
        canvas.create_line(prevPoint[0], prevPoint[1], x, y, fill=stroke_color.get(), width=stroke_size.get())

    # Update the previous point to the current point
    prevPoint = (x, y)

def reset_prev_point(event):
    global prevPoint
    prevPoint = None

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", reset_prev_point)

root.resizable(False, False)
root.mainloop()
