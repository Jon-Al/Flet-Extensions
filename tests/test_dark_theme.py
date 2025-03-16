import pytest
import flet as ft
from unittest.mock import MagicMock

from other.dark_theme_toggle import theme_toggle_button


@pytest.fixture
def mock_page():
    """Creates a mock Flet page."""
    page = MagicMock(spec=ft.Page)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update = MagicMock()
    return page


def test_theme_toggle_button(mock_page):
    """Tests the theme toggle button's functionality with rapid clicks."""
    button = theme_toggle_button(mock_page)

    # Ensure initial state
    assert mock_page.theme_mode == ft.ThemeMode.LIGHT
    assert button.icon == ft.Icons.BRIGHTNESS_2_OUTLINED

    # Simulate rapid clicks
    for _ in range(5):
        button.on_click(None)

    # Odd number of clicks should leave it in DARK mode
    assert mock_page.theme_mode == ft.ThemeMode.DARK
    assert button.icon == ft.Icons.BRIGHTNESS_HIGH

    # Simulate more rapid clicks
    for _ in range(3):
        button.on_click(None)

    # Total clicks = 8, so it should be back to LIGHT mode
    assert mock_page.theme_mode == ft.ThemeMode.LIGHT
    assert button.icon == ft.Icons.BRIGHTNESS_2

    mock_page.update.assert_called()
