#Author: Jani Maaranen
#Date: 16.11.2019

###################################################
#This is task provided by Reaktor, which shows data
#from .csv file, which contains carbon emissions
#from year 1960 to 2014. Application shows data in
#table format and also graphs. You can search data
#using year and country.
###################################################

import tkinter as tk
import numpy as np
import pandas as pd

#use ctrl + ' to comment

def load_screen():
#Create Window
    root= tk.Tk()
    root.title('Carbon emissions')
    root.geometry('1200x800')

#Main screen contents

    #Header
    header = tk.Label(root, text = "Carbon emissions", bg="gray", width=100, font = ("Calibri, 16"))
    header.pack()

    #Canvases
    canvas = tk.Canvas(root, height=200, width=200)
    canvas.pack()

    #Upperframe
    upperframe = tk.Frame(root, bg='gray')
    upperframe.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

    #Middleframe
    middleframe = tk.Frame(root, bg='gray')
    middleframe.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.65)

    #How to use text
    how_to_use = tk.Label(root, text = "How to use:\n\n This program shows amount of carbon\n dioxide emissions from year 1960 to 2014.\n You are able to search results by using year and country")
    how_to_use.place(relwidth=0.3, relheight=0.16, relx=0.02, rely=0.068 )

    #Search
    Search_Year = ""
    Search_Country = ""

    Year_Label = tk.Label(root, text = 'Year: ')
    Year_Label.place(relwidth=0.05, relheight=0.05, relx=0.35, rely=0.08)
    Year_Entry = tk.Entry(root, textvariable = Search_Year)
    Year_Entry.place(relwidth=0.3, relheight=0.05, relx=0.4, rely=0.08)


    Country_Label = tk.Label(root, text = 'Country: ')
    Country_Label.place(relwidth=0.05, relheight=0.05, relx=0.35, rely=0.14)
    Country_Entry = tk.Entry(root, textvariable = Search_Country)
    Country_Entry.place(relwidth=0.3, relheight=0.05, relx=0.4, rely=0.14)
    
    Search_Button = tk.Button(root, text = 'Search')
    Search_Button.place(relwidth=0.15, relheight=0.1, relx=0.72, rely=0.085)

    #load the screen
    root.mainloop()

    
def load_csv_data():
    data = pd.read_csv('data\carbon_data\organized_carbon.csv', delimiter = ';')
    #print(data.head(10))
    #column_test = data.loc[[0, 1, 2, 3, 4, 5], :]
    #column_test = data.loc[0:2, :]

load_screen()
