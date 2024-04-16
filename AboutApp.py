import pathlib
import tkinter as tk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "about.ui"


class AboutApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

    def run(self):
        self.__mainwindow.mainloop()

    def get_top_frame(self):
        return self.__mainwindow


if __name__ == '__main__':
    root = tk.Tk()
    root.title("About the app")
    app = AboutApp(root)
    app.run()