import flet as ft

class Login(ft.UserControl):
    def __init__(self,page,*args, **kwargs):
        super().__init__()
        self.page = page
    def build(self):
        return ft.Column([ft.Row([ft.TextButton("Create Account",on_click=lambda _:self.page.go("/signup"))], alignment=ft.MainAxisAlignment.END),
                          ft.Row([ft.Text("Login", size = 30,weight="bold")],alignment=ft.MainAxisAlignment.CENTER),
                          ft.Row([ft.Text("Please enter your information below in order to login to your account.",width=275,text_align="center")], alignment=ft.MainAxisAlignment.CENTER),
                          ft.Container(content=ft.Column([
                              ft.Row([ft.Text("User Name:")]),
                              ft.Row([ft.TextField()]),
                              ft.Row([ft.Text("Password:")]),
                              ft.Row([ft.TextField()]),
                              ft.Row([ft.Text("Forgot password?")],ft.MainAxisAlignment.END),
                              ft.Row([ft.Container(content=ft.ElevatedButton("Login",expand=1,bgcolor="orange",color="white"),width=300,height=40,border_radius=15)],ft.MainAxisAlignment.CENTER),
                              ft.Row([ft.Text("Or use social media account for login")],alignment=ft.MainAxisAlignment.CENTER),
                              ]),padding=10)])

class Signup(ft.UserControl):
    def __init__(self,page,*args, **kwargs):
        super().__init__()
        self.page = page
    def build(self):
        return ft.Column([ft.Row([ft.IconButton(icon=ft.icons.ARROW_LEFT,on_click=lambda _:self.page.go("/"))], alignment=ft.MainAxisAlignment.START),
                          ft.Row([ft.Text("Sign Up", size = 30,weight="bold")],alignment=ft.MainAxisAlignment.CENTER),
                          ft.Row([ft.Text("Please enter your information below in order to login to your account.",width=275,text_align="center")], alignment=ft.MainAxisAlignment.CENTER),
                          ft.Container(content=ft.Column([
                              ft.Row([ft.Text("User Name:")]),
                              ft.Row([ft.TextField()]),
                              ft.Row([ft.Text("Email:")]),
                              ft.Row([ft.TextField()]),
                              ft.Row([ft.Text("Password:")]),
                              ft.Row([ft.TextField()]),
                              ft.Row([ft.Text("Confirm Password:")]),
                              ft.Row([ft.TextField()]),
                              ft.Row([ft.ElevatedButton("Sign Up",expand=1,bgcolor="orange",color="white")],ft.MainAxisAlignment.CENTER),
                              ft.Row([ft.Text("Or use social media account for login")],alignment=ft.MainAxisAlignment.CENTER),
                              ]),padding=ft.padding.only(left=10,right=10))])


def main(page: ft.Page):
    page.window.width = 360
    page.window.height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_chnage(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(ft.View("/",[Login(page)]))
        if page.route == "/signup":
            page.views.append(ft.View("/signup",[Signup(page)]))

        page.update()
    page.on_route_change = route_chnage
    page.go("/")


ft.app(main)
