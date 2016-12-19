import falcon
import json
import MySQLdb
import yaml
import subprocess
import shlex
import mimetypes
__author__ = 'weldpua2008@gmail.com'



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


class Stations(object):
    def on_get(self, req, resp, station=None):
        """Handles GET requests"""
        # db = MySQLdb.connect(host="localhost",    # your host, usually localhost
        #                      user="root",         # your username
        #                      passwd="",  # your password
        #                      db="5trips")        # name of the data base

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
        # resp.content_type = 'application/x-yaml'
        resp.body = yaml.dump(quote,default_flow_style=False)


class FileLoader(object):

    def on_get(self, req, resp, file_path=None, dir_path=None):
        # pylint: disable=unused-argument
        if dir_path is None and file_path is None:
            filename = "html/index.html"
        elif dir_path is None:
            filename = "html/%s" % file_path
        else:
            filename = "html/%s/%s" % (dir_path, file_path)
        try:
            with file(filename) as file_content:
                respound = file_content.read()
            resp.body = respound
            resp.status = falcon.HTTP_200
            # TODO: mimetypes.guess_type
            try:
                content_type = mimetypes.guess_type(filename)[0]
                resp.content_type = content_type
            # pylint: disable=broad-except,invalid-name
            except Exception as e:
                if filename.endswith('html') or filename.endswith('htm'):
                    resp.content_type = 'text/html'
                if filename.endswith('js') or filename.endswith('css'):
                    resp.content_type = 'text/plain'
                else:
                    cmd = shlex.split('file --mime-type {0}'.format(filename))
                    result = subprocess.check_output(cmd)
                    mime_type = result.split()[-1]
                    resp.content_type = mime_type
        # pylint: disable=broad-except,invalid-name
        except Exception as e:
            #resp.body ="error"
            resp.content_type = 'text/html'
            resp.body = '''<!DOCTYPE HTML>
            <html lang="en-US">
            <head profile="http://gmpg.org/xfn/11">
            <title>Error 404: Not Found</title>
            <meta charset="UTF-8" />
            </head>
            <body>
            <h2 class="page-subtitle">The page you are looking for was not found.</h2>
            <img src="/html/jpeg/404.jpeg">
            </body>
            </html>
            '''
            resp.status = falcon.HTTP_404

api = falcon.API()
api.add_route('/stations/{station}', Stations())


api.add_route('/index.html', FileLoader())
api.add_route('/html/{dir_path}/{file_path}', FileLoader())

