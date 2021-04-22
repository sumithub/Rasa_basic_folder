## story_1_location_cuisine_valid
* greet
    - utter_greet
* ask_restaurant
    - utter_ask_location
* ask_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
  - utter_goodbye

## story_2_location_invalid_retry
  * greet
      - utter_greet
  * ask_restaurant
      - utter_ask_location
  * ask_restaurant{"location": "melbourne"}
      - slot{"location": "melbourne"}
      - utter_ask_cuisine
  * ask_restaurant{"cuisine": "Mexican"}
      - slot{"cuisine": "Mexican"}
      - action_location_valid
      - slot{"location_validity": "invalid"}
      - utter_location_invalid
  * ask_restaurant{"location": "delhi"}
      - slot{"location": "delhi"}
      - action_location_valid
      - slot{"location_validity": "valid"}
      - action_search_restaurants
  * affirm
      - utter_goodbye

## interactive_story_2
  * greet
      - utter_greet
  * ask_restaurant
      - utter_ask_location
  * ask_restaurant{"location": "delhi"}
      - slot{"location": "delhi"}
      - utter_ask_cuisine
  * ask_restaurant{"cuisine": "chinese"}
      - slot{"cuisine": "chinese"}
      - action_location_valid
      - slot{"location_validity": "valid"}
      - slot{"location": "delhi"}
      - utter_ask_budget
  * ask_budget{"budget": "more than 700"}
      - slot{"budget": "more than 700"}
      - action_search_restaurants
  * affirm
      - utter_goodbye
