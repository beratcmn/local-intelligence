import flet as ft


def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 200
    page.bgcolor = "transparent"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.bgcolor = "transparent"
    page.window.resizable = False
    page.window.focused = True
    page.window.always_on_top = True

    page.add(
        ft.WindowDragArea(
            content=ft.Container(
                bgcolor="blue200",
                padding=10,
                content=ft.Text("Drag me around", size=30),
                animate_scale=ft.animation.Animation(100, "bounceInOut"),
                border_radius=30,
                shadow=ft.BoxShadow(
                    spread_radius=1, blur_radius=30, color="white", blur_style="outer"
                ),
            )
        )
    )


# ft.app(main, view=ft.AppView.WEB_BROWSER, port=5050)
ft.app(main)
