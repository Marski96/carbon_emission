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
import pandas as pd

from tkinter import *

## Methods ##
def get_csv_data():

    #clear output
    output_basicdata.delete('1.0', END)

    #get input values
    country = Country_Entry.get()
    year = Year_Entry.get()
    year_specified = "Year_" + year

    #read csv
    data = pd.read_csv('data\carbon_data\organized_carbon.csv', delimiter = ';')
    df_carbon = pd.DataFrame(data, columns=['Country_Name', 'Country_Code', year_specified])
    

    #get data according to name
    #Get_data_by_country_name = df_carbon.loc[df_carbon['Country_Name'] == country] ##toimii, hakee nimenmukaan KAIKEN

    Get_data_by_country_name = df_carbon.loc[df_carbon['Country_Name']==country]

    
    output_basicdata.insert(END, Get_data_by_country_name)
    
    return  

######################################## Main screen contents #################################################################

#Define root
root = tk.Tk()
root.title('Carbon emissions')
root.geometry('1200x800')

#backgroundImage
background_image = tk.PhotoImage(file='pictures\GIF\imageForest.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#Header
header = tk.Label(root, text = 'Carbon emissions', bg='gray', width=100, font = ('Calibri, 16'))
header.pack()

#Upperframe
upperframe = tk.Frame(root, bg='gray')
upperframe.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

#Output box
output_basicdata = Text(root, bg='gray')
output_basicdata.place(relx=0.02, rely=0.28, relwidth=0.3, relheight=0.1)

#Output box
output_development = Text(root, bg='gray')
output_development.place(relx=0.02, rely=0.40, relwidth=0.3, relheight=0.1)

#How to use text
how_to_use = tk.Label(root, text = 'How to use:\n\n This program shows amount of carbon\n dioxide emissions from year 1960 to 2014.\n You are able to search results by using year and country')
how_to_use.place(relwidth=0.3, relheight=0.16, relx=0.02, rely=0.068 )


#Search#################################################################
#Labels
Year_Label = tk.Label(root, text = 'Year: ')
Year_Label.place(relwidth=0.05, relheight=0.05, relx=0.35, rely=0.08)
Country_Label = tk.Label(root, text = 'Country: ')
Country_Label.place(relwidth=0.05, relheight=0.05, relx=0.35, rely=0.14)

#Entries'

Year_Entry = tk.Entry(root, textvariable='year')
Year_Entry.pack()
Year_Entry.place(relwidth=0.3, relheight=0.05, relx=0.4, rely=0.08)

Country_Entry = tk.Entry(root, textvariable='country')
Country_Entry.pack()
Country_Entry.place(relwidth=0.3, relheight=0.05, relx=0.4, rely=0.14)

#Search button
Search_Button = tk.Button(root, text = 'Search', command=get_csv_data)
Search_Button.place(relwidth=0.15, relheight=0.1, relx=0.72, rely=0.085)
##########################################################################

#load the screen
root.mainloop()