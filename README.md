### 下载Youtube的列表视频

>  建议先**【下滑刷新】**youtube**列表视频**的网页，这样可以加载所有的视频
>
>  Mac系统（python2.7）,运行 catch_mac_py27.py
>
>  Win系统（python3.6）,运行 catch_win_py36.py

* 1. save当前网页内容，命名为 web.htm

* 2. 使用python语言编写以下脚本,命名为 catch.py

  ···

  ``` 
  import re
  pattern = '<a.+?href="(.+?)".+?>.+?</a>'
  with open('download.sh', 'w') as fd:
    with open("web.htm", "r") as fp:
      count = 0
          for line in fp:
              ret = re.search(pattern, line)
              if ret:
  				       for x in ret.groups():
  					         if ('/watch?' in x):
  		                  print 'youtube-dl --format=mp4 ' + x
  						          fd.write ('youtube-dl --format=mp4 ' + x + '\n')
  						          count += 1
  						          fd.write ('echo "dowload the ' + str(count) + ' video"\n')
  		print 'count:',count
  ```



* 3. 运行 python catch.py 生成 download.sh文件
* 4. 运行 nohup sh download.sh&
* 5. 使用 tail -f nohup.out 查看
