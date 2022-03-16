from itertools import zip_longest
import csv
from bs4 import BeautifulSoup
import requests
from requests.api import request
# 1st step install and import modules
# -- pip/pip3 install lxml
# -- pip/pip3 install requests
# -- pip/pip3 install beautifulsoup4

job_title = []
company_name = []
location_name = []
skills = []
links = []
salary = []

# 2nd step use requets to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# 3rd step save page content/markup
# تحويل محتوى الصفحة
src = result.content
# print(src)

# 4th step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
# print(soup)


# # 5th step find the elements containing info we need
# # -- job titles, job skills, company names, location names

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
location_names = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})

# # 6th step loop over returned lists to extract needed info other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(job_skills[i].text)
    print(job_title)

# for link in links:
#     result = requests.get(link)
#     src = result.content
#     soup = beautifulsoup(src, "lxml")
#     salaries = soup.find_all("span", {"class": "css-4xky9y"})
#     salary.append(salaries.text)

# 7th step create csv file and fill it with values
# يقصد ب fille list ترتيب
file_list = [job_titles, company_names,
             location_names, skills, links]
# يقصد بتفريغ المحتوى في file list
exported = zip_longest(*file_list)
with open("C:/Users/Probook PRO/Desktop/do python/jobstest1.csv", "w") as myfile:
    wr = csv.writer(myfile)
    # كتابة العناوين تعني writerow
    wr.writerow(["job title", "company name", "location",
                "skills", "links"])
    wr.writerows(exported)
