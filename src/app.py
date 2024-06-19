import tkinter as tk
import keyboard
import pyautogui
import customtkinter as ctk
from concurrent.futures import ThreadPoolExecutor
from utils.llm import LLM
from utils.prompts import get_task_prompts
import pyperclip


class CopilotApp:
    """
    CopilotApp is a GUI application that provides a set of buttons to perform various text processing tasks.
    It uses a language model (LLM) to generate responses based on clipboard content and displays the results in a new window.
    """

    def __init__(self, root):
        self.llm = LLM()
        self.prompts = get_task_prompts()
        self.root = root
        self._initialize_root_window()
        self._create_layout()
        self._create_buttons()
        self.executor = ThreadPoolExecutor(max_workers=5)

    def _initialize_root_window(self):
        """
        Initialize the main application window with specific attributes.
        """
        self.root.title("Button Tree")
        self.root.geometry("400x300")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", self.root["bg"])
        self.root.withdraw()  # Hide the window initially

    def _create_layout(self):
        """
        Create the layout for the application, including frames for icon and buttons.
        """
        self.icon_frame = tk.Frame(self.root, width=100, height=100, bg=self.root["bg"])
        self.icon_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        self.buttons_frame = tk.Frame(self.root, bg=self.root["bg"])
        self.buttons_frame.grid(row=0, column=1, padx=10, pady=10)

        self.icon_label = tk.Label(
            self.icon_frame,
            text="✨",
            bg=self.root["bg"],
            font=("Roboto", 24),
            fg="yellow",
        )
        self.icon_label.pack()

    def _create_buttons(self):
        """
        Create buttons for different tasks and add them to the buttons frame.
        """
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

        tasks = [
            ("Summarize", 0),
            ("Compose Mail", 1),
            ("Fix Grammar", 2),
            ("Extract Keywords", 3),
            ("Explain", 4),
        ]

        for i, (text, index) in enumerate(tasks):
            button = ctk.CTkButton(
                self.buttons_frame,
                text=text,
                command=lambda i=index: self.on_button_click(i),
                **button_options,
            )
            button.grid(row=i, column=0, pady=5)

    def toggle_window(self):
        """
        Toggle the visibility of the main application window.
        """
        if self.root.state() == "withdrawn":
            x, y = pyautogui.position()
            self.root.geometry(f"+{x-50}+{y-100}")
            self.root.deiconify()
        else:
            self.root.withdraw()

    def on_button_click(self, task_index):
        """
        Handle button click events by triggering the corresponding task.
        """
        self.toggle_window()
        self.executor.submit(self.handle_button_click, task_index)

    def handle_button_click(self, task_index):
        """
        Execute the task corresponding to the clicked button.
        """
        prompt = self.prompts[task_index]["prompt"]
        prompt = prompt.format(text=pyperclip.paste())
        generated_text = self.llm.generate(prompt)
        pyperclip.copy(generated_text)
        self.root.after(0, self.show_generated_text, generated_text)

    def show_generated_text(self, text):
        """
        Display the generated text in a new, borderless window near the mouse cursor.
        """
        new_window = tk.Toplevel(self.root)
        new_window.title("Generated Text")
        new_window.geometry("600x400")
        new_window.overrideredirect(True)
        new_window.attributes("-transparentcolor", new_window["bg"])

        center_frame = ctk.CTkFrame(
            new_window,
            fg_color="white",
            corner_radius=10,
            width=580,
            height=380,
        )
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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
        text_box.configure(state="disabled")

        x, y = pyautogui.position()
        new_window.geometry(f"+{x-300}+{y-300}")

        def on_focus_out(event):
            if not new_window.focus_get():
                new_window.destroy()

        new_window.bind("<FocusOut>", on_focus_out)
        new_window.focus_force()


def main():
    root = ctk.CTk()
    app = CopilotApp(root)
    keyboard.add_hotkey("ctrl+space", app.toggle_window)
    root.mainloop()


if __name__ == "__main__":
    main()
