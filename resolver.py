#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from ipaddress import IPv4Network
from dns import reversename, resolver


with open('./data/prefixes.json') as json_data:
    d = json.load(json_data)
    print(d[0]['network'])

with open('./data/reverse.json', 'w') as outfile:
    for addr in IPv4Network(d[0]['network']):
        ip = str(addr)
        process = reversename.from_address(ip)
        '''
        # Dump
        print(ip + ' ===> ' + str(resolver.query(process, "PTR")[0]))
        '''
        reverse = str(resolver.query(process, "PTR")[0])
        result = {"ip": ip}, {'reverse': reverse}
        json.dump(result, outfile)
