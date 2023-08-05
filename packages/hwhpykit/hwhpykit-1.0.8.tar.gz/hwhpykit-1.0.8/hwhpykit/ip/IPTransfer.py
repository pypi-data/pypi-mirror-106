import geoip2.database
import os
import sys


class IPTransfer(object):

    def __init__(self, db_path=None):
        if not db_path:
            base_path = os.path.abspath(__file__)
            folder = os.path.dirname(base_path)
            db_path = os.path.join(folder, 'GeoLite2-City.mmdb')
        self.reader = geoip2.database.Reader(db_path)

    def ip_to_city(self, ip):
        try:
            response = self.reader.city(ip)
            if response.city.names['zh-CN']:
                return response.city.names['zh-CN']
            else:
                return response.city.name
        except Exception as e:
            print(e)
            return None


#if __name__ == '__main__':
    #IPTransfer.ip_to_city("47.244.101.138")