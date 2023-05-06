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

    
<h2>EdgeWebDriver class</h2>
<p>The <code>EdgeWebDriver</code> class provides a set of methods to scrape job postings from Indeed's job portal. It has the following methods:</p>
<h3><code>__init__(self, driver_path='msedgedriver.exe', url='https://uk.indeed.com')</code></h3>
<p>The constructor method that initializes the EdgeWebDriver instance. It takes two optional parameters:</p>

<ul><li><code>driver_path</code>: The path to the <code>msedgedriver.exe</code> file (default: <code>'msedgedriver.exe'</code>).</li><li><code>url</code>: The URL of the website to scrape (default: <code>'https://uk.indeed.com'</code>).</li></ul><h3><code>launch(self) -&gt; None</code></h3><p>A method that launches the Edge web driver with the specified path and website. It uses the <code>webdriver.Edge</code> method to create a new instance of the Edge browser, and then navigates to the specified URL. If an error occurs during the launching process, it prints an error message.</p><h3><code>get_url_patterns(self, url) -&gt; list[str]</code></h3><p>A method that scrapes all the job posting URLs from a given webpage. It takes a single parameter:</p><ul><li><code>url</code>: The URL of the webpage to read listings from.</li></ul><p>It then retrieves all the <code>&lt;a&gt;</code> tags on the page, and checks if they contain '/clk' or '/company'. If they do, it appends the URL to a list of URLs, which it then returns.</p><h3><code>get_job_details(self, url) -&gt; dict</code></h3><p>A method that extracts job details from a given job page URL and returns them as a dictionary. It takes a single parameter:</p><ul><li><code>url</code>: The URL of the job page to extract information from.</li></ul><p>It then retrieves the full job description from the page and uses regular expressions to extract the following details:</p><ul><li>'title': The title of the job.</li><li>'company': The company offering the job.</li><li>'location' The location for the job.</li><li>'Salary' The Salary for the job.</li><li>'job_type': The type(s) of the job (e.g. full-time, part-time, etc.).</li><li>'shift_schedule': The job's shift and schedule information.</li><li>'job_qualification': The job's required qualifications.</li><li>'job_benefits': The benefits offered with the job.</li><li>'job_description': The full job description.</li><li>'job_insight': Hiring insights or other relevant information.</li></ul><p>It then stores these details in a dictionary and returns it.</p><p>Note that this method relies on certain keywords appearing in the job description, so it may not always extract all the details correctly. Additionally, it may not work for all job postings.</p>


