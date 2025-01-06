import flet as ft


def main(page:ft.Page):
    page.title = "Multi-Page Navigation Example"
    page.theme_mode = "light"

    def home_page():
        return ft.View(
            "/home",
            controls=[
                ft.Text("Welcome to the Home Page!", size=24, weight="bold"),
                ft.Text("Use the navigation bar to switch pages."),
            ],
            appbar=ft.AppBar(title=ft.Text("Home")),
            navigation_bar=navigation_bar("home"),
        )
    def settings_page():
        return ft.View(
            "/settings",
            controls=[
                ft.Text("Settings Page", size=24, weight="bold"),
                ft.Text("Here you can configure your preferences."),
            ],
            appbar=ft.AppBar(title=ft.Text("Settings")),
            navigation_bar=navigation_bar("settings"),
        )   
    def about_page():    
        return ft.View(
            "/about",
            controls=[
                ft.Text("About Page", size=24, weight="bold"),
                ft.Text("Learn more about this application."),
            ],
            appbar=ft.AppBar(title=ft.Text("About")),
            navigation_bar=navigation_bar("about"),
        )   

    def navigate_to(page_name):
        page.views.clear()
        if page_name == "home":
            page.views.append(home_page())
        elif page_name == "settings":
            page.views.append(settings_page())
        elif page_name == "about":
            page.views.append(about_page())
        page.update()

    def navigation_bar(selected_page):
        return ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),  
                ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Settings"), 
                ft.NavigationBarDestination(icon=ft.icons.INFO, label="About")],
                selected_index=["home", "settings", "about"].index(selected_page),
                on_change=lambda e: navigate_to(["home", "settings", "about"][e.control.selected_index]),)
    
    
    page.views.append(home_page())
    page.update()

    
ft.app(target=main, assets_dir="assets")
    