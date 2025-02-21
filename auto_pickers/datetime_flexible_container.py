import enum
from datetime import datetime
from enum import IntFlag
from flet import Row, Column, Container, ElevatedButton, Icons

from auto_pickers.date_picker_container import DatePickerContainer
from auto_pickers.time_picker_container import TimePickerContainer


class DateTimeFlag(IntFlag):
    DATE = enum.auto()
    TIME = enum.auto()
    DATETIME = DATE | TIME
    AUTO_MODE = enum.auto()
    ALL = DATETIME | AUTO_MODE


class DateTimeFlexibleContainer(Container):
    def __init__(self, mode):
        super().__init__()
        self._mode = None
        self._datepicker = None
        self._timepicker = None
        self._now_button = None
        self._today_button = None
        self.content = Row([Column()])
        self.mode = mode


    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

        self._datepicker = DatePickerContainer() if DateTimeFlag.DATE in value else None
        self._timepicker = TimePickerContainer() if DateTimeFlag.TIME in value else None
        self._now_button = ElevatedButton(
            text="Now", icon=Icons.ACCESS_TIME_FILLED, on_click=self._pick_now
        ) if self._timepicker and DateTimeFlag.AUTO_MODE in value else None

        self._today_button = ElevatedButton(
            text="Today", icon=Icons.CALENDAR_TODAY, on_click=self._pick_today
        ) if self._datepicker and DateTimeFlag.AUTO_MODE in value else None

        self._update_content()

    def _update_content(self):
        column_items = []
        if self._datepicker:
            column_items.append(self._datepicker)
        if self._timepicker:
            column_items.append(self._timepicker)
        if self._now_button:
            column_items.append(self._now_button)
        if self._today_button:
            column_items.append(self._today_button)

        self.content = Row([Column(column_items)])


    def _pick_now(self, e):
        if self._timepicker:
            self._timepicker.value = datetime.now().time()
            self.update()

    def _pick_today(self, e):
        if self._datepicker:
            self._datepicker.value = datetime.now().date()
            self.update()
