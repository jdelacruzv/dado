from dice import Dice


class Controller:
    """
    Manages the application logic (Model) and user interactions (View).
    """
    def __init__(self, gui_instance):
        self.dice = Dice()  
        # Instancia de la Vista (Gui), inyectada desde fuera
        self.gui = gui_instance  
        # Conectar la Vista al Controlador para que la Vista pueda llamar a sus métodos
        self.gui.set_controller(self)

    def play_dice(self):
        """
        Handles the event when the 'play dice' button is clicked.
        Orchestrates the Model (Dice) and the View (Gui).
        """
        # 1. Reproducir sonido del dado (le pide al Modelo que realice una acción)
        self.dice.play_sound()
        # 2. Obtener la cantidad de dados seleccionados por el usuario (desde la Vista)
        num_dice = self.gui.option_dice.get()

        # 3. Generar los valores de los dados (le pide al Modelo que obtenga datos)
        dice_values = [self.dice.get_throw_value() for _ in range(num_dice)]
        # 4. Actualizar la Vista para mostrar los resultados (le dice a la Vista qué mostrar)
        # La Vista es responsable de cómo se muestran estos valores.
        if num_dice == 1:
            self.gui.create_frame_dice1(dice_values)
        elif num_dice == 2:
            self.gui.create_frame_dice2(dice_values)
        elif num_dice == 3:
            self.gui.create_frame_dice3(dice_values)
        elif num_dice == 4:
            self.gui.create_frame_dice4(dice_values)
        elif num_dice == 5:
            self.gui.create_frame_dice5(dice_values)
        elif num_dice == 6:
            self.gui.create_frame_dice6(dice_values)
        else:
            print(f"Número de dados no soportado: {num_dice}")
            # Podrías mostrar un mensaje de error en la GUI también si es necesario

    def handle_num_dice_selection(self, selected_num_dice):
        """
        Handles the event when a radio button for number of dice is selected.
        Currently, just clears the display. Could trigger other logic.
        """
        print(f"Número de dados seleccionado: {selected_num_dice}")
        self.gui.destroy_frame_dice()
        # Aquí podrías decidir si quieres redibujar un estado inicial
        # o hacer algo más complejo antes de que el usuario haga clic en "jugar dado".
