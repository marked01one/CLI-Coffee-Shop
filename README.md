# Marked's Coffee Shop

<img src="https://media.giphy.com/media/qHBvLR5Ly9bcB9oaJ6/giphy.gif" width="50%" />
#### A simulation of a coffee shop using the command-line interface!

## Planned features:
  + [COMPLETE] An updated ASCII menu board created using prettytable 
  + [COMPLETE] A resources inventory containing water, milk, and coffee, alongside potential addons such as sugar and cream
  + [TESTING] Capability to receive personalized order sentences that utilizes natural language processing (maybe?) 
  + [COMPLETE] For an admin: ability to check amount of resources left in inventory & amount of money received, refill on lacking resources, and even add or remove different flavours of coffee.
  + [COMPLETE] Admin abilities safely secured behind a 2FA system using phone messages via the Twilio API.
  + And more...

## Before running the program...
 After downloading your own instance. Please fill in the required fields contained within the `EDIT_ME.py` file to allow Admin Mode to function.
 These fields contains the admin's authentication password, along with the admin's phone number and Twilio SMS account details which allow the authentication to function.

## To open the Cafe, use this command:
  
  ```
  python [full file path goes here]/main.py
  ```
Currently looking into a more elegant way of opening the Cafe, but for now, this is the most optimal solution.
