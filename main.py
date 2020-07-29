#main
from calculator import Calculator
from tkinter import *

class Application(Tk):

    def __init__(self, color_theme="light"):

        self.color_theme = color_theme #dark mode support in future release

        self.CANVAS_WIDTH  = 400
        self.CANVAS_HEIGHT = 500
        self.CANVAS_COLOR  = "dark gray"
        self.DISPLAY_WIDTH = 0.96
        self.DISPLAY_HEIGHT= 0.15
        self.DISPLAY_X     = 0.50
        self.DISPLAY_Y     = 0.02
        self.DISPLAY_ANCHOR= 'n'
        self.DISPLAY_COLOR = "#E4F3FA"
        self.BUTTONfRAME_WIDTH  = 0.96
        self.BUTTONfRAME_HEIGHT = 0.84
        self.BUTTONfRAME_X      = 0.50
        self.BUTTONfRAME_Y      = 0.20
        self.BUTTONfRAME_ANCHOR = 'n'
        self.BUTTONfRAME_COLOR  = "dark gray"
        self.SINGLEBUTTON_WIDTH = 50
        self.SINGLEBUTTON_HEIGHT= 40
        self.SINGLEBUTTON_X     = 0.00
        self.SINGLEBUTTON_Y     = 0.00
        self.SINGLEBUTTON_ANCHOR= 'nw'
        self.SINGLEBUTTON_COLOR = "light gray"
        self.DOUBLEBUTTON_WIDTH = 105
        self.DOUBLEBUTTON_HEIGHT= 40
        self.DOUBLEBUTTON_X     = 0.00
        self.DOUBLEBUTTON_Y     = 0.00
        self.DOUBLEBUTTON_ANCHOR= 'nw'
        self.DOUBLEBUTTON_COLOR = "light gray"
        self.BUTTON_FONT = 40
        self.BUTTON_GAP  = 5
        self.BUTTON_LABELS =["MC", "MR", "MS", "M+", "M-",
                        "AC", "C", "+/-", "^2", "^y",
                        "7", "8", "9", "/", "sqrt",
                        "4", "5", "6", "x", "1/x",
                        "1", "2", "3", "-", "=",
                        "0", ".", "+"]

    def setButtons():
        calc = Calculator()
        root = Tk()
        root.grid_rowconfigure(1, weight=1)
    
        canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=CANVAS_COLOR)
        canvas.place(relx=0.5, rely=0.0 , relwidth=1, relheight=1, anchor=DISPLAY_ANCHOR)
    
        display_frame = Frame(canvas, bg=DISPLAY_COLOR)
        display_frame.place(relx=DISPLAY_X, rely=DISPLAY_Y , relwidth=DISPLAY_WIDTH, relheight=DISPLAY_HEIGHT, anchor=DISPLAY_ANCHOR)
    
        display_label = Label(display_frame, text = "0", font=10, bg=DISPLAY_COLOR)
        display_label.place(relx=DISPLAY_X, rely=0.95 , relwidth=0.95, relheight=0.95, anchor='sw')
    
        button_frame = Frame(canvas, bg=BUTTONfRAME_COLOR)
        button_frame.place(relx=BUTTONfRAME_X, rely=BUTTONfRAME_Y , relwidth=BUTTONfRAME_WIDTH, relheight=BUTTONfRAME_HEIGHT, anchor=BUTTONfRAME_ANCHOR)
    
        buttons = {}
    
        for button_text in BUTTON_LABELS:
    
            current_button = Button(button_frame, text=button_text, bg=SINGLEBUTTON_COLOR, font=BUTTON_FONT)
            buttons[current_button] = button_text
    
        row_count, column_count = 1, 1
    
        for button in buttons:
            if(buttons[button] == "0"):
                button.grid(column=1, row=6, columnspan=2, ipadx=45, ipady=5, padx=15, pady=1.5)
                column_count += 1
    
            if(buttons[button] == "MR"):
                button.grid(column=column_count, row=row_count, ipadx=3, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "MS"):
                button.grid(column=column_count, row=row_count, ipadx=2.5, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "M+"):
                button.grid(column=column_count, row=row_count, ipadx=4.5, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "M-"):
                button.grid(column=column_count, row=row_count, ipadx=7, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "AC"):
                button.grid(column=column_count, row=row_count, ipadx=4, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "C"):
                button.grid(column=column_count, row=row_count, ipadx=4.5, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "+/-"):
                button.grid(column=column_count, row=row_count, ipadx=5.5, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "^2"):
                button.grid(column=column_count, row=row_count, ipadx=8, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "^y"):
                button.grid(column=column_count, row=row_count, ipadx=8, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "sqrt"):
                button.grid(column=column_count, row=row_count, ipadx=0, ipady=0, padx=1.5, pady=1.5)
    
            if(buttons[button] == "/"):
                button.grid(column=column_count, row=row_count, ipadx=10, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "x"):
                button.grid(column=column_count, row=row_count, ipadx=8, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "-"):
                button.grid(column=column_count, row=row_count, ipadx=10, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "+"):
                button.grid(column=column_count, row=row_count, ipadx=11, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "1/x"):
                button.grid(column=column_count, row=row_count, ipadx=4, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "."):
                button.grid(column=column_count, row=row_count, ipadx=14, ipady=2, padx=1.5, pady=1.5)
    
            if(buttons[button] == "="):
                button.grid(column=column_count, row=row_count, rowspan=2, ipadx=10, ipady=20, padx=1.5, pady=1.5)
    
            elif(buttons[button] is not None):
                button.grid(column=column_count, row=row_count, ipadx=6, ipady=2, padx=1.5, pady=1.5)
    
            else:
                button.grid(column=column_count, row=row_count, ipadx=2, ipady=2, padx=1.5, pady=1.5)
    
            column_count += 1
    
            if column_count > 5:
                column_count = 1
                row_count += 1
    
    
        root.mainloop()
