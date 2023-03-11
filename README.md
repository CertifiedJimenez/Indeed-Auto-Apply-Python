# Indeed-Auto-Apply-Python
This is an indeed apply automated program that applies for jobs. 


# Search Engine
In the python code you'll find a search engine class.
With this you have access to 3 types of functions. All of them will return a list of all the jobs the api has scraped.

Custom Search
In custom search we can define the title, and location along with how many pages will it scrape.
You can aslo define rules you want it to follow by defining the rule the program will save this in 
an excel so you can used it for later usage.

```
SearchEngine.CustomSearch(console, 'Flask', 'London', 5, 1)

returns = [['https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BFWKp4myphoz2RoAbLi7EmRheur09jFeUtvXr9Yhoy_xVV6RfQV5j6p1bFfTvlS-wziuEeh6TaoOw5lmceiomE3X7IA0CI9JliF2TAqzjAr2J335YUWLB-R-YKtuXj0JY3EA4Rc5vbrMUc3nAC8UHE6YTcnro-aKwNr9X6UAAd_zZ3jlIfpzrHCe72frZ-5ioaOMheDk66nY4G_1J3hqhrV7Hv66vAzMBFOl2pRXQ-cFAHjOotFrs291hwruXwMwLTD7Gf9Zk7p-FNlxNTqnnOA4rfFXMpWws-s8iGzfDwPobjr3HJ86bQpgHnrxBX3NDpNxyoEHHKj4kaYAY2rd74Znro8uTsf5x553M_5AWSdG1coC9CiZFKMKXFlF4QZYIcXRNTUMvkmXIj0MtMYmYJFxDf2E81dr-DdmZEO_qBiX13J6bKpq6lW-VrUB8bd9GZKuJnPA2eW19m34-cPGi15FFVHUCgFJvRSRvSk6eWnkICJk4Xrnhc8gJv1-OhLKZReDfFypceSq3fXLhV3i86ISckNZTIed3weS-1t5Ak_Q==&xkcb=SoCw-_M3SpGJsJWHER0IbzkdCdPP&p=0&fvj=1&vjs=3']]

```


