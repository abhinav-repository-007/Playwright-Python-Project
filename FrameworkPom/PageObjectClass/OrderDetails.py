from .PlacedOrderHistory import PlacedOrderHistoryPage


class OrderDetailsPage:

    def __init__(self, page):
        self.page = page

    def click_view_for_order(self, order_id):
        desired_row = self.page.locator("tr").filter(has_text=order_id)
        desired_row.get_by_role("button", name="View").click()
        # If we are 100% sure that post clicking View button Order History page will come,
        # then we can make object for PlacedOrderHistoryPage class here only to avoid extra code in test method.
        order_history = PlacedOrderHistoryPage(self.page)
        return order_history