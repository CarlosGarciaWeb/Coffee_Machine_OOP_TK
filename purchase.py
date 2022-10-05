import datetime
import json
import os
from re import T
from tkinter import messagebox

class Resources():

    def __init__(self):
        self.coffee = {'Price': 2.50, 'Water': 5, 'Milk': 0, 'Coffee': 15}
        self.flat_wite = {'Price': 3.25, 'Water': 2.5, 'Milk': 2.5, 'Coffee': 15}
        self.cappucino = {'Price': 3.00, 'Water': 3.0, 'Milk': 2.0, 'Coffee': 15}
        self.moccacino = {'Price': 3.50, 'Water': 3.0, 'Milk': 2.0, 'Coffee': 7.5, 'Cocoa': 7.5}
        self.items_machine = {'Coffee':self.coffee['Price'], 'Flat White': self.flat_wite['Price'], 'Cappucino': self.cappucino['Price'], 'Moccacino': self.moccacino['Price']}
        self.resources = {'Water': 0, 'Milk': 0, 'Coffee': 0, 'Cocoa': 0, 'Cash': 0}
        self.increments = {k: v for k, v in self.resources.items()}
        self.res_limit = {k: v for k, v in self.resources.items()}
        self.cash = 0
        self.items_bought = {key: 0 for key, _ in self.items_machine.items()}
        self.date = datetime.datetime.today()

    
    def add_to_bought(self, key):
        self.items_bought[key] += 1
        print(self.items_bought)
        self.add_cash(key)

    def add_cash(self, key):
        price_product = self.items_machine[key]
        self.cash += price_product
        print(self.cash)

    def view_resources(self):
        self.establish_limit_increments()
        if not os.path.exists('resource.json'):
            with open('resource.json', 'w') as json_file_output:
                json.dump(self.resources, json_file_output)
        else:
            with open('resource.json') as json_file_output:
                self.resources = json.load(json_file_output)
        return self.resources


    def add_resource(self, resource, qty):
        data_resources = self.view_resources()
        if data_resources[resource] < self.res_limit[resource]:
            data_resources[resource] += qty
            with open('resource.json', 'w') as jsonfile:
                json.dump(data_resources, jsonfile)
        else:
            messagebox.showwarning(title='Resource Limit Reached', message=f'Capacity for {resource} is full')
            

        

    def establish_limit_increments(self):
        for k in self.increments.keys():
            if k == 'Water' or k =='Milk':
                self.increments[k] = 10
                self.res_limit[k] = 20
            elif k == 'Coffee' or k == 'Cocoa':
                self.increments[k] = 5
                self.res_limit[k] = 20
            else:
                self.increments[k] = 10
                self.res_limit[k] = 100
     
        

    
    def dec_resource(self, resource, qty):
        data_resources = self.view_resources()
        if data_resources[resource] > 0:
            data_resources[resource] -= qty
            with open('resource.json', 'w') as jsonfile:
                json.dump(data_resources, jsonfile)
        else:
            messagebox.showwarning(title='Resource unavailable', message=f'{resource} is empty, cannot remove more.')



    