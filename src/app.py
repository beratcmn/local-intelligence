import tkinter as tk
import keyboard
import pyautogui
import customtkinter as ctk
from concurrent.futures import ThreadPoolExecutor
from utils.llm import LLM
from utils.prompts import get_task_prompts, get_editor_prompts
import pyperclip


class CopilotApp:
    """
    CopilotApp is a GUI application that provides a set of buttons to perform various text processing tasks.
    It uses a language model (LLM) to generate responses based on clipboard content and displays the results in a new window.
    """

    def __init__(self, root):
        self.llm = LLM()
        self.prompts = get_task_prompts()
        self.editor_prompts = get_editor_prompts()
        self.root = root
        self._initialize_root_window()
        self._create_layout()
        self._create_buttons()
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.drag_data = {"x": 0, "y": 0}  # Store the drag data
        self.border_color = "#363537"

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

        # Load the icon image
        self.icon_image = tk.PhotoImage(file="./assets/sparkles_72x72.png")

        self.icon_label = tk.Label(
            self.icon_frame,
            image=self.icon_image,
            bg=self.root["bg"],
            height=72,
            width=72,
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
            "font": ("Roboto", 18, "normal"),
            "text_color": "#363537",
            "hover_color": "gray",
            "border_width": 2,
            "border_color": "#363537",
        }

        tasks = [
            ("Summarize", 0),
            ("Compose Mail", 1),
            ("Fix Grammar", 2),
            ("Extract Keywords", 3),
            ("Explain", 4),
        ]

        colors = ["#ED7D3A", "#1E90FF", "#0CCE6B", "#DCED31", "#EF2D56"]

        for i, (text, index) in enumerate(tasks):
            button_options["border_color"] = colors[i]
            button_options["hover_color"] = colors[i]
            button = ctk.CTkButton(
                self.buttons_frame,
                text=text,
                command=lambda i=index: self.on_button_click(i, color=colors[i]),
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

    def on_button_click(self, task_index, color=None):
        """
        Handle button click events by triggering the corresponding task.
        """
        self.toggle_window()
        self.executor.submit(self.handle_button_click, task_index)
        self.border_color = color

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
        new_window.geometry("600x450")
        new_window.overrideredirect(True)
        new_window.attributes("-transparentcolor", new_window["bg"])

        center_frame = ctk.CTkFrame(
            new_window,
            fg_color="white",
            corner_radius=15,
            border_width=2,
            border_color=self.border_color,
            width=560,
            height=410,
        )
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, bordermode="outside")

        text_box = ctk.CTkTextbox(
            center_frame,
            wrap=tk.WORD,
            font=("Roboto", 18),
            corner_radius=10,
            fg_color="#212230",
            # border_width=1,
            # border_color="#363537",
            width=560,
            height=360,
        )
        text_box.pack(expand=True, fill="both", padx=(10, 10), pady=(10, 0))
        text_box.insert(tk.END, text)
        text_box.configure(state="disabled")

        # Create buttons for editing text
        edit_buttons_frame = ctk.CTkFrame(center_frame, fg_color="white")
        edit_buttons_frame.pack(padx=10, pady=10)

        edit_button_options = {
            "width": 100,
            "height": 40,
            "corner_radius": 10,
            "fg_color": "white",
            "font": ("Roboto", 16, "normal"),
            "text_color": "#363537",
            "hover_color": "gray",
            "border_width": 2,
            "border_color": "#363537",
        }

        edit_button_fg_colors = ["#ED7D3A", "#1E90FF", "#0CCE6B", "#EF2D56", "#DCED31"]

        edit_tasks = ["Casual", "Formal", "Professional", "Technical", "Simple"]

        for i, task in enumerate(edit_tasks):
            edit_button_options["border_color"] = edit_button_fg_colors[i]
            edit_button_options["hover_color"] = edit_button_fg_colors[i]
            edit_button = ctk.CTkButton(
                edit_buttons_frame,
                text=task,
                command=lambda t=task: self.edit_text(t, text, text_box),
                **edit_button_options,
            )
            edit_button.grid(row=0, column=i, padx=5)

        x, y = pyautogui.position()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Adjust the window position to stay within screen boundaries
        window_width = 600
        window_height = 450

        x = min(max(0, x - window_width // 2), screen_width - window_width)
        y = min(max(0, y - window_height // 2), screen_height - window_height)

        new_window.geometry(f"+{x}+{y}")

        def on_focus_out(event):
            if not new_window.focus_get():
                new_window.destroy()

        new_window.bind("<FocusOut>", on_focus_out)
        new_window.focus_force()

        # Bind mouse events for dragging the window
        center_frame.bind(
            "<Button-1>", lambda event: self.start_drag(event, new_window)
        )
        center_frame.bind("<B1-Motion>", lambda event: self.do_drag(event, new_window))

    def start_drag(self, event, window):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def do_drag(self, event, window):
        x = window.winfo_x() + event.x - self.drag_data["x"]
        y = window.winfo_y() + event.y - self.drag_data["y"]
        window.geometry(f"+{x}+{y}")

    def edit_text(self, task, text, text_box):
        """
        Handle text editing tasks. Implement the logic as needed.
        """
        editor_prompt = next(
            (item for item in self.editor_prompts if item["editor"] == task), None
        )

        if editor_prompt:
            prompt = editor_prompt["prompt"]
            prompt = prompt.format(text=text)
            generated_text = self.llm.generate(prompt)
            pyperclip.copy(generated_text)
            text_box.configure(state="normal")
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, generated_text)
            text_box.configure(state="disabled")


def main():
    root = ctk.CTk()
    app = CopilotApp(root)
    keyboard.add_hotkey("ctrl+space", app.toggle_window)
    root.mainloop()


if __name__ == "__main__":
    main()
