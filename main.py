from dado import Dado
from gui import Gui


class Main:
    """Class that works as the application controller"""
    def __init__(self):
        self.dado = Dado()
        self.gui = Gui(self)


    def call_throw_dado(self):
        """Call print_value() method Dado class"""
        return self.dado.print_value()


    def call_play_sound(self):
        """Call play_sound() method Dado class"""
        return self.dado.play_sound


    def play_dado(self):
        """Displays the frame according to the number of the selected dado"""
        self.gui.destroy_frame_dados()
        opt = self.gui.option_dados.get()
        if opt == 1:
            self.gui.create_frame_dados1()
        if opt == 2:
            self.gui.create_frame_dados2()
        if opt == 3:
            self.gui.create_frame_dados3()
        if opt == 4:
            self.gui.create_frame_dados4()
        if opt == 5:
            self.gui.create_frame_dados5()
        if opt == 6:
            self.gui.create_frame_dados6()


    def main_gui(self):
        """Call method Gui class"""
        self.gui.start_mainloop()


if __name__ == '__main__':
    main = Main()
    main.main_gui()
