#main

#from calculator import Calculator
from tkinter import *

CANVAS_WIDTH  = 300
CANVAS_HEIGHT = 600
CANVAS_COLOR  = "light gray"

DISPLAY_WIDTH = 0.97
DISPLAY_HEIGHT= 0.10
DISPLAY_X     = 0.50
DISPLAY_Y     = 0.02
DISPLAY_ANCHOR= 'n'
DISPLAY_COLOR = "#E4F3FA"

BUTTONfRAME_WIDTH  = 0.97
BUTTONfRAME_HEIGHT = 0.84
BUTTONfRAME_X      = 0.50
BUTTONfRAME_Y      = 0.14
BUTTONfRAME_ANCHOR = 'n'
BUTTONfRAME_COLOR  = "light gray"

SINGLEBUTTON_WIDTH = 50
SINGLEBUTTON_HEIGHT= 40
SINGLEBUTTON_X     = 0.00
SINGLEBUTTON_Y     = 0.00
SINGLEBUTTON_ANCHOR= 'nw'
SINGLEBUTTON_COLOR = "blue"

DOUBLEBUTTON_WIDTH = 105
DOUBLEBUTTON_HEIGHT= 40
DOUBLEBUTTON_X     = 0.00
DOUBLEBUTTON_Y     = 0.00
DOUBLEBUTTON_ANCHOR= 'nw'
DOUBLEBUTTON_COLOR = "blue"

BUTTON_FONT = 40
BUTTON_GAP  = 5

BUTTON_TEXT=["MC", "MR", "MS", "M+", "M-", "AC", "C", "+/-", "^2", "^y", "7", "8", "9", "/", "sqrt", "4", "5", "6", "x", "1/x", "1", "2", "3", "-", "=", "0", ".", "+"]

def main():
  root = Tk()

  canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=CANVAS_COLOR)
  canvas.pack()

  display_frame = Frame(canvas, bg=DISPLAY_COLOR)
  display_frame.place(relx=DISPLAY_X, rely=DISPLAY_Y , relwidth=DISPLAY_WIDTH, relheight=DISPLAY_HEIGHT, anchor=DISPLAY_ANCHOR)

  button_frame = Frame(canvas, bg=BUTTONfRAME_COLOR)
  button_frame.place(relx=BUTTONfRAME_X, rely=BUTTONfRAME_Y , relwidth=BUTTONfRAME_WIDTH, relheight=BUTTONfRAME_HEIGHT, anchor=BUTTONfRAME_ANCHOR)

  # button1 = Button(button_frame, text="MC", bg="gray", font=BUTTON_FONT)
  # button1.place(relx=SINGLEBUTTON_X, rely=SINGLEBUTTON_Y, width=SINGLEBUTTON_WIDTH, height=SINGLEBUTTON_HEIGHT)

  # button2 = Button(button_frame, text="MR", bg="gray", font=BUTTON_FONT)
  # button2.place(relx=SINGLEBUTTON_X + 0.19, rely=SINGLEBUTTON_Y, width=SINGLEBUTTON_WIDTH, height=SINGLEBUTTON_HEIGHT)

  # button3 = Button(button_frame, text="MR", bg="gray", font=BUTTON_FONT)
  # button3.place(relx=DOUBLEBUTTON_X, rely=DOUBLEBUTTON_Y + 0.09, width=DOUBLEBUTTON_WIDTH, height=DOUBLEBUTTON_HEIGHT)

  button1 = Button(button_frame, text="MC", bg="gray", font=BUTTON_FONT)
  button1.grid(column=0, row=0, ipadx=4, ipady=4, padx=2, pady=1.5)

  button2 = Button(button_frame, text="MR", bg="gray", font=BUTTON_FONT)
  button2.grid(column=1, row=0, ipadx=4, ipady=4, padx=2, pady=1.5)

  button3 = Button(button_frame, text="MS", bg="gray", font=BUTTON_FONT)
  button3.grid(column=2, row=0, columnspan=1, ipadx=4.5, ipady=4, padx=2, pady=1.5)

  button4 = Button(button_frame, text="M+", bg="gray", font=BUTTON_FONT)
  button4.grid(column=3, row=0, columnspan=1, ipadx=5.5, ipady=4, padx=2, pady=1.5)

  button5 = Button(button_frame, text="M-", bg="gray", font=BUTTON_FONT)
  button5.grid(column=4, row=0, columnspan=1, ipadx=8, ipady=4, padx=2, pady=1.5)

  long_button = Button(button_frame, text="  =  ", bg="gray", font=BUTTON_FONT)
  long_button.grid(column=0, row=1, columnspan=2, ipadx=28, ipady=4, padx=1.5, pady=3)



  root.mainloop()

if __name__ == 'main':
  main()
