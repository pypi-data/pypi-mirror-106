#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import nos
import time

from urllib import quote_plus
from namekox_nos.constants import NOS_CONFIG_KEY
from namekox_core.core.friendly import AsLazyProperty
from namekox_nos.core.signature import generate_signature
from namekox_core.core.service.dependency import Dependency


class NosHelper(Dependency):
    def __init__(self, domain, **options):
        self.client = None
        self.domain = domain
        self.options = options

        self.end_point = ''
        self.enable_ssl = False
        self.access_key_id = ''
        self.access_key_secret = ''
        super(NosHelper, self).__init__(domain, *options)

    def setup(self):
        config = self.configs[self.domain]
        config.update(self.options)
        self.end_point = config.get('end_point', '')
        self.enable_ssl = config.get('enable_ssl', False)
        self.access_key_id = config.get('access_key_id', '')
        self.access_key_secret = config.get('access_key_secret', '')
        self.client = nos.Client(**config)

    @AsLazyProperty
    def configs(self):
        return self.container.config.get(NOS_CONFIG_KEY, {})

    def gen_url(self, bucket_name, object_name, ttl=31536000):
        name = quote_plus(object_name)
        expires_time = int(time.time()) + ttl
        path = '/{}/{}'.format(bucket_name, name)
        data = '{}\n{}\n{}\n{}\n{}{}'.format('GET', '', '', expires_time, '', path)
        sign = generate_signature(self.access_key_secret, data)
        protocol = 'https' if self.enable_ssl else 'http'
        data = [
            protocol, bucket_name, self.end_point,
            name, self.access_key_id, expires_time, sign
        ]
        return '{}://{}.{}/{}?NOSAccessKeyId={}&&Expires={}&Signature={}'.format(*data)
