import enum
import re
from datetime import datetime
from typing import Any, Optional, Union

import flet as ft
from dateutil import parser
from flet import DatePicker
from flet.core.animation import AnimationValue
from flet.core.badge import BadgeValue
from flet.core.date_picker import DatePickerEntryMode
from flet.core.text_style import StrutStyle
from flet.core.textfield import KeyboardType
from flet.core.tooltip import TooltipValue
from flet.core.types import (
    BorderRadiusValue,
    ColorValue,
    DurationValue,
    OffsetValue,
    OptionalControlEventCallable,
    PaddingValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue, DateTimeValue, )

name = "Date field"


class DatePickerPlacement(enum.Enum):
    BEFORE = DEFAULT = enum.auto()
    PREFIX = enum.auto()
    SUFFIX = enum.auto()
    DISABLED = enum.auto()


class DateField(ft.TextField):
    def __init__(
            self,
            current_date: DateTimeValue = datetime.now(),
            first_date: DateTimeValue = datetime(year=1900, month=1, day=1),
            last_date: DateTimeValue = datetime(year=2050, month=1, day=1),
            datepicker_placement: Optional[DatePickerPlacement] = DatePickerPlacement.DEFAULT,
            read_only: Optional[bool] = None,
            text_align: Optional[ft.TextAlign] = None,
            show_cursor: Optional[bool] = None,
            cursor_color: Optional[ColorValue] = None,
            cursor_error_color: Optional[ColorValue] = None,
            cursor_width: ft.OptionalNumber = None,
            cursor_height: ft.OptionalNumber = None,
            cursor_radius: ft.OptionalNumber = None,
            selection_color: Optional[ColorValue] = None,
            clip_behavior: Optional[ft.ClipBehavior] = None,
            mouse_cursor: Optional[ft.MouseCursor] = None,
            strut_style: Optional[StrutStyle] = None,
            on_submit: OptionalControlEventCallable = None,
            on_focus: OptionalControlEventCallable = None,
            on_blur: OptionalControlEventCallable = None,
            on_change: OptionalControlEventCallable = None,
            on_click: OptionalControlEventCallable = None,
            #
            # FormField
            #
            text_size: ft.OptionalNumber = None,
            text_style: Optional[ft.TextStyle] = None,
            text_vertical_align: Union[ft.VerticalAlignment, ft.OptionalNumber] = None,
            label: Optional[Union[str, ft.Control]] = "Input date",
            label_style: Optional[ft.TextStyle] = None,
            border: Optional[ft.InputBorder] = None,
            color: Optional[ColorValue] = None,
            bgcolor: Optional[ColorValue] = None,
            border_radius: Optional[BorderRadiusValue] = None,
            border_width: ft.OptionalNumber = None,
            border_color: Optional[ColorValue] = None,
            focused_color: Optional[ColorValue] = None,
            focused_bgcolor: Optional[ColorValue] = None,
            focused_border_width: ft.OptionalNumber = None,
            focused_border_color: Optional[ColorValue] = None,
            content_padding: Optional[PaddingValue] = None,
            dense: Optional[bool] = None,
            filled: Optional[bool] = None,
            fill_color: Optional[ColorValue] = None,
            hover_color: Optional[ColorValue] = None,
            hint_text: Optional[str] = "YYYY-MM-DD",
            hint_style: Optional[ft.TextStyle] = None,
            helper: Optional[ft.Control] = None,
            helper_text: Optional[str] = None,
            helper_style: Optional[ft.TextStyle] = None,
            counter: Optional[ft.Control] = None,
            counter_text: Optional[str] = None,
            counter_style: Optional[ft.TextStyle] = None,
            error_style: Optional[ft.TextStyle] = None,
            focus_color: Optional[ColorValue] = None,
            align_label_with_hint: Optional[bool] = None,
            hint_fade_duration: Optional[DurationValue] = None,
            hint_max_lines: Optional[int] = None,
            helper_max_lines: Optional[int] = None,
            error_max_lines: Optional[int] = None,
            size_constraints: Optional[ft.BoxConstraints] = None,
            collapsed: Optional[bool] = None,
            fit_parent_size: Optional[bool] = None,
            #
            # ConstrainedControl and AdaptiveControl
            #
            ref: Optional[ft.Ref] = None,
            key: Optional[str] = None,
            width: ft.OptionalNumber = None,
            height: ft.OptionalNumber = None,
            expand: Union[None, bool, int] = None,
            expand_loose: Optional[bool] = None,
            col: Optional[ResponsiveNumber] = None,
            opacity: ft.OptionalNumber = None,
            rotate: Optional[RotateValue] = None,
            scale: Optional[ScaleValue] = None,
            offset: Optional[OffsetValue] = None,
            aspect_ratio: ft.OptionalNumber = None,
            animate_opacity: Optional[AnimationValue] = None,
            animate_size: Optional[AnimationValue] = None,
            animate_position: Optional[AnimationValue] = None,
            animate_rotation: Optional[AnimationValue] = None,
            animate_scale: Optional[AnimationValue] = None,
            animate_offset: Optional[AnimationValue] = None,
            on_animation_end: OptionalControlEventCallable = None,
            tooltip: Optional[TooltipValue] = None,
            badge: Optional[BadgeValue] = None,
            visible: Optional[bool] = None,
            disabled: Optional[bool] = None,
            data: Any = None,
            rtl: Optional[bool] = None,
            adaptive: Optional[bool] = None):

        self.__date_patter = re.compile(r"^([0-9]{0,4})"
                                        r"^([0-9]{0,4})-"

                                        r"([0-9]{0,2}(?:-[0-9]{0,2})?)?")
        self._date_picker = DatePicker(value=None, date_picker_entry_mode=DatePickerEntryMode.CALENDAR_ONLY,
                                       on_change=self._on_dismiss,
                                       on_dismiss=self._on_dismiss, current_date=current_date,
                                       first_date=first_date, last_date=last_date)

        self._datepicker_button = ft.IconButton(
            icon=ft.Icons.EDIT_CALENDAR,
            tooltip="Open Date Picker",
            on_click=lambda e: self.page.open(self._date_picker) if self.page else None
        )

        # Call parent constructor with modified parameters
        super().__init__(
            value=self._date_to_string(self._date_picker.value, None),
            keyboard_type=KeyboardType.TEXT,
            multiline=False,
            min_lines=1,
            max_lines=1,
            password=False,
            can_reveal_password=False,
            read_only=read_only,
            shift_enter=False,
            text_align=text_align,
            autofocus=False,
            autocorrect=False,
            enable_suggestions=False,
            show_cursor=show_cursor,
            cursor_color=cursor_color,
            cursor_error_color=cursor_error_color,
            cursor_width=cursor_width,
            cursor_height=cursor_height,
            cursor_radius=cursor_radius,
            selection_color=selection_color,
            on_focus=on_focus,
            on_click=on_click,
            text_size=text_size,
            text_style=text_style,
            text_vertical_align=text_vertical_align,
            label=label,
            label_style=label_style,
            clip_behavior=clip_behavior,
            mouse_cursor=mouse_cursor,
            strut_style=strut_style,
            border=border,
            color=color,
            bgcolor=bgcolor,
            border_radius=border_radius,
            border_width=border_width,
            border_color=border_color,
            focused_color=focused_color,
            focused_bgcolor=focused_bgcolor,
            focused_border_width=focused_border_width,
            focused_border_color=focused_border_color,
            content_padding=content_padding,
            dense=dense,
            collapsed=collapsed,
            filled=filled,
            fill_color=fill_color,
            hover_color=hover_color,
            hint_text=hint_text,
            hint_style=hint_style,
            helper=helper,
            helper_text=helper_text,
            helper_style=helper_style,
            counter=counter,
            counter_text=counter_text,
            counter_style=counter_style,
            error_text="",
            error_style=error_style,
            focus_color=focus_color,
            align_label_with_hint=align_label_with_hint,
            hint_fade_duration=hint_fade_duration,
            hint_max_lines=hint_max_lines,
            helper_max_lines=helper_max_lines,
            error_max_lines=error_max_lines,
            size_constraints=size_constraints,
            fit_parent_size=fit_parent_size,
            ref=ref,
            key=key,
            width=width,
            height=height,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            badge=badge,
            visible=visible,
            disabled=disabled,
            data=data,
            rtl=rtl,
            adaptive=adaptive
        )
        self._datepicker_placement = None
        self.datepicker_placement = datepicker_placement
        self.on_submit = on_submit
        self.on_blur = on_blur
        self.on_change = on_change
        self._last_input = self.value

    @property
    def datepicker_placement(self):
        return self._datepicker_placement

    @datepicker_placement.setter
    def datepicker_placement(self, value: Optional[DatePickerPlacement]):
        if value == self._datepicker_placement:
            return
        match self._datepicker_placement:
            case DatePickerPlacement.DEFAULT | DatePickerPlacement.BEFORE:
                self.icon = None
            case DatePickerPlacement.PREFIX:
                self.prefix = None
            case DatePickerPlacement.SUFFIX:
                self.suffix = None
            case DatePickerPlacement.DISABLED:
                pass
        match value:
            case DatePickerPlacement.DEFAULT | DatePickerPlacement.BEFORE:
                self.icon = self._datepicker_button
            case DatePickerPlacement.PREFIX:
                self.prefix = self._datepicker_button
            case DatePickerPlacement.SUFFIX:
                self.suffix = self._datepicker_button
            case DatePickerPlacement.DISABLED:
                self._datepicker_button.visible = False
                self._datepicker_button.disabled = True
        self._datepicker_placement = value
        if self.page:
            self.update()

    @property
    def first_date(self):
        return self._date_picker.first_date

    @first_date.setter
    def first_date(self, value: Optional[datetime]):
        self._date_picker.first_date = value

    @property
    def current_date(self):
        return self._date_picker.current_date

    @property
    def last_date(self):
        return self._date_picker.last_date

    @last_date.setter
    def last_date(self, value: Optional[datetime]):
        self._date_picker.last_date = value

    @property
    def value(self) -> Optional[str]:
        return self._get_attr("value", def_value="")

    @value.setter
    def value(self, value: Optional[str]):
        if self._parse_date_string(value, None) is not None:
            self._set_attr("value", value)
        else:
            self._set_attr("value", '')

    def _on_dismiss(self, e):
        value = self._date_to_string(self._date_picker.value, None)
        if value is not None:
            self.value = value
            self.on_change(e)

    @property
    def date_value(self) -> datetime | None:
        return self._parse_date_string(self.value, None)

    @staticmethod
    def _parse_date_string(date: str, default: Any):
        try:
            r = parser.parse(date, dayfirst=False, yearfirst=True, fuzzy=False)
            return r
        except (ValueError, TypeError, parser.ParserError):
            return default

    @staticmethod
    def _date_to_string(date: datetime, default: Any):
        try:
            return datetime.strftime(date, "%Y-%m-%d")
        except (ValueError, TypeError, parser.ParserError):
            return default

    # on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler: OptionalControlEventCallable):
        def _on_change(e):
            if self.error_text is not None and len(self.value) <= 10:
                self.error_text = None
                self.update()
            if handler:
                handler(e)

        self._add_event_handler("change", _on_change)
        self._set_attr("onChange", True if _on_change is not None else None)

    # on_submit
    @property
    def on_submit(self) -> OptionalControlEventCallable:
        return self._get_event_handler("submit")

    @on_submit.setter
    def on_submit(self, handler: OptionalControlEventCallable):
        def _on_submit(e):
            result = self._parse_date_string(self.value, None)
            if result is not None:
                self.value = result.strftime("%Y-%m-%d")
                if handler:
                    handler(e)
            else:
                self.error_text = "Invalid entry; use YYYY-MM-DD format."
            self.update()
            self._last_input = self.value

        self._add_event_handler("submit", _on_submit)

    # on_blur
    @property
    def on_blur(self) -> OptionalControlEventCallable:
        return self._get_event_handler("blur")

    @on_blur.setter
    def on_blur(self, handler: OptionalControlEventCallable):
        def _on_blur(e):
            result = self._parse_date_string(self.value, None)
            if result is not None:
                self.value = result.strftime("%Y-%m-%d")
                if handler:
                    handler(e)
            elif len(self.value) == 0 and handler:
                handler(e)
            else:
                self.error_text = "Invalid; use YYYY-MM-DD format."
            self.update()
            self._last_input = self.value

        self._add_event_handler("blur", _on_blur)


def main(page: ft.Page):
    page.add(
        DateField()
    )


ft.app(target=main)
