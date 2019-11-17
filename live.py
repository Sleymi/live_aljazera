import os
import sys
import time
from req import getdata


data="""
curl 'https://aja-hd-web-hls-live.secure.footprint.net/egress/chandler/aljazeera2/arabichd/{}' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0' -H 'Accept: */*' -H 'Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3' --compressed -H 'Referer: https://players.brightcove.net/665001584001/SyN2noqa_default/index.html?videoId=5146642090001' -H 'Origin: https://players.brightcove.net' -H 'Connection: keep-alive'>>alj_live
"""


#y=int(sys.argv[1])

while(True):
	y=getdata()
	cmd1=data.format(y)
	os.system(cmd1)
	#y+=1
	print(y)
	time.sleep(9)
