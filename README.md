# Indeed-Auto-Apply-Python
This is an indeed apply automated program that applies for jobs. 


# Search Engine
In the python code you'll find a search engine class.
With this you have access to 3 types of functions. All of them will return a list of all the jobs the app has scraped.

## Custom Search

Custom search allows the user to specify search criteria, such as job title and location, as well as the number of pages to be scraped. Furthermore, the program offers the option to set search rules that will be saved in an Excel file, enabling the user to retrieve and analyze the data at a later time.

```
SearchEngine.CustomSearch(console, 'Flask', 'London', 5, 1)

returns = [['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3']]

```

## Direct Search

Direct Search enables users to specify search criteria such as job title and location, and directly displays the specific page(s) of interest. Additionally, users can set search rules that will be saved in an Excel file for future reference and analysis. For instance, if a user specifies they want to access all pages on Indeed up to page 5, Direct Search will return those specific pages and exclude any extraneous results.

```
SearchEngine.CustomSearch(console, 'Flask', 'London', 5, 1)

returns = [['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3']]

```


