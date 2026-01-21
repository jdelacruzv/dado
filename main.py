from gui import Gui
from controller import Controller


class Main:
    """
    Main application entry point. Handles GUI initialization and
    ties the GUI with the Controller.
    """
    def __init__(self):
        self.gui = Gui()
        self.controller = Controller(self.gui)
        # Asegurarse de que la Vista tenga una referencia al Controlador
        self.gui.set_controller(self.controller)

    def start(self):
        """
        Starts the GUI mainloop.
        """
        print("Iniciando la aplicación GUI...")
        self.gui.start_mainloop()
        print("Aplicación GUI finalizada.")


if __name__ == '__main__':
    app = Main()
    app.start()
