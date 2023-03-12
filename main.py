from selenium import webdriver
import json
import yaml
import os
import time
import openpyxl
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import math
from bs4 import BeautifulSoup
import requests




class ScraperConfig:


    def __init__(self, driver_path='msedgedriver.exe', authentication_file='/cookies/authentication.json', url='https://uk.indeed.com'):
        self.driver = None
        self.authentication = os.path.isfile('auth.json')
        self.driver_path = driver_path
        self.url = url 
        self.launch()

    # Built-In

    def launch(self, path='msedgedriver.exe', url='https://uk.indeed.com'):
        """"
        Path redirects to the driver and the url redirects
        to the assosiated Indeed version of the site.
        """
        self.driver = webdriver.Edge(executable_path=self.driver_path)
        self.driver.get(self.url)


    def authenticate(self):
        """
        This is the authentication method for
        the user to be able to login.
        """
        driver = self.driver
        element = driver.find_element_by_xpath('//body')

        if(self.authentication and not 'Sign in' in element.text):
            # Authenticated user the page will refresh
            with open('auth.json', 'r') as auth:
                for i in json.load(auth):
                    try:
                        driver.add_cookie(i)
                    except: break
                driver.refresh()
        else:
            # authenitcated users expected to login
            driver.get('https://secure.indeed.com/settings/account')
            while driver.current_url != 'https://secure.indeed.com/settings/account':
                time.sleep(1)
                print('Authentication is required.')
            with open('auth.json', 'w') as auth:
                cookies = driver.get_cookies()
                json.dump(cookies, auth, ensure_ascii=False, indent=4)

    # Decorators

    def authentication_required(func):
        """
            This means when this is applied we will check for 
            authentication and login
        """

        def wrapper(*args, **kwargs):
            print("Before the function is called.")
            ScraperConfig.authenticate(args[0])

            # print(*args[0])

            result = func(*args, **kwargs)
            print("After the function is called.")
            return result
        return wrapper

    # Code functions


    def readListings(self, url, rule=None):
        """
        This will read through all the listings
        and get it processed by our proofreader
        """
        # Method of getting it is find elements by href to store links

        driver = self.driver
        driver.get(url)

        foundListings = []
        a_tags = driver.find_elements_by_tag_name("a")
        for item in a_tags:
            href = item.get_attribute('href')
            if '/clk' in href:
                foundListings.append(href)
            elif '/company' in href:
                foundListings.append(href)
        if rule is not None: self.saveLinks(foundListings, rule)
        return foundListings


    def saveLinks(self, links, rule):
        """
        This saves the links into an excel file 
        until later on we can actually begin applying for these
        """
        excel_manager = ExcelManager('links.xlsx')
        for link in links:
            excel_manager.add_link(link, rule)
        excel_manager.save()
        

    def readListing(self, url, config):
        """"
        This uses regex to identify the main elements of the app
        to know weather its easy to apply or relavent to the job spek.
        """
        driver = self.driver 
        driver.get(url)
        
        element = driver.find_element_by_xpath('//body')
        text = element.text
        
        try:
            element.find_element_by_id('indeedApplyButton')
            for ignore in config['Ignore']:
                if ignore in text:
                    return False
            
            for word in config['Must']:
                if word not in text:
                    return False

            for keyword in config['Keywords']:
                if keyword in text:
                    return True
                
        except NoSuchElementException:
            print("❌")
            print("Invalid button for direct apply")
        return False


    @authentication_required
    def sendApplication(self,url = None):
        """
        This function will apply the listings and fill the form
        """

        driver = self.driver 
        if url != None: driver.get(url)
        
        button = driver.find_element_by_id('indeedApplyButton')

        # Checks if the job has already been applied to.
        excel_manager = ExcelManager('links.xlsx')

        print("Applying")

        time.sleep(5)
        if button.is_enabled():
            button.click()

            time.sleep(3)
            with open('autoComplete.js', 'r') as f:
                autoComplete = f.read()
            driver.execute_script(autoComplete)
            result = False
            while True:
                print("Waiting")
                if 'Failed' in driver.title:
                    excel_manager.update(url,'Link','status','Required')
                    result = False
                    break
                elif 'Your application has been submitted | Indeed.com' in driver.title:
                    excel_manager.update(url,'Link','status',' Applied')
                    result = True
                    break
            return result


        # for the form handling i would want to add a comute button
        # I also want to focus on intensive input that require high level inputs.
        # We need a delay per page to fill 

        # lastly we need a way to know if an error accours how to ignore it 

        # it will use the continue button as a way to click and then lastly it will find submit application then itll be done.
        # when clicked it will either look for this Your application has been submitted! or when click redirect to the next listing


