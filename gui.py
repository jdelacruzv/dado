import tkinter as tk


class Gui(tk.Tk):
    """
    Manages the GUI components and user interactions.
    """
    dict_img128 = {}    # Dictionaries for 128 images
    dict_img64 = {}     # Dictionaries for 64 images

    def __init__(self):
        super().__init__()
        self.title('Dado')
        self.iconphoto(True, tk.PhotoImage(file='res/dado.png'))
        self.resizable(False, False)
        self.center_window(320, 430)
        self.config(bg='white')
		# The reference to the controller will be established after
        self._controller = None  
        self.option_dice = tk.IntVar()
        self.option_dice.set(2)

        # Load images
        self.img_one128 = tk.PhotoImage(file='res/img128/1.png')
        self.img_two128 = tk.PhotoImage(file='res/img128/2.png')
        self.img_three128 = tk.PhotoImage(file='res/img128/3.png')
        self.img_four128 = tk.PhotoImage(file='res/img128/4.png')
        self.img_five128 = tk.PhotoImage(file='res/img128/5.png')
        self.img_six128 = tk.PhotoImage(file='res/img128/6.png')
        self.img_one64 = tk.PhotoImage(file='res/img64/1.png')
        self.img_two64 = tk.PhotoImage(file='res/img64/2.png')
        self.img_three64 = tk.PhotoImage(file='res/img64/3.png')
        self.img_four64 = tk.PhotoImage(file='res/img64/4.png')
        self.img_five64 = tk.PhotoImage(file='res/img64/5.png')
        self.img_six64 = tk.PhotoImage(file='res/img64/6.png')

        self.dict_img128 = {
            1: self.img_one128, 2: self.img_two128, 3: self.img_three128,
            4: self.img_four128, 5: self.img_five128, 6: self.img_six128
        }
        self.dict_img64 = {
            1: self.img_one64, 2: self.img_two64, 3: self.img_three64,
            4: self.img_four64, 5: self.img_five64, 6: self.img_six64
        }

        # Initialize empty dice frame
        self.frm_dice = tk.Frame(self, bg='white')
        self.frm_dice.grid(row=2, columnspan=6)

        self._create_widgets()

    def _create_widgets(self):
        """
        Helper method to create all GUI widgets.
        """
        # Frame header
        self.frm_head = tk.LabelFrame(
            self,
            text='Cantidad dados:',
            bg='white',
            bd=2
        )
        self.frm_head.grid(row=0, columnspan=3, padx=35, pady=15)

        # Radiobutton (they now call a local method that can notify the controller)
        tk.Radiobutton(self.frm_head, text='1', bg='white', variable=self.option_dice,
                       value=1, command=self._on_radio_select).grid(row=0, column=0)
        tk.Radiobutton(self.frm_head, text='2', bg='white', variable=self.option_dice,
                       value=2, command=self._on_radio_select).grid(row=0, column=1)
        tk.Radiobutton(self.frm_head, text='3', bg='white', variable=self.option_dice,
                       value=3, command=self._on_radio_select).grid(row=0, column=2)
        tk.Radiobutton(self.frm_head, text='4', bg='white', variable=self.option_dice,
                       value=4, command=self._on_radio_select).grid(row=0, column=3)
        tk.Radiobutton(self.frm_head, text='5', bg='white', variable=self.option_dice,
                       value=5, command=self._on_radio_select).grid(row=0, column=4)
        tk.Radiobutton(self.frm_head, text='6', bg='white', variable=self.option_dice,
                       value=6, command=self._on_radio_select).grid(row=0, column=5)

        # Button dice play (the controller command will be assigned in set_controller)
        self.play_button = tk.Button(
            self,
            text='[ Click jugar dado ]',
            bg='white',
            fg='red',
            relief='flat',
            overrelief='raised',
            command=None  # The command will be set to set_controller
        )
        self.play_button.grid(row=1, columnspan=6, pady=10)

    def set_controller(self, controller_instance):
        """
        Sets the controller instance for the GUI.
        """
        self._controller = controller_instance
        # Once the controller is set up, we can bind its methods to the GUI events 
        self.play_button.config(command=self._controller.play_dice)

    def _on_radio_select(self):
        """
        Handles radio button selection. Notifies controller or handles locally.
        """
        if self._controller:
            self._controller.handle_num_dice_selection(
                self.option_dice.get())
        else:
            self.destroy_frame_dice()

    def destroy_frame_dice(self):
        """
        Destroy the current screen frame and recreate an empty one as a placeholder.
        """
        # Check if frame exists before destroying
        if self.frm_dice:
            self.frm_dice.destroy()
        # Recreate an empty frame to maintain the structure and avoid referencing errors
        self.frm_dice = tk.Frame(self, bg='white')
        # Fallback if controller not set yet
        self.frm_dice.grid(row=2, columnspan=6)

    def create_frame_dice1(self, values):  
        """
        Create 1 dice frame with the given value.
        """
        self.destroy_frame_dice()
        self.frm_dice = tk.Frame(self, bg='white')
        self.frm_dice.grid(row=2, columnspan=6)
        tk.Label(
            self.frm_dice, bg='white',
            image=self.dict_img128[values[0]]
        ).grid(row=2, columnspan=6, pady=50)

    def create_frame_dice2(self, values):
        """
        Create 2 dice frame with the given values.
        """
        self.destroy_frame_dice()
        self.frm_dice = tk.Frame(self, bg='white')
        self.frm_dice.grid(row=2, columnspan=6)
        tk.Label(
            self.frm_dice, bg='white',
            image=self.dict_img128[values[0]]
        ).grid(row=2, columnspan=6, pady=15)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img128[values[1]]
        ).grid(row=3, columnspan=6)

    def create_frame_dice3(self, values):
        """
        Create 3 dice frame with the given values.
        """
        self.destroy_frame_dice()
        self.frm_dice = tk.Frame(self, bg='white')
        self.frm_dice.grid(row=2, columnspan=6)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img128[values[0]]
        ).grid(row=2, columnspan=6, padx=5, pady=15)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img128[values[1]]
        ).grid(row=3, column=0, padx=5)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img128[values[2]]
        ).grid(row=3, column=2, padx=5)

    def create_frame_dice4(self, values):
        """
        Create 4 dice frame with the given values.
        """
        self.destroy_frame_dice()
        self.frm_dice = tk.Frame(self, bg='white')
        self.frm_dice.grid(row=2, columnspan=6)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img128[values[0]]
        ).grid(row=2, column=0, pady=15)
        tk.Label(
            self.frm_dice, bg='white',
            image=self.dict_img128[values[1]]
        ).grid(row=2, column=2, padx=5)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img128[values[2]]
        ).grid(row=3, column=0, padx=5)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img128[values[3]]
        ).grid(row=3, column=2)

    def create_frame_dice5(self, values):
        """
        Create 5 dice frame with the given values.
        """
        self.destroy_frame_dice()
        self.frm_dice = tk.Frame(self, bg='white')
        self.frm_dice.grid(row=2, columnspan=6)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[0]]
        ).grid(row=2, columnspan=6, pady=15)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[1]]
        ).grid(row=3, column=1, padx=10)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[2]]
        ).grid(row=3, column=3)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[3]]
        ).grid(row=3, column=5, padx=10)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[4]]
        ).grid(row=4, columnspan=6, pady=15)

    def create_frame_dice6(self, values):
        """
        Create 6 dice frame with the given values.
        """
        self.destroy_frame_dice()
        self.frm_dice = tk.Frame(self, bg='white')
        self.frm_dice.grid(row=2, columnspan=6)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[0]]
        ).grid(row=2, column=1, padx=10, pady=15)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[1]]
        ).grid(row=2, column=3, padx=10, pady=15)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[2]]
        ).grid(row=3, column=1, padx=10)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[3]]
        ).grid(row=3, column=3, padx=10)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[4]]
        ).grid(row=4, column=1, padx=10, pady=15)
        tk.Label(
            self.frm_dice,
            bg='white',
            image=self.dict_img64[values[5]]
        ).grid(row=4, column=3, padx=10, pady=15)

    def center_window(self, w, h):
        """
        Center window.
        """
        x = (self.winfo_screenwidth() - w) / 2
        y = (self.winfo_screenheight() - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def start_mainloop(self):
        """
        Run the main window loop.
        """
        self.mainloop()
