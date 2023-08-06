#!/usr/bin/env python

import csv
import datetime
import os
import re
import signal
import sys

import bonsai
import requests


def main():
    response = requests.get("http://argos.charite.de/api/charite-pki/valid_certificates")

    valid_certs = response.json()

    for cert in valid_certs:
        emails = []
        if "email" in cert and cert["email"]:
            if ", " in cert["email"]:
                emails = cert["email"].split(", ")
            else:
                emails = [cert["email"]]

        role = cert["role"]
        if role == "802.1.X User":
            for mail in emails:
                if "bihealth.de" in mail and len(emails) < 2:
                    print(emails)
                    print(cert)
                    name = ""
                    if cert['additional_name']:
                        name = cert['additional_name']
                    else:
                        if cert["subject"]:
                            print(cert["subject"])
                            name = re.search(r'CN=([\w+\s-]*),', cert["subject"]).group(1)
                        else:
                            name = "Unbekannt"
                    print(f"Das Zertifikat vom Nutzer {name} besitzt nur einen @bihealt.de-Maileintrag.")





def test():

    response = requests.get("http://argos.charite.de/api/charite-pki/valid_certificates")

    valid_certs = response.json()


    function_email_list = []

    with open("function_emails.csv", "r") as csv_file:
        func_email_reader = csv.reader(csv_file)
        function_email_list = [row[0] for row in func_email_reader]

    base = "cn=Personen,dc=charite.de"

    ldap_user = "uid=adminread,cn=Personen,dc=charite.de"
    ldap_secret = "itzldap"

    i = 0
    client = bonsai.LDAPClient("ldaps://kruemel.charite.de")
    client.set_credentials("SIMPLE", user=ldap_user, password=ldap_secret)

    conn = client.connect()

    for cert in valid_certs:
        email = []
        if "email" in cert and cert["email"]:
            if ", " in cert["email"]:
                email = cert["email"].split(", ")
            else:
                email = [cert["email"]]

        add_email = []
        if "additonal_email" in cert and cert["additonal_email"]:
            if ", " in cert["additonal_email"]:
                add_email = cert["additonal_email"].split(", ")
            else:
                add_email = [cert["additonal_email"]]
        emails = list(set(email + add_email))

        role = cert["role"]
        if role == "802.1.X User":
            # if not any(func_email in emails for func_email in function_email_list):
            for func_mail in function_email_list:
                if func_mail in emails:
                    emails = [e for e in emails if e != func_mail]
            if emails:
                results = [conn.search(base, 2, f"(mail={email_addr[:email_addr.index('@')+1]}*)") for email_addr in emails]
                if [res for res in results if res != []]:
                    pass
                    print(results)

    conn.close()


if __name__ == "__main__":
    main()
