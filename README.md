# gmailc2
     A Fully Undetectable C2 Server That Communicates Via Google SMTP to evade Antivirus Protections 
     and Network Traffic Restrictions
![gma](https://user-images.githubusercontent.com/82051128/210650476-b153229d-b70e-4d24-ad8a-ed08b6a3144b.png)


# Note:
     This RAT communicates Via Gmail SMTP (or u can use any other smtps as well) but Gmail SMTP is valid
     because most of the companies block unknown traffic so gmail traffic is valid and allowed everywhere.
     
# Contact:
    Telegram:- https://t.me/machine1337
# Warning:
     1. Don't Upload Any Payloads To VirusTotal.com Bcz This tool will not work
        with Time.
     2. Virustotal Share Signatures With AV Comapnies.
     3. Again Don't be an Idiot!
   
# How To Setup
     1. Create Two seperate Gmail Accounts.
     2. Now enable SMTP On Both Accounts (check youtube if u don't know)
     3. Suppose you have already created Two Seperate Gmail Accounts With SMTP enabled
        A -> first account represents  Your_1st_gmail@gmail.com
        B -> 2nd account   represents  your_2nd_gmail@gmail.com
     4. Now Go To server.py file and fill the following at line 67:
        smtpserver="smtp.gmail.com"          (don't change this)
        smtpuser="Your_1st_gmail@gmail.com"  
        smtpkey="your_1st_gmail_app_password"
        imapserver="imap.gmail.com"    (don't change this)
        imapboy="your_2nd_gmail@gmail.com"
    5. Now Go To client.py file and fill the following at line 16:
        imapserver = "imap.gmail.com"          (dont change this)
        username = "your_2nd_gmail@gmail.com"
        password = "your2ndgmailapp password"
        getting = "Your_1st_gmail@gmail.com"
        smtpserver = "smtp.gmail.com"          (don't change this)
    6. Enjoy
# How To Run:-
     *:- For Windows:-
     1. Make Sure python3 and pip is installed and requriements also installed
     2. python server.py  (on server side)
     
   
     *:- For Linux:-
     1. Make Sure All Requriements is installed.
     2. python3 server.py  (on server side)
# C2 Feature:-
     1) Persistence (type persist)
     2) Shell Access 
     3) System Info (type info)
     4) More Features Will Be Added 
    
# Features:-

    1) FUD Ratio 0/40
    2) Bypass Any EDR's Solutions
    3) Bypass Any Network Restrictions
    4) Commands Are Being Sent in Base64 And Decoded on server side
    5) No More Tcp Shits
  
# Warning:-
    Use this tool Only for Educational Purpose And I will Not be Responsible For ur cruel act.
  
    
   
