import falcon
import json
import MySQLdb
import yaml

__author__ = 'weldpua2008@gmail.com'


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="5trips")        # name of the data base

TOA_HOURS = '10'
TOA_SECONDS = '0'
Station = 13031

try:
    with open("/app/settings.yml", 'r') as stream:
        try:
            settings = yaml.load(stream)
            try:
                if 'toa' in settings:
                    TOA = settings['toa']
                    TOA_HOURS = TOA.split(":")[0]
                    TOA_SECONDS = TOA.split(":")[1]
            except Exception:
                pass

            try:
                if 'station' in settings:
                    Station = settings['station']
            except Exception:
                pass

        except yaml.YAMLError as exc:
            pass
except Exception:
    pass


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        # cur = db.cursor()
        #
        # # Use all the SQL you like
        # cur.execute("SELECT * FROM YOUR_TABLE_NAME")
        #
        # # print all the first cell of all the rows
        # for row in cur.fetchall():
        #     print row[0]
        #
        # db.close()
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }
        resp.content_type = 'application/x-yaml'
        resp.body = yaml.dumps(quote)

api = falcon.API()
api.add_route('/quote', QuoteResource())