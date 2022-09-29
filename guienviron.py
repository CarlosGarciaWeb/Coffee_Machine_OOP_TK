import tkinter as tk
from tkinter import *
from tkinter.messagebox import showwarning
from turtle import bgcolor
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


        buy_button = Button(text='Buy', highlightthickness=0, command=self.select_item, font=(FONT, 25, 'bold'), fg=BG_Button, bg=BG_Softbrown)
        buy_button.grid(column=1, row=4)


            

        row_counter = 0

        for name, price in purchase_method.items_machine.items():
            product_button = Radiobutton(text=f'{name} - ${price}', highlightthickness=0, font=(FONT, 24, 'bold'), fg=BG_Button, bg=BG_Softbrown, variable=self.var, value=name)   
            product_button.grid(column=1, row=row_counter)
            row_counter += 1    

        self.var.set(str(list(purchase_method.items_machine.values())[0]))


        # Any window that opens must be behind this line of code
        self.window.mainloop()

    def select_item(self):
        try:
            selection = self.var.get()
            price = purchase_method.items_machine[selection]
            text_test = f'The price for {selection} is ${price}'
            self.confirm_purchase_screen(text_test)
        except:
            showwarning('Invalid option', message='Please Select a product')
            



    def confirm_purchase_screen(self, selected_item_text):
        purchase_window = Toplevel(self.window, bg=BG_Softbrown, pady=25, padx=25)
        purchase_window.title('Purchase Screen')
        purchase_window.geometry('500x200')
        Label(purchase_window, text=f'This is the purchase confirmation screen. {selected_item_text}', bg=BG_Softbrown, pady=25).pack()

        def exit_screen():
                    purchase_window.destroy()
                    purchase_window.update()


        exit_button = Button(purchase_window, text='Cancel', bg='#F96666', highlightthickness=0, command=exit_screen)
        exit_button.pack()

        








        



