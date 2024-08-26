
# Substack Article Scraper

This repository contains a Python script that automates the process of scraping article data from the archive page of the Substack blogs. The script extracts titles, subtitles, and links to the articles, storing the collected data in an Excel file.

## Features

- **Automated Web Scraping**: The script uses Selenium to automatically load and scroll through the archive page to ensure all articles are captured.
- **HTML Parsing**: BeautifulSoup is used to parse the loaded HTML content, allowing for easy extraction of data.
- **Data Extraction**: The script extracts the title, subtitle, and link (URL) for each article.
- **Data Storage**: All extracted data is stored in an Excel file for easy access and analysis.

## Requirements

To run the script, you need the following Python libraries:

- `selenium`
- `webdriver_manager`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

You can install these dependencies using pip:

```bash
pip install selenium webdriver_manager beautifulsoup4 pandas openpyxl
```

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/substack-article-scraper.git
    cd substack-article-scraper
    ```

2. **Run the Script**:
    Simply run the script using Python:
    ```bash
    python main.py
    ```

3. **Output**:
    The script will generate an Excel file named `substack_articles_with_links.xlsx` in the same directory, containing the titles, subtitles, and links of all articles found on the "RhinoInsight" Substack archive page.

## Customization

- **Scroll Speed**: If your internet connection is slow, you might need to adjust the `time.sleep(3)` value in the script to allow more time for the page to load.
- **Output File**: The name of the output Excel file can be changed by modifying the `df.to_excel` line in the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

If you have any questions or suggestions, feel free to contact me at [@RhinoInsight](https://x.com/RhinoInsight).
