import falcon
import json
import MySQLdb


__author__ = 'weldpua2008@gmail.com'


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="5trips")        # name of the data base

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

        resp.body = json.dumps(quote)

api = falcon.API()
api.add_route('/quote', QuoteResource())