from automation.browser_controller import BrowserController

browser = BrowserController()

print("=" * 50)
print("Browser Test")
print("=" * 50)

while True:

    website = input("Website (exit to quit): ").strip()

    if website.lower() == "exit":
        break

    print(browser.open_website(website))