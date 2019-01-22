import re

pattern = '<a.+?href="(.+?)".+?>.+?</a>'

with open('download.sh', 'w') as fd:
	with open("web.htm", "r", encoding='UTF-8') as fp:

		count = 0

		for line in fp:

			ret = re.search(pattern, line)

			if ret:

				for x in ret.groups():

					if ('/watch?' in x):

						print('youtube-dl --format=mp4 ' + x)

						fd.write('youtube-dl --format=mp4 ' + x + '\n')

						count += 1

						fd.write('echo "dowload the ' + str(count) + ' video"\n')

		print('count:', count)
