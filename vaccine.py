import requests
import time
from datetime import date

def main():
	retry = 1000
	for q in range(retry):
		today = date.today()
		today = today.strftime("%d-%m-%Y")
		district_id = 294
		check_method(today, district_id)
		print("waiting for 1/2 minute")
		time.sleep(30)
			


def check_method(date, district_id):
		url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=%s&date=%s" %(district_id, date)
		headers1 = { 'authority': 'cdn-api.co-vin.in',
 		'accept': 'application/json, text/plain, */*',
 		 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
 		'origin': 'https://selfregistration.cowin.gov.in',
 		'sec-fetch-site': 'cross-site',
 		'sec-fetch-mode': 'cors',
 		'sec-fetch-dest': 'empty',
 		'referer':'https://selfregistration.cowin.gov.in/',
 		'accept-language': 'en-US,en;q=0.9,pa-IN;q=0.8,pa;q=0.7',
		}
		all_center_list = []
		all_session_list = []

		r = requests.get(url,headers=headers1)
		if r.status_code !=200:
			print("status code failure")
			print(r.status_code)
			print(url)
			print(r)
		else:
			json = r.json()
			# print(json)
			list_center = json.get("centers")

			for center in list_center:
				session_list = center.get("sessions")
				for session in session_list:
					if session.get("min_age_limit") == 18:
						all_center_list.append(center)
						all_session_list.append(session)
		print("          ")

		for  a in range(len(all_center_list)):
			if all_session_list[a].get('available_capacity') > 0:
				print("\a\a\a\a\a\a\a\a\a\a")
				print(all_center_list[a].get("name"))
				print(all_center_list[a])
				print(all_session_list[a].get('available_capacity'))
				print("------------")
				print("------------")



if __name__ == "__main__":
    main()