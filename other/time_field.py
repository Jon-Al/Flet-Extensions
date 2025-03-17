from datetime import datetime, time
from typing import Any, Optional, Union

import flet as ft
from dateutil import parser
from flet import TimePicker
from flet.core.animation import AnimationValue
from flet.core.badge import BadgeValue
from flet.core.text_style import StrutStyle
from flet.core.textfield import KeyboardType
from flet.core.time_picker import TimePickerEntryMode
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
    ScaleValue, )

from other.placement import Placement


class TimeField(ft.TextField):
    def __init__(
            self,
            current_time: Optional[time] = datetime.now().time(),
            timepicker_placement: Optional[Placement] = Placement.DEFAULT,
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
            label: Optional[Union[str, ft.Control]] = "Input time",
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
            hint_text: Optional[str] = "HH:MM (AM/PM)",
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
        self._time_picker = TimePicker(value=current_time, time_picker_entry_mode=TimePickerEntryMode.DIAL_ONLY,
                                       on_change=self._on_dismiss,
                                       on_dismiss=self._on_dismiss)

        self._timepicker_button = ft.IconButton(
            icon=ft.Icons.TIMER,
            tooltip="Open Time Picker",
            on_click=lambda e: self.page.open(self._time_picker) if self.page else None
        )

        # Call parent constructor with modified parameters
        super().__init__(
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
        self._timepicker_placement = None
        self.timepicker_placement = timepicker_placement
        self.on_submit = on_submit
        self.on_blur = on_blur
        self.on_change = on_change
        # Initialize with the current time in HH:MM format
        if current_time:
            self.value = current_time.strftime("%H:%M")
        else:
            self.value = datetime.now().time().strftime("%H:%M")
        self._last_input = self.value

    @property
    def timepicker_placement(self):
        return self._timepicker_placement

    @timepicker_placement.setter
    def timepicker_placement(self, value: Optional[Placement]):
        if value == self._timepicker_placement:
            return
        match self._timepicker_placement:
            case Placement.DEFAULT | Placement.BEFORE:
                self.icon = None
            case Placement.PREFIX:
                self.prefix = None
            case Placement.SUFFIX:
                self.suffix = None
            case Placement.DISABLED:
                pass
        match value:
            case Placement.DEFAULT | Placement.BEFORE:
                self.icon = self._timepicker_button
            case Placement.PREFIX:
                self.prefix = self._timepicker_button
            case Placement.SUFFIX:
                self.suffix = self._timepicker_button
            case Placement.DISABLED:
                self._timepicker_button.visible = False
                self._timepicker_button.disabled = True
        self._timepicker_placement = value
        if self.page:
            self.update()

    @property
    def value(self) -> Optional[str]:
        return self._get_attr("value", def_value="")

    @value.setter
    def value(self, value: Optional[str]):
        if self._parse_time_string(value, None) is not None:
            self._set_attr("value", value)
        else:
            self._set_attr("value", '')

    def _on_dismiss(self, e):
        if self._time_picker.value:
            value = self._time_to_string(self._time_picker.value, None)
            if value is not None:
                self.value = value
                self.on_change(e)

    @property
    def time_value(self) -> time | None:
        return self._parse_time_string(self.value, None)

    @staticmethod
    def _parse_time_string(time_str: str, default: Any) -> time | None:
        try:
            # Try parsing various time formats
            if time_str is None or time_str.strip() == '':
                return default

            # Handle 24-hour format (HH:MM)
            if ':' in time_str and len(time_str.split(':')) == 2:
                hour, minute = map(int, time_str.split(':'))
                if 0 <= hour < 24 and 0 <= minute < 60:
                    return time(hour, minute)

            # Try using dateutil parser as fallback
            parsed_time = parser.parse(time_str).time()
            return parsed_time
        except (ValueError, TypeError, parser.ParserError):
            return default

    @staticmethod
    def _time_to_string(time_value: time, default: Any) -> str | None:
        try:
            return time_value.strftime("%H:%M")
        except (ValueError, TypeError, AttributeError):
            return default

    # on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler: OptionalControlEventCallable):
        def _on_change(e):
            if self.error_text is not None and len(self.value) <= 5:
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
            result = self._parse_time_string(self.value, None)
            if result is not None:
                self.value = result.strftime("%H:%M")
                if handler:
                    handler(e)
            else:
                self.error_text = "Invalid entry; use HH:MM (24H) format."
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
            result = self._parse_time_string(self.value, None)
            if result is not None:
                self.value = result.strftime("%H:%M")
                if handler:
                    handler(e)
            elif len(self.value) == 0 and handler:
                handler(e)
            else:
                self.error_text = "Invalid; use HH:MM format."
            self.update()
            self._last_input = self.value

        self._add_event_handler("blur", _on_blur)


def main(page: ft.Page):
    page.add(
        TimeField()
    )


ft.app(target=main)
