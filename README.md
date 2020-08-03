

PROBLEM STATEMENT
Cloud Counselage is a Pan India IT, Management, and Career services provider. To expand its reach across all the colleges in Mumbai and surrounding colleges that might be interested to collaborate with the company and automate the application process. The company is expecting interns to develop an automated system for scraping the contact details of college TPOs and official mail IDs ranging from at least 1000 Engineering colleges/universities
Input:
Getting a List of colleges and their website to scrape (can automate the collection of the list)
Data requirements of CC
Output:
A structured dataset of all collected scraped data with minimal manual error corrections and at
least 50-100 colleges
The minimum requirement of data is
1. College Name
2. Location
3. Contact Number
4. Email Address
5. Website link
6. TPO Name
7. TPO Contact Number
8. Other Companies collaboration (optional)
● Visualization of Data is also needed (Using Matplotlib or flask)
















DESIGN AND METHODOLOGY

Web Crawler Requests:
A very necessary component of web scraper, web crawler module, is used to navigate the target website by making HTTP or HTTPS request to the URLs. The crawler downloads the unstructured data (HTML contents) and passes it to extractor, the next module. Here urlib3 request module is used to go to the next step.

Extractor:
The extractor processes the fetched HTML content and extracts the data into semi structured format. This is also called as a parser module and uses different parsing techniques like HTML Parsing using beautiful soup.

Data Transformation and Cleaning Module:
The data extracted above is not suitable for ready use. It must pass through some cleaning module so that we can use it. The methods like String manipulation or regular expression can be used for this purpose. Or extract the data using regular expression.

Storage Module:
The data extracted in the above step need to be stored in a format where it can be used for user visibility or for analysis purpose. Here it is saved in a csv format. 



















Web Crawler
TOOLS USED

PYTHON 3.0: Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

BEAUTIFUL SOUP: Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. (pip install beautifulsoup4)for installing.

URLLIB: urllib is a Python module that can be used for opening URLs. It defines functions and classes to help in URL actions.
With Python you can also access and retrieve data from the internet like XML, HTML, JSON, etc. You can also use Python to work with this data directly. In this tutorial we are going to see how we can retrieve data from the web. For example, here we used a guru99 video URL, and we are going to access this video URL using Python as well as print HTML file of this URL.

PYCHARM: PyCharm is an integrated development environment (IDE) used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains.[6] It provides code analysis, a graphical debugger, an integrated unit tester, integration with version control systems (VCSes), and supports web development with Django as well as Data Science with Anaconda. PyCharm is cross-platform, with  Windows ,  macOS and Linux versions.
MATPLOTLIB: Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged.[3] SciPy makes use of Matplotlib.
PANDAS: In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license.
ANALYSIS
1.	NO OF COLLEGES WITH ALL THE DATA AS MENTIONED
 
2.	NO OF COLLEGES PER STATE
 
3.	NO OF DISTRICT IN ONE STATE CONTAINING COLLEGES 

FUTURE SCOPE
Since the websites changes dynamically some code might not work in future when the structure of the website changes .so in future we aim to rebuild this scrapper in such a way that it can scrap data when sites have changed partially or fully. For the time span our code works best in the moment and in future also this information will help company to expand their business and grow or in choosing the colleges for fresher effectively.
CONCLUSION
The extraction of data hidden web data is a major challenge nowadays because of autonomous and heterogeneous nature of hidden web content traditional stress engine has now become an ineffective way to search this kind of data. The main outcomes of this project were user friendly search interface, indexing, query processing, and effective data extraction technique based on web structure, Hidden web data need synthetic and semantic matching to fully achieve automatic integration in this thesis fully automatic and domain dependent prototype system is proposed that extract and integrate the data lying behind the search form for tpo’s. And other websites as study guides for the college details .






















REFERENCES
For getting an overview how scrapping takes place: https://www.youtube.com/watch?v=mKxFfjNyj3c
Beautiful soup documentation:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
pandas and matplotlib documentation:
https://tanthiamhuat.files.wordpress.com/2018/04/pythondatasciencehandbook.pdf