class ExcelManager:
    def __init__(self, filename):
        self.filename = filename
        if os.path.isfile(filename):
            self.df = pd.read_excel(filename)
        else:
            self.df = pd.DataFrame(columns=['Link','valid','rule','status'])

    def add_link(self, link, rule):
        if link not in self.df['Link'].values:
            self.df = self.df.append({'Link': link, 'rule': rule}, ignore_index=True)   

    # def invalid_link(self,link):
    #     if link not in self.df['valid'].values:
    #         self.df = self.df.append({'Link': link}, ignore_index=True)

    def update(self, Key, column, targetcolumn, value):
        if Key in self.df[column].values:
            self.df.loc[self.df[column] == Key, targetcolumn] = value
            self.save()

    def save(self):
        self.df.to_excel(self.filename, index=False)

    def read(self,title):
        if title in self.df.columns:
            return self.df[title].tolist()
        else:
            return None
        
    def returnRow(self,title,value):
        matching_row = self.df.loc[self.df[title] == value]
        # If a matching row was found, return its information
        if not matching_row.empty:
            row = matching_row.iloc[0]
            return row
        else:
            return None


def get_config(config='config.yml'):
    if os.path.isfile('config.json'):
        with open('config.json', 'r') as file:
            return json.load(file)
        

class ApplyEngine:
    """"
    This uses the excel sheet to read throguh all the
    listings and qualify the relavent and applicable ones.
    """

    
    # Loads and directly applies to listing
    def DirectApply(driver, url):
        driver.sendApplication(url)

    # Debates weather job is eligble for direct apply
    # def RuleListing(driver,url):
    #     driver.readListing()


    # sorts the data on the for loop to get relavent info
    def __forRules(excel_manager,config):
        output = []
        for url in excel_manager.read('Link'):
            row = excel_manager.returnRow('Link',url)
            if 'nan' == str(row.status):
                specifiedConfig = {}
                for rule in config['Filter']:
                    if rule['rules']['rule'] == row.rule:
                        specifiedConfig = rule['rules']
                        output.append([url, specifiedConfig])
        return output


    # Begins to filter all the relavent jobs and irrelavent ones
    def DefualtRule(driver):
        excel_manager = ExcelManager('links.xlsx')
        config = get_config() 
        appliedListings, cancelledListing = [], []  
        for url, specifiedConfig in ApplyEngine.__forRules(excel_manager,config):
            if driver.readListing(url,specifiedConfig):
                excel_manager.update(url,'Link','valid','True')
            else:
                excel_manager.update(url,'Link','valid','False')
        return appliedListings, cancelledListing


    # beings to apply for all the jobs in the links
    def DefaultApply(driver):
        excel_manager = ExcelManager('links.xlsx')
        config = get_config()        
        appliedListings, cancelledListing = [], []
        for url, specifiedConfig in ApplyEngine.__forRules(excel_manager,config):
            if driver.readListing(url,specifiedConfig):
                    """
                    Form handling
                    """
                    print("✔")
                    print('Valid for direct apply')
                    excel_manager.update(url,'Link','valid','True')
                    driver.sendApplication(url)
                    appliedListings.append(url)
                    excel_manager.update(url,'Link','status',' applied')
            else:
                # Cross it and mark it as impractible
                time.sleep(2)
                excel_manager.update(url,'Link','valid','False')
                excel_manager.update(url,'Link','status',' cancelled')
        return appliedListings, cancelledListing

    # applies outside and uses a function to wait to load on next applciation

class SearchEngine:
    """
    This takes creates the url and uses as the way
    to search for jobs written in the config YMAL file.
    """

    # Load pages but save listings
    def CustomSearch(driver, Title, Location, TotalPages, Rule = None):
        listings = [] 
        for i in range(TotalPages-1):
            Page = 10*i
            url = 'https://uk.indeed.com/jobs?q={0}&l={1}&start={2}'.format(Title,Location,Page)
            listings.append(driver.readListings(url, Rule))
        return listings

    #Get Direct Page
    def DirectSearch(driver, Title, Location, Page = 0, Rule = None):
        url = 'https://uk.indeed.com/jobs?q={0}&l={1}&start={2}'.format(Title,Location,Page)
        return driver.readListings(url, Rule)

    # Page search using the config settings.
    def DefualtSearch(driver, TotalPages = 20):
        listings = [] 
        config = get_config()
        for item in config['Search']:
            for i in range(TotalPages-1):
                Page = 10*i
                url = 'https://uk.indeed.com/jobs?q={0}&l={1}&start={2}'.format(item['Role']['Title'],item['Role']['Location'],Page)
                listings.append(driver.readListings(url, item['Role']['rule']))
        return listings


console = ScraperConfig()
easy = SearchEngine.CustomSearch(console, 'Flask', 'London', 5, 1)
print(easy)
# ApplyEngine.DefaultApply(console)



