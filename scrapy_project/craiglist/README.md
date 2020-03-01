# Web Scraping and Crawling with Python using Scrapy Tool

## Craiglist site crawler to get list of jobs in NewYork and details for each job

- Site URL: https://newyork.craigslist.org/search/egr

- Command to Run this project from CMD when scrapy is installed
  > Go to the directory where project is downloaded
  > RUN: scrapy crawl jobs -o items.csv 
  
- To run the scrapy as a standalon script
1. Install scrapy
2. download jobs.py file
3. open jobs.py file 
4. replace "yield" command with "print"
5. Go to the path in cmd where jobs.py file is saved
6. RUN Command to print on console: **scrapy runspider jobs.py**
7. RUN Command to create a file and save data in it: **scrapy runspider jobs.py -o items.csv**