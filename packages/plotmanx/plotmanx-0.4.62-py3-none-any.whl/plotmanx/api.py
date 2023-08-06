#!/usr/bin/python
#
import json
import os
import socketserver
import sqlite3
import sys
from datetime import datetime
from http.server import SimpleHTTPRequestHandler
from threading import Thread

import requests

from .configuration import PlotmanConfig, get_db_path


def PostDat(dp: dict, cfg: PlotmanConfig):
    # sending post request and saving response as response object
    payload = json.loads(json.dumps(dp))
    r = requests.post(url=f'{cfg.apis.target}:{cfg.apis.port}/report', data=payload)
    print(r.text)


"""


from prometheus_client.core import GaugeMetricFamily

class PlotmanCollector:

    def collect(self):
        cfg = configuration.get_validated_configs()
        jobs = Job.get_running_jobs(cfg.directories.log)
        count = len(sorted(jobs, key=job.Job.get_time_wall))
        yield GaugeMetricFamily("plotman_jobs_count", "Number of plotting jobs running", value=count)



if __name__ == "__main__":
    start_http_server(8001)
    REGISTRY.register(PlotmanCollector())
    while True:
        time.sleep(1)
"""


class GetHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        try:
            if self.path.endswith("/report"):
                content_len = int(self.headers.getheader('content-length', 0))
                post_body = self.rfile.read(content_len).decode("utf-8")
                remote_addr = os.environ.get('REMOTE_ADDR', '-')
                ts = datetime.now().strftime('%m-%d %H:%M:%S')

                con = sqlite3.connect(get_db_path)
                cur = con.cursor()

                cur.execute('''CREATE TABLE IF NOT EXISTS systemchia (
                                   tid text PRIMARY KEY,
                                   block text NOT NULL,
                                   ip text NOT NULL
                           );''')

                # Insert a row of data
                cur.execute(f"INSERT INTO systemchia VALUES ('{ts}','{post_body}','{remote_addr}')")

                con.commit()
                con.close()
                print(post_body)

                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                output = '0'
                self.wfile.write(output.encode())

        except IOError:
            self.send_error(404, "Bad request %s" % self.path)

        except ValueError:
            self.send_error(404, "{}".format(sys.exc_info()[0]))
            print(sys.exc_info())

        except KeyError:
            print(sys.exc_info())

        except IndexError:
            print(sys.exc_info())

    def do_GET(self):
        # logging.error(self.headers)
        SimpleHTTPRequestHandler.do_GET(self)


Handler = GetHandler


def apiOpen(cfg: PlotmanConfig):
    with socketserver.TCPServer(("0.0.0.0", cfg.apis.port), Handler) as httpd:
        print(f"api port %s is now listening {cfg.apis.port}")
        # httpd.serve_forever()
        httpd_thread = Thread(target=httpd.serve_forever)
        httpd_thread.setDaemon(True)
        httpd_thread.start()
        """
        try:
            thread.start()
        except KeyboardInterrupt:
            server.shutdown()
            sys.exit(0)
        """
