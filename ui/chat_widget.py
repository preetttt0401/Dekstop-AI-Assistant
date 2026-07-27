import customtkinter as ctk


class ChatWidget(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=15
        )

    def add_user(self, text):

        label = ctk.CTkLabel(

            self,

            text=f"You\n\n{text}",

            justify="left",

            anchor="w",

            fg_color="#2563eb",

            corner_radius=12,

            padx=15,

            pady=15

        )

        label.pack(fill="x", pady=8)

    def add_ai(self, text):

        label = ctk.CTkLabel(

            self,

            text=f"Assistant\n\n{text}",

            justify="left",

            anchor="w",

            fg_color="#1e293b",

            corner_radius=12,

            padx=15,

            pady=15

        )

        label.pack(fill="x", pady=8)