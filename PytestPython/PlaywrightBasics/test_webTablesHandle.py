from playwright.sync_api import Page, expect


def test_webTablesHandle(page : Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    #Our goal is to check the Price of Rice should be 37
    #1. Identify the Price column, coz the table is dynamic, Price column can be at any place.
    #2. Identify the Rice row, coz the table is dynamic, Rice row can be at any place.

    #1.
    for i in range(page.locator("th").count()):
        # If nth(0) means 1st column text is Price, then count will be 1 otherwise 0.
        # print (page.locator("th").nth(i).filter(has_text="Price").count())
        if page.locator("th").nth(i).filter(has_text= "Price").count() > 0: #nth = Returns locator to the n-th matching element.
            priceColm = i   #Take the i value in priceColm to use later.
            break
    #2.
    riceRow = page.locator("tr").filter(has_text= "Rice")
    expect(riceRow.locator("td").nth(priceColm)).to_have_text("37")