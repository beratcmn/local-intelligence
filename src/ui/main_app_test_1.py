import flet as ft


def main(page: ft.Page):
    width = 300
    height = 300
    page.window.width = width
    page.window.height = height
    page.bgcolor = "transparent"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.bgcolor = "transparent"
    page.window.resizable = False
    page.window.focused = True
    page.window.always_on_top = True
    page.window.left = 1920 / 2 - width / 2
    page.window.top = 1080 / 2 - height / 2

    button_colors = ["#ED7D3A", "#1E90FF", "#0CCE6B", "#DCED31", "#EF2D56"]

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

    page.add(
        ft.Container(
            # alignment="center",
            content=ft.Row(
                controls=[
                    # ? Icon of the app
                    ft.WindowDragArea(
                        content=ft.Image(
                            "./assets/sparkles_72x72.png", width=72, height=72
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
    )


ft.app(main)
