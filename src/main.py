import flet as ft
from scraper import *

def main(page: ft.Page):
    page.title = "Rune Novel Reader"
    # page.vertical_alignment = ft.TextAlign.CENTER
    page.horizontal_alignment = ft.TextAlign.CENTER

    def home():
        page.clean()
        title = ft.Text(value="Rune Novel Reader", margin=25, size=24, color="#76e6a3")
        page.add(title, ft.Text(value="Placeholder", size=16), ft.Image(src="splash_android.png"), ft.Button("Read", on_click=read))

    def read():
        page.clean()
        content = ft.Text('"I always knew Dior was an idiot. It was just a matter of time."\n\n' \
        'Noel passed them without slowing, eyes forward, jaw tight.', size=16)
        page.add(ft.Text(value="\n"), content, ft.Divider(), ft.Button("Home", on_click=home))

    home()

if __name__ == "__main__":
    ft.run(main)