import tkinter as tk
import keyboard
import pyautogui
import customtkinter as ctk
from concurrent.futures import ThreadPoolExecutor
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
            fg="yellow",
        )
        self.icon_label.pack()

        # Add buttons
        button_options = {
            "width": 160,
            "height": 40,
            "corner_radius": 10,
            "fg_color": "white",
            "font": ("Roboto", 14, "normal"),
            "text_color": "#212121",
            "hover_color": "gray",
            "border_width": 1,
            "border_color": "#212121",
        }

        summarize_button = ctk.CTkButton(
            self.buttons_frame,
            text="Summarize",
            command=lambda i=0: self.on_button_click(i),
            **button_options,
        )
        summarize_button.grid(row=0, column=0, pady=5)

        compose_mail_button = ctk.CTkButton(
            self.buttons_frame,
            text="Compose Mail",
            command=lambda i=1: self.on_button_click(i),
            **button_options,
        )
        compose_mail_button.grid(row=1, column=0, pady=5)

        fix_grammer_button = ctk.CTkButton(
            self.buttons_frame,
            text="Fix Grammar",
            command=lambda i=2: self.on_button_click(i),
            **button_options,
        )
        fix_grammer_button.grid(row=2, column=0, pady=5)

        get_keywords_button = ctk.CTkButton(
            self.buttons_frame,
            text="Extract Keywords",
            command=lambda i=3: self.on_button_click(i),
            **button_options,
        )
        get_keywords_button.grid(row=3, column=0, pady=5)

        explain_button = ctk.CTkButton(
            self.buttons_frame,
            text="Explain",
            command=lambda i=4: self.on_button_click(i),
            **button_options,
        )
        explain_button.grid(row=4, column=0, pady=5)

        self.executor = ThreadPoolExecutor(max_workers=5)

    def toggle_window(self):
        if self.root.state() == "withdrawn":
            # Get the current mouse position
            x, y = pyautogui.position()
            self.root.geometry(f"+{x-50}+{y-100}")
            self.root.deiconify()
        else:
            self.root.withdraw()

    def on_button_click(self, task_index):
        self.toggle_window()
        self.executor.submit(self.handle_button_click, task_index)

    def handle_button_click(self, task_index):
        prompt = self.prompts[task_index]["prompt"]
        prompt = prompt.format(text=pyperclip.paste())
        generated_text = self.llm.generate(prompt)
        pyperclip.copy(generated_text)  # Automatically copy generated text to clipboard
        self.root.after(0, self.show_generated_text, generated_text)

    def show_generated_text(self, text):
        new_window = tk.Toplevel(self.root)
        new_window.title("Generated Text")
        new_window.geometry("600x400")
        new_window.overrideredirect(True)  # Make the window borderless

        # Make the window transparent
        new_window.attributes("-transparentcolor", new_window["bg"])

        # Center frame for rounded corners effect
        center_frame = ctk.CTkFrame(
            new_window,
            fg_color="white",
            corner_radius=10,
            width=580,
            height=380,
        )
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a CTkTextbox for text display with a scrollbar
        text_box = ctk.CTkTextbox(
            center_frame,
            wrap=tk.WORD,
            font=("Roboto", 18),
            corner_radius=10,
            border_width=1,
            border_color="#212121",
            width=560,
            height=360,
        )
        text_box.pack(expand=True, fill="both", padx=5, pady=5)
        text_box.insert(tk.END, text)
        text_box.configure(state="disabled")  # Make the text box read-only

        # Position the new window near the mouse cursor
        x, y = pyautogui.position()
        new_window.geometry(f"+{x-300}+{y-300}")

        # Function to close window if focus is lost
        def on_focus_out(event):
            if not new_window.focus_get():
                new_window.destroy()

        new_window.bind("<FocusOut>", on_focus_out)
        new_window.focus_force()  # Force focus to the new window


def main():
    root = ctk.CTk()
    app = ButtonTreeApp(root)

    # Bind the CTRL + Space key combination to toggle the button tree
    keyboard.add_hotkey("ctrl+space", app.toggle_window)

    root.mainloop()


if __name__ == "__main__":
    main()
