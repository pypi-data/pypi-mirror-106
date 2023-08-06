from ping3 import ping
import time
from datetime import datetime
from colorama import Fore
import smtplib

class PingChecker:

    def __init__(self, url_list):

        self.url_list = url_list

        print("")
        print("")
        print(f"{Fore.CYAN}  #####   #######    #    #    #######  ")
        print(f"{Fore.CYAN}  #   #      #       # #  #    #")
        print(f"{Fore.CYAN}  ####       #       #  # #    #######  ")
        print(f"{Fore.CYAN}  #          #       #   ##    #     #  ")
        print(f"{Fore.CYAN}  #       #######    #    #    #######  ")
        print("")
        print(f"{Fore.CYAN}  ----------------------------------------  ")
        print("")

        if self.url_list == "":
            print("      ----- ENTER A VALID URL -----")


    def ping_server(self, timeDelay = 15, gmailNotify = False, emailUsername = "", userPassword = "", userRecipient = ""):

        self.timeDelay = timeDelay
        self.gmailNotify = gmailNotify

        if self.gmailNotify == True:
                self.emailUsername = emailUsername
                self.userPassword = userPassword
                self.userRecipient = userRecipient

        print("")

        if self.url_list != "":

            while True:

                self.now = datetime.now()
                self.today = self.now.strftime("%d/%m/%Y %H:%M:%S")

                print(f"{Fore.CYAN}  --- Checking every {self.timeDelay} seconds ---")
                print("")
                print("")

                if type(self.url_list) == str:

                    self.r = ping(self.url_list)
                    
                    if self.r is None or False:
                        print(f"{Fore.RED}  SERVER --- {self.url_list} -> IS DOWN --- {Fore.CYAN}  {self.today}")
                        print(f"{Fore.MAGENTA}  -------------------------------------------------------------------------------------------")
                        print("")
                        print(f"{Fore.RED}  ----- ^ ^ ^ ^ ^ CHECK SERVER ^ ^ ^ ^ ^ -----")
                        print("")
                        print("")

                        if self.gmailNotify == True:
                            self.EmailNotify(self.url_list)
                        
                    else: 
                        print(f"{Fore.GREEN}  SERVER --- {self.url_list} -> IS UP: --- RESPONSE: {str(round(self.r, 5))} --- {Fore.CYAN} {self.today}")
                        print(f"{Fore.MAGENTA}   -------------------------------------------------------------------------------------------")
                        print("")
                        print("")


                elif type(self.url_list) == list:

                    for self.curr_url in self.url_list:

                        self.res = ping(self.curr_url)
                        
                        if self.res is None or False:
                            print(f"{Fore.RED}  SERVER ---- {self.curr_url} -> IS DOWN --- {Fore.CYAN} {self.today}")
                            print(f"{Fore.MAGENTA}  -------------------------------------------------------------------------------------------")
                            print("")
                            print(f"{Fore.RED}  ----- ^ ^ ^ ^ ^ CHECK SERVER ^ ^ ^ ^ ^ -----")
                            print("")
                            print("")

                            if self.gmailNotify == True:
                                self.EmailNotify(self.curr_url)
                        
                        else:
                            print(f"{Fore.GREEN}  SERVER --- {self.curr_url} -> IS UP: --- RESPONSE: {str(round(self.res, 5))} --- {Fore.CYAN} {self.today}")
                            print(f"{Fore.MAGENTA}  -------------------------------------------------------------------------------------------")
                            print("")
                            print("")

                print("")
                print("")
                time.sleep(self.timeDelay)



    def EmailNotify(self, urlDown):

        self.urlDown = urlDown

        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.emailUsername, self.userPassword)
        self.body = f"{self.urlDown} IS DOWN. \n\n CHECK IMMEDIATELY! \n\n PING"
        self.subject = "PING - SERVER IS DOWN"
        self.serverMessage = 'Subject: {}\n\n{}'.format(self.subject, self.body)
        self.server.sendmail(self.emailUsername, self.userRecipient, self.serverMessage)
        self.server.quit()
        print("")
        print(f"{Fore.MAGENTA}  EMAIL HAS BEEN SENT TO {self.userRecipient}")