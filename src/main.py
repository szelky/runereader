import flet as ft

def main(page: ft.Page):
    page.title = "Rune Novel Reader"
    # page.vertical_alignment = ft.TextAlign.CENTER
    page.horizontal_alignment = ft.TextAlign.CENTER
    result = ft.Text(value="Rune Novel Reader", margin=40, size=20, color="#76e6a3")

    page.add(result)

ft.run(main)