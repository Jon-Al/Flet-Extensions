from enum import Enum

import flet as ft


class Key(Enum):
    # Letters
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"

    # Digits
    DIGIT_0 = "0"
    DIGIT_1 = "1"
    DIGIT_2 = "2"
    DIGIT_3 = "3"
    DIGIT_4 = "4"
    DIGIT_5 = "5"
    DIGIT_6 = "6"
    DIGIT_7 = "7"
    DIGIT_8 = "8"
    DIGIT_9 = "9"

    # Function keys
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"
    F10 = "F10"
    F11 = "F11"
    F12 = "F12"

    # Special keys
    ENTER = "Enter"
    ESCAPE = "Escape"
    TAB = "Tab"
    SPACE = " "
    BACKSPACE = "Backspace"
    CONTEXT_MENU = "Context Menu"
    SHIFT = "Shift"
    CTRL = "Ctrl"
    ALT = "Alt"
    META = "Meta"
    INSERT = "Insert"
    DELETE = "Delete"
    HOME = "Home"
    END = "End"
    PAGE_UP = "Page Up"
    PAGE_DOWN = "Page Down"

    CAPS_LOCK = "Caps Lock"
    SCROLL_LOCK = "Scroll Lock"
    NUM_LOCK = "Num Lock"

    # Arrow keys
    ARROW_UP = "Arrow Up"
    ARROW_DOWN = "Arrow Down"
    ARROW_LEFT = "Arrow Left"
    ARROW_RIGHT = "Arrow Right"

    # Punctuation and symbols
    SEMICOLON = ";"
    EQUAL = "="
    COMMA = ","
    MINUS = "-"
    PERIOD = "."
    SLASH = "/"
    BACKQUOTE = "`"
    LEFT_BRACKET = "["
    BACKSLASH = "\\"
    RIGHT_BRACKET = "]"
    QUOTE = "'"

    # Numpad keys
    NUMPAD_0 = "Numpad 0"
    NUMPAD_1 = "Numpad 1"
    NUMPAD_2 = "Numpad 2"
    NUMPAD_3 = "Numpad 3"
    NUMPAD_4 = "Numpad 4"
    NUMPAD_5 = "Numpad 5"
    NUMPAD_6 = "Numpad 6"
    NUMPAD_7 = "Numpad 7"
    NUMPAD_8 = "Numpad 8"
    NUMPAD_9 = "Numpad 9"
    NUMPAD_DECIMAL = "Numpad Decimal"
    NUMPAD_DIVIDE = "Numpad Divide"
    NUMPAD_MULTIPLY = "Numpad Multiply"
    NUMPAD_SUBTRACT = "Numpad Subtract"
    NUMPAD_ADD = "Numpad Add"
    NUMPAD_ENTER = "Enter"

    def __lt__(self, other):
        if isinstance(other, Key):
            # Define ordering priority: modifiers first, then other keys
            modifiers = [Key.SHIFT, Key.CTRL, Key.ALT, Key.META]

            # If both are modifiers, use predefined order
            if self in modifiers and other in modifiers:
                return modifiers.index(self) < modifiers.index(other)

            # Modifiers come before regular keys
            if self in modifiers and other not in modifiers:
                return True

            if self not in modifiers and other in modifiers:
                return False

            # For non-modifiers, compare by name
            return self.name < other.name
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Key):
            # Use the inverse of __lt__
            lt_result = self.__lt__(other)
            if lt_result is NotImplemented:
                return NotImplemented
            return not lt_result and self != other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Key):
            return self < other or self == other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Key):
            return self > other or self == other
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Key):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == other
        return NotImplemented

    def __ne__(self, other):
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        return not eq_result

    def __hash__(self):
        return hash(self.name)

    def is_modifier(self):
        return self in [Key.SHIFT, Key.CTRL, Key.ALT, Key.META]

    def is_letter(self) -> bool:
        if not self.name:
            return False
        return self.name in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def is_digit(self):
        return self.name.startswith("DIGIT_")

    def is_function_key(self):
        return self.name.startswith("F") and self.name[1:].isdigit()

    def is_arrow(self):
        return self.name.startswith("ARROW_")

    def is_numpad(self):
        return self.name.startswith("NUMPAD_")


class KeyCombo:
    def __init__(self, *keys: Key):
        self.keys = frozenset(keys)  # Unordered set for O(1) lookups


def create_key_signature(pressed_key, shift=False, ctrl=False, alt=False, meta=False):
    modifiers = []
    if shift: modifiers.append("Shift")
    if ctrl: modifiers.append("Ctrl")
    if alt: modifiers.append("Alt")
    if meta: modifiers.append("Meta")
    return "+".join(sorted(modifiers) + [pressed_key])


def on_keyboard(e: ft.KeyboardEvent):
    """
    Example action
    """
    key: str = e.key
    shift: bool = e.shift
    ctrl: bool = e.ctrl
    alt: bool = e.alt
    meta: bool = e.meta
    return {
        "key":   key,
        "shift": shift,
        "ctrl":  ctrl,
        "alt":   alt,
        "meta":  meta}
