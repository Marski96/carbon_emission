#Author: Jani Maaranen
#Date: 16.11.2019

###################################################
#This is task provided by Reaktor, which shows data
#from .csv file, which contains carbon emissions
#from year 1960 to 2014. Application shows data
#using pandas and prints it to tkinter.
###################################################

import tkinter as tk
import pandas as pd
import os as os

from tkinter import *

## Methods ##
def get_csv_data():

    #clear output always at first
    output_basicdata.delete('1.0', END)
    output_development.delete('1.0', END)
    output_population.delete('1.0', END)

    #get input values
    country = Country_Entry.get()
    year = Year_Entry.get()
    year_specified = "Year_" + year

    #read csv
    carbon_data = pd.read_csv('data\carbon_data\organized_carbon.csv', delimiter= ';', decimal=',')
    population_data = pd.read_csv('data\population_data\organized_population.csv', delimiter= ';', decimal=',')

    #Get basic values
    df_carbon = pd.DataFrame(carbon_data, columns=['Country_Name', 'Country_Code', year_specified])
    Get_data_by_country_nameCARBON = df_carbon.loc[df_carbon['Country_Name']==country]
    carbon_tostring = Get_data_by_country_nameCARBON.to_string(index=False) #printing dataframe as a string and disapling index

    #Get population data
    df_population = pd.DataFrame(population_data, columns=['Country_Name', year_specified])
    Get_data_by_country_namePOPULATION = df_population.loc[df_population['Country_Name']==country]
    population_tostring = Get_data_by_country_namePOPULATION.to_string(index=False) #printing dataframe as a string and disapling index
    
    #Calculate development
    df_carbon_development = pd.DataFrame(carbon_data, columns=['Year_1960', 'Year_1970', 'Year_1980', 'Year_1990', 'Year_2000', 'Year_2014'])
    carbon_development_data = df_carbon_development.loc[df_carbon['Country_Name']==country]
    carbon_development_tostring = carbon_development_data.to_string(index=False) #printing dataframe as a string and disapling index

    #output data to program
    output_basicdata.insert(END, carbon_tostring)
    output_development.insert(END, carbon_development_tostring)
    output_population.insert(END, population_tostring)
    return

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


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
header = tk.Label(root, text = 'Carbon emissions', bg='gray', width=100, font = ('Calibri, 18'))
header.pack()

#Upperframe
upperframe = tk.Frame(root, bg='gray')
upperframe.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

#Output box basicdata
output_basicdata = Text(root, bg='gray')
output_basicdata.place(relx=0.3, rely=0.30, relwidth=0.6, relheight=0.1)

#Output box development
output_development = Text(root, bg='gray')
output_development.place(relx=0.3, rely=0.45, relwidth=0.6, relheight=0.1)

#Ouput box population
output_population = Text(root, bg='gray')
output_population.place(relx=0.3, rely=0.60, relwidth=0.6, relheight=0.1)

#How to use text
how_to_use = tk.Label(root, text = 'How to use:\n\n This program shows amount of carbon\n dioxide emissions from year 1960 to 2014.\n You are able to search results by using year and country\n\n Results are in (kt)')
how_to_use.place(relwidth=0.3, relheight=0.16, relx=0.02, rely=0.068 )

#Labels
Output_basicdata_Label = tk.Label(root, text ='Results', bg='gray', font = ('Calibri, 16'))
Output_basicdata_Label.place(relx=0.075, rely=0.30, relwidth=0.18, relheight=0.1)
Output_development_Label = tk.Label(root, text ='Development', bg='gray', font = ('Calibri, 16'))
Output_development_Label.place(relx=0.075, rely=0.45, relwidth=0.18, relheight=0.1)
Output_population_Label = tk.Label(root, text = 'Population', bg='gray', font = ('Calibri, 16'))
Output_population_Label.place(relx=0.075, rely=0.60, relwidth=0.18, relheight=0.1)
Country_Label = tk.Label(root, text = 'Country: ')
Country_Label.place(relwidth=0.05, relheight=0.05, relx=0.35, rely=0.08)
Year_Label = tk.Label(root, text = 'Year: ')
Year_Label.place(relwidth=0.05, relheight=0.05, relx=0.35, rely=0.14)

#Entries
Country_Entry = tk.Entry(root, textvariable='country')
Country_Entry.pack()
Country_Entry.place(relwidth=0.3, relheight=0.05, relx=0.4, rely=0.08)
Year_Entry = tk.Entry(root, textvariable='year')
Year_Entry.pack()
Year_Entry.place(relwidth=0.3, relheight=0.05, relx=0.4, rely=0.14)

#Buttons
Search_Button = tk.Button(root, text = 'Search', command=get_csv_data)
Search_Button.place(relwidth=0.10, relheight=0.05, relx=0.72, rely=0.14)
Reset_Button = tk.Button(root, text = 'Restart program', command=restart_program)
Reset_Button.place(relwidth=0.10, relheight=0.042, relx=0, rely=0)

#load the screen
root.mainloop()