from tkinter import *
from PIL import Image, ImageTk
from enum import Enum
import os
import sys
import pyperclip # type: ignore


class Action(Enum):
    LogIn = 1
    Register = 2
    Account = 3


class GUI:

    login_geometry = [500, 300]
    register_geometry = [500, 335]
    form_geometry = [650, 410]
    __images = []

    # * Function to get Images from AppData
    # * No Parameters
    # * Return: Base Path -> String
    @classmethod
    def imagePath(cls) -> str:

        try:
            base_path = os.path.join(sys._MEIPASS, 'images')
        except:
            base_path = r'.\images'

        return base_path

    # * Function to Clear Images
    # * No Parameters
    # * No Return Value

    @classmethod
    def clearImg(cls):
        cls.__images.clear()

    # * Function to Fetch Images for Account Form and Account List
    # * No Parameters
    # * No Return Value
    @classmethod
    def frmLstInit(cls):
        import_tick_image = Image.open(GUI.imagePath()+r"\tick_image.png")
        import_cross_image = Image.open(GUI.imagePath()+r"\cross_image.png")
        import_generate_password_image = Image.open(
            GUI.imagePath()+r"\generate_password.png")
        resized_tick_image = import_tick_image.resize(
            (40, 40), Image.LANCZOS)
        resized_cross_image = import_cross_image.resize(
            (25, 25), Image.LANCZOS)
        resized_generate_password_image = import_generate_password_image.resize(
            (40, 40), Image.LANCZOS)
        cls.__images.append(ImageTk.PhotoImage(resized_tick_image))
        cls.__images.append(ImageTk.PhotoImage(resized_cross_image))
        cls.__images.append(ImageTk.PhotoImage(
            resized_generate_password_image))

    # * Function to Fetch Images for Login and Register
    # * No Parameters
    # * No Return Value
    @classmethod
    def lgnRegInit(cls):
        import_tick_image = Image.open(GUI.imagePath()+r"\tick_image.png")
        import_cross_image = Image.open(GUI.imagePath()+r"\cross_image.png")
        resized_tick_image = import_tick_image.resize(
            (40, 40), Image.LANCZOS)
        resized_cross_image = import_cross_image.resize(
            (25, 25), Image.LANCZOS)
        cls.__images.append(ImageTk.PhotoImage(resized_tick_image))
        cls.__images.append(ImageTk.PhotoImage(resized_cross_image))

    # * Login Page Screen
    # * Parameters: root, SignIn Function and Login to Register Function
    # * No Return Value
    @classmethod
    def login(cls, root: Frame, signInFunction, lgnToRegShifter) -> None:

        master_user_name = StringVar()
        master_password = StringVar()
        f = Frame(root, width=500, height=195, bg='#333333')

        Label(
            f,
            text="Sign In",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15, 0)
        )
        Label(
            f,
            text="Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5),
            sticky=E
        )
        e_master_user_name = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=master_user_name
        )
        e_master_user_name.grid(
            row=1,
            column=1,
            pady=(25, 10),
            sticky=W
        )
        Label(
            f,
            text="Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
            sticky=E
        )
        e_master_password = Entry(
            f,
            textvariable=master_password,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_master_password.grid(
            row=2,
            column=1,
            sticky=W
        )
        Button(
            f,
            width=7,
            height=1,
            relief=SOLID,
            borderwidth=2,
            cursor='hand2',
            command=lambda: [
                signInFunction(master_user_name.get(), master_password.get(
                )), e_master_user_name.delete(0, END), e_master_password.delete(0, END)
            ],
            text="Sign In",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(20, 0)
        )

        Label(
            f,
            text="Dont Have an Account?",
            font=('JetBrains Mono Medium', 9),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            pady=(12, 0)
        )

        l = Label(
            f,
            text="Register",
            font=('Kamerik 105 W00 Bold', 12),
            bg='#333333',
            fg='#75E6DA',
            cursor='hand2'
        )
        l.bind("<Button-1>", lgnToRegShifter)
        l.grid(row=6, column=0, columnspan=2)

        f.pack()

    # * Function to Display Login Successfull
    # * Parameters: root and Action Value -> Enum
    # * No Return Value
    @classmethod
    def successfullMessage(cls, root: Frame, actionValue) -> None:

        if actionValue == Action.LogIn:
            message = 'Login Successfull'
        elif actionValue == Action.Register:
            message = 'Registration Successfull'
        elif actionValue == Action.Account:
            message = 'Account Information has been Added'

        f = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f,
            image=cls.__images[0],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            pady=(0, 5)
        )

        Label(
            f,
            text=message,
            fg="#59d400",
            bg="#333333",
            font=('Kamerik 105 W00 Bold', 12),
        ).grid(
            row=0,
            column=1,
            pady=(0, 5)
        )

        f.pack(side='bottom', anchor='center', fill='both')

    # * Function to Display Login Unsuccessfull
    # * Parameters: root and Action Value -> Enum
    # * No Return Value
    @classmethod
    def unsuccessfullMessage(cls, root: Frame, actionValue) -> None:

        if actionValue == Action.LogIn:
            message = 'Login Unsuccessfull'
        elif actionValue == Action.Register:
            message = 'Registration Unsuccessfull'
        elif actionValue == Action.Account:
            message = 'Account Information cannot be Added'

        f = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f,
            image=cls.__images[1],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            pady=(5, 0)
        )
        Label(
            f,
            text=message,
            fg="#de151f",
            bg="#333333",
            font=('Kamerik 105 W00 Bold', 12),
        ).grid(
            row=0,
            column=1,
            pady=(5, 0)
        )

        f.pack(side='bottom', anchor='s', fill='both')

    # * Register Page Screen
    # * Parameters: root, SignUp Function and Register to Login Function
    # * No Return Value
    @classmethod
    def register(cls, root: Frame, signUpFunction, regToLgnShifter) -> None:
        first_name = StringVar()
        master_user_name = StringVar()
        master_password = StringVar()

        f = Frame(root, width=500, height=305, bg='#333333')

        Label(
            f,
            text="Sign Up",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15, 0)
        )

        Label(
            f,
            text="First Name: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5),
            sticky=E
        )

        e_first_name = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=first_name
        )
        e_first_name.grid(
            row=1,
            column=1,
            pady=(25, 10),
            sticky=W
        )

        Label(
            f,
            text="Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_master_user_name = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=master_user_name
        )
        e_master_user_name.grid(
            row=2,
            column=1,
            pady=(0, 10),
            sticky=W
        )

        Label(
            f,
            text="Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=3,
            column=0,
            sticky=E
        )

        e_master_password = Entry(
            f,
            textvariable=master_password,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_master_password.grid(
            row=3,
            column=1,
            sticky=W
        )

        Button(
            f,
            width=7,
            height=1,
            relief=SOLID,
            borderwidth=2,
            cursor='hand2',
            command=lambda: [
                signUpFunction(first_name.get(),
                               master_user_name.get(), master_password.get()),
                e_first_name.delete(0, END), e_master_user_name.delete(
                    0, END), e_master_password.delete(0, END)
            ],
            text="Sign Up",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(20, 0)
        )

        Label(
            f,
            text="Already Have an Account?",
            font=('JetBrains Mono Medium', 9),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            pady=(12, 0)
        )

        l = Label(
            f,
            text="Login",
            font=('Kamerik 105 W00 Bold', 12),
            bg='#333333',
            fg='#75E6DA',
            cursor='hand2'
        )
        l.bind("<Button-1>", regToLgnShifter)
        l.grid(row=6, column=0, columnspan=2)

        f.pack()

    # * Welcome Message
    # * Parameters: root, First Name -> String
    # * No Return Value
    @classmethod
    def welcomeMsg(cls, root: Frame, firstName: str, getAccountTable) -> None:

        f = Frame(root, width=650, height=55, bg='#333333')
        platform_list = []

        Label(
            f,
            text="Hello,",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white',
        ).grid(
            row=0,
            column=0,
            pady=(2, 0),
            padx=(2, 0),
            sticky=E
        )

        Label(
            f,
            text=firstName,
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='#75E6DA',
        ).grid(
            row=0,
            column=1,
            pady=(2, 0),
            sticky=W
        )

        l = Label(
            f,
            text='View Account List',
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white',
            cursor='hand2'
        )
        l.grid(row=0, column=2, pady=(2, 0), padx=(325, 0), sticky=E)
        l.bind("<Button-1>", lambda e: GUI.subWindow(f, getAccountTable()))

        f.pack(anchor='w', fill='x')

    # * Account Form Screen
    # * Parameters: root
    # * No Return Value

    @classmethod
    def accountForm(cls, root: Frame, addAccount, getGeneratedPassword):

        platform = StringVar()
        url = StringVar()
        email = StringVar()
        user_name = StringVar()
        password = StringVar()
        password_length = StringVar()
        password_length.set('Password Length')

        f = Frame(root, width=650, height=305, bg='#333333')

        Label(
            f,
            text='Account Form',
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA',
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15, 0)
        )

        Label(
            f,
            text="Platform Name: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5),
            sticky=E
        )

        e_platform = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=platform,
        )
        e_platform.grid(row=1, column=1, pady=(25, 10), sticky=W)

        Label(
            f,
            text="Platform URL: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_url = Entry(
            f,
            textvariable=url,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_url.grid(row=2, column=1, pady=(0, 10), sticky=W)

        Label(
            f,
            text="Account Email: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=3,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_email = Entry(
            f,
            textvariable=email,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_email.grid(row=3, column=1, pady=(0, 10), sticky=W)

        Label(
            f,
            text="Account Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=4,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_user_name = Entry(
            f,
            textvariable=user_name,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_user_name.grid(row=4, column=1, pady=(0, 10), sticky=W)

        Label(
            f,
            text="Account Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            sticky=E
        )

        e_password = Entry(
            f,
            textvariable=password,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_password.grid(row=5, column=1, sticky=W)

        drop_down = OptionMenu(
            f,
            password_length,
            *range(10, 21),

        )

        drop_down.config(
            bg='#333333',
            fg='white',
            relief=FLAT,
            font=('JetBrains Mono Medium', 10),
            direction='below'
        )

        drop_down['menu'].config(
            bg='#333333',
            fg='white',
            relief=FLAT,
            borderwidth=1,
            font=('JetBrains Mono Medium', 10),
        )

        drop_down["highlightthickness"] = 0
        drop_down.grid(
            row=6,
            column=0,
            sticky=E,
            padx=(0, 20)
        )

        l = Label(
            f,
            text=' Click to Generate',
            image=cls.__images[2],
            compound=LEFT,
            font=('JetBrains Mono Medium', 10),
            bg='#333333',
            fg='white',
            cursor='hand2'
        )
        l.bind("<Button-1>",
               lambda e: [
                   e_password.delete(0, END), e_password.insert(
                       0, getGeneratedPassword(
                           int(password_length.get()) if password_length.get() != 'Password Length' else 15))
               ]
               )
        l.grid(row=6, column=1, sticky=W)

        Button(
            f,
            width=12,
            height=1,
            relief=SOLID,
            borderwidth=2,
            cursor='hand2',
            command=lambda: [
                addAccount(platform.get(), url.get(), email.get(),
                           user_name.get(), password.get()),
                e_platform.delete(0, END), e_url.delete(
                    0, END), e_email.delete(0, END),
                e_user_name.delete(0, END), e_password.delete(0, END)
            ],
            text="Add Account",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=7,
            column=0,
            columnspan=2,
            pady=(5, 0)
        )

        f.pack()

    # * All Accounts List Sub Screen
    @classmethod
    def subWindow(cls, root: Frame, account_list: list[list[str]]) -> None:

        heading_list = ['Platform', 'URL', 'Email', 'Username', 'Password (Click to Copy)']

        sub_window = Toplevel(
            root,
            bg='#333333',
            height=400,
            width=1300
        )

        sub_window.resizable(0, 1)
        sub_window.minsize(1550, 200)
        sub_window.maxsize(1550, 793)

        upper_frame = Frame(sub_window, width=1300, bg='#333333')
        middle_frame = Frame(sub_window, width=1300, bg='#333333')

        Label(
            upper_frame,
            text="Saved Accounts",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(
            row=0,
            column=0,
            pady=(15, 30)
        )

        upper_frame.pack()

        for heading in heading_list:

            Label(
                middle_frame,
                text=heading,
                font=('JetBrains Mono Medium', 12),
                bg='#333333',
                fg='#75E6DA',
                borderwidth=1,
                relief=SOLID,
                width=25
            ).grid(
                row=0,
                column=heading_list.index(heading),
                ipady=7
            )

        i = 1

        for record in account_list:

            j = 0
            if i == len(account_list):
                padding_bottom = 20
            else:
                padding_bottom = 0

            for idx, cell_data in enumerate(record):

                if idx not in {3, 4}:
                    Label(
                        middle_frame,
                        text=cell_data,
                        font=('JetBrains Mono Medium', 12),
                        bg='#333333',
                        fg='white',
                        borderwidth=1,
                        relief=SOLID,
                        width=25
                    ).grid(
                        row=i,
                        column=j,
                        ipady=7,
                        pady=(0, padding_bottom)
                    )
                
                else:
                    Button(
                        middle_frame, 
                        text=cell_data,
                        font=('JetBrains Mono Medium', 12),
                        bg='#333333',
                        fg='white',
                        borderwidth=1,
                        relief=SOLID,
                        width=25,
                        command=lambda: pyperclip.copy(record[idx])
                    ).grid(
                        row=i,
                        column=j,
                        ipady=2,
                        pady=(0, padding_bottom)
                    )

                j += 1

            


            i += 1

        middle_frame.pack()
