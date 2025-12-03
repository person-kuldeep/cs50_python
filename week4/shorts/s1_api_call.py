import requests
# import json
def find_titles(artist_name):
	try:
		response = requests.get("https://api.artic.edu/api/v1/artworks") 
		print("Status Code:", response.status_code)
	except requests.exceptions.RequestException as e:
		print(f"An error occurred: {e}")
		return
	else:
		data = response.json()
		# json_data = json.dumps(data, indent=4)
		# print(json_data)
		arts = data['data']
		for a in arts:
			if artist_name == a.get('artist_title'):
				print(f"* {a['title']} ")


		# print(data)
if __name__ == "__main__":		
	find_titles("Kay Rosen")		