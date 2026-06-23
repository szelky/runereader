import flet as ft
from scraper import *

def main(page: ft.Page):
    page.title = "Rune Novel Reader"
    # page.vertical_alignment = ft.TextAlign.CENTER
    page.horizontal_alignment = ft.TextAlign.CENTER

    def home():
        page.clean()
        title = ft.Text(value="Rune Novel Reader", margin=25, size=20, color="#76e6a3")
        page.add(title, ft.Text(value="test"), ft.Button("Read", on_click=read))

    def read():
        page.clean()
        test = ft.Text('"I always knew Dior was an idiot. It was just a matter of time."\n\n' \
        'Noel passed them without slowing, eyes forward, jaw tight.', size=16, margin=25)
        page.add(test, ft.Button("Home", on_click=home))

    home()

ft.run(main)