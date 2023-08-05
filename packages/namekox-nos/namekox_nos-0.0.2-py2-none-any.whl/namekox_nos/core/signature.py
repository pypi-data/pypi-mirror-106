#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import hmac
import base64
import hashlib

from urllib import quote_plus


def generate_signature(secret, data):
    mac = hmac.new(secret, data, hashlib.sha256).digest()
    b64 = base64.b64encode(bytes(mac))
    return quote_plus(b64)
