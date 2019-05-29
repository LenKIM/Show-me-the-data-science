# zepplin 활용

[설치 가이드](https://zeppelin.apache.org/docs/0.8.1/quickstart/install.html)

[다운로드](https://zeppelin.apache.org/download.html)

[HDFS와 Zepplin 참고사이트](https://zeppelin.apache.org/docs/0.7.0/install/cdh.html)

포트포워딩 localhost:8080 localhost:8080

start command - `bin/zeppelin-daemon.sh start`

stop command - `bin/zeppelin-daemon.sh stop`



![](https://ws2.sinaimg.cn/large/006tNc79gy1g1yelx15anj31h70fwdjc.jpg)



처음 접속하면 위에처럼 anonymous로 접속되므로 권한 설정 해줘야 한다.

<http://localhost:8080/>

![](https://ws2.sinaimg.cn/large/006tNc79gy1g1yf7eitcvj30dg01mjrg.jpg)

권한 설정은 

![](https://ws2.sinaimg.cn/large/006tNc79gy1g1yf8n93e5j30ak00h744.jpg)

요기서 설정.



ID / PW

admin / admin
jk / jk
th / th
dh / dh

---

#### Config

1. cd ~(위치)/zeppelin-0.7.2-bin-all/conf
   ![](https://ws1.sinaimg.cn/large/006tNc79gy1g1ync8nw9yj30eh04igm7.jpg)
2. cp zeppelin-site.xml.template zeppelin-site.xml   
   여기서 제플린의 PORT, ADDRESS를 설정해 줄수 있다.
3. cp zeppelin-env.sh.template zeppelin-env.sh  
   아래와 같은 환경변수를 설정할 수 있다.
4. cp shiro.ini.tenplate shiro.ini  
   계정관련 설정을 할 수 있다.
5. vi zeppelin-env.sh

   - export SPARK_HOME=/usr/lib/spark

   - export PYTHONPATH=/usr/lib/spark/python
   - export PYSPARK_PYTHON=/usr/lib/spark/python

6. 제플린 UI에서   
   ![](https://ws3.sinaimg.cn/large/006tNc79gy1g1zt14e5aoj305c07ewem.jpg)
   Interpreter =>Spark => Properties.master 부분에  
   만약 클라우데라매니저와 함께 YARN을 쓰고 있다면 master 부분에 yarn-client를 넣어준다.

