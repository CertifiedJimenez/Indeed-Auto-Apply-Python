# Indeed-Web-Scraper-Python
This is an indeed automated program that applies for jobs.
This uses the microsoft's edge Web driver and selenium to be able to work.

![Alt Text](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjJmMzRhODUzZGNkMzBmYzcxNmZlNTY4YTdhY2M4MDIzMjllYjA4MSZjdD1n/quLdspjzl02UkpxpCS/giphy.gif)

# Setup
To get the application running you will need to download the microsoft edge webdriver.
You can [get the web driver here.](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

Once installed then make sure the executable is in the same file as main.py When you are finished then you need to download the dependancies.
Make sure you type this code in your python terminal to download the requirements.

## Installation
```
$ pip install -r requirements.txt
```

## EdgeWebDriver class
The EdgeWebDriver class provides a set of methods to scrape job postings from Indeed's job portal. It has the following methods:
<br>
```
__init__(self, driver_path='msedgedriver.exe', url='https://uk.indeed.com')
``` 
The constructor method that initializes the EdgeWebDriver instance. It takes two optional parameters: <br>`driver_path:` The path to the msedgedriver.exe file (default: 'msedgedriver.exe').<br>`url:` The URL of the website to scrape (default: 'https://uk.indeed.com').

<br>

``` 
launch(self) -> None
``` 

A method that launches the Edge web driver with the specified path and website. It uses the webdriver.Edge method to create a new instance of the Edge browser, and then navigates to the specified URL. If an error occurs during the launching process, it prints an error message.

<br>

``` 
 get_url_patterns(self, url) -> list[str]
``` 

A method that scrapes all the job posting URLs from a given webpage. It takes a single parameter: `url:` The URL of the webpage to read listings from.<br>
It then retrieves all the <a> tags on the page, and checks if they contain '/clk' or '/company'. If they do, it appends the URL to a list of URLs, which it then returns.

```
get_job_details(self, url) -> dict
``` 
    
A method that extracts job details from a given job page URL and returns them as a dictionary. It takes a single parameter:

``url:`` The URL of the job page to extract information from.<br>
It then retrieves the full job description from the page and uses regular expressions to extract the following details:
<br>
    
 ```
'title': The title of the job.
'company': The company offering the job.
'location' The location for the job.
'Salary' The Salary for the job.
'job_type': The type(s) of the job (e.g. full-time, part-time, etc.).
'shift_schedule': The job's shift and schedule information.
'job_qualification': The job's required qualifications.
'job_benefits': The benefits offered with the job.
'job_description': The full job description.
'job_insight': Hiring insights or other relevant information.
 ```
    
It then stores these details in a dictionary and returns it.

### Note
This method relies on certain keywords appearing in the job description, so it may not always extract all the details correctly. Additionally, it may not work for all job postings.

