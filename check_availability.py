import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

COURSE_AVAILABILITY_URL = 'https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in={term}&crn_in={csn}'
DEFAULT_TERM = 202405

def get_availability(csn : str, term = DEFAULT_TERM):

	html_content = fetch_html(
		COURSE_AVAILABILITY_URL.format(csn = csn, term = term)
		)
	soup = BeautifulSoup(html_content, 'html.parser')

	# import table datadisplaytable
	tables = soup.find_all('table')
	table = tables[4]
	# Use pandas to read HTML table
	df = pd.read_html(str(table))[0]

	print(df[3][1], df[3][2])

	# return df['Remaining']


def fetch_html(url):
	try:
		response = requests.get(url)
		# Check if the request was successful (status code 200)
		if response.status_code == 200:
			return response.text
		else:
			print(f"Failed to fetch HTML. Status code: {response.status_code}")
			return None
	except Exception as e:
		print(f"An error occurred: {e}")
		return None


if __name__ == "__main__":
	print( get_availability('52498') )