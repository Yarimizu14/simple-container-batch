#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime

msg = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
r = requests.post('http://ec2-54-199-208-148.ap-northeast-1.compute.amazonaws.com/messages/{}'.format(msg))
print r.content
