# Various Flet Controls.

* [Dark Theme Toggle](https://github.com/Jon-Al/Flet_Extentions/blob/main/dark_theme_toggle.py) - an easy-to-use dark theme toggle. Uses icons.
* [Auto pickers](https://github.com/Jon-Al/Flet_Extentions/blob/main/auto_pickers) - Date and Time pickers with optional automatic buttons to pick `today`/`now` (respectively). All contained within a subclass of `ft.Container`. Requires all three classes to work.
* [Color Scheme MenuBar](https://github.com/Jon-Al/Flet_Extentions/blob/main/color_menu_main.py) - method to add a color scheme [MenuBar](https://flet-controls-gallery.fly.dev/navigation/menubar) to an existing application.
    * Pressing on the items will change the theme according to the chosen seed color.
    * Pressing on named items will copy them to the clipboard automatically.
    * Pressing on the 'Random' menu item will randomize the color scheme, and open a banner
        * The banner can be closed, or
    * Define your own custom themes in ``color_scheme_button.py``.
    * See the [example](https://github.com/Jon-Al/Flet-Extensions/blob/main/color_menu/color_scheme_menu_example.py) for more details.

### Related Links

* [Felt GitHub repository](https://github.com/flet-dev/flet)
* [Flet website](https://flet.dev/)
  color_menu/color_scheme_menu_example.py
