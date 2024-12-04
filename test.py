from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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

    # Extract critical CSS for above-the-fold content
    critical_css = driver.execute_script("""
        let criticalCSS = '';
        const viewportHeight = window.innerHeight;
        
        // Get all elements in the DOM
        const elements = document.querySelectorAll('*');
        
        // Iterate through elements to find styles used in the viewport
        for (let element of elements) {
            const rect = element.getBoundingClientRect();
            if (rect.top < viewportHeight && rect.bottom > 0) { // Check if in the viewport
                const styles = window.getComputedStyle(element);
                for (let property of styles) {
                    criticalCSS += `${property}: ${styles.getPropertyValue(property)}; `;
                }
            }
        }
        return criticalCSS;
    """)

    with open("critical.css", "w") as f:
        f.write(critical_css)

    print("Critical CSS for the first viewport has been extracted and saved to 'critical.css'.")
finally:
    driver.quit()
