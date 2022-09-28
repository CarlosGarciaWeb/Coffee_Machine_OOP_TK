from select import select
import tkinter as tk
from tkinter import *
from tokenize import String
from turtle import width
from purchase import Prices


# purchase section

purchase_method = Prices()


#Colors
BG_Softbrown = '#DFD3C3'

BG_Button = '#472D2D'

Text_color = '#2C3639'

FONT = 'Courier'





# UI SET UP
class GuiEnvironment():

    def __init__(self):
        self.window = Tk()
        self.var = StringVar()
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

        coffee_button = Radiobutton(text='Coffee', highlightthickness=0,  font=(FONT, 24, 'bold'), fg=BG_Button, bg=BG_Softbrown, variable= self.var, value='Coffee')
        coffee_button.grid(column=1, row=0)
        flat_white_button = Radiobutton(text='Flat White', highlightthickness=0,  font=(FONT, 25, 'bold'), fg=BG_Button, bg=BG_Softbrown, variable= self.var, value='Flat White')
        flat_white_button.grid(column=1, row=1)
        cappucino_button = Radiobutton(text='Cappucino', highlightthickness=0,  font=(FONT, 25, 'bold'), fg=BG_Button, bg=BG_Softbrown, variable= self.var, value='Cappucino')
        cappucino_button.grid(column=1, row=2)
        moccacino_button = Radiobutton(text='Moccacino', highlightthickness=0,  font=(FONT, 25, 'bold'), fg=BG_Button, bg=BG_Softbrown, variable= self.var, value='Moccacino')
        moccacino_button.grid(column=1, row=3)
        buy_button = Button(text='Buy', highlightthickness=0, command=self.select_item, font=(FONT, 25, 'bold'), fg=BG_Button, bg=BG_Softbrown)
        buy_button.grid(column=1, row=4)       


        self.window.mainloop()

    def select_item(self):
        selection = self.var.get()
        price = purchase_method.items[selection]
        print(f'The price for {selection} is {price}')


        



