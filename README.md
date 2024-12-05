# Extract Critical CSS

This script extracts **Critical CSS** (the CSS used in the first viewport) from a webpage. Critical CSS helps improve **page speed** and the **Speed Index**, both of which are crucial for a better **user experience** and **Core Web Vitals** scores.

---

## **Why Extract Critical CSS?**

- **Speed Optimization**: Loading only the critical CSS inline minimizes render-blocking, allowing the page to load faster.
- **Improve Core Web Vitals**: Faster rendering of above-the-fold content improves metrics like LCP (Largest Contentful Paint).
- **Better Performance**: By focusing on the most-used CSS, we avoid loading unnecessary styles, saving bandwidth and reducing page load times.

### How It Works:
1. **Identify Stylesheets**: The script iterates over document.styleSheets to access all stylesheets loaded on the page.
2. **Check Rules for Elements in Viewport**: For each rule:
   - It finds all elements matching the selector.
   - Checks if the element is visible in the viewport.
   - Verifies if the rule is applied to the element.
3. **Collect and Save Critical CSS**:It saves only the CSS rules from external stylesheets that are used for the visible viewport.
---

## **Setup Instructions**

### Prerequisites

1. **Python** (3.7 or above)
2. **Google Chrome** installed on your system.
3. **ChromeDriver** installed and added to your system's PATH.
   - Download the appropriate version of ChromeDriver for your browser version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install selenium
   ```

4. **Verify ChromeDriver Path**:
   - Ensure `chromedriver.exe` is accessible or add its path to the script.

---

## **Usage**

1. Open the script `critical.py` and update the URL in this line to the webpage you want to analyze:
   ```python
   driver.get("https://www.example.com/")
   ```

2. Run the script:
   ```bash
   python critical.py
   ```

3. The extracted critical CSS will be saved to `critical.css` in the same directory.

---

## **How It Works**

1. **Enable Coverage API**:
   - The script uses Chrome's **Profiler** API to collect precise usage data for CSS files loaded during page rendering.

2. **Fetch Coverage Results**:
   - It extracts the CSS files used and determines which parts of the file are utilized for rendering the first viewport.

3. **Process Used CSS**:
   - The script extracts only the `startOffset` to `endOffset` ranges of used bytes from each CSS file.

4. **Save Critical CSS**:
   - Writes the extracted CSS into a file `critical.css`.

---

## **Customization**

### Headless Mode
By default, the browser runs in **headless mode** (no UI). To disable it for debugging:
```python
options.add_argument("--headless")  # Comment out this line
```

### Debug Logging
Enable additional logging by uncommenting `print` statements in the script:
```python
print(coverage_results)
```

---

## **Troubleshooting**

### Empty `critical.css` File
- Ensure the website is accessible and that the `Coverage API` collects valid data.
- Some cross-origin CSS files may not be accessible due to security restrictions. Add these Chrome options if needed:
  ```python
  options.add_argument("--disable-web-security")
  options.add_argument("--allow-running-insecure-content")
  ```

### ChromeDriver Errors
- Ensure the `chromedriver.exe` path matches your installed Chrome version.
- Test ChromeDriver by running:
  ```bash
  chromedriver --version
  ```

---

## **Next Steps**
- Inline the `critical.css` into your HTML files for faster rendering.
- Optimize remaining CSS files by lazy-loading or deferring them.
- Consider automating this process for multiple pages.

---

## **License**
This script is open-source and provided under the MIT License. Feel free to modify and use it in your projects.
