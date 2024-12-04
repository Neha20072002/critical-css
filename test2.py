from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def initialize_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    return driver

try:
    driver = initialize_driver()
    driver.get("https://www.valuebound.com/")

    critical_css = driver.execute_script("""
        let used = '';
        for (let sheet of document.styleSheets) {
            try {
                for (let rule of sheet.cssRules) {
                    if (rule.cssText) used += rule.cssText;
                }
            } catch (e) {} // Catch cross-origin errors
        }
        return used;
    """)

    with open("critical.css", "w") as f:
        f.write(critical_css)

    print("Critical CSS has been extracted and saved to 'critical.css'.")
finally:
    driver.quit()