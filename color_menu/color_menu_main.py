from dataclasses import dataclass
from enum import Enum
from typing import Optional, List

from flet import Page, Colors, Theme
from flet.core import alignment
from flet.core.banner import Banner
from flet.core.buttons import ButtonStyle
from flet.core.icon import Icon
from flet.core.icons import Icons
from flet.core.menu_bar import MenuStyle, MenuBar
from flet.core.menu_item_button import MenuItemButton
from flet.core.snack_bar import SnackBar
from flet.core.submenu_button import SubmenuButton
from flet.core.text import Text
from flet.core.text_button import TextButton
from flet.core.text_style import TextStyle
from flet.core.theme import ColorScheme
from flet.core.types import ColorValue

SHADES = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900"]
ACCENT_SHADES = ["100", "200", "400", "700"]
WHITE_SHADES = ["10", "12", "24", "30", "38", "54", "70"]
BLACK_SHADES = ["12", "26", "38", "45", "54", "87"]


class ColorSwatch:
    def __init__(self, name, display_name, accent=True):
        self.name = name
        self.display_name = display_name
        self.accent = accent


class Color:
    def __init__(self, swatch, shade="", accent=False):
        if shade == "":
            self.name = swatch.name
            self.display_name = swatch.display_name
        else:
            if not accent:
                self.name = f"{swatch.name}{shade}"
                self.display_name = f"{swatch.display_name}_{shade}"
            else:
                self.name = f"{swatch.name}accent{shade}"
                self.display_name = f"{swatch.display_name}_ACCENT_{shade}"


def apply_theme(page: Page, color: Colors):
    page.theme = Theme(color_scheme_seed=color)
    page.update()


def apply_scheme(page: Page, color_scheme: ColorScheme):
    page.theme = Theme(color_scheme=color_scheme)
    page.update()


def copy_to_clipboard(e):
    e.control.page.set_clipboard(f"ft.Colors.{e.control.content.value}")
    e.control.page.open(
        SnackBar(
            Text(f"Picked: ft.Colors.{e.control.content.value}"),
            open=True,
        )
    )


def generate_color_names(swatch):
    colors_buttons = []
    base_color = Color(swatch=swatch)
    colors_buttons.append(base_color)
    if swatch.name == "white":
        for shade in WHITE_SHADES:
            color = Color(swatch=swatch, shade=shade)
            colors_buttons.append(color)
        return colors_buttons
    if swatch.name == "black":
        for shade in BLACK_SHADES:
            color = Color(swatch=swatch, shade=shade)
            colors_buttons.append(color)
        return colors_buttons
    for shade in SHADES:
        color = Color(swatch=swatch, shade=shade)
        colors_buttons.append(color)
    if swatch.accent:
        for shade in ACCENT_SHADES:
            color = Color(swatch=swatch, shade=shade, accent=True)
            colors_buttons.append(color)
    return colors_buttons


def custom_color_scheme(
        primary: Optional[ColorValue] = None,
        on_primary: Optional[ColorValue] = None,
        primary_container: Optional[ColorValue] = None,
        on_primary_container: Optional[ColorValue] = None,
        secondary: Optional[ColorValue] = None,
        on_secondary: Optional[ColorValue] = None,
        secondary_container: Optional[ColorValue] = None,
        on_secondary_container: Optional[ColorValue] = None,
        tertiary: Optional[ColorValue] = None,
        on_tertiary: Optional[ColorValue] = None,
        tertiary_container: Optional[ColorValue] = None,
        on_tertiary_container: Optional[ColorValue] = None,
        error: Optional[ColorValue] = None,
        on_error: Optional[ColorValue] = None,
        error_container: Optional[ColorValue] = None,
        on_error_container: Optional[ColorValue] = None,
        background: Optional[ColorValue] = None,
        on_background: Optional[ColorValue] = None,
        surface: Optional[ColorValue] = None,
        on_surface: Optional[ColorValue] = None,
        surface_variant: Optional[ColorValue] = None,
        on_surface_variant: Optional[ColorValue] = None,
        outline: Optional[ColorValue] = None,
        outline_variant: Optional[ColorValue] = None,
        shadow: Optional[ColorValue] = None,
        scrim: Optional[ColorValue] = None,
        inverse_surface: Optional[ColorValue] = None,
        on_inverse_surface: Optional[ColorValue] = None,
        inverse_primary: Optional[ColorValue] = None,
        surface_tint: Optional[ColorValue] = None,
        on_primary_fixed: Optional[ColorValue] = None,
        on_secondary_fixed: Optional[ColorValue] = None,
        on_tertiary_fixed: Optional[ColorValue] = None,
        on_primary_fixed_variant: Optional[ColorValue] = None,
        on_secondary_fixed_variant: Optional[ColorValue] = None,
        on_tertiary_fixed_variant: Optional[ColorValue] = None,
        primary_fixed: Optional[ColorValue] = None,
        secondary_fixed: Optional[ColorValue] = None,
        tertiary_fixed: Optional[ColorValue] = None,
        primary_fixed_dim: Optional[ColorValue] = None,
        secondary_fixed_dim: Optional[ColorValue] = None,
        surface_bright: Optional[ColorValue] = None,
        surface_container: Optional[ColorValue] = None,
        surface_container_high: Optional[ColorValue] = None,
        surface_container_low: Optional[ColorValue] = None,
        surface_container_lowest: Optional[ColorValue] = None,
        surface_dim: Optional[ColorValue] = None,
        tertiary_fixed_dim: Optional[ColorValue] = None):
    return ColorScheme(
        primary=primary,
        on_primary=on_primary,
        primary_container=primary_container,
        on_primary_container=on_primary_container,
        secondary=secondary,
        on_secondary=on_secondary,
        secondary_container=secondary_container,
        on_secondary_container=on_secondary_container,
        tertiary=tertiary,
        on_tertiary=on_tertiary,
        tertiary_container=tertiary_container,
        on_tertiary_container=on_tertiary_container,
        error=error,
        on_error=on_error,
        error_container=error_container,
        on_error_container=on_error_container,
        background=background,
        on_background=on_background,
        surface=surface,
        on_surface=on_surface,
        surface_variant=surface_variant,
        on_surface_variant=on_surface_variant,
        outline=outline,
        outline_variant=outline_variant,
        shadow=shadow,
        scrim=scrim,
        inverse_surface=inverse_surface,
        on_inverse_surface=on_inverse_surface,
        inverse_primary=inverse_primary,
        surface_tint=surface_tint,
        on_primary_fixed=on_primary_fixed,
        on_secondary_fixed=on_secondary_fixed,
        on_tertiary_fixed=on_tertiary_fixed,
        on_primary_fixed_variant=on_primary_fixed_variant,
        on_secondary_fixed_variant=on_secondary_fixed_variant,
        on_tertiary_fixed_variant=on_tertiary_fixed_variant,
        primary_fixed=primary_fixed,
        secondary_fixed=secondary_fixed,
        tertiary_fixed=tertiary_fixed,
        primary_fixed_dim=primary_fixed_dim,
        secondary_fixed_dim=secondary_fixed_dim,
        surface_bright=surface_bright,
        surface_container=surface_container,
        surface_container_high=surface_container_high,
        surface_container_low=surface_container_low,
        surface_container_lowest=surface_container_lowest,
        surface_dim=surface_dim,
        tertiary_fixed_dim=tertiary_fixed_dim,
    )


def generate_random_color_scheme():
    return custom_color_scheme(
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(), Colors.random(),
        Colors.random()
    )


def color_scheme_text_list(scheme):
    t = []
    for i in dir(scheme):
        attr = getattr(scheme, i, None)
        if attr is None or i in ['__doc__', '__module__']:
            continue
        elif isinstance(attr, Enum):
            t.append(f"{i}: {attr.name}")
        elif isinstance(attr, str):
            t.append(f"{i}: {attr}")
    return t


def create_random_scheme_item(page: Page):
    scheme = generate_random_color_scheme()

    def close_banner(e):
        banner.open = False
        e.control.page.update()

    def copy_scheme(e):
        e.control.page.set_clipboard("\n".join(color_scheme_text_list(scheme)))
        e.control.page.update()

    def apply(e):
        nonlocal scheme
        scheme = generate_random_color_scheme()
        apply_scheme(page, scheme)
        banner.open = True
        page.update()

    banner = Banner(content=Text("Random scheme applied.\nPress 'Copy' to copy the scheme.\nPress 'Close' to close."),
                    actions=[
                        TextButton("Copy", icon=Icons.COPY, icon_color=Colors.ON_PRIMARY, on_click=copy_scheme, ),
                        TextButton("Close", icon=Icons.CLOSE, icon_color=Colors.ERROR, on_click=close_banner),
                    ], bgcolor=Colors.AMBER_100, )

    item = MenuItemButton(content=Text("Random"),
                          leading=Icon(Icons.QUESTION_MARK_SHARP),
                          on_click=apply)
    page.add(banner)
    return item


def create_color_menu_subitem(swatch: ColorSwatch, page: Page):
    colors = generate_color_names(swatch)
    subitems = []
    for color in colors:
        subitems.append(
            create_color_menu_item(color, page)
        )
    return SubmenuButton(
        content=Text(colors[0].display_name),
        style=ButtonStyle(
            bgcolor=colors[0].name
        ),
        expand=True,
        controls=subitems,
    )


@dataclass
class CustomScheme:
    scheme: ColorScheme
    name: str


def custom_color_scheme_menu_item(custom_scheme: CustomScheme, page: Page):
    def pick_scheme(e):
        copy_to_clipboard(e)
        apply_scheme(page, custom_scheme.scheme)
        page.update()

    return MenuItemButton(
        content=Text(custom_scheme.name),
        style=ButtonStyle(
            bgcolor=custom_scheme.scheme.secondary_container,
            text_style=TextStyle(color=custom_scheme.scheme.on_secondary_container),
        ),
        expand=True,
        on_click=pick_scheme,
    )


def create_custom_color_scheme_menu_subitem(schemes: List[CustomScheme], page: Page):
    menu_item = SubmenuButton(content=Text("Custom"))
    if not schemes:
        menu_item.controls.append(MenuItemButton(Text("No custom schemes added")))
    for s in schemes:
        menu_item.controls.append(custom_color_scheme_menu_item(s, page))
    return menu_item


def create_color_menu_item(color: Color, page: Page):
    def pick_color(e):
        copy_to_clipboard(e)
        apply_theme(page, e.control.style.bgcolor)
        page.update()

    return MenuItemButton(
        content=Text(color.name),
        style=ButtonStyle(
            bgcolor=color.name
        ),
        expand=True,
        on_click=pick_color,
    )


def create_color_menu(page: Page):
    custom_schemes: List[CustomScheme] = []  # Add custom schemes here.
    swatches = [
        ColorSwatch(name="red", display_name="RED"),
        ColorSwatch(name="pink", display_name="PINK"),
        ColorSwatch(name="purple", display_name="PURPLE"),
        ColorSwatch(name="deeppurple", display_name="DEEP_PURPLE"),
        ColorSwatch(name="indigo", display_name="INDIGO"),
        ColorSwatch(name="blue", display_name="BLUE"),
        ColorSwatch(name="lightblue", display_name="LIGHT_BLUE"),
        ColorSwatch(name="cyan", display_name="CYAN"),
        ColorSwatch(name="teal", display_name="TEAL"),
        ColorSwatch(name="green", display_name="GREEN"),
        ColorSwatch(name="lightgreen", display_name="LIGHT_GREEN"),
        ColorSwatch(name="lime", display_name="LIME"),
        ColorSwatch(name="yellow", display_name="YELLOW"),
        ColorSwatch(name="amber", display_name="AMBER"),
        ColorSwatch(name="orange", display_name="ORANGE"),
        ColorSwatch(name="deeporange", display_name="DEEP_ORANGE"),
        ColorSwatch(name="brown", display_name="BROWN", accent=False),
        ColorSwatch(name="grey", display_name="GREY", accent=False),
        ColorSwatch(name="bluegrey", display_name="BLUE_GREY", accent=False),
        ColorSwatch(name="white", display_name="WHITE"),
        ColorSwatch(name="black", display_name="BLACK"),
    ]
    menubar = MenuBar(
        expand=True,
        style=MenuStyle(
            alignment=alignment.top_left
        ), controls=[])
    menubar.controls.append(create_random_scheme_item(page))
    menubar.controls.append(create_custom_color_scheme_menu_subitem(custom_schemes, page))

    for swatch in swatches:
        menubar.controls.append(create_color_menu_subitem(swatch, page))
    return menubar
