from pkgutil import iter_modules
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
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
            confirmation_purchase_text = f'The price for {selection} is ${price}'
            self.confirm_purchase_screen(confirmation_purchase_text, selection, float(price))
        except:
            showwarning('Invalid option', message='Please Select a product')
            



    def confirm_purchase_screen(self, selected_item_text, product_item, item_price):
        purchase_window = Toplevel(self.window, bg=BG_Softbrown, pady=25, padx=25)
        purchase_window.title('Purchase Screen')
        purchase_window.geometry('700x300')
        label_purchase_window = Label(purchase_window, text=f'{selected_item_text}\nPlease insert money below.', bg=BG_Softbrown, pady=25, font=(FONT, 20, 'bold'))

        text_purchase_window = Text(purchase_window, font=(FONT, 25, 'bold'), height=1, width=16, pady=5)

        def exit_screen():
            purchase_window.destroy()
            purchase_window.update()


        def purchase_product(product_item, item_price):
            input_value = text_purchase_window.get("1.0", "end-1c")
            is_digit = check_amount(input_value)
            if is_digit:
                if float(input_value) < 0:
                    showwarning('Invalid input', message='Invalid input')
                elif float(input_value) < item_price:
                    showwarning('Insufficient cash', message=f'The amount deposited is not enough. You are short by ${item_price - float(input_value)}')
                else:
                    purchase_method.add_to_bought(product_item)
                    if float(input_value) == item_price:
                        showinfo('Thank you', message=f'Thank you for your purchase, enjoy your {product_item}. :)')
                    else:
                        showinfo('Thank you', message=f'Thank you for your purchase, enjoy your {product_item}.\nYour change is ${float(input_value) - item_price}.\n:)')
                    exit_screen()
            else:
                showwarning('Invalid input' , message='Please put amount required for purchase')

        purchase_button = Button(purchase_window, text='Buy', bg='#ADDDD0', highlightthickness=0, command= lambda: purchase_product(product_item, item_price), height=2, width=10, relief='flat', borderwidth=5)
        exit_button = Button(purchase_window, text='Cancel', bg='#F96666', highlightthickness=0, command=exit_screen, height=2, width=10, relief='flat', borderwidth=5)
        
        label_purchase_window.pack()
        text_purchase_window.pack()
        purchase_button.pack()
        exit_button.pack()




def check_amount(input_amount):
    try:
        value = float(input_amount)
        return True
    except ValueError:
        return False
        








        



