# internet_speed_test

This script runs an internet speedtest via the speedtest-cli package: https://github.com/sivel/speedtest-cli

speedtest-cli can be installed using:

```
pip install speedtest-cli
```

The output will be a csv file with the following fields extracted from speedtest-cli:
timestamp
d_speed = average download speed (bytes/s)
u_speed = average upload speed (bytes/s)
ping
bytes_sent
client_ip = your public ip
server_host = server that speedtest.net determined was your best option

This can be run as a chronjob or Windows task to run frequently and give you feedback about the health of your internet connection.