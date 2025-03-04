import flet as ft
from typing_extensions import Sequence


class TemplateView(ft.View):
    def __init__(self, controls: Sequence[ft.Control] = None):
        controls = list(controls) if controls else []
        controls.append(ft.Container(ft.Text("I am a text"),
                                     bgcolor=ft.Colors.random(),
                                     width=100,
                                     height=100))
        super().__init__(
            controls=controls,
            scroll=ft.ScrollMode.AUTO,
            decoration=ft.BoxDecoration(border=ft.border.all(1, ft.Colors.OUTLINE))
        )
