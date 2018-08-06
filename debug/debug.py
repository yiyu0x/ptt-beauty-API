
import re
a = '"https://imgur.com/NtxSMJO.jpg"'


match = re.search(r'"http(s)?://(i\.)?imgur\.com/(.*?)"',a)

if match:
	print('ok')