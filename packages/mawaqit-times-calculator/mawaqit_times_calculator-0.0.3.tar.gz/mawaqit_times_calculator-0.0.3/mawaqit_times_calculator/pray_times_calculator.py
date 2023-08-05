from datetime import datetime
import os
import requests
from datetime import datetime, timedelta




class MawaqitTimesCalculator:


    def __init__(
        self,
        latitude: float,
        longitude: float,
        mosquee: str,
        login: str,
        password: str,
        token: str,
    ):

        self._latitude = latitude
        self._longitude = longitude
        self._login = login
        self._password = password
        self._mosquee = mosquee
        self._token = token



        if self._mosquee == '': 
            self._mosque = self.all_mosques_neighberhood()[0]["uuid"]
        else: self._mosque = mosquee


        if self._token == '': 
            self._token = self.apimawaqit()
        else: self._token = token



    def apimawaqit(self):
      url = 'https://mawaqit.net/api/2.0/me'
      user = self._login
      password = self._password
      response = requests.get(url, auth=(user, password))
      # if needed to save locally
      #current_dir = os.path.dirname(os.path.realpath(__file__))
      #if not os.path.exists('{}/data'.format(current_dir)):
      #  os.makedirs('{}/data'.format(current_dir))
      #text_file = open('{}/data/api.txt'.format(current_dir), "w")
      #n = text_file.write(response.json()["apiAccessToken"])
      #text_file.close()
      return response.json()["apiAccessToken"]

    def post_and_get_json(self, url, params=None, data=None, headers=None):
      import time
      import json
      session = requests.Session()
      response1 = session.get(url, params=params, data=json.dumps(data), headers=headers, timeout=30)
      response1.raise_for_status()
      return response1.json()


    def all_mosques_neighberhood(self):
        api = self.apimawaqit()
        payload = {
            "lat": self._latitude,
            "lon": self._longitude
             }
        headers = {
        'Authorization': api,
        'Content-Type': 'application/json',
         }
        api_url0 = 'https://mawaqit.net/api/2.0/mosque/search'
        all_mosques = self.post_and_get_json(url = api_url0, params=payload, data=None, headers=headers)
        # if needed to save locally
        #current_dir = os.path.dirname(os.path.realpath(__file__))  
        #text_file = open('{}/data/all_mosquee.txt'.format(current_dir), "w")
        #n = text_file.write(str(all_mosques))
        #text_file.close()
        return all_mosques


    def fetch_prayer_times(self):
      api_token = self._token
      mosque_id = self._mosque 
      headers = {'Content-Type': 'application/json',
             'Api-Access-Token': format(api_token)}	
      api_url_base = 'https://mawaqit.net/api/2.0/'
      api_url = api_url_base + 'mosque/' + mosque_id + '/prayer-times'

      response = requests.get(api_url, headers=headers)
      s1 = response.json()["times"][0]
      formater = '%H:%M'
      d = datetime.strptime(s1, formater) - timedelta(hours=0, minutes=10)

      if response.status_code == 200:
      	  
          myjson3 = {
                'Fajr': response.json()["times"][0],
                'Sunrise': response.json()["shuruq"],
                'Dhuhr': response.json()["times"][1],
                'Asr': response.json()["times"][2],
                'Sunset': response.json()["times"][3],
                'Maghrib': response.json()["times"][3],
                'Isha': response.json()["times"][4],
                'Imsak': d.strftime('%H:%M'),
                'Midnight': '00:00',
                'Jumua': response.json()["jumua"],
                'Shuruq': response.json()["shuruq"],
                'Mosque': response.json()
            }
          return myjson3 
      else:
          return response.status_code



#mawaqittimescalculator = MawaqitTimesCalculator('45.7754498', '4.7785644', "fd646008-a351-44bc-bde8-44380962f972", "???", "???" , "")
#mawaqittimescalculator = MawaqitTimesCalculator("", "", "fd646008-a351-44bc-bde8-44380962f972", "????", "???" , "")


#-------------------------- Test Code --------------------------

# sample code to run in standalone mode only
#if __name__ == "__main__":
   # api = mawaqittimescalculator.apimawaqit()
   # print(api)
   # salat = mawaqittimescalculator.fetch_prayer_times()
   # print(salat)
   # allmosque = mawaqittimescalculator.all_mosques_neighberhood()
   # print(allmosque)
