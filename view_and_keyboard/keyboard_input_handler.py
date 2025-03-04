from typing import Union, Sequence, Any, Callable

import flet as ft

from view_and_keyboard.keyboard_keys import Key, KeyCombo


class KeyboardInputHandler:
    def __init__(self, page: ft.Page):
        self.__on_keyboard_event = None
        self.__on_key = {}
        self.page = page
        self.page.on_keyboard_event = self.__handle_keyboard_event

    def call_event(self, e: Union[ft.KeyboardEvent, Key, Sequence[Key], KeyCombo]):
        if isinstance(e, ft.KeyboardEvent):
            # Convert keyboard event to combo
            keys = []
            if e.key:
                pressed_key = next((k for k in Key if k.value == e.key), None)
                if pressed_key:
                    keys.append(pressed_key)
            if e.shift:
                keys.append(Key.SHIFT)
            if e.ctrl:
                keys.append(Key.CTRL)
            if e.alt:
                keys.append(Key.ALT)
            if e.meta:
                keys.append(Key.META)
            combo = KeyCombo(*keys)
        elif isinstance(e, Key):
            combo = KeyCombo(e)
        elif isinstance(e, KeyCombo):
            combo = e
        elif isinstance(e, (list, tuple)):
            combo = KeyCombo(*e)
        else:
            raise TypeError("Event must be KeyboardEvent, Key, Sequence[Key], or KeyCombo")

        # Find and call matching handler
        for registered_combo, (callback, params) in self.__on_key.items():
            if combo.keys == registered_combo.keys:
                if params is not None:
                    callback(e, params)
                else:
                    callback(e)
                return


    def add_on_key_event(self, keys: Union[Key, Sequence[Key], KeyCombo], on_key: Callable, params: Any = None) -> None:
        # Convert to KeyCombo for consistent handling
        if isinstance(keys, Key):
            combo = KeyCombo(keys)
        elif isinstance(keys, (list, tuple)):
            combo = KeyCombo(*keys)
        elif isinstance(keys, KeyCombo):
            combo = keys
        else:
            raise TypeError("keys must be Key, Sequence[Key], or KeyCombo")

        # Store the handler
        self.__on_key[combo] = (on_key, params)

        # Set up the keyboard event handler if not already set
        if not hasattr(self, '__on_keyboard_event') or not self.__on_keyboard_event:
            self.__on_keyboard_event = self.__handle_keyboard_event

    def __handle_keyboard_event(self, e: ft.KeyboardEvent) -> None:
        # Find the key enum matching the pressed key
        pressed_key = next((k for k in Key if k.value == e.key), None)
        if pressed_key is None:
            return

        # Build set of all active keys
        active_keys = {pressed_key}
        if e.shift: active_keys.add(Key.SHIFT)
        if e.ctrl: active_keys.add(Key.CTRL)
        if e.alt: active_keys.add(Key.ALT)
        if e.meta: active_keys.add(Key.META)

        active_combo = KeyCombo(*active_keys)

        # Find matching handler - O(1) lookup with frozenset equality
        for combo, (callback, params) in self.__on_key.items():
            if combo.keys == active_combo.keys:
                if params is not None:
                    callback(e, params)
                else:
                    callback(e)
                return

    def remove_on_key_event(self, key: Sequence[Key]) -> None:
        if isinstance(key, (list, tuple)):
            modifiers = sorted([k for k in key if k in (Key.SHIFT, Key.CTRL, Key.ALT, Key.META)])
            main_keys = [k for k in key if k not in (Key.SHIFT, Key.CTRL, Key.ALT, Key.META)]
            event_key = (*modifiers, *main_keys)
        else:
            event_key = (key,)

        if event_key in self.__on_key:
            del self.__on_key[event_key]
