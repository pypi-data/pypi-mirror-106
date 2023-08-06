#!/usr/bin/env python

import click

from public_service import PublicServicePKI
from registration_service import RegistrationService
from domain_service import DomainService
from utils import get_wsdl


@click.command()
@click.version_option()
def main():

    proxy = {"http": "http://proxy.charite.de:8080", "https": "http://proxy.charite.de:8080"}

    pki = PublicServicePKI("../config.ini", proxy=proxy)
    ca_info = pki.get_ca_info(510)

    # print(ca_info)

    with open("PN_Robert_Graetz_-_Charite_Teilnehmerservice_Berlin_2021-01-04.p12", 'rb') as pkcs12_file:
        pkcs12_data = pkcs12_file.read()

        print(pkcs12_data)
        print(type(pkcs12_data))
    pkcs12_password = "5+k,%yyy"
    rs = RegistrationService("../config.ini", proxy, pkcs12_data, pkcs12_password)

    print(rs.get_ca_info())

    result = rs.search_items_2("certificate", "VALID", None, 510, None, 1)
    # print(result)

    ds = DomainService("../config.ini", proxy, pkcs12_data, pkcs12_password)
    result = ds.list_domains(510)
    # print(result)

    # return obj.DFNCERTTypesDomainListResult(res.Change, results, acl)
    domain_list_results = ds.list_extended_domains(510)
    test = domain_list_results.result
    for domain in test:
        print(domain)
        print(type(domain))
        print(domain.name)
        print(domain.type)
        print(domain.secret)
        print(domain.approved)
        print(domain.approved_date)
        print(domain.method)
        print(domain.br_version)
        print(domain.challenge_mail_address)
        print(domain.last_challenge_mail_sent)
        print(domain.valid_until)



if __name__ == '__main__':
    main()
