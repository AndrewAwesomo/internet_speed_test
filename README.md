# internet_speed_test

This script runs an internet speedtest via the speedtest-cli package: https://github.com/sivel/speedtest-cli

speedtest-cli can be installed using:

```
pip install speedtest-cli
```

The output will be a csv file with the following fields extracted from speedtest-cli:<br />
timestamp<br />
d_speed = average download speed (bytes/s)<br />
u_speed = average upload speed (bytes/s)<br />
ping<br />
bytes_sent<br />
client_ip = your public ip<br />
server_host = server that speedtest.net determined was your best option

This can be run frequently as a cron job or Windows task to give you feedback about the health of your internet connection over time.