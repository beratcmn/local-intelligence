import tkinter as tk
import keyboard
import pyautogui
import customtkinter as ctk
from utils.llm import LLM
from utils.prompts import get_task_prompts
import pyperclip


class ButtonTreeApp:
    def __init__(self, root):
        self.llm = LLM()
        self.prompts = get_task_prompts()
        self.root = root
        self.root.title("Button Tree")
        self.root.geometry("400x300")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", self.root["bg"])
        self.root.withdraw()  # Hide the window initially

        # Create frames for layout
        self.icon_frame = tk.Frame(self.root, width=100, height=100, bg=self.root["bg"])
        self.icon_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        self.buttons_frame = tk.Frame(self.root, bg=self.root["bg"])
        self.buttons_frame.grid(row=0, column=1, padx=10, pady=10)

        # Add icon
        self.icon_label = tk.Label(
            self.icon_frame,
            text="✨",
            bg=self.root["bg"],
            font=("Roboto", 24),
            fg=("yellow"),
        )
        self.icon_label.pack()

        # Add buttons

        summarize_button = ctk.CTkButton(
            self.buttons_frame,
            text="Summarize",
            width=160,
            height=40,
            corner_radius=10,
            command=lambda i=0: self.on_button_click(i),
            fg_color="white",
            font=("Roboto", 14, "normal"),
            text_color="#212121",
            hover_color="gray",
        )
        summarize_button.grid(row=0, column=0, pady=5)

        compose_mail_button = ctk.CTkButton(
            self.buttons_frame,
            text="Compose Mail",
            width=160,
            height=40,
            corner_radius=10,
            command=lambda i=1: self.on_button_click(i),
            fg_color="white",
            font=("Roboto", 14, "normal"),
            text_color="#212121",
            hover_color="gray",
        )
        compose_mail_button.grid(row=1, column=0, pady=5)

        fix_grammer_button = ctk.CTkButton(
            self.buttons_frame,
            text="Fix Grammar",
            width=160,
            height=40,
            corner_radius=10,
            command=lambda i=2: self.on_button_click(i),
            fg_color="white",
            font=("Roboto", 14, "normal"),
            text_color="#212121",
            hover_color="gray",
        )
        fix_grammer_button.grid(row=2, column=0, pady=5)

        get_keywords_button = ctk.CTkButton(
            self.buttons_frame,
            text="Extract Keywords",
            width=160,
            height=40,
            corner_radius=10,
            command=lambda i=3: self.on_button_click(i),
            fg_color="white",
            font=("Roboto", 14, "normal"),
            text_color="#212121",
            hover_color="gray",
        )
        get_keywords_button.grid(row=3, column=0, pady=5)

    def toggle_window(self):
        if self.root.state() == "withdrawn":
            # Get the current mouse position
            x, y = pyautogui.position()
            self.root.geometry(f"+{x-50}+{y-100}")
            self.root.deiconify()
        else:
            self.root.withdraw()

    def on_button_click(self, task_index):
        prompt = self.prompts[task_index]["prompt"]
        prompt = prompt.format(text=pyperclip.paste())
        print(prompt)
        self.toggle_window()


def main():
    root = ctk.CTk()
    app = ButtonTreeApp(root)

    # Bind the Alt + Space key combination to toggle the button tree
    keyboard.add_hotkey("ctrl+space", app.toggle_window)

    root.mainloop()


if __name__ == "__main__":
    main()
