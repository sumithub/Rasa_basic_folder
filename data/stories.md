## story_1_location_cuisine_valid
* greet
    - utter_greet
* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* ask_budget{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## story_2_cuisine_is_invalid
* greet
  - utter_greet
* ask_restaurant{"cuisine": "portugese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
* affirm
  - utter_goodbye
