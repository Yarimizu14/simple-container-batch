#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://www.hashicorp.com/')
print r.content
