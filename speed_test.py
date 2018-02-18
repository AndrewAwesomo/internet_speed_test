import speedtest
import csv
import os

CSVFILE = 'speedtest_results.csv'

servers = []

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

r = s.results.dict()

timestamp = r['timestamp']
u_speed = r['upload'] # upload speed (bits/s)
d_speed = r['download'] # download speed (bits/s)
ping = r['ping']
bytes_sent = r['bytes_sent']
client_ip = r['client']['ip'] # my ip
server_host = r['server']['host'] # web address of test server

csvHeader = ['timestamp', 'd_speed', 'u_speed', 'ping', 'bytes_sent', 'client_ip', 'server_host']
csvRow = [timestamp, d_speed, u_speed, ping, bytes_sent, client_ip, server_host]

# if file doesn't exit, create file and add header
if not os.path.isfile(CSVFILE):
    with open(CSVFILE, 'a', newline='') as f:
        wr = csv.writer(f, dialect='excel')
        wr.writerow(csvHeader)

# write row
with open(CSVFILE, 'a', newline='') as f:
    wr = csv.writer(f, dialect='excel')
    wr.writerow(csvRow)