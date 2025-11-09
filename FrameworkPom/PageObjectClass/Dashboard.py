from .OrderDetails import OrderDetailsPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def click_orders(self):
        self.page.get_by_role("button", name="ORDERS").click()
        # If we are 100% sure that post clicking Orders button Order details page will come,
            # then we can make object for OrderDetailsPage class here only to avoid extra code in test method.
        order_details = OrderDetailsPage(self.page)
        return order_details
