# from http.server import BaseHTTPRequestHandler, HTTPServer
#
#
# # HTTPRequestHandler
#
# class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         # send response status
#         self.send_response(200)
#
#         # send header
#         self.send_header("Content-type", "text/html ")
#         self.end_headers()
#
#         # write message
#         self.wfile.write(bytes("Hello, world", "utf8"))
#         return
#
#
# # configure server
# port = 8080
# server_address = ("0.0.0.0", port)
# httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
#
# # run server
# httpd.serve_forever()


import sqlite3

connection = sqlite3.connect("new.db")
c = connection.cursor()
# c.execute('''
# CREATE TABLE record(
# Name varchar(255) NOT NULL,
# Last varchar(255)
# );''')
c.execute('''INSERT INTO record (Name, Last) VALUES('Abdulahi', 'Khalif');''')
connection.commit()
