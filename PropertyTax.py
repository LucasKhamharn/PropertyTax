# Aurthor: Lucas Khamharn
# Date: 20230510
# Prog: PropertyTax.py
# Descr: This program is designed to create a graphical user interface for
#        calculating and displaying the property tax and assessed value

from tkinter import *

from tkinter import messagebox 


class PropertyTax_GUI:
   
    def __init__(self):
       
        self.mainWindow = Tk()
        self.mainWindow.title('Property Tax')
        self.mainWindow.geometry('400x200')
        self.mainWindow.eval('tk::PlaceWindow . center')
        
# first row
        self.landAcreLabel = Label(self.mainWindow,
                                text = 'Enter the amount of land in acres:')
        
        self.landAcreTextBox = Entry(self.mainWindow, width = 10)
        self.landAcreLabel.grid(row = 0, column = 0)
        self.landAcreTextBox.grid(row = 0, column = 1)
        
# second row   
        self.valuePerAcreLabel = Label(self.mainWindow,
                                text = 'Enter value per acre:')
        self.valuePerAcreTextBox = Entry(self.mainWindow, width = 10)
        self.valuePerAcreLabel.grid(row = 1, column = 0)
        self.valuePerAcreTextBox.grid(row = 1, column = 1)
        
# third row      
        self.assessedValueLabel = Label(self.mainWindow,
                                text = 'Assessed Value:')
        self.calculatedAssessedValueLabel = Label(self.mainWindow, text = '')
        self.assessedValueLabel.grid(row = 2, column = 0)
        self.calculatedAssessedValueLabel.grid(row = 2, column = 1)
        
        
# fourth row
        self.propertyTaxLabel = Label(self.mainWindow,
                                text = 'Property Tax:')
        self.calculatedPropertyTaxLabel = Label(self.mainWindow, text = '')
        self.propertyTaxLabel.grid(row = 3, column = 0)
        self.calculatedPropertyTaxLabel.grid(row = 3, column = 1)
        
# buttons
        self.calcButton = Button(self.mainWindow,
                                 text = 'Calculate Assessed Value and Tax',
                                 command = self.calcButton_Click)
        self.exitButton = Button(self.mainWindow,
                                 text = 'Exit',
                                 command = self.exitButton_Click)
        self.calcButton.grid(row = 4, column = 0)
        self.exitButton.grid(row = 4, column = 1)

        
        
        # main loop
        self.mainWindow.mainloop()
        
        
    # calculation event handler
    def calcButton_Click(self):
        landAcre = float(self.landAcreTextBox.get())
        valuePerAcre = float(self.valuePerAcreTextBox.get())
        assessedValue = .6 * (landAcre * valuePerAcre)
        self.calculatedAssessedValueLabel.configure(text = '$'+format(assessedValue, '.2f'))
        propertyTax = (assessedValue / 100) * .64
        self.calculatedPropertyTaxLabel.configure(text = '$'+format(propertyTax, '.2f'))
        return
        

    
    #exit button event handler
    def exitButton_Click(self):
        response = messagebox.askyesno(title = 'Exit Confirmation',
                                       message = 'Are you sure you want to exit?')
        if response == True:
            self.mainWindow.destroy()
        return
        
def main():
    PropertyTax = PropertyTax_GUI()
    
# begin by calling main
main()
        
