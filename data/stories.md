## complete path
* greet
    - utter_greet
* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* ask_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* ask_restaurant{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* ask_restaurant{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye


## happy_path
* greet
    - utter_greet
* ask_restaurant{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* ask_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
