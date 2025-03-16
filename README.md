# Various Flet Controls.

* [Dark Theme Toggle](https://github.com/Jon-Al/Flet_Extentions/blob/main/other/dark_theme_toggle.py) - an easy-to-use dark theme toggle. Uses icons.
* [Auto pickers](https://github.com/Jon-Al/Flet_Extentions/blob/main/auto_pickers) - Date and Time pickers with optional automatic buttons to pick `today`/`now` (respectively). All contained within a subclass of `ft.Container`. Requires all three classes to work.
* [Color Scheme MenuBar](https://github.com/Jon-Al/Flet-Extensions/tree/main/color_menu) - method to add a color scheme [MenuBar](https://flet-controls-gallery.fly.dev/navigation/menubar) to an existing application.
    * Pressing on the items will change the theme according to the chosen seed color.
    * Pressing on named items will copy them to the clipboard automatically.
    * Pressing on the 'Random' menu item will randomize the color scheme, and open a banner
        * The banner can be closed, or
    * Define your own custom themes in ``color_scheme_button.py``.
    * See the [example](https://github.com/Jon-Al/Flet-Extensions/blob/main/color_menu/color_scheme_menu_example.py) for more details.
* [Views and Keyboard Input Handler](https://github.com/Jon-Al/Flet-Extensions/tree/main/view_and_keyboard) - Proof of concept for keyboard inputs.
    * [KeyboardInputHandler](https://github.com/Jon-Al/Flet-Extensions/tree/main/view_and_keyboard/keyboard_input_handler.py) - A class to manage and handle keyboard inputs, instead of having to manage them individually. Uses a fairly simple system.
    * Also demonstrates hwo to work with Views.
    * See [example](https://github.com/Jon-Al/Flet-Extensions/tree/main/view_and_keyboard/example.py) for more information.
* [Date Field](https://github.com/Jon-Al/Flet-Extensions/tree/main/other/date_field.py) - A textfield with a DateInput, meant for inputting dates. Allows inputting dates without adding the overlay. Error on invalid entry is enabled, with a limited error checking. Uses python-dateutils 2.9.0. Contains an example in the file.

### Related Links

* [Felt GitHub repository](https://github.com/flet-dev/flet)
* [Flet website](https://flet.dev/)
  color_menu/color_scheme_menu_example.py

### Current requirements:

* flet: 0.27.6
* pytest: 8.3.4
* typing_extensions: 4.12.2
* python-dateutil: 2.9.0