import requests
import time


# curl = "curl 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=294&date=01-05-2021',
#  'authority: cdn-api.co-vin.in',
#  'accept: application/json, text/plain, */*',
#  'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJjYzVkNjA0Ny0xMDJlLTQwYTEtYjQyMi1kNzA3MGI0ZmM0MzIiLCJ1c2VyX2lkIjoiY2M1ZDYwNDctMTAyZS00MGExLWI0MjItZDcwNzBiNGZjNDMyIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo4MDk1MTMzMDAwLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjk3ODI0NzYwNTEzMTYwLCJ1YSI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS84OC4wLjQzMjQuMTkyIFNhZmFyaS81MzcuMzYiLCJkYXRlX21vZGlmaWVkIjoiMjAyMS0wNS0wMVQwOTo0NjoyMy44NzBaIiwiaWF0IjoxNjE5ODYyMzgzLCJleHAiOjE2MTk4NjMyODN9.W3XVGgLkF6gkbdk5b7TV26rYmVlc0RGemuLuFPu48HA',
#  'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
#  'origin: https://selfregistration.cowin.gov.in',
#  'sec-fetch-site: cross-site',
#  'sec-fetch-mode: cors',
#  'sec-fetch-dest: empty',
#  'referer: https://selfregistration.cowin.gov.in/',
#  'accept-language: en-US,en;q=0.9,pa-IN;q=0.8,pa;q=0.7',
#  'if-none-match: W/\"3d6a3-y5MA18KGbw8LmcO/+78AV4gDahU\"',
#   --compressed"



def main():
	retry = 1000
	for q in range(retry):
		date = 1
		check_method("02-05-2021")
		print("waiting for 2 nd 1/2 minute")
		time.sleep(30)
		# 	time.sleep(60)
		# while date <10 :
		# 	date_s = "0%s-05-2021" %date
		# 	check_method(date_s)
		# 	date  = date + 1
		# 	print("waiting for a minute")

		# 	time.sleep(60)
			


def check_method(date):
		url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=294&date=%s" %date
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
		# date = date +1



if __name__ == "__main__":
    main()