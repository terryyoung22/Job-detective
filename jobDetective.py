from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup
import os
from emailcsv import email

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--whitelisted-ips=')
chrome_options.add_argument('--disable-dev-shm-usage')
service_args = ['--verbose']
driver = webdriver.Chrome(chrome_options=chrome_options, service_args=service_args)
# driver = webdriver.Chrome(executable_path='/usr/local/bin/macdriver', chrome_options=chrome_options, service_args=service_args)
# ^ This can be changed to look for driver in path like main script


## Comment/uncomment line for correct driver
# driver = webdriver.Chrome("./drivers/macdriver")
# driver = webdriver.Chrome("./drivers/linuxdriver", chrome_options=Options) #download linuxdriver if needed

dataframe = pd.DataFrame(columns=["Title","Location","Company","Sponsored","Description"]) # Columns for CSV

joblink = "linkhere"
# Scraping
for i in range(0,50,10):

	##Step1: Get the page
	driver.get(joblink+str(i)) # Change to the indeed link you want
	# driver.get("https://www.indeed.com/jobs?q=Devops+Engineer+%240&l=Tysons+Corner%2C+VA&radius=25&sort=date"+str(i)) # <-- Example
	driver.implicitly_wait(4)

	## Finding all Elements
	all_jobs = driver.find_elements_by_class_name('result')

	for job in all_jobs:

		result_html = job.get_attribute('innerHTML')
		soup = BeautifulSoup(result_html,'html.parser')

		try:
			title = soup.find("a",class_="jobtitle").text.replace('\n','')
		except:
			title = 'None'

		try:
			location = soup.find(class_="location").text
		except:
			location = 'None'

		try:
			company = soup.find(class_="company").text.replace("\n","").strip()
		except:
			company = 'None'


		dataframe = dataframe.append({'Title':title,'Location':location,"Company":company},ignore_index=True)


dataframe.to_csv("jobs.csv",index=False)

## Here results can be emailed or moved to an s3 bucket
# For email, modify the variables at the top of emailcsv.py

# email()
# os.system('aws s3 mv ./jobs.csv s3://YourS3Bucket')

print('**** SUCCESSFULLY FOUND JOBS ****')

