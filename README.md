# Indeed-Auto-Apply-Python
This is an indeed apply automated program that applies for jobs.
This uses the microsft's edge Web driver and selenium to be able to work.

![Alt Text](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjJmMzRhODUzZGNkMzBmYzcxNmZlNTY4YTdhY2M4MDIzMjllYjA4MSZjdD1n/quLdspjzl02UkpxpCS/giphy.gif)

# Setup
To get the application running you will need to download the microsft edge webdriver. 
You can [get the web driver here.](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

Once installed then make sure the executable is in the same file as main.py When you are finished then you need to download the dependancies.
Make sure you type this code in your python terminal to download the requirements.

## Installation
```
$ pip install -r requirements.txt
```

# Search Engine
In the python code you'll find a search engine class.
With this you have access to 3 types of functions. All of them will return a list of all the jobs the app has scraped.

## Defualt Search

Default search is a search without any specific criteria. The only parameter it takes is the number of pages to scrape. All other information required for the search to run is located in the 'config.json' file.

In the 'config.json' file, you can customize your search criteria. Here, you define the rules that will be applied to the 'readListing' function in the applying engine. For example, the title field will apply to the job role and the location field will apply to the job location.

You can also create multiple searches. In this example, I am searching for a Flask developer job in London and a JavaScript job in Norwich with different rule IDs.


### Config.Json
```
    {
    "Search": [
        { "Role": 
            {
                "rule": 1,
                "Title": "Flask Developer",
                "Location": "London"
            }
            
        },
        { "Role": 
            {
                "rule": 2,
                "Title": "Javascript Developer",
                "Location": "Norwich"
            }
            
        }]
     }
```


### Main.py
```
SearchEngine.DefualtSearch(console, 20)

returns = [['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3']]

```

## Custom Search

Custom search allows the user to specify search criteria, such as job title and location, as well as the number of pages to be scraped. Furthermore, the program offers the option to set search rules that will be saved in an Excel file, enabling the user to retrieve and analyze the data at a later time.

```
SearchEngine.CustomSearch(console, 'Flask', 'London', 5, 1)

returns = [['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3']]

```

## Direct Search

Direct Search enables users to specify search criteria such as job title and location, and directly displays the specific page of interest. Additionally, users can set search rules that will be saved in an Excel file for future reference and analysis. For instance, if a user specifies they want to access one page on Indeed up to page 5, Direct Search will return those specific pages and exclude any extraneous results.

```
SearchEngine.DirectSearch(console, 'Flask', 'London', 5, 1)

returns = [['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3']]

```

# Apply Engine
In the python code you'll find a Apply engine class. When ever you call a function it will alaways return a 2D list. In the first row you will see all the applied and confirmed listings and on the other you will find failed or couldn't be listings.

## Defualt Apply

The Default Apply function runs the application and initiates the client's job posting application process. It uses the rules specified in the 'config.json' file to determine the relevance of each job posting. While this method is not perfect and can be improved, its accuracy depends on the quality of the rules in the configuration file.

When applied for the job the excel will update and have the show the status of the jobs to either be applied or cancelled.
The link in the jobs will mean if it has the easy apply button if it doesn't it will return false else it will return true.

The rules in the configuration file have four primary fields:

1. The 'rule' field is used to reference the identifer on the Excel sheet or filter params. 

2. The 'must' field contains essential words that must match to pass the validation check. If no words match, the job posting will be deemed irrelevant regardless of other keywords. 

3. The 'keywords' field lists words that must be present in the job description for it to be considered relevant. 

4. The 'ignore' field contains a blacklist of words. If any of these words appear in the job description, the posting will automatically be deemed irrelevant, similar to the 'must' field.


### Config.Json
```
    "Filter": [
        { "rules": 
            {
                "rule": 1,
                "Must": ["Flask","London"],
                "Keywords": ["CSS","HTML","Flask","Django","Jquery","Javascript"],
                "Ignore": ["Senior","On site", "Noodles"]
            },
                        {
                "rule": 2,
                "Must": ["Javascript","Norwich"],
                "Keywords": ["CSS","HTML","React","Jquery","Javascript"],
                "Ignore": ["Senior","On site", "Chicken"]
            }
            
        }
    ]
```

### Main.py
```
ApplyEngine.DefaultApply(console)

returns = [['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3'],['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3']]

```


