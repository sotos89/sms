import smtplib
import requests
import csv

subject = "ddfdf"
msg = "fdffd"
gmail_account = {"user":"john.ce9@gmail.com", "password": "ljpovhtqcsicrfmt"}


def mail2textmsg(carrier:"smtp.gmail.com", msgtype="sms", phone_num="6945783433"):
    gateway = gatewaylookup(carrier=carrier, typ=msgtype)
    ph = phone_num.replace("-","")
    ph = ph.replace("(","")
    ph = ph.replace(")","")
    ph = ph.replace("+","")
    
    if len(ph) == 10:
        to = '%s@%s' % (ph, gateway)
    
        gmail_user = gmail_account["username"]
        gmail_pwd = gmail_account["password"]

        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + ph + '\n' + 'From:  ' + gmail_user + '\n' + 'Subject:%s \n'
        print(header)
        mesg = "\n".join([header, "RE: %s" % subject, ' %s \n\n' % msg])
        smtpserver.sendmail(gmail_user, ph, mesg)
        print('mail sent!')
        smtpserver.close()
    else:
        print("Phone Number is Invalid Length. Should only include 10 digits.")
        
def gatewaylookup(carrier, typ):
    gatewaylist = "https://cdn.rawgit.com/just-dantastic/blog/d20dbeab/data/textmsg_carriers.ls"
    fields = ["provider","sms","mms","other"]
    req = requests.get(gatewaylist)
    readr = csv.DictReader(req.text, fieldnames=fields)
    if carrier.lower() in [p.lower() for p in row["provider"]]:
        for row in readr:
            if carrier.lower() == row["provider"].lower():
                return row[typ]
            else:
                pass
    else:
        print("Carrier Name is Invalid. Please be sure to remove all not alphanumeric characters.")