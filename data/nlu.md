## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- okay
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- alright

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- tc


## intent:greet
- hey
- hola
- howdy
- hey there
- hello
- hallo
- good day
- good morning
- good evening
- good afternoon
- dear sir
- hi
- sup
- Whats up
- wassup
- wasup

## intent:ask_restaurant
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- can you find a [american](cuisine) restaurant in [gurgaon](location).
- can you suggest an exclusive [mexican](cuisine) in [pune](location).
- are there good [pizza](cuisine:italian) in [ahmedabad](location).
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- show me restaurants in [delhi](location) under [500](price)
- I'm looking for a [chinese](cuisine) restaurant under [1000](price)
- Show me [italian](cuisine) restaurants in [pune](location)
- [Mexican](cuisine) restaurants in [Pondicherry](location).
- I want [south indian](cuisine) food
- I'm hungry for [chinese](cuisine) food. I live in [Aurangabad](location) and i have [500](price) rupees
- Im [broke](price:low)
- [Cheap](price:low) places to eat
- [Pocket friendly](price:low) restaurants
- I feel like having food from [south india](cuisine)
- Table for [3](people)
- There are [5](people) of us
- [budget friendly](price:low)
- I want to [splurge](price:high) on [italian](cuisine) food
- I feel like eating at an [expensive](price:high) restaurant
- [Just me](people:1)

## intent:ask_budget
- My maximum budget is 750
- I need a cheap less than Rs 300 restaurant serving yummy chinese food
- I don't mind paying more than 1000 for dinner in a fine dine restaurant.
- Are there any reasonable priced mexican food restaurants

## intent:ask_email
- my email address is secret@abc.com
- u can mail me abc@xyz.com
- this is my email hello@mail.com

## intent:out_of_scope
 - can you suggest good french cuisine restaurants
 - can you book mexican restaurant in salt lake city
 - i want to eat bengali food for dinner
## synonym:5
- five

## synonym:4
- four

## synonym:3
- three

## synonym:2
- two

## synonym:1
- one

## synonym:Delhi
- New Delhi
- deli
- dilli
- dhilli

## synonym:Pune
- poona
- puna

## synonym:Mysore
- Mysuru

## synonym:Bangalore
- Bengaluru
- blore

## synonym:Puducherry
- Pondicherry

## synonym:Kolkata
- Calcutta

## synonym:Shimla
- Simla

## synonym:Vizag
- Visakhapatnam

## synonym:Kochi
- Cochin

## synonym:Chennai
- mardas

## synonym:chinese
- chines
- Chinese
- Chines
- dumplings

## synonym:South Indian
- South india
- North india

## synonym:Mexican
- mexico

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg
- veg

## regex:greet
- hey[^\s]*
- hello[^\s]*

## regex:pincode
- [0-9]{6}
