import requests

def getdata():
	headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': '*/*',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://players.brightcove.net/665001584001/SyN2noqa_default/index.html?videoId=5146642090001',
    'Origin': 'https://players.brightcove.net',
    'Connection': 'keep-alive',
    'If-Modified-Since': 'Tue, 28 May 2019 13:03:03 GMT',
    'If-None-Match': '"5ced3187-151"',
	}

	response = requests.get('https://aja-hd-web-hls-live.secure.footprint.net/egress/chandler/aljazeera2/arabichd/index255.m3u8', headers=headers)
	text = response.text

	all = text.split('\n')
	return all[-2]

