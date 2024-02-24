browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome Browser")
    case "firefox":
        print("Firefox Browser")
    case _:
        print("No browser found")