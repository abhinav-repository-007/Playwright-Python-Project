from playwright.sync_api import expect


class PlacedOrderHistoryPage:

    def __init__(self, page):
        self.page = page

    def verify_order(self):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")