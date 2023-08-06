def get_errors():

    result = {}

    valid_certs = models.ValidCertificates.query.all()

    function_email_list = []

    with open("app/function_emails.csv", "r") as csv_file:
        func_email_reader = csv.reader(csv_file)
        function_email_list = [row[0] for row in func_email_reader]


    base = "cn=Personen,dc=charite.de"

    ldap_user = "uid=adminread,cn=Personen,dc=charite.de"
    ldap_secret = "itzldap"

    client = bonsai.LDAPClient("ldaps://kruemel.charite.de")
    client.set_credentials("SIMPLE", user=ldap_user, password=ldap_secret)

    conn = client.connect()

    for cert in valid_certs:
        if isinstance(cert.email, list):
            emails = cert.email.split(", ")
        else:
            emails = []
        alt_email = cert.additional_email
        role = cert.role

        if emails and role == "8":
            email_addresses = emails.split(", ")
            if not any(func_email in emails for func_email in function_email_list):
                results = [conn.search(base, 2, f"(mail={email_addr})") for email_addr in email_addresses]
                if not [res for res in results if res != []]:
                    result[cert.serial] = cert

    conn.close()

    return result
