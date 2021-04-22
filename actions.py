from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import logging

logger = logging.getLogger(__name__)
ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		results = RestaurantSearch(City=loc,Cuisine=cuisine)
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in RestaurantSearch(loc,cuisine).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"

		dispatcher.utter_message("-----"+response)
		return
		#return [SlotSet('location',loc)]

""" Custom action to validate input location
"""
class ActionValidateLocation(Action):
    def name(self):
        return "action_location_valid"

    def run(self, dispatcher, tracker, domain):
    	location = tracker.get_slot("location")
    	logger.debug(f"Find location -> '{location}'")
    	location_validity = ("valid" if location.lower() in (city.lower() for city in WeOperate) else "invalid")
    	return [SlotSet("location_validity", location_validity)]

""" Custom action to validate input cuisine
"""
class ActionValidateCuisine(Action):
    def name(self):
        return "action_cuisine_valid"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        cuisine_validity = "valid"

        if not cuisine:
            cuisine_validity = "invalid"
        else:
            supported_cuisines = [
                "american",
                "chinese",
                "italian",
                "mexican",
                "north indian",
                "south indian",
            ]

            cuisine_validity = (
                "invalid" if cuisine.lower() not in supported_cuisines else "valid"
            )

        return [SlotSet("cuisine_validity", cuisine_validity)]

def filter_restaurant_by_budget(self, budget, restaurant_list) -> list:
	filtered_restaurant_list = []

	"""
		Set the budget range based on input
	"""
	rangeMin = 0
	rangeMax = 999999

	if budget == "lesser than 300":
		rangeMax = 299
	elif budget == "between 300 to 700":
		rangeMin = 300
		rangeMax = 700
	elif budget == "more than 700":
		rangeMin = 701
	else:
		"""
			Default budget
		"""
		rangeMin = 0
		rangeMax = 9999

	for restaurant in restaurant_list:
		avg_cost = int(restaurant["Average Cost for two"])

		if avg_cost >= rangeMin and avg_cost <= rangeMax:
			filtered_restaurant_list.append(restaurant)

	return filtered_restaurant_list


class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		sendmail(MailID,response)
		return [SlotSet('mail_id',MailID)]
