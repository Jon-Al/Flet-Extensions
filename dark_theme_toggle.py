import flet as ft


def theme_toggle_button(page: ft.Page, ft=None) -> ft.IconButton:
    """
    Creates a button that toggles between light and dark themes.

    :param page: The Flet page where the theme will be toggled.
    :return: An IconButton for theme switching.
    """
    
    def on_click(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            dark_light_text.value = "Dark theme"
            dark_light_icon.icon = ft.Icons.BRIGHTNESS_HIGH
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            dark_light_text.value = "Light theme"
            dark_light_icon.icon = ft.Icons.BRIGHTNESS_2
        page.update()
    
    dark_light_text = ft.Text("Light theme")
    dark_light_icon = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_2_OUTLINED,
        tooltip="Toggle brightness",
        on_click=on_click
    )
    return dark_light_icon
