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
* affirm
    - utter_goodbye

## story_2_location_cuisine_valid_deny_email
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
  * deny
      - utter_bon_appetit

## story_3_location_invalid_retry
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
* affirm
    - utter_goodbye

## story_4_location_given
  * greet
    - utter_greet
  * ask_restaurant{"location": "surat"}
    - slot{"location": "surat"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
  * ask_restaurant{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
  * ask_budget{"budget": "lesser than 300"}
    - slot{"budget": "lesser than 300"}
    - action_search_restaurants
    - slot{"email_message": ""}
    - utter_ask_details
  * affirm
    - utter_ask_email
  * ask_email{"email": "petu@south.com"}
    - slot{"email": "petu@south.com"}
    - action_send_email
    - utter_confirm_email
  * affirm
    - utter_goodbye

## story_5_no_greet
* ask_restaurant{"location": "vizag"}
  - slot{"location": "vizag"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "North Indian"}
  - slot{"cuisine": "North Indian"}
  - utter_ask_budget
* ask_budget{"budget": "lesser than 300"}
  - slot{"budget": "lesser than 300"}
  - action_search_restaurants
  - slot{"email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "petu@south.com"}
  - slot{"email": "petu@south.com"}
  - action_send_email
  - utter_confirm_email
* affirm
  - utter_goodbye

## story_6_no_greet_invalid_location_retry
* ask_restaurant{"location": "vizi"}
  - slot{"location": "vizi"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
* ask_restaurant{"location": "vizag"}
  - slot{"location": "vizag"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Italian"}
  - slot{"cuisine": "Italian"}
  - utter_ask_budget
* ask_budget{"budget": "between 300 to 700"}
  - slot{"budget": "between 300 to 700"}
  - action_search_restaurants
  - slot{"email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": ".com"}
  - slot{"email": ".com"}
  - action_send_email
  - utter_confirm_email
* affirm
  - utter_goodbye

## story_7_given_location_cuisine_with_valid_email
* ask_restaurant{"cuisine": "chinese", "location": "goa"}
  - slot{"cuisine": "chinese"}
  - slot{"location": "goa"}
  - utter_ask_budget
* ask_budget{"budget": "more than 700"}
  - slot{"budget": "more than 700"}
  - action_search_restaurants
  - slot{"email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@typ.com"}
  - slot{"email": "abc@typ.com"}
  - action_send_email
  - slot{"email": "abc@typ.com"}
  - utter_confirm_email
* affirm
  - utter_goodbye

## story_8_given_location_cuisine_deny_email
* ask_restaurant{"location": "pune", "cuisine": "north indian"}
  - slot{"cuisine": "north indian"}
  - slot{"location": "pune"}
  - utter_ask_budget
* ask_budget{"budget": "more than 700"}
  - slot{"budget": "more than 700"}
  - action_search_restaurants
  - slot{"email_message": ""}
  - utter_ask_details
* deny
  - utter_bon_appetit

## story_9_location_out_of_scope_goodbye
  * ask_restaurant{"cuisine": "italian", "location": "milan"}
      - slot{"cuisine": "italian"}
      - slot{"location": "milan"}
      - action_location_valid
      - slot{"location_validity": "invalid"}
      - utter_location_invalid
  * goodbye
      - utter_goodbye

## story_10_given_valid_location_cuisine_email
  * ask_restaurant{"cuisine": "chinese", "location": "pune"}
      - slot{"cuisine": "chinese"}
      - slot{"location": "pune"}
      - action_location_valid
      - slot{"location_validity": "valid"}
      - action_cuisine_valid
      - slot{"cuisine_validity": "valid"}
      - utter_ask_budget
  * ask_budget{"budget": "more than 700"}
      - slot{"budget": "more than 700"}
      - action_search_restaurants
      - slot{"email_message": ""}
      - utter_ask_details
  * affirm
      - utter_ask_email
  * ask_email{"email": "abc@xyz.com"}
      - slot{"email": "abc@xyz.com"}
      - action_send_email
      - slot{"email": "abc@xyz.com"}
      - utter_confirm_email
  * affirm
      - utter_goodbye

## story_11_given_invalid_cuisine_retry
  * ask_restaurant{"cuisine": "rajasthani"}
      - slot{"cuisine": "rajasthani"}
      - action_cuisine_valid
      - slot{"cuisine_validity": "invalid"}
      - utter_cuisine_invalid
      - utter_ask_cuisine
  * ask_restaurant{"cuisine": "chinese"}
      - slot{"cuisine": "chinese"}
      - utter_ask_location
  * ask_restaurant{"location": "Kolkata"}
      - slot{"location": "Kolkata"}
      - action_location_valid
      - slot{"location_validity": "valid"}
      - utter_ask_budget
  * ask_budget{"budget": "more than 700"}
      - slot{"budget": "more than 700"}
      - action_search_restaurants
      - slot{"email_message": ""}
      - utter_ask_details
  * ask_email{"email": "foodie@vgt.com"}
      - slot{"email": "foodie@vgt.com"}
      - action_send_email
      - slot{"email": "foodie@vgt.com"}
      - utter_confirm_email
  * affirm
      - utter_goodbye
