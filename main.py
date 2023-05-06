from selenium import webdriver
from selenium.webdriver.common.by import By

import yaml
import re 

import logging
from selenium.webdriver.remote.remote_connection import LOGGER

# Disable logging from the Selenium WebDriver
LOGGER.setLevel(logging.CRITICAL)


class EdgeWebDriver:

    def __init__(self, driver_path='msedgedriver.exe', url='https://uk.indeed.com'):
        self.driver_path = driver_path
        self.url = url
        self.launch()

    def launch(self) -> None:
        """Launches the Edge web driver with the specified path and Indeed."""
        try:
            self.driver = webdriver.Edge(executable_path = 'msedgedriver.exe')
            self.driver.get(self.url)
        except Exception as e:
            if 'executable' in str(e):
                raise ValueError(f"Edge executable not found at {self.driver_path}")
            else:
                print(f"Error launching Edge web driver: {e}")
        
    def get_url_patterns(self, url) -> list[str]:
        """
        Scrapes all the url job postings in that particular url.

        Args:
            url (str): The URL of the webpage to read listings from.
            rule (str, optional): The name of the rule to use for saving links.

        Returns:
            list: A list of URLs for the found listings.
        """
    
        self.driver.get(url)

        urls = []
        a_tags = self.driver.find_elements(By.TAG_NAME, "a")
        for item in a_tags:
            href = item.get_attribute('href')
            if '/clk' in href or '/company' in href:
                urls.append(href)

        return urls
    
    def get_job_details(self, url) -> dict:
        """
        Extracts job details from a given job page URL and returns them as a dictionary.

        Args:
            url (str): The URL of the job page to extract information from.

        Returns:
            dict: A dictionary containing the following keys:
                - 'title': The title of the job.
                - 'company': The company offering the job.
                - 'location' The location for the job.
                - 'Salary' The Salary for the job.
                - 'job_type': The type(s) of the job (e.g. full-time, part-time, etc.).
                - 'shift_schedule': The job's shift and schedule information.
                - 'job_qualification': The job's required qualifications.
                - 'job_benefits': The benefits offered with the job.
                - 'job_description': The full job description.
                - 'job_insight': Hiring insights or other relevant information.
        """

        job = {}
        self.driver.get(url)
        page_text = self.driver.find_element(By.TAG_NAME, 'body').text
        pattern = re.compile(r'Find Jobs(.*)Report job', re.DOTALL)
        result = pattern.search(page_text)
        if result:
            extracted_text = result.group(1)
            extracted_text_split = extracted_text.split('\n')

            # Assign values
            title = extracted_text_split[1]
            company = extracted_text_split[2]
            location = extracted_text_split[3]
            salary = extracted_text_split[4]

            job_type = []
            shift_schedule = []
            job_qualification = []
            job_benefits = []
            job_description = []
            job_insight = []
            mode = '' # The mode to extract the words on key words
            
            def read_lines(lst, word):
                """ Reads the text in the job description """
                
                nonlocal mode
                if word in line or mode == word:
                    if word in line: mode = word
                    lst.append(line)

            for line in extracted_text_split:
                # Assign Modes
                read_lines(job_type, "Job type")
                read_lines(shift_schedule, "Shift and schedule")  
                read_lines(job_qualification, "Qualifications")  
                read_lines(job_benefits, "Benefits")  
                read_lines(job_description, "Full Job Description")  
                read_lines(job_insight, "Hiring Insights")  

            job['title'] = title
            job['company'] = company
            job['salary'] = salary
            job['location'] = location
            job['job_type'] = job_type
            job['shift_schedule'] = shift_schedule
            job['job_qualification'] = job_qualification
            job['job_benefits'] = job_benefits
            job['job_description'] = ''.join(job_description)
            job['job_insight'] = job_insight
        else:
            print("Pattern not found.")
        return job


