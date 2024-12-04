from selenium import webdriver

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    return driver

try:
    driver = initialize_driver()
    driver.get("https://www.valuebound.com/")

    # Extract critical CSS for elements in the viewport
    critical_css = driver.execute_script("""
        const criticalCSS = [];
        const viewportHeight = window.innerHeight;

        // Iterate over stylesheets
        for (const sheet of document.styleSheets) {
            try {
                const rules = sheet.cssRules || []; // Get rules, skip if inaccessible
                for (const rule of rules) {
                    if (rule.selectorText) {
                        // Find elements matching the rule's selector
                        const elements = document.querySelectorAll(rule.selectorText);
                        for (const element of elements) {
                            const rect = element.getBoundingClientRect();
                            // Check if the element is in the viewport
                            if (rect.top < viewportHeight && rect.bottom > 0) {
                                criticalCSS.push(rule.cssText);
                            }
                        }
                    }
                }
            } catch (e) {
                console.warn("Skipped stylesheet due to CORS or invalid rules.");
            }
        }

        return criticalCSS.join(' ');
    """)

    # Save the critical CSS to a file
    with open("critical.css", "w") as f:
        f.write(critical_css)

    print("Critical CSS for the first viewport has been extracted and saved to 'critical.css'.")
finally:
    driver.quit()
