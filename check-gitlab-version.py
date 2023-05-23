import requests
import json
from optparse import OptionParser
import urllib3
import warnings

# Disable urllib3 warnings
warnings.filterwarnings('ignore', category=urllib3.exceptions.InsecureRequestWarning)

def banner():
	print(
r'''
        _ _   _       _            
       (_) | | |     | |           
   __ _ _| |_| | __ _| |__         
  / _` | | __| |/ _` | '_ \        
 | (_| | | |_| | (_| | |_) |       
  \__, |_|\__|_|\__,_|_.__/        
   __/ |            (_)            
 _|___/____ _ __ ___ _  ___  _ __  
 \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
  \ V /  __/ |  \__ \ | (_) | | | |
   \_/ \___|_|  |___/_|\___/|_| |_|
''')

def get_version(url):
	with open('gitlab_hashes.json', 'r') as file:
		version_list = json.loads(file.read())
	url = "https://" + url
	req = requests.get(url+"/assets/webpack/manifest.json", verify=False)
	hash = json.loads(req.content)['hash']
	return version_list[hash]

def print_version(url, data):
	print('''- Host: {}		
	[+] Build: {}
	[+] Version: {}
'''.format(url, data['build'], data['versions']))

def update_hash():
	hash_url = "https://raw.githubusercontent.com/righel/gitlab-version-nse/main/gitlab_hashes.json"
	try:
		req = requests.get(hash_url)
		js = json.loads(req.content)

		# check if build exist
		if (js[list(js)[1]]['build']):
			with open('gitlab_hashes.json', 'wb') as file:
				file.write(req.content)
			print('[+] Updated successfully')
	except Exception as e:
		print('[!] Update failed')

def main():
	banner()
	parser = OptionParser(usage=
	r'''	python3 %prog -u example.com
	python3 %prog -f file.txt
	python3 %prog -t update''')
	parser.add_option("-u", dest="url", help="URL to check")
	parser.add_option("-t", dest="update", help="Update hash list of gitlab version")
	parser.add_option("-f", dest="file", help="File with list of URLs")

	(options, args) = parser.parse_args()

	if options.url:
		url = options.url
		try:
			print_version(url, get_version(url))
		except Exception as e:
			pass
		
	if options.file:
		urls = []
		with open(options.file, 'r') as file:
			for url in file:
				urls.append(url.strip())

		for url in urls:
			try:
				print_version(url, get_version(url))
			except Exception as e:
				pass

	if options.update:
		update_hash()

if __name__ == "__main__":
    main()