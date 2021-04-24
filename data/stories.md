## story_1_location_cuisine_valid_with_email
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
* ask_budget{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "abc@abc.com"}
    - slot{"email": "abc@abc.com"}
    - action_send_email
    - utter_confirm_email

## interactive_story_1
  * greet
      - utter_greet
  * ask_restaurant
      - utter_ask_location
  * ask_restaurant{"location": "Bangalore"}
      - slot{"location": "Bangalore"}
      - action_location_valid
      - slot{"location_validity": "valid"}
      - utter_ask_cuisine
  * ask_restaurant{"cuisine": "chinese"}
      - slot{"cuisine": "chinese"}
      - utter_ask_budget
  * ask_budget{"budget": "300-700 range"}
      - slot{"budget": "300-700 range"}
      - action_search_restaurants
      - slot{"email_message": ""}
      - utter_ask_details
  * ask_email{"email": "ahbcdj@dkj.com"}
      - slot{"email": "ahbcdj@dkj.com"}
      - action_send_email
      - utter_confirm_email

## interactive_story_2_deny_email
  * greet
      - utter_greet
  * ask_restaurant
      - utter_ask_location
  * ask_restaurant{"location": "Bangalore"}
      - slot{"location": "Bangalore"}
      - action_location_valid
      - slot{"location_validity": "valid"}
      - utter_ask_cuisine
  * ask_restaurant{"cuisine": "chinese"}
      - slot{"cuisine": "chinese"}
      - utter_ask_budget
  * ask_budget{"budget": "300-700 range"}
      - slot{"budget": "300-700 range"}
      - action_search_restaurants
      - slot{"email_message": ""}
      - utter_ask_details
  * deny_email
      - utter_bon_appetit

## story_2_location_invalid_retry
* greet
    - utter_greet
* ask_restaurant{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
* ask_restaurant{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* ask_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* ask_budget{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_details
* ask_email{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - utter_confirm_email
