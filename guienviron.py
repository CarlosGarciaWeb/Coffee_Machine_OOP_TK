import re
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from purchase import Resources


# purchase section

purchase_method = Resources()


#Colors
BG_Softbrown = '#DFD3C3'

BG_Button = '#472D2D'

Text_color = '#2C3639'

green_button = '#ADDDD0'
red_button = '#F96666'

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

        resource_window_button = Button(text='Resources', highlightthickness=0, command=self.resource_screen, font=(FONT, 24, 'bold'), fg=BG_Button, width=25)
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




    def resource_screen(self):
        available_resources = purchase_method.view_resources()
        resource_window = Toplevel(self.window, bg=BG_Softbrown, padx=25, pady=25)
        resource_window.title('Resources')
        resource_window.geometry('1250x400')
        col_variation = 1
        row_val = 1
        row_key = 2
        button_resource_row = 3
        button_resource_col_add = 1
        button_resource_col_dec = 2
        # for resource_key, resource_value in available_resources.items():
        #     if resource_key == 'Water' or resource_key == 'Milk':
        #         resource_label_value = Label(resource_window, text=f'{resource_value} ml', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        #     elif resource_key == 'Coffee Beans' or resource_key == 'Cocoa':
                
        #         resource_label_value = Label(resource_window, text=f'{resource_value} gr', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        #     else:
        #         resource_label_value = Label(resource_window, text=f'${resource_value}', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        #     if len(resource_key.split()) == 2:
        #         resource_label_key = Label(resource_window, text=resource_key.split()[0], font=(FONT, 24, 'bold'), bg=BG_Softbrown, padx=35, pady=15)
        #     else:
        #         resource_label_key = Label(resource_window, text=resource_key, font=(FONT, 24, 'bold'), bg=BG_Softbrown, padx=35, pady=15)
        #     resource_label_value.grid(column=col_variation, row=row_val, columnspan=2)
            
        #     resource_label_key.grid(column=col_variation, row=row_key, columnspan=2)
        #     col_variation += 2

        resource_label_value_water = Label(resource_window, text=f'{available_resources["Water"]} ml', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        resource_label_value_water.grid(column=col_variation, row=row_val, columnspan=2)
        resource_label_key_water = Label(resource_window, text='Water', font=(FONT, 24, 'bold'), bg=BG_Softbrown, padx=35, pady=15)
        resource_label_key_water.grid(column=col_variation, row=row_key, columnspan=2)

        resource_label_value_milk = Label(resource_window, text=f'{available_resources["Milk"]} ml', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        resource_label_value_milk.grid(column=col_variation+2, row=row_val, columnspan=2)
        resource_label_key_milk = Label(resource_window, text='Milk', font=(FONT, 24, 'bold'), bg=BG_Softbrown, padx=35, pady=15)
        resource_label_key_milk.grid(column=col_variation+2, row=row_key, columnspan=2)

        resource_label_value_coffee = Label(resource_window, text=f'{available_resources["Coffee Beans"]} gr', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        resource_label_value_coffee.grid(column=col_variation+4, row=row_val, columnspan=2)
        resource_label_key_coffee = Label(resource_window, text='Coffee', font=(FONT, 24, 'bold'), bg=BG_Softbrown, padx=35, pady=15)
        resource_label_key_coffee.grid(column=col_variation+4, row=row_key, columnspan=2)

        resource_label_value_cocoa = Label(resource_window, text=f'{available_resources["Cocoa"]} gr', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        resource_label_value_cocoa.grid(column=col_variation+6, row=row_val, columnspan=2)
        resource_label_key_cocoa = Label(resource_window, text='Cocoa', font=(FONT, 24, 'bold'), bg=BG_Softbrown, padx=35, pady=15)
        resource_label_key_cocoa.grid(column=col_variation+6, row=row_key, columnspan=2)

        resource_label_value_cash = Label(resource_window, text=f'${available_resources["Cash"]}', font=(FONT, 24, 'bold'), bg=BG_Softbrown, pady=15, padx=35)
        resource_label_value_cash.grid(column=col_variation+8, row=row_val, columnspan=2)
        resource_label_key_cash = Label(resource_window, text='Cash', font=(FONT, 24, 'bold'), bg=BG_Softbrown, padx=35, pady=15)
        resource_label_key_cash.grid(column=col_variation+8, row=row_key, columnspan=2)


            
        add_button_water = Button(resource_window, text='+', font=(FONT, 24, 'bold'), bg=green_button, command=lambda: add_refresh_label('Water', purchase_method.increments['Water'], resource_label_value_water))
        decrease_button_water = Button(resource_window, text='-', font=(FONT, 24, 'bold'), bg=red_button)
        add_button_water.grid(row=button_resource_row, column=button_resource_col_add)
        decrease_button_water.grid(row=button_resource_row, column=button_resource_col_dec)

        add_button_milk = Button(resource_window, text='+', font=(FONT, 24, 'bold'), bg=green_button, command=lambda: add_refresh_label('Milk', purchase_method.increments['Milk'], resource_label_value_milk))
        decrease_button_milk = Button(resource_window, text='-', font=(FONT, 24, 'bold'), bg=red_button)
        add_button_milk.grid(row=button_resource_row, column=button_resource_col_add+2)
        decrease_button_milk.grid(row=button_resource_row, column=button_resource_col_dec+2)

        add_button_coffee = Button(resource_window, text='+', font=(FONT, 24, 'bold'), bg=green_button, command=lambda: add_refresh_label('Coffee Beans', purchase_method.increments['Coffee Beans'], resource_label_value_coffee))
        decrease_button_coffee = Button(resource_window, text='-', font=(FONT, 24, 'bold'), bg=red_button)
        add_button_coffee.grid(row=button_resource_row, column=button_resource_col_add+4)
        decrease_button_coffee.grid(row=button_resource_row, column=button_resource_col_dec+4)

        add_button_cocoa = Button(resource_window, text='+', font=(FONT, 24, 'bold'), bg=green_button, command=lambda: add_refresh_label('Cocoa', purchase_method.increments['Cocoa'], resource_label_value_cocoa))
        decrease_button_cocoa = Button(resource_window, text='-', font=(FONT, 24, 'bold'), bg=red_button)
        add_button_cocoa.grid(row=button_resource_row, column=button_resource_col_add+6)
        decrease_button_cocoa.grid(row=button_resource_row, column=button_resource_col_dec+6)

        add_button_cash = Button(resource_window, text='+', font=(FONT, 24, 'bold'), bg=green_button, command=lambda: add_refresh_label('Cash', purchase_method.increments['Cash'], resource_label_value_cash))
        decrease_button_cash = Button(resource_window, text='-', font=(FONT, 24, 'bold'), bg=red_button)
        add_button_cash.grid(row=button_resource_row, column=button_resource_col_add+8)
        decrease_button_cash.grid(row=button_resource_row, column=button_resource_col_dec+8)
        


        def add_refresh_label(resource, qty, label_item):
            purchase_method.add_resource(resource, qty)
            new_qty_resources = purchase_method.view_resources()
            if resource == 'Coffee' or resource == 'Cocoa':
                label_item.config(text=f'{new_qty_resources[resource]} gr')
            elif resource == 'Water' or resource == 'Milk':
                label_item.config(text=f'{new_qty_resources[resource]} ml')
            else:
                label_item.config(text=f'${new_qty_resources[resource]}')



        



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

        purchase_button = Button(purchase_window, text='Buy', bg=green_button, highlightthickness=0, command= lambda: purchase_product(product_item, item_price), height=2, width=10, relief='flat', borderwidth=5)
        exit_button = Button(purchase_window, text='Cancel', bg=red_button, highlightthickness=0, command=exit_screen, height=2, width=10, relief='flat', borderwidth=5)
        
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
        








        



