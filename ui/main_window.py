import customtkinter as ctk
import threading

from assistant import DesktopAssistant

from ui.styles import *
from ui.chat_widget import ChatWidget
from ui.sidebar import Sidebar


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.assistant = DesktopAssistant()

        self.title("AI Desktop Assistant")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.configure(fg_color=BG)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.build_sidebar()

        self.build_main()

    # ------------------------------------------

    def build_sidebar(self):

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns",
            padx=15,
            pady=15
        )

        self.sidebar.screenshot.configure(
            command=lambda: self.execute_command(
                "take screenshot"
            )
        )

        self.sidebar.battery.configure(
            command=lambda: self.execute_command(
                "battery status"
            )
        )

        self.sidebar.time.configure(
            command=lambda: self.execute_command(
                "current time"
            )
        )

        self.sidebar.date.configure(
            command=lambda: self.execute_command(
                "current date"
            )
        )

    # ------------------------------------------

    def build_main(self):

        self.main = ctk.CTkFrame(
            self,
            fg_color=BG
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=15
        )

        self.main.grid_rowconfigure(1, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(

            self.main,

            text="🤖 AI Desktop Assistant",

            font=("Segoe UI", 28, "bold")

        )

        self.title_label.grid(
            row=0,
            column=0,
            pady=(10, 5)
        )

        self.status = ctk.CTkLabel(

            self.main,

            text="🟢 Ready",

            font=("Segoe UI", 16)

        )

        self.status.grid(
            row=0,
            column=1,
            padx=20
        )

        self.chat = ChatWidget(self.main)

        self.chat.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=20,
            pady=20
        )

        self.bottom = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.bottom.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=15
        )

        self.bottom.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(

            self.bottom,

            placeholder_text="Type a message..."

        )

        self.entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10)
        )

        self.entry.bind(
            "<Return>",
            self.send_message
        )

        self.send_button = ctk.CTkButton(

            self.bottom,

            text="Send",

            width=90,

            command=self.send_message

        )

        self.send_button.grid(
            row=0,
            column=1,
            padx=5
        )

        self.mic_button = ctk.CTkButton(

            self.bottom,

            text="🎤",

            width=60,

            command=self.listen

        )

        self.mic_button.grid(
            row=0,
            column=2
        )
        # ------------------------------------------

    def send_message(self, event=None):

        text = self.entry.get().strip()

        if not text:
            return

        self.entry.delete(0, "end")

        self.chat.add_user(text)

        self.status.configure(text="🟡 Thinking...")

        threading.Thread(
            target=self.process_text,
            args=(text,),
            daemon=True
        ).start()

    # ------------------------------------------

    def process_text(self, text):

        try:

            answer = self.assistant.process_text(text)

            if not answer:
                answer = "Done."

        except Exception as e:

            answer = str(e)

        self.after(
            0,
            lambda: self.finish_response(answer)
        )

    # ------------------------------------------

    def finish_response(self, answer):

        self.chat.add_ai(answer)

        self.status.configure(
            text="🟢 Ready"
        )

    # ------------------------------------------

    def listen(self):

        self.status.configure(
            text="🎤 Listening..."
        )

        threading.Thread(
            target=self.listen_worker,
            daemon=True
        ).start()

    # ------------------------------------------

    def listen_worker(self):

        try:

            text, answer = self.assistant.listen_once()

            if text:

                self.after(
                    0,
                    lambda: self.chat.add_user(text)
                )

            if answer:

                self.after(
                    0,
                    lambda: self.chat.add_ai(answer)
                )

        except Exception as e:

            self.after(
                0,
                lambda: self.chat.add_ai(str(e))
            )

        finally:

            self.after(
                0,
                lambda: self.status.configure(
                    text="🟢 Ready"
                )
            )
if __name__ == "__main__":

    app = MainWindow()

    app.mainloop()