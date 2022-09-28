from email.mime import image
import tkinter as tk
from tkinter import *
from turtle import width



#Colors
BG_Softbrown = '#DFD3C3'

BG_Button = '#472D2D'

Text_color = '#2C3639'

FONT = 'Courier'

# UI SET UP
class GuiEnvironment():

    def __init__(self):
        self.window = Tk()
        self.initate_gui()

    def initate_gui(self):

        self.window.title('Coffee Machine')

        self.window.config(padx=100, pady=50, bg=BG_Softbrown)

        title_gui = Label(text='Coffee Machine', font=(FONT, 35, 'bold'), bg=BG_Softbrown)
        title_gui.grid(column=0, row=0)

        canva = Canvas(width=600, height=600, bg=BG_Softbrown, highlightthickness=0)
        coffee_machine_img = PhotoImage(file='coffee machine img.png')
        canva.create_image(200, 200 ,image=coffee_machine_img)

        canva.grid(column=0, row=1, rowspan=3)

        # See resources screen

        resource_window_button = Button(text='Resources', highlightthickness=0, command=None, font=(FONT, 24, 'bold'), fg=BG_Button, width=25)
        resource_window_button.grid(column=0, row=4)


        self.window.mainloop()



