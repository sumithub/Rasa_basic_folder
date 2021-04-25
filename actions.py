from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import logging
import operator

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		#print('budget -> ' +budget)
		results = RestaurantSearch(City=loc,Cuisine=cuisine)
		#print(len(results))
		# filter list by ask_budget
		filtered_restaurant_list = filter_restaurant_by_budget(budget,results)
		#print(len(filtered_restaurant_list))
		console_response=""
		email_response=""
		are_results_valid = "valid"
		if len(filtered_restaurant_list) == 0:
			console_response= "no results"
		else:
			title = 'Showing you top rated ' + cuisine + ' restaurants in ' + loc +'\n \n'
			console_response = console_response + title
			email_response = email_response + title
			counter = 0
			for restaurant in filtered_restaurant_list:
				if (counter <10):
					counter = counter+1
					# email_response
					email_response=email_response + F" {counter}.Restaurant: {restaurant['Restaurant Name']} \n Address: {restaurant['Address']} \n Average Cost for two: {restaurant['Average Cost for two']} \n Zomato user rating: {restaurant['Aggregate rating']} \n\n"
					# console response
					if (counter < 5):
						console_response=console_response + F" {counter}. {restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']}\n\n"
				else:
					break
		dispatcher.utter_message("-----"+console_response)
		# check results validity
		are_results_valid = (
			"invalid" if len(filtered_restaurant_list) == 0 else "valid"
		)
		return [SlotSet("email_message", email_response), SlotSet("results_validity", are_results_valid)]

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

def filter_restaurant_by_budget(budget, restaurant_list) -> list:
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

	for restaurant in restaurant_list.iloc[:100].iterrows():
		restaurant = restaurant[1]
		#print(restaurant['Average Cost for two'])
		avg_cost = restaurant["Average Cost for two"]

		if avg_cost >= rangeMin and avg_cost <= rangeMax:
			filtered_restaurant_list.append(restaurant)
			#print(restaurant['Average Cost for two'])
	sorted_list = new_list = sorted(filtered_restaurant_list, key=operator.attrgetter('Aggregate rating'), reverse=True)
	return sorted_list


class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		email_message = tracker.get_slot('email_message')
		sendmail(email,email_message)
		return [SlotSet('email',email)]

def sendmail(email,email_message):
    print(email_message)
    mail_content = email_message
    #The mail addresses and password
    sender_address = 'aibot2501@gmail.com'
    sender_pass = 'humtum123'
    receiver_address = email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Rasa Chatbot. It has Top restaurant list'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as e:
        print("failed to send an email")
        print(e)
