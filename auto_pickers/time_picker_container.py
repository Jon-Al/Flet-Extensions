import flet as ft


name = "TimePickerContainer"


class TimePickerContainer(ft.Column):
    def __init__(self):
        super().__init__()
        self._timepicker = ft.TimePicker(
            confirm_text="Confirm",
            error_invalid_text="Time out of range",
            help_text="Pick your time slot",
            on_change=self.change_time,
        )
        self.selected_time = ft.Text()

        self.controls = [
            ft.ElevatedButton(
                "Pick time",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=self.open_time_picker,
            ),
            self.selected_time,
        ]

    @property
    def value(self):
        return self.selected_time.value

    @value.setter
    def value(self, value):
        self.selected_time.value = value

    @property
    def picker(self):
        return self._timepicker

    def open_time_picker(self, e):
        e.control.page.open(self._timepicker)

    def change_time(self, e):
        self.selected_time.value = f"{self._timepicker.value}"
        e.control.page.update()

    def did_mount(self):
        self.page.overlay.append(self._timepicker)
        self.page.update()

    def will_unmount(self):
        self.page.overlay.remove(self._timepicker)
        self.page.update()
