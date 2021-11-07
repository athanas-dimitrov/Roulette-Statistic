# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import PyQt5

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")
import tkinter
import time

Window_Width = 800

Window_Height = 600

Ball_Start_XPosition = 50

Ball_Start_YPosition = 50

Ball_Radius = 30

Ball_min_movement = 5

Refresh_Sec = 0.01


def create_animation_window():
    Window = tkinter.Tk()
    Window.title("Python Guides")

    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="Blue")
    canvas.pack(fill="both", expand=True)
    return canvas


def animate_ball(Window, canvas, xinc, yinc):
    ball = canvas.create_oval(Ball_Start_XPosition - Ball_Radius,
                              Ball_Start_YPosition - Ball_Radius,
                              Ball_Start_XPosition + Ball_Radius,
                              Ball_Start_YPosition + Ball_Radius,
                              fill="Red", outline="Black", width=4)
    while True:
        canvas.move(ball, xinc, yinc)
        Window.update()
        time.sleep(Refresh_Sec)
        ball_pos = canvas.coords(ball)
        # unpack array to variables
        al, bl, ar, br = ball_pos
        if al < abs(xinc) or ar > Window_Width - abs(xinc):
            xinc = -xinc
        if bl < abs(yinc) or br > Window_Height - abs(yinc):
            yinc = -yinc


Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()


label = Label(master,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()
