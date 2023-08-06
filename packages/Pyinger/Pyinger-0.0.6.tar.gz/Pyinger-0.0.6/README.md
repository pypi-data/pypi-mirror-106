You will need python3

PACKAGES
---------------------------------------

import like so:

from Pyinger import checker

To use instantiate an object of Pinger like:

Server = checker.PingChecker("www.google.com")
---------------------------------------

You can either pass in a list of url's or just one as a string like:

server_list = ['www.google.com', "www.youtube.com", "www.facebook.com"]
Server = checker.PingChecker(server_list)

OR 


ServerChecker = checker.Pinger("www.google.com")
---------------------------------------

To call the ping server method do so like:
ServerChecker.ping_server(10, False, "email@username", "email@password", "email@recipient")

---------------------------------------

The first argument is how often you want to ping the server. 15 seconds is the default.
The second argument is a boolean if you would like to email which notifies which server is down.
By default it is False. Set to True to turn on. Only works for GMAIL.

The next three arguments are:

email username
email password
email recipient




