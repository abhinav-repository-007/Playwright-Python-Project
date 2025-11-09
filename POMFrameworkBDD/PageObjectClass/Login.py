from .Dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def launch_url(self):
        self.page.goto("https://rahulshettyacademy.com/client/")
        #We can send url name as well dynamically from terminal, hence copy the above line and paste in
            # conftest browser_selection fixture

    def login(self, userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
        #If we are 100% sure that post clicking login button Dashboard page will come, then we can make object for
            # Dashboard class here only to avoid extra code in test method.
        dashboard = DashboardPage(self.page)
        return dashboard
