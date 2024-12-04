from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize WebDriver
def initialize_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    return webdriver.Chrome(options=options)

try:
    driver = initialize_driver()
    driver.get("https://www.valuebound.com/")

    # Enable Coverage collection
    driver.execute_cdp_cmd("Profiler.enable", {})
    driver.execute_cdp_cmd("Profiler.startPreciseCoverage", {"callCount": False, "detailed": True})

    # Wait for the page to load completely
    driver.implicitly_wait(5)

    # Get coverage results
    coverage_results = driver.execute_cdp_cmd("Profiler.takePreciseCoverage", {})
    driver.execute_cdp_cmd("Profiler.stopPreciseCoverage", {})
    driver.execute_cdp_cmd("Profiler.disable", {})

    used_css = ""
    for entry in coverage_results['result']:
        if ".css" in entry["url"]:  # Filter only CSS files
            for range in entry["ranges"]:
                used_css += entry["text"][range["startOffset"]:range["endOffset"]]

    # Save the used CSS to a file
    with open("critical.css", "w") as f:
        f.write(used_css)

    print("Critical CSS has been saved to 'critical.css'.")

finally:
    driver.quit()
