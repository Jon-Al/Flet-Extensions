import flet as ft

name = "DatePickerContainer"


class DatePickerContainer(ft.Column):
    def __init__(self):
        super().__init__()
        self.datepicker = ft.DatePicker(
            on_change=self.change_date,
        )

        self.selected_date = ft.Text()

        self.controls = [
            ft.ElevatedButton(
                "Pick date",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=self.open_date_picker,
            ),
            self.selected_date,
        ]

    def open_date_picker(self, e):
        # self.datepicker.pick_date()
        e.control.page.open(self.datepicker)

    def change_date(self, e):
        self.selected_date.value = f"{self.datepicker.value}"
        e.control.page.update()

    @property
    def value(self):
        return self.selected_date.value

    @value.setter
    def value(self, value):
        self.selected_date.value = value
    

    @property
    def picker(self):
        return self.datepicker

    def did_mount(self):
        self.page.overlay.append(self.datepicker)
        self.page.update()

    def will_unmount(self):
        self.page.overlay.remove(self.datepicker)
        self.page.update()
