import tkinter as tk


class Gui(tk.Tk):
    """Class that works as the application view"""
    dict_img128 = {}    # dictionaries for 128 images
    dict_img64 = {}     # dictionaries for 64 images

    def __init__(self, main):
        super().__init__()
        self.title('Dado')
        self.iconphoto(True, tk.PhotoImage(file='res/dado.png'))
        self.resizable(False, False)
        self.center_window(320, 430)
        self.config(bg='white')
        self.main = main
        self.option_dados = tk.IntVar()
        self.option_dados.set(2)

        # set dado images
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
            1: self.img_one128, 
            2: self.img_two128, 
            3: self.img_three128,
            4: self.img_four128, 
            5: self.img_five128, 
            6: self.img_six128
        }

        self.dict_img64 = {
            1: self.img_one64, 
            2: self.img_two64, 
            3: self.img_three64,
            4: self.img_four64, 
            5: self.img_five64, 
            6: self.img_six64
        }

        # frame dado
        self.frm_dado = tk.Frame(self, bg='white')
        self.frm_dado.grid(row=2, columnspan=6)

        # frame head
        self.frm_head = tk.LabelFrame(
            self, 
            text='Cantidad dados:', 
            bg='white', 
            bd=2
        )
        self.frm_head.grid(row=0, columnspan=3, padx=35, pady=15)

        # radiobutton
        tk.Radiobutton(
            self.frm_head, 
            text='1', 
            bg='white', 
            variable=self.option_dados, 
            value=1, 
            command=self.destroy_frame_dados
        ).grid(row=0, column=0)
        
        tk.Radiobutton(
            self.frm_head, 
            text='2', 
            bg='white', 
            variable=self.option_dados, 
            value=2, 
            command=self.destroy_frame_dados
        ).grid(row=0, column=1)
        
        tk.Radiobutton(
            self.frm_head, 
            text='3', 
            bg='white', 
            variable=self.option_dados, 
            value=3, 
            command=self.destroy_frame_dados
        ).grid(row=0, column=2)
        
        tk.Radiobutton(
            self.frm_head, 
            text='4', 
            bg='white', 
            variable=self.option_dados, 
            value=4, 
            command=self.destroy_frame_dados
        ).grid(row=0, column=3)
        
        tk.Radiobutton(
            self.frm_head, 
            text='5', 
            bg='white', 
            variable=self.option_dados, 
            value=5, 
            command=self.destroy_frame_dados
        ).grid(row=0, column=4)
        
        tk.Radiobutton(
            self.frm_head, 
            text='6', 
            bg='white', 
            variable=self.option_dados, 
            value=6, 
            command=self.destroy_frame_dados
        ).grid(row=0, column=5)

        # button dado play
        tk.Button(
            self, 
            text='[ Click jugar dado ]', 
            bg='white', 
            fg='red', 
            relief='flat',  
            overrelief='raised',
            command=self.main.play_dado
        ).grid(row=1, columnspan=6, pady=10)


    def destroy_frame_dados(self):
        """Destroy the current screen frame"""
        self.frm_dado.destroy()


    def create_frame_dados1(self):
        """Create 1 dado frame"""
        self.main.call_play_sound()
        self.frm_dado = tk.Frame(self, bg='white')
        self.frm_dado.grid(row=2, columnspan=6)
        
        tk.Label(
            self.frm_dado, bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=2, columnspan=6, pady=50)


    def create_frame_dados2(self):
        """Create 2 dados frame"""
        self.main.call_play_sound()
        self.frm_dado = tk.Frame(self, bg='white')
        self.frm_dado.grid(row=2, columnspan=6)
        
        tk.Label(
            self.frm_dado, bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=2, columnspan=6, pady=15)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=3, columnspan=6)


    def create_frame_dados3(self):
        """Create 3 dados frame"""
        self.main.call_play_sound()
        self.frm_dado = tk.Frame(self, bg='white')
        self.frm_dado.grid(row=2, columnspan=6)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=2, columnspan=6, padx=5, pady=15)

        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=3, column=0, padx=5)

        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=3, column=2, padx=5)


    def create_frame_dados4(self):
        """Create 4 dados frame"""
        self.main.call_play_sound()
        self.frm_dado = tk.Frame(self, bg='white')
        self.frm_dado.grid(row=2, columnspan=6)

        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=2, column=0, pady=15)
        
        tk.Label(
            self.frm_dado, bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=2, column=2, padx=5)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=3, column=0, padx=5)
        
        tk.Label(
            self.frm_dado, 
            bg='white',
            image=self.dict_img128[self.main.call_throw_dado()]
        ).grid(row=3, column=2)


    def create_frame_dados5(self):
        """Create 5 dados frame"""
        self.main.call_play_sound()
        self.frm_dado = tk.Frame(self, bg='white')
        self.frm_dado.grid(row=2, columnspan=6)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=2, columnspan=6, pady=15)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=3, column=1, padx=10)
        
        tk.Label(
            self.frm_dado, 
            bg='white',
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=3, column=3)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=3, column=5, padx=10)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=4, columnspan=6, pady=15)


    def create_frame_dados6(self):
        """Create 6 dados frame"""
        self.main.call_play_sound()
        self.frm_dado = tk.Frame(self, bg='white')
        self.frm_dado.grid(row=2, columnspan=6)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=2, column=1, padx=10, pady=15)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=2, column=3, padx=10, pady=15)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
            ).grid(row=3, column=1, padx=10)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=3, column=3, padx=10)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=4, column=1, padx=10, pady=15)
        
        tk.Label(
            self.frm_dado, 
            bg='white', 
            image=self.dict_img64[self.main.call_throw_dado()]
        ).grid(row=4, column=3, padx=10, pady=15)


    def center_window(self, w, h):
        """Center window"""
        x = (self.winfo_screenwidth() - w) / 2
        y = (self.winfo_screenheight() - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def start_mainloop(self):
        """Run the main window loop"""
        self.mainloop()
