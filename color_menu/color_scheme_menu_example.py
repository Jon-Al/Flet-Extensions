import flet as ft

from color_menu.color_menu_main import create_color_menu
from dark_theme_toggle import theme_toggle_button


name = "Theme colors"


def example():
    class Color:
        def __init__(self, display_name, name, is_dark=False):
            self.name = name
            self.display_name = display_name
            self.is_dark = is_dark

    theme_colors = [
        Color("PRIMARY", "primary"),
        Color("ON_PRIMARY", "onprimary"),
        Color("PRIMARY_CONTAINER", "primarycontainer"),
        Color("ON_PRIMARY_CONTAINER", "onprimarycontainer", True),
        Color("SECONDARY", "secondary"),
        Color("ON_SECONDARY", "onsecondary"),
        Color("SECONDARY_CONTAINER", "secondarycontainer"),
        Color("ON_SECONDARY_CONTAINER", "onsecondarycontainer", True),
        Color("TERTIARY", "tertiary"),
        Color("ON_TERTIARY", "ontertiary"),
        Color("TERTIARY_CONTAINER", "tertiarycontainer"),
        Color("ON_TERTIARY_CONTAINER", "ontertiarycontainer", True),
        Color("ERROR", "error"),
        Color("ON_ERROR", "onerror"),
        Color("ERROR_CONTAINER", "errorcontainer"),
        Color("ON_ERROR_CONTAINER", "onerrorcontainer", True),
        Color("OUTLINE", "outline"),
        Color("OUTLINE_VARIANT", "outlinevariant", True),
        Color("BACKGROUND", "background"),
        Color("ON_BACKGROUND", "onbackground", True),
        Color("SURFACE", "surface"),
        Color("ON_SURFACE", "onsurface", True),
        Color("SURFACE_TINT", "surfacetint"),
        Color("SURFACE_VARIANT", "surfacevariant"),
        Color("ON_SURFACE_VARIANT", "onsurfacevariant", True),
        Color("INVERSE_SURFACE", "inversesurface", True),
        Color("ON_INVERSE_SURFACE", "oninversesurface"),
        Color("INVERSE_PRIMARY", "inverseprimary"),
        Color("SHADOW", "shadow", True),
        Color("SCRIM", "scrim", True),
    ]

    def copy_to_clipboard(e):
        if e.page.theme.color_scheme:
            color_name = e.control.content.value
            color_value = getattr(e.page.theme.color_scheme, color_name.lower())
            e.control.page.set_clipboard(color_value)
            s = f"Copied to clipboard: {color_value}"
        else:
            e.control.page.set_clipboard(f"ft.Colors.{e.control.content.value}")
            s = f"Copied to clipboard: ft.Colors.{e.control.content.value}"

        e.control.page.open(
            ft.SnackBar(
                ft.Text(s),
                open=True,
            ))

    theme_colors_rows = ft.ResponsiveRow(spacing=0, expand=True)

    theme_colors_rows.controls = []

    for color in theme_colors:
        if color.is_dark:
            text_color = ft.Colors.SURFACE
        else:
            text_color = ft.Colors.ON_SURFACE

        theme_colors_rows.controls.append(
            ft.Container(
                bgcolor=color.name,
                content=ft.Text(color.display_name, color=text_color),
                alignment=ft.alignment.center,
                on_click=copy_to_clipboard,
                col=3,
                height=50
            )
        )

    return ft.Container(border_radius=10, content=theme_colors_rows)


def main(page: ft.Page):
    page.add(ft.Container(create_color_menu(page)))
    page.theme = ft.Theme()
    page.theme.color_scheme_seed = 'blue'
    page.add(example())
    page.update()
    page.add(theme_toggle_button(page))


if __name__ == "__main__":
    ft.app(target=main)
