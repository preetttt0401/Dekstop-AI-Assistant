import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        ctk.CTkLabel(

            self,

            text="Quick Actions",

            font=("Segoe UI",20,"bold")

        ).pack(pady=20)

        self.screenshot = ctk.CTkButton(

            self,

            text="📸 Screenshot"

        )

        self.screenshot.pack(fill="x", padx=20, pady=8)

        self.battery = ctk.CTkButton(

            self,

            text="🔋 Battery"

        )

        self.battery.pack(fill="x", padx=20, pady=8)

        self.time = ctk.CTkButton(

            self,

            text="🕒 Time"

        )

        self.time.pack(fill="x", padx=20, pady=8)

        self.date = ctk.CTkButton(

            self,

            text="📅 Date"

        )

        self.date.pack(fill="x", padx=20, pady=8)