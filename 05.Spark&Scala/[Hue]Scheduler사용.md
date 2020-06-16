# Hue

![image-20190626114447587](http://ww3.sinaimg.cn/small/006tNc79gy1g4ed3d2nsvj30bk0d8gm8.jpg)



`Hue` -> `Hue Web UI` -> `<host>:8889`

![image-20190626114832253](http://ww1.sinaimg.cn/large/006tNc79gy1g4ed77s4d7j31f50u0dkk.jpg)

기본 화면



![image-20190626114901532](http://ww2.sinaimg.cn/mw1024/006tNc79gy1g4ed7q8t7tj30lo0bmdh2.jpg)



- 계정은 `HDFS`로 접근

  

![image-20190626174007888](http://ww2.sinaimg.cn/large/006tNc79gy1g4end2idsbj31f50u0qa8.jpg)

이 화면은 Hive Query 할 수 있게 해주는 화면.



- `Editor`에서 동작되는 `Spark` 생성
  ![image-20190626115153194](http://ww4.sinaimg.cn/mw1024/006tNc79gy1g4edapp896j31f50u079y.jpg)

- 그럼 위와 같은 화면이 나옴 (계정이 Hdfs 계정이여야 함)



![image-20190626174236683](http://ww4.sinaimg.cn/large/006tNc79gy1g4enfmqi3yj31f50u0wjz.jpg)

- 보라색 부분이 내가 쓸 라이브러리 jars 삽입,  다른 것들도 포함해서 jar만들면 좋지만, sbt에서 작업하려면 공수가 많이 들고 무겁기 때문에 따로 라이브러리만 넣었음



그리고 그 밑에 class 부분에 내가 실행시키고자 하는 main 클래스 이름을 넣어주면 일단 `Editor` 해야될 건 다했음.



그리고 오른쪽 상단에 있는 Save with name and descrition을 적어주고 저장버튼을 누릅니다.



![image-20190626174549252](http://ww3.sinaimg.cn/mw1024/006tNc79gy1g4enizb9uoj30d106sjrv.jpg)



스케쥴링을 하기 위해서는 Editor에서 만든 Spark Application을 Workflow로 만들어 주어야 한다.



![image-20190626174714087](http://ww4.sinaimg.cn/large/006tNc79gy1g4enkgnybcj31f50u0n1h.jpg)



여기서 `Workflow` 를 만들 수 있는데, 해당 프로젝트는 모두다 Spark이기 때문에 Spark를 `Drag&Drop` 합니다.



그러면 다음과 화면이 나옵니다.

![image-20190626174830697](http://ww1.sinaimg.cn/large/006tNc79gy1g4enls88dbj30ts0x4dj0.jpg)

아래 화살표를 누르면 다음과 내가 만들어 놓은 문서들을 볼 수 있다.

![image-20190626174849571](http://ww3.sinaimg.cn/large/006tNc79gy1g4enm3erpyj31f50u0tdf.jpg)





만들어 놓은 `WorkFlow` 를 참고하면, 아래와 같은 이름으로 만들어진다.

![image-20190626175148967](http://ww4.sinaimg.cn/large/006tNc79gy1g4enp7llkpj31f50u0gqj.jpg)



다시 스케쥴러로 이동하여 아래와 같은 화면으로 이동된다.

![image-20190626175221130](http://ww1.sinaimg.cn/large/006tNc79gy1g4enpr9ok3j30at05m3yn.jpg)



![image-20190626175246378](http://ww4.sinaimg.cn/large/006tNc79gy1g4enqdtmz1j31f50u0jw2.jpg)



이후 앞서 작성한 workflow를 눌러서 crontab 처럼 스켸줄링을 하면된다.

----

추가..! 네이버 클라우드 플랫폼에서도 제공해주는데, 좀더 쉽게 가이드가 나와있어 첨부

 https://docs.ncloud.com/ko/hadoop/chadoop-4-3.html