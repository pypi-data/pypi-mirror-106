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
                results = [conn.search(base, 2, f"(mail={email_addr})") for email_addr in emails]
                if not [res for res in results if res != []]:
                    # check_other_domain(conn, base, emails)
                    # i = i + 1
                    # print(results)
                    pass

                    # found user with wrong email address

    # print(i)
    conn.close()


def check_other_domain(conn, base: str, emails: list):
    results = [conn.search(base, 2, f"(mail={email_addr[:email_addr.index('@')]}*)") for email_addr in emails]
    if not [res for res in results if res != []]:

        mail = emails[0]
        if '.' not in mail[:mail.index('@')]:
            return None
        cn_normal = mail[:mail.index('@')]
        cn_normal = re.sub(r'[.-_]', '', cn_normal)
        cn_normal_search = conn.search(base, 2, f"(cnNormal={cn_normal})")
        if len(cn_normal_search) > 0 and "DatumExStudenten" in cn_normal_search[0]:
            date_str = list(cn_normal_search[0]["DatumExStudenten"])[0]
            # print(f"date_str: {date_str}")
            try:
                exit_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                # print(exit_date)
                if datetime.datetime.now() > exit_date:
                    print(exit_date)
                    print(cn_normal_search)
                    cn = list(cn_normal_search[0].get("cn", "Unbekannt"))[0]
                    print(cn)
            except ValueError as value_err:
                print(value_err)


def find_ey_employee():
    pass


if __name__ == "__main__":
    main()
