from speedtest import SpeedTest
from send_post import SendPost

speedtest = SpeedTest()
speedtest.run_test()

sp = SendPost()
sp.login(username="mastodonbot.8qr3o@passinbox.com", password="KA6afwDK9rZ#qT=Sf5")
sp.send_post(f"Download: {speedtest.download_speed} Mbps\nUpload: {speedtest.upload_speed} Mbps")