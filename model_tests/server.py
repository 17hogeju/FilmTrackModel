import http.server
import socketserver
import urllib.parse
import pandas as pd
import json
from time import sleep
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

data = pd.read_csv('media.csv')
movie_data = data.loc[data["media_type"] == "movie"]
tv_data = data.loc[data["media_type"] == "tv"]
m_odf = pd.read_csv('./models/movie_overview.csv')
m_gdf = pd.read_csv('./models/movie_genres.csv')
m_cdf = pd.read_csv('./models/movie_credits.csv')

t_odf = pd.read_csv('./models/tv_overview.csv')
t_gdf = pd.read_csv('./models/tv_genres.csv')
t_cdf = pd.read_csv('./models/tv_credits.csv')


def apply_cos(df, media_lst, past_recs):
    res = []
    all_media = []
    all_media.extend(media_lst)
    all_media.extend(past_recs)
    for media in media_lst:
        new_l = df.loc[media].sort_values(ascending=False).index.tolist()[1:]
        new_l = [int(x) for x in new_l if int(x) not in all_media]
        res.append(new_l[:5])
    print(res)
    return res

def get_index(data, id):
    return data.index[data['id'] == id][0]

def get_cos_dict(data_indeces, odf, gdf, cdf, past_recs):
    cos_dict = {}
    overview_list = apply_cos(odf, data_indeces, past_recs)
    genres_list = apply_cos(gdf, data_indeces, past_recs)
    credits_list = apply_cos(cdf, data_indeces, past_recs)

    for index, m_loc in enumerate(data_indeces):
        m_loc = str(m_loc)
        print(f'm_loc: {m_loc}, {type(m_loc)}')
        for loc in overview_list[index]:
            print(f'loc: {loc}, {type(loc)}')
            if loc in cos_dict:
                cos_dict[loc] += odf[m_loc][loc]
            else:
                cos_dict[loc] = odf[m_loc][loc]
        for loc in credits_list[index]:
            loc = int(loc)
            if loc in cos_dict:
                cos_dict[loc] += cdf[m_loc][loc]
            else:
                cos_dict[loc] = cdf[m_loc][loc]
        for loc in genres_list[index]:
            loc = int(loc)
            if loc in cos_dict:
                cos_dict[loc] += gdf[m_loc][loc]
            else:
                cos_dict[loc] = gdf[m_loc][loc]
    sorted_cos_dict = sorted(cos_dict.items(), key=lambda x:x[1], reverse=True)

    return sorted_cos_dict



# class MyHandler(http.server.SimpleHTTPRequestHandler):
#     def _send_response(self, content):
#         self.send_response(200)
#         self.send_header('Content-Type', 'application/json')
#         self.send_header('Content-Length', str(len(content)))
#         self.end_headers()
#         self.wfile.write(content.encode('utf-8'))
        
#     def do_POST(self):
#         content_length = int(self.headers['Content-Length'])
#         raw_data = self.rfile.read(content_length)
#         parsed_data = json.loads(raw_data)
#         print("Received data:", parsed_data)

#         data_indeces = parsed_data['data']
#         past_recs = parsed_data['past_recs']

#         res = []
#         if parsed_data['media_type'] == "movie":
#             data_indeces = [get_index(movie_data, x) for x in data_indeces]
#             past_recs = [get_index(movie_data, x) for x in past_recs]
#             sorted_cos_dict = get_cos_dict(data_indeces, m_odf, m_gdf, m_cdf, past_recs)
#             for m_id, _ in sorted_cos_dict[:5]:
#                 res.append(str(movie_data.loc[m_id]["id"]))
#         else:
#             data_indeces = [get_index(tv_data, x) for x in data_indeces]
#             past_recs = [get_index(tv_data, x) for x in past_recs]
#             sorted_cos_dict = get_cos_dict(data_indeces, t_odf, t_gdf, t_cdf, past_recs)
#             for m_id, _ in sorted_cos_dict[:5]:
#                 res.append(str(tv_data.loc[m_id]["id"]))
#         print("res")
#         print(res)
#         response_data = {"result": res}
#         response_json = json.dumps(response_data)

#         self._send_response(response_json)

class MyHandler(BaseHTTPRequestHandler):
    def _send_response(self, content):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        raw_data = self.rfile.read(content_length)
        parsed_data = json.loads(raw_data)
        print("Received data:", parsed_data)

        data_indeces = parsed_data['data']
        past_recs = parsed_data['past_recs']

        res = []
        if parsed_data['media_type'] == "movie":
            data_indeces = [get_index(movie_data, x) for x in data_indeces]
            print(f'data indeces: {[x for x in data_indeces]}')
            past_recs = [get_index(movie_data, x) for x in past_recs]
            sorted_cos_dict = get_cos_dict(data_indeces, m_odf, m_gdf, m_cdf, past_recs)
            for m_id, _ in sorted_cos_dict[:5]:
                res.append(str(movie_data.loc[m_id]["id"]))
        else:
            data_indeces = [get_index(tv_data, x) for x in data_indeces]
            past_recs = [get_index(tv_data, x) for x in past_recs]
            sorted_cos_dict = get_cos_dict(data_indeces, t_odf, t_gdf, t_cdf, past_recs)
            for m_id, _ in sorted_cos_dict[:5]:
                res.append(str(tv_data.loc[m_id]["id"]))
        print("res")
        print(res)
        response_data = {"result": res}
        response_json = json.dumps(response_data)
        self._send_response(response_json)
        

Handler = MyHandler

class WebServer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.port = PORT
        self.ws = HTTPServer(("0.0.0.0", self.port), MyHandler)

    def run(self):
        print("WebServer started at Port:", self.port)
        self.ws.serve_forever()

    def shutdown(self):
        # set the two flags needed to shutdown the HTTP server manually
        self.ws._BaseServer__is_shut_down.set()
        self.ws.__shutdown_request = True

        print('Shutting down server.')
        # call it anyway, for good measure...
        self.ws.shutdown()
        print('Closing server.')
        self.ws.server_close()
        print('Closing thread.')
        self.join()

# with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
#     print(f'serving at port: {PORT}')
#     httpd.serve_forever()


if __name__=='__main__':
    webServer = WebServer()
    webServer.start()
    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            print('Keyboard Interrupt sent.')
            webServer.shutdown()
            exit(0)

# print(m_odf['0'][834])