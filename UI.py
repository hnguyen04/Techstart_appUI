

from pathlib import Path

from tkinter import *
from PIL import Image, ImageTk


# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



class root(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")
        self.geometry("746x661")

        # creating a frame and assigning it to container
        container = Frame(self)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (login_frame, sign_up_frame):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(login_frame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class login_frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="#FFFFFF")
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=661,
            width=746,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            112.0,
            73.0,
            634.6497802734375,
            614.183349609375,
            fill="#989898",
            outline="")

        def txt_on_click(e):
            txt.configure(fg="#666666")
            controller.show_frame(sign_up_frame)

        txt = Label(self, text="Register here", font=(
            "Lato Regular", 14 * -1), fg="white", bg="#989898")
        txt.place(x=406.0, y=543.0)
        txt.bind('<Button-1>', txt_on_click)
        txt.bind('<Enter>', lambda e: txt.configure(fg="#BBBBBB"))
        txt.bind('<Leave>', lambda e: txt.configure(fg="white"))

        canvas.create_text(
            253.0,
            545.0,
            anchor="nw",
            text="Don’t have an account?",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        self.button_image_1 = PhotoImage(file=r'.\assets\frame1\button_1.png')
        self.button_image_2 = PhotoImage(file=r'.\assets\frame1\button_1_hover.png')
        self.button_image_3 = PhotoImage(file=r'.\assets\frame1\button_1_onclick.png')

        def button_1_onclick():
            button_1.configure(image=self.button_image_3)
            ## nhảy sang home page tính sau

        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=button_1_onclick,
            relief="flat"
        )
        button_1.bind('<Enter>', lambda e: button_1.configure(image=self.button_image_2))
        button_1.bind('<Leave>', lambda e: button_1.configure(image=self.button_image_1))
        
        button_1.place(
            x=273.6806335449219,
            y=480.0,
            width=198.3193359375,
            height=54.0
        )

        canvas.create_text(
            221.0,
            198.0,
            anchor="nw",
            text="Username/Email*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            223.0,
            298.0,
            anchor="nw",
            text="Password*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            328.0,
            94.52175903320312,
            anchor="nw",
            text="LOGIN",
            fill="#FFFFFF",
            font=("Lato Regular", 29 * -1)
        )

        username = StringVar()
        password = StringVar()

        self.entry_image_1 = PhotoImage(file=r'.\assets\frame1\entry_1.png')
        entry_bg_1 = canvas.create_image(
            372.6672668457031,
            248.09378051757812,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=username
        )
        entry_1.place(
            x=230.26683902740479,
            y=224.0,
            width=284.8008556365967,
            height=46.18756103515625
        )

        self.entry_image_2 = PhotoImage(file=r'.\assets\frame1\entry_2.png')
        entry_bg_2 = canvas.create_image(
            372.8357849121094,
            344.1086120605469,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=('Lato'),
            textvariable=password,
            show="*"
        )
        entry_2.place(
            x=230.43535709381104,
            y=320.01483154296875,
            width=284.8008556365967,
            height=46.18756103515625
        )


class sign_up_frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="#FFFFFF")

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=661,
            width=746,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            111.81982421875,
            59.925567626953125,
            634.4696044921875,
            601.1089172363281,
            fill="#989898",
            outline="")

        self.button_image_1 = PhotoImage(file=r'.\assets\frame0\button_1.png')
        self.button_image_2 = PhotoImage(file=r'.\assets\frame0\button_1_hover.png')
        self.button_image_3 = PhotoImage(file=r'.\assets\frame0\button_1_onclick.png')

        def button_1_onclick():
            button_1.configure(image=self.button_image_3)
            #gọi hàm check 
            #hiện Label đăng nhập ok
            #2 cái này lm sau zzz

        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=button_1_onclick,
            relief="flat"
        )
        button_1.bind('<Enter>', lambda e: button_1.configure(image=self.button_image_2))
        button_1.bind('<Leave>', lambda e: button_1.configure(image=self.button_image_1))
        button_1.place(
            x=273.6806640625,
            y=480.0,
            width=198.3193359375,
            height=54.0
        )

        canvas.create_text(
            223.0,
            148.0,
            anchor="nw",
            text="Username*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            223.0,
            372.0,
            anchor="nw",
            text="Repeat Password*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            223.0,
            224.0,
            anchor="nw",
            text="E-mail*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            223.0,
            298.0,
            anchor="nw",
            text="Password*",
            fill="#FFFFFF",
            font=("Lato Regular", 14 * -1)
        )

        canvas.create_text(
            314.4547119140625,
            94.52175903320312,
            anchor="nw",
            text="SIGN UP",
            fill="#FFFFFF",
            font=("Lato Regular", 29 * -1)
        )

        username = StringVar()
        password = StringVar()
        Email = StringVar()
        repeated_pass = StringVar()

        self.entry_image_1 = PhotoImage(file=r'.\assets\frame0\entry_1.png')
        entry_bg_1 = canvas.create_image(
            373.6672668457031,
            196.09378051757812,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=username
        )
        entry_1.place(
            x=231.26683902740479,
            y=172.0,
            width=284.8008556365967,
            height=46.18756103515625
        )

        self.entry_image_2 = PhotoImage(file=r'.\assets\frame0\entry_2.png')
        entry_bg_2 = canvas.create_image(
            372.8357849121094,
            418.24334716796875,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFDFD",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=repeated_pass,
            show="*"
        )
        entry_2.place(
            x=230.43535709381104,
            y=394.1495666503906,
            width=284.8008556365967,
            height=46.18756103515625
        )

        self.entry_image_3 = PhotoImage(file=r'.\assets\frame0\entry_3.png')
        entry_bg_3 = canvas.create_image(
            372.8357849121094,
            344.1086120605469,
            image=self.entry_image_3
        )
        entry_3 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=password,
            show="*"
        )
        entry_3.place(
            x=230.43535709381104,
            y=320.01483154296875,
            width=284.8008556365967,
            height=46.18756103515625
        )

        self.entry_image_4 = PhotoImage(file=r'.\assets\frame0\entry_4.png')
        entry_bg_4 = canvas.create_image(
            372.8357849121094,
            269.9739227294922,
            image=self.entry_image_4
        )
        entry_4 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Lato"),
            textvariable=repeated_pass,
            show="*"
        )
        entry_4.place(
            x=230.43535709381104,
            y=245.88014221191406,
            width=284.8008556365967,
            height=46.18756103515625
        )


if __name__ == "__main__":
    testObj = root()
    testObj.mainloop()
