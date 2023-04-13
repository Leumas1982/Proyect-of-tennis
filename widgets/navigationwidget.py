from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.properties import (
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout



Builder.load_string(
    """
<CustomBottomNavigation>:
    orientation: 'vertical'
    size_hint_y: .1
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'pomodoro'
            icon: 'clock'
            PopomodoroScreen:
        MDBottomNavigationItem:
            name: 'options'
            icon: 'cog'
            SettingsScreen:
        MDBottomNavigationItem:
            name: 'map'
            icon: 'map-marker'
            MapViewScreen:
    MDFlatButton:
        text: "Exit"
        theme_text_color: "Custom"
        text_color: "green"
        on_release: app.root.current = "start"
"""
)


class CustomBottomNavigation(MDBoxLayout):
    pass