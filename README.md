# Web Scraper for Exam Papers from exam.naer.edu.tw

This is a Python script for scraping exam papers from the website exam.naer.edu.tw. The script uses the `requests`, `bs4`, and `tqdm` libraries to send HTTP requests, parse HTML, and display a progress bar, respectively.

## Requirements

- Python 3.x
- `requests`
- `bs4` (BeautifulSoup)
- `tqdm`

You can install the required libraries by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone this repository:

```
git clone https://github.com/your_username/exam-papers-scraper.git
cd exam-papers-scraper
```

2. Run the script:

```
python scraper.py
```

The script will start scraping exam papers from page 1 to page 4767 (as of September 2021) and save the results in a JSON file named `data.json`. If the file already exists, the script will resume scraping from the last page recorded in the file.

You can change the number of pages to scrape by modifying the `total_pages` variable in the script.

## Output

The scraped data will be saved in a JSON file named `data.json`. Each record in the file contains the following fields:

- "縣市": The city or county where the school is located.
- "學校名稱": The name of the school.
- "年級": The grade level.
- "學年度": The academic year.
- "領域/群科": The domain or group of the exam paper.
- "科目": The subject of the exam paper.
- "種類": The type of the exam paper.
- "版本": The version of the exam paper.
- "點閱率": The number of views of the exam paper.
- "下載試卷": The download link for the exam paper.
- "下載答案": The download link for the answer paper.
- "page": The page number where the record was found.

## License

This script is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the script as long as you include the original license file.
