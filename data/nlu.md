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
- okie dokie
- nw
- no worries
- all good
- gud
- all gud
- yes please
- awesome
- perfect
- absolutely
- correct
- sweet
- how nice
- lovely
- ok i accept
- yo
- yay

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
- take care
- c ya
- see you later
- bye for now
- b4n
- bye
- bye it was nice talking to you
- ok then c u later
- c ya later
- catch you later
- ta ta
- ta ta bye bye
- thats enough

## intent:greet
- hey
- hiya
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
- Whats up
- wassup
- wasup
- howz going
- how r u?

## intent:ask_restaurant
- i'm looking for a place to eat
- I’m hungry. Looking out for some good restaurants
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
- how can you help me find a restaurant
- I am feeling hungry
- I need a new restaurant
- Suggest me a good restaurant
- Find a restaurant for me to eat
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you find a [american](cuisine) restaurant in [gurgaon](location).
- can you suggest an exclusive [mexican](cuisine) in [pune](location).
- where should i eat?
- I'm gonna need help finding a restaurant
- Show me an open restaurant
- are there good [pizza](cuisine:italian) in [ahmedabad](location).
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- pick a restaurant for me
- please find a restaurant for me
- I'm hungry. Looking out for some good restaurants
- I want to eat
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- show me restaurants in [delhi](location)
- I'm looking for a [chinese](cuisine) restaurant
- Show me [italian](cuisine) restaurants in [pune](location)
- [Mexican](cuisine) restaurants in [Pondicherry](location).
- I want [south indian](cuisine) food
- I'm hungry for [chinese](cuisine) food. I live in [Aurangabad](location).
- I feel like having food from [south india](cuisine)
- I feel like eating authentic [south indian](cuisine) restaurant
- Can you suggest some good restaurants in [Rishikesh](location)
- Okay. Show me some in [Allahabad](location)
- I’ll prefer [chines](cuisine:chinese)
- can you find [portuguese](cuisine) restaurant?
- I want to book [sri lankan](cusine) restaurant for dinner

## intent:ask_budget
- My maximum budget is 750
- I need a cheap less than Rs 300 restaurant serving yummy chinese food
- I don't mind paying more than 1000 for dinner in a fine dine restaurant.
- Are there any reasonable priced mexican food restaurants
- looking for cheap under 500 chinese food to eat

## intent:ask_email
- Please mail this information to me
- can you mail this to me?
- can u mail it to my email address?
- would appreciate if you send this to my email address
- can you post this info to my email?
- Send it to me
- Please email this to me
- mail me [emial@india.com](email)
- Email it to me
- my email address is [secret@abc.com](email)
- u can mail me [abc@xyz.com](email)
- this is my email [hello@mail.com](email)
- mail me the list
- email me a list of top 10 restaurants
- mail me the names of restaurants
- please mail me the list to [abc@domain.com](email)
- please share this with me
- share few more restaurant names with me
- share this over mail
- share this information with me over email

## intent:out_of_scope
 - can you suggest good french cuisine restaurants
 - can you book mexican restaurant in salt lake city
 - i want to eat bengali food for dinner
 - pls book thai restaurant tonite for two people

## lookup:cuisine
- american
- chinese
- italian
- mexican
- north indian
- south indian

## lookup:location
- New Delhi
- Gurgaon
- Noida
- Faridabad
- Allahabad
- Bhubaneshwar
- Mangalore
- Mumbai
- Ranchi
- Patna
- Mysore
- Aurangabad
- Amritsar
- Puducherry
- Varanasi
- Nagpur
- Vadodara
- Dehradun
- Vizag
- Agra
- Ludhiana
- Kanpur
- Lucknow
- Surat
- Kochi
- Indore
- Ahmedabad
- Coimbatore
- Chennai
- Guwahati
- Jaipur
- Hyderabad
- Bangalore
- Nashik
- Pune
- Kolkata
- Bhopal
- Goa
- Chandigarh
- Ghaziabad
- Ooty
- Gangtok
- Shimla

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
- b'lore

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
