[docs](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/WebHDFS.html)





Cloudera Manager에서 설정하는 방법.

![](https://ws3.sinaimg.cn/large/006tNc79gy1g1yhmw6raoj31h00n6dk5.jpg)



여기에 Enable WebHDFS를 체크 표시.



그리고 클라우드매니저가 설치된 PC가 아니라 HDFS가 설치된 노드에서 쿼리를 테스트해보면

![](https://ws2.sinaimg.cn/large/006tNc79gy1g1yhp947vjj30qc09kmzs.jpg)

와 같이 나옴.



create mkdir은

`curl -i -X PUT "http://172.22.1.134:50070/webhdfs/v1/user/jk/testmkdir?user.name=jk&op=MKDIRS"`

![](https://ws3.sinaimg.cn/large/006tNc79gy1g1yidzoaw2j30lm06i75i.jpg)



`curl -i  "http://172.22.1.134:50070/webhdfs/v1/user/jk?user.name=jk&op=LISTSTATUS"`

![](https://ws4.sinaimg.cn/large/006tNc79gy1g1ykb3kx0oj30qd07amyk.jpg)


