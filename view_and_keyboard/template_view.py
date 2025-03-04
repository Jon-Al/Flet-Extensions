import flet as ft
from typing_extensions import Sequence

from view_and_keyboard.example import main


class TemplateView(ft.View):
    def __init__(self, controls: Sequence[ft.Control] = None):
        super().__init__(
            controls=controls,
            scroll=ft.ScrollMode.AUTO,
            bgcolor=ft.Colors.random(),
            decoration=ft.BoxDecoration(border=ft.border.all(1, ft.Colors.OUTLINE))
        )
