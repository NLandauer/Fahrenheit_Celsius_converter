#******************************************************************************
# Author:           Noelle Landauer & Casey ******
# Lab:              Lab 8
# Date:             3.5.2022
# Description:      App with Fahrenheit to Celsius converter, Celsius to Fahrenheit
#                   converter, About tab
# Input:            Fahrenheit or Celsius degrees
# Output:           Celsius or Fahrenheit degrees
# Sources:          Lab 8 specifications, lesson videos
#******************************************************************************

import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from Ftc import FtcApp
from C2F import C2FApp


# Overall app containing 3 tabs
class MainApp:

# Build MainApp GUI
    def __init__(self, master):
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

# Call outer window/frame on MainApp
        self.__mainwindow = self.__main_notebook

# Call AboutApp and add as tab to main_notebook
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About")

# Call fahrenheit to celsius App and add as tab to main_notebook
        fahr_celsius_app = FtcApp(self.__mainwindow)
        self.__main_notebook.add(fahr_celsius_app.get_top_frame(), text="Fahr to Celsius")

# Call celsius to fahrenheit
        celsius_fahr_app = C2FApp(self.__mainwindow)
        self.__main_notebook.add(celsius_fahr_app.get_top_frame(), text="Celsius to Fahr")

# Run mainwindow (outer window)
    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Temperature App")
    app = MainApp(root)
    app.run()

