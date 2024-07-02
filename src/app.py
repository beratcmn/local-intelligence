import flet as ft
from pathlib import Path
import pyautogui
import keyboard
from utils.llm import LLM
from utils.prompts import get_task_prompts, get_editor_prompts
from concurrent.futures import ThreadPoolExecutor
import pyperclip

executor = ThreadPoolExecutor(max_workers=5)
prompts = get_task_prompts()
editor_prompts = get_editor_prompts()
llm = LLM()


def main(page: ft.Page):
    page.title = "Local Intelligence App"
    width = 300
    height = 300
    page.window_width = width
    page.window_height = height
    page.bgcolor = "transparent"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_bgcolor = "transparent"
    page.window_resizable = False
    page.window_focused = True
    page.window_always_on_top = True
    page.window_visible = False
    # page.window_skip_task_bar = True

    button_colors = ["#ED7D3A", "#1E90FF", "#0CCE6B", "#DCED31", "#EF2D56"]
    components = {}

    def toggle_window():
        print("Changing visibility")
        if page.window_visible:
            page.window_visible = False
            page.update()
        else:
            width = 300
            height = 300
            page.window_width = width
            page.window_height = height
            page.window_visible = True
            x, y = pyautogui.position()
            page.window_left = x - width / 2 + 100
            page.window_top = y - height / 2
            page.controls.clear()
            page.add(components["main_view"])
            page.update()

    def hover_zoom_effect(e):
        if e.data == "true":
            e.control.scale = ft.transform.Scale(1.1)
        else:
            e.control.scale = ft.transform.Scale(1)

        page.update()

    def hover_color_effect(e, index=0):
        if e.data == "true":
            e.control.style.bgcolor = button_colors[index]
        else:
            e.control.style.bgcolor = "white"

        page.update()

    def show_generated_text(text, task_index):
        """
        Display the generated text in a new, borderless window near the mouse cursor.
        """

        width = 600
        height = 400
        page.window_width = width
        page.window_height = height
        page.window_visible = True
        x, y = pyautogui.position()
        page.window_left = x - width / 2
        page.window_top = y - height / 2
        page.controls.clear()
        page.add(
            ft.Container(
                width=width - 10,
                height=height - 10,
                bgcolor="white",
                border_radius=10,
                border=ft.Border(
                    top=ft.BorderSide(width=5, color=button_colors[task_index]),
                    bottom=ft.BorderSide(width=5, color=button_colors[task_index]),
                    left=ft.BorderSide(width=5, color=button_colors[task_index]),
                    right=ft.BorderSide(width=5, color=button_colors[task_index]),
                ),
                padding=ft.padding.only(right=10, left=10),
                content=ft.Column(
                    spacing=0,
                    tight=True,
                    controls=[
                        # ? Close Button
                        ft.WindowDragArea(
                            maximizable=False,
                            content=ft.Container(
                                width=width - 20,
                                height=30,
                                bgcolor="transparent",
                                padding=0,
                                alignment=ft.alignment.center_right,
                                content=ft.IconButton(
                                    icon=ft.icons.CLOSE,
                                    icon_color="red",
                                    alignment=ft.alignment.center_right,
                                    on_click=lambda e: toggle_window(),
                                ),
                            ),
                        ),
                        # ? Text Area
                        ft.Column(
                            scroll=ft.ScrollMode.ALWAYS,
                            height=height - 50,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(bottom=20),
                                    content=ft.Text(
                                        value=text,
                                        size=16,
                                        color="black",
                                        selectable=True,
                                        overflow=ft.TextOverflow.VISIBLE,
                                        # height=height,
                                    ),
                                )
                            ],
                        ),
                    ],
                ),
            )
        )

        page.update()

    def handle_task_button_click(task_index):
        global prompts
        """
        Execute the task corresponding to the clicked button.
        """
        prompt = prompts[task_index]["prompt"]
        prompt = prompt.format(text=pyperclip.paste())
        generated_text = llm.generate(prompt)
        pyperclip.copy(generated_text)
        print("Generated text:", generated_text)
        show_generated_text(generated_text, task_index)

    def on_task_button_click(task_index):
        print(f"Task {task_index} clicked")
        page.window_visible = False
        page.update()
        executor.submit(handle_task_button_click, task_index)
        # show_generated_text("Generated text", task_index)

    keyboard.add_hotkey("ctrl+space", toggle_window)

    components = {
        "main_view": ft.Container(
            # alignment="center",
            content=ft.Row(
                controls=[
                    # ? Icon of the app
                    ft.WindowDragArea(
                        maximizable=False,
                        content=ft.Image(
                            (
                                Path(__file__).parent.parent
                                / "assets/sparkles_72x72.png"
                            ),
                            width=72,
                            height=72,
                        ),
                    ),
                    # ? Column of Buttons for the app: Summarize, Compose Mail, Fix Grammar, Extract Keywords, Explain tasks.
                    ft.Column(
                        controls=[
                            # ? Summarize Button
                            ft.Container(
                                on_hover=hover_zoom_effect,
                                animate_scale=ft.animation.Animation(
                                    100, "bounceInOut"
                                ),
                                content=ft.FilledButton(
                                    text="Summarize",
                                    width=160,
                                    height=40,
                                    on_hover=lambda e: hover_color_effect(e, 0),
                                    on_click=lambda e: on_task_button_click(0),
                                    style=ft.ButtonStyle(
                                        bgcolor="white",
                                        side=ft.BorderSide(
                                            width=2, color=button_colors[0]
                                        ),
                                    ),
                                ),
                            ),
                            # ? Compose Mail Button
                            ft.Container(
                                on_hover=hover_zoom_effect,
                                animate_scale=ft.animation.Animation(
                                    100, "bounceInOut"
                                ),
                                content=ft.FilledButton(
                                    text="Compose Mail",
                                    width=160,
                                    height=40,
                                    on_hover=lambda e: hover_color_effect(e, 1),
                                    on_click=lambda e: on_task_button_click(1),
                                    style=ft.ButtonStyle(
                                        bgcolor="white",
                                        side=ft.BorderSide(
                                            width=2, color=button_colors[1]
                                        ),
                                    ),
                                ),
                            ),
                            # ? Fix Grammar Button
                            ft.Container(
                                on_hover=hover_zoom_effect,
                                animate_scale=ft.animation.Animation(
                                    100, "bounceInOut"
                                ),
                                content=ft.FilledButton(
                                    text="Fix Grammar",
                                    width=160,
                                    height=40,
                                    on_hover=lambda e: hover_color_effect(e, 2),
                                    on_click=lambda e: on_task_button_click(2),
                                    style=ft.ButtonStyle(
                                        bgcolor="white",
                                        side=ft.BorderSide(
                                            width=2, color=button_colors[2]
                                        ),
                                    ),
                                ),
                            ),
                            # ? Extract Keywords Button
                            ft.Container(
                                on_hover=hover_zoom_effect,
                                animate_scale=ft.animation.Animation(
                                    100, "bounceInOut"
                                ),
                                content=ft.FilledButton(
                                    text="Extract Keywords",
                                    width=160,
                                    height=40,
                                    on_hover=lambda e: hover_color_effect(e, 3),
                                    on_click=lambda e: on_task_button_click(3),
                                    style=ft.ButtonStyle(
                                        bgcolor="white",
                                        side=ft.BorderSide(
                                            width=2, color=button_colors[3]
                                        ),
                                    ),
                                ),
                            ),
                            # ? Explain Button
                            ft.Container(
                                on_hover=hover_zoom_effect,
                                animate_scale=ft.animation.Animation(
                                    100, "bounceInOut"
                                ),
                                content=ft.FilledButton(
                                    text="Explain",
                                    width=160,
                                    height=40,
                                    on_hover=lambda e: hover_color_effect(e, 4),
                                    on_click=lambda e: on_task_button_click(4),
                                    style=ft.ButtonStyle(
                                        bgcolor="white",
                                        side=ft.BorderSide(
                                            width=2, color=button_colors[4]
                                        ),
                                    ),
                                ),
                            ),
                        ]
                    ),
                ]
            ),
        )
    }

    page.add(ft.Container())


ft.app(main)
