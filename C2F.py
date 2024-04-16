# Casey

import pathlib
import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import tkinter.messagebox as mb

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "C2F.ui"

# C2FApp implements a calculator that converts degrees celsius to degrees fahrenheit
class C2FApp:
    def __init__(self, master=None):
        # Builds ktinker interface from C2F.ui
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        self.conversion_label_variable = None
        self.fahrenheit_entry_variable = None
        builder.import_variables(self, ['conversion_label_variable', 'fahrenheit_entry_variable'])

        # accesses entries for calculation()
        self.__celsius_entry = builder.get_object('celsius_entry', master)
        self.__fahrenheit_entry_variable = builder.get_variable('fahrenheit_entry_variable')

    # returns GUI top frame to mainApp to be displayed in tab
    def get_top_frame(self):
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()

    # calculates c > f and validates user input
    def calculate(self):
        try:
            celsius = float(self.__celsius_entry.get())
            fahrenheit = float(celsius * 1.8) + 32
            self.__fahrenheit_entry_variable.set("{:.1f}".format(fahrenheit))
        except ValueError:
            mb.showerror(title="Error.", message="Please enter a valid number. Please try again.")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Celsius to Fahrenheit")
    app = C2FApp(root)
    app.run()