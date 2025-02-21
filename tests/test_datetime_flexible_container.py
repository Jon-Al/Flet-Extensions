# Note: The Flet development team have yet to implement a testing suite, which leaves manual testing as the most time-effective approach for simple control.

import flet as ft

from auto_pickers.datetime_flexible_container import DateTimeFlag, DateTimeFlexibleContainer


def main(page: ft.Page):
    page.title = "DateTimeFlexibleContainer Test"

    def mode_changed(e):
        container.mode = DateTimeFlag(int(dropdown.value))
        page.update()

    dropdown = ft.Dropdown(
        label="Select Mode",
        options=[
            ft.dropdown.Option(key=str(DateTimeFlag.DATE), text="Date"),
            ft.dropdown.Option(key=str(DateTimeFlag.TIME), text="Time"),
            ft.dropdown.Option(key=str(DateTimeFlag.DATETIME), text="Date & Time"),
            ft.dropdown.Option(key=str(DateTimeFlag.AUTO_MODE), text="Auto Mode"),
            ft.dropdown.Option(key=str(DateTimeFlag.ALL), text="All Modes"),
        ],
        value=str(DateTimeFlag.ALL),
        on_change=mode_changed,
    )

    container = DateTimeFlexibleContainer(mode=DateTimeFlag.ALL)

    page.add(dropdown, container)


ft.app(target=main)
