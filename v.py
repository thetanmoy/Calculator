import tkinter as tk
from tkinter import ttk

class V(tk.Tk):
    padding=10
    max_button_per_row=4
    caption_of_buttons=[
        'C','+/-','%','/',
        7 , 8 , 9 ,'*',
        4 , 5 , 6 ,'-',
        1 , 2 , 3 ,'+',
        0,'.','='
    ]
    def __init__(self,controller):
        super().__init__()
        self.title("Calculator")
        self.config(bg ='black')
        self.controller = controller
        self.value_var=tk.StringVar()
        self._mainfram()
        self._label()
        self._button()
        self._center_window()
        self._config_button_style()

    def main(self):
        self.mainloop()

    def _mainfram(self):
        self.mainframe = ttk.Frame(self)
        self.mainframe.pack(padx=self.padding,pady=self.padding)

    def _config_button_style(self):
        style = ttk.Style()
        style.theme_use('alt')
        print(style.theme_names())
        #number button style
        style.configure('N.TButton', background='black', foreground='white')
        #operator button style
        style.configure('O.TButton', background="blue",foreground='black')
        #baki button
        style.configure('B.TButton', background ='darkblue',foreground='black')



    def _label(self):
        label = ttk.Label(self.mainframe,anchor='e' , textvariable = self.value_var, background="black", foreground="white",font=("Arial",30))
        label.pack(fill = 'x' )

    def _button(self):
        outer_bframe = ttk.Frame(self.mainframe)
        outer_bframe.pack()

        is_first_row = True
        buttons_in_row = 0;
        for caption in self.caption_of_buttons:
            if is_first_row or buttons_in_row == self.max_button_per_row:
                is_first_row=False
                bframe = ttk.Frame(outer_bframe)
                bframe.pack(fill='x')
                buttons_in_row = 0;
            if isinstance(caption, int):
                style_prefix = 'N'
            elif self._isoperator(caption):
                style_prefix='O'
            else:
                style_prefix="B"

            style_name=f"{style_prefix}.TButton"
            btn = ttk.Button(bframe , text=caption , command =(lambda button=caption: self.controller.on_button_click(button) ) ,style=style_name)
            if caption==0:
                fill ='x'
                expand = 2
            else:
                fill = 'none'
                expand = '0'
            btn.pack(fill=fill,expand=expand,side = "left")
            buttons_in_row +=1
    def _isoperator(self,button_caption):
        return button_caption in {'/','*','-','+','='}

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth()-width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry( f'{width}x{height}+{x_offset}+{y_offset}')


