import time

from bs4 import BeautifulSoup
import requests


def find_jobs():
  html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='
  ).text
  soup = BeautifulSoup(html_text, "lxml")
  skillset = ['python', 'django']
  user_skillset = set(skillset)

  jobs = soup.find_all(
    'li',
    class_="clearfix job-bx wht-shd-bx")  #list of all jobs on current page
  for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if published_date == 'Posted few days ago':
      company_name = job.find('h3', class_='joblist-comp-name').text.replace(
        ' ', '')
      skills_required = job.find('span',
                                 class_='srp-skills').text.replace(' ', '')
      skillset_required = [
        skill.strip() for skill in skills_required.split(',')
      ]
      required = set(skillset_required)
      link = job.h2.a['href']  #to access a part of a tag
      print(company_name.strip())
      print(skills_required.strip())
      print(published_date)
      missing_skills = required - user_skillset  # Find missing skills using set difference
      if missing_skills:
        print("Missing skills are:", ", ".join(missing_skills))
      print(link)
      print("")


for i in range(10):
  find_jobs()
  time.sleep(3600)  # it runs every 1 hour
