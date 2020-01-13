#links of ref
#Documentations: 
#   https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#   https://2.python-requests.org/en/master/
#Where I got this info:
#   https://realpython.com/beautiful-soup-web-scraper-python/
#How to get requests library for windows:
#   https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
#VERY Important about lambda functions/expressions!!!!!!!
#   https://realpython.com/courses/python-lambda-functions/
#   https://www.w3schools.com/python/python_lambda.asp

import requests
from bs4 import BeautifulSoup
URL = "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"
page = requests.get(URL)
# print(page.text) this will print the DOM of the HTML
# print(page.header) this prints only the header of the HTML document

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify) - will output HTML contents nicely to console

results = soup.find(id = "ResultsContainer")

job_elems = results.find_all('section', class_ = 'card-content')

# The lambda function looks at the text of each <h2> element, converts it to lowercase, 
# and checks whether the substring 'python' is found anywhere in there. Now you’ve got a match:
# you can pass in functions in to the string = parameter
python_jobs = results.find_all('h2', string = lambda text : 'python' in text.lower())

for jobs in job_elems: 
     # Each jobs is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = jobs.find('h2', class_ = 'title')
    company_elem = jobs.find('div', class_ = 'company')
    location_elem = jobs.find('div', class_ = 'location')
    #print(jobs, end = '\n'*2)


    #This if statement checks if title_elem is None or not because sometimes ads are under the same 'section' tag 
    #that would return None and cause the program to crash!
    #Try commenting out this if statement to see what happens
    if None in (title_elem, company_elem, location_elem) : 
        continue


    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

#python_jobs is a list of filtered results
for pyjobs in python_jobs : 
    link = pyjobs.find('a')['href']
    print(pyjobs.text.strip())
    print(f"Apply here: {link}\n")
print(type(python_jobs))