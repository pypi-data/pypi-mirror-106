#!/usr/bin/env python

import base64
import time

import paramiko


def main():

    hostname = "argos.charite.de"
    username = "rgraetz-adm"
    password = "5+k,%yyy"
    cert_password = "5+k,%yyy"
    cert_file_name = "PN_Robert_Graetz_-_Charite_Teilnehmerservice_Berlin_2021-01-04.p12"
    with open(cert_file_name, 'rb') as pkcs12_file:
        pkcs12_data = pkcs12_file.read()

    b = base64.b64encode(pkcs12_data)

    commands = [
        "unset HISTFILE",
        # "source venv/bin/activate",
        # "pip freeze",
        # f"python3 test.py '5+k,%yyy' '{b}'"
        f"bash run_pki.sh '{cert_password}' \"{b}\""
    ]

    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    # execute the commands
    for command in commands:
        print("="*50, command, "="*50)
        # timeout=20
        stdin, stdout, stderr = client.exec_command(command)
        time.sleep(5)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)


if __name__ == "__main__":
    main()
