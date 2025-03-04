import flet as ft

from view_and_keyboard.keyboard_input_handler import KeyboardInputHandler
from view_and_keyboard.keyboard_keys import Key
from view_and_keyboard.template_view import TemplateView


def main(page: ft.Page):
    view_pop_history = []

    def last_view(e):
        if len(view_pop_history) > 0:
            page.views.append(view_pop_history.pop())
            page.update()
            print(f'last view: view history: {len(view_pop_history)} page.views: {len(page.views)}')

    def next_view(e):
        if len(page.views) > 0:
            view_pop_history.append(page.views.pop())
            page.update()
            print(f'next view: view history: {len(view_pop_history)} page.views: {len(page.views)}')

    demo_text = ft.Text("Demo Text")
    last_view_button = ft.Button("Last View", on_click=lambda e: last_view(e))
    next_view_button = ft.Button("Next View", on_click=lambda e: next_view(e))
    views = [TemplateView([demo_text, last_view_button, next_view_button]) for i in range(10)]
    for v in views:
        v.controls.append(ft.Text(f"{v.bgcolor}"))
        page.views.append(v)
    page.add(ft.Text("Another Text"))
    page.add(last_view_button)
    page.add(next_view_button)
    kih = KeyboardInputHandler(page)
    kih.add_on_key_event([Key.ARROW_LEFT, Key.CTRL], next_view)
    kih.add_on_key_event([Key.ARROW_RIGHT, Key.CTRL], last_view)
    page.on_keyboard_event = kih.call_event
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