class IndeedScraper(EdgeWebDriver):
    
    def __init__(self, driver_path='msedgedriver.exe', url='https://uk.indeed.com'):
        super().__init__(driver_path, url)


    def scrape_direct_page_index(self, Title: str, Location: str, Page: int) -> list[str]:
        """
        Scrapes a direct indeed jobs urls by the page number
        
        Args:
            title (str): The role name your searching for.
            location (str): The role location your searching for.
            page (int): The page number you are searching for.

        Returns:
            list: A list of URLs for the found listings.
        """

        url = f'{self.url}/jobs?q={Title}&l={Location}&start={str(Page)}'
        return self.get_url_patterns(url)

    def scrape_bundle_pages(self, Title, Location, MaxPages: int) -> list[str]:
        """
        Scrapes a multiple indeed jobs urls until max page param is hit.
        
        Args:
            title (str): The role name your searching for.
            location (str): The role location your searching for.
            MaxPages (int): The page number you want to search to.

        Returns:
            list: A list of URLs for the found listings.
        """

        listings = [] 
        for currentPage in range( MaxPages ):
            listings.extend(self.scrape_direct_page_index(Title, Location, currentPage))
        
        return listings
    
    def scrape_config_pages(self) -> list[str]:
        """
        Scrapes a multiple indeed jobs urls based on the config
        
        Required:
            config.yml (dict) the file will have the config to add multiple
            custom searches.

        Returns:
            list: A list of URLs for the found listings.
        """

        listings = [] 
        data = self._getConfig()
        for search in data['jobs']:
            listings.extend(self.scrape_bundle_pages(search['title'],search['location'],search['pages']))
        return listings

    def scrape_job_listing(self, link: str) -> dict:
        """
            Extracts job details from a given job page URL and returns them as a dictionary.

            Args:
                url (str): The URL of the job page to extract information from.

            Returns:
                dict: A dictionary containing the following keys:
                    - 'title': The title of the job.
                    - 'company': The company offering the job.
                    - 'location' The location for the job.
                    - 'Salary' The Salary for the job.
                    - 'job_type': The type(s) of the job (e.g. full-time, part-time, etc.).
                    - 'shift_schedule': The job's shift and schedule information.
                    - 'job_qualification': The job's required qualifications.
                    - 'job_benefits': The benefits offered with the job.
                    - 'job_description': The full job description.
                    - 'job_insight': Hiring insights or other relevant information.
        """
        return self.get_job_details(link)

    def scrape_multiple_job_listing(self, jobs: list[str]) -> list[dict]:
        """
        Extracts job details from a given job page URL and returns them as a dictionary.

        Args:
            url (list): The list URL of the job page to extract information from.

        Returns:
            list(dict): A dictionary containing the following keys:
                - 'title': The title of the job.
                - 'company': The company offering the job.
                - 'location' The location for the job.
                - 'Salary' The Salary for the job.
                - 'job_type': The type(s) of the job (e.g. full-time, part-time, etc.).
                - 'shift_schedule': The job's shift and schedule information.
                - 'job_qualification': The job's required qualifications.
                - 'job_benefits': The benefits offered with the job.
                - 'job_description': The full job description.
                - 'job_insight': Hiring insights or other relevant information.
        """

        listings = [] 
        for link in jobs:
            listings.append(self.get_job_details(link))
        return listings
        
    def _getConfig(self) -> dict:
        """ Gets the config in the file for custom searches """

        with open('config.yaml', 'r') as stream:
            try:
                data = yaml.safe_load(stream)
                return data
            except yaml.YAMLError as e:
                print(e)
        return {}


import json

def save_to_json(data, file_path):
    """
    Saves a list of dictionaries as a JSON file.

    Args:
        data (list): A list of dictionaries to save.
        file_path (str): The file path to save the JSON file to.
    """

    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)


scrape = IndeedScraper()
jobs = scrape.scrape_bundle_pages('Django','London',1)
details = scrape.scrape_multiple_job_listing(jobs)
print(details)
save_to_json(details, 'my_data.json')
input('Completed')
