# Noelle Landauer
import pathlib
import tkinter as tk
import tkinter.messagebox as mb
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "FtC.ui"

# Code from pygubu-designer to build app window from FtC.ui file
class FtcApp:

# constructs app window
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_level', master)
        builder.connect_callbacks(self)

        self.__fahr_entry = builder.get_object('fahr_entry', master)
        self.__celsius_entry_variable = builder.get_variable('celsius_entry_variable')

# runs the app window
    def run(self):
        self.__mainwindow.mainloop()

# Calculation fahrenheit to celsius
# try/except error in case non-number is entered
    def calculate(self):
        try:
            fahr = float(self.__fahr_entry.get())
            celsius = round(((fahr - 32) * 5 / 9), 1)
            self.__celsius_entry_variable.set(str(celsius))
        except ValueError:
            mb.showerror(title="Error Calculating Celsius",
                         message="Fahrenheit must be a decimal number. Please try again.")

# Returns this app to, in order to run simultaneously with other tabs in same window
    def get_top_frame(self):
        return self.__mainwindow

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Fahrenheit to Celsius Converter")
    app = FtcApp(root)
    app.run()

