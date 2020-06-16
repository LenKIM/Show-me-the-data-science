Spark는 in-memory 기반의 모델로 RDD라는 읽기전용 메모리 블럭을 사용하여 기존 Hadoop Mapreduce보다 월등히 향상된 속도를 자랑하며, 장애처리 또한 기존에 복구 로직(장애 발생 시점 파일에 쓰고, 다시 로드하는 처리)이 아니라, 처음부터 수행한다.



- Default 로 Spark는 Lazy-execution 방식으로 동작.



# 클러스터를 구동하는 방식은 3가지

- Stand-alone 모드
- Yarn 모드
- Mesos 모드



프로젝트에서 사용된 방식은 CM을 활용하여 Yarn모드에서 동작

Yarn클러스터를 사용할 시, Spark로 개발되 app가 Hadoop Yarn의 RM(Resource Manager)을 통해 스케쥴링되며, 분산 처리를 수행한다.



Spark App은 app을 수행할 때, Driver와 Executor로 동작된다.

따라서 memory, core와 같은 설정값도 개별적으로 등록해야 한다.  

쉽게 이해하자면, 로직상 driver는 executor외의 부분이며, executor는 실제 분산처리를 위한 map/reduce를 수행한다.







![img](http://ww2.sinaimg.cn/large/006tNc79gy1g4bz818dsqj30go09e0t3.jpg)



![img](http://ww4.sinaimg.cn/large/006tNc79gy1g4bzadyx6bj30go09a3yq.jpg)



**Spark App을 yarn으로 수행시 2가지모드**

- **Yarn-Client**  
  driver가 ApplicationMaster 외부 클라이언트로 수행하는 것 (ApplicationMaster, driver, executor)
- **Yarn-Cluster**  
  ApplicationMaster 내부에서 driver가 수행되는 것(ApplicationMaster, executor)

참고 사이트 - https://www.cloudera.com/documentation/enterprise/5-4-x/topics/cdh_ig_running_spark_on_yarn.html

**주요 Spark Configuration Properties**

- spark.master - 클러스터 마스터 지정 (Yarn모드에서는 client, cluster, stand-alone모드에서는  spark://.,..)
- spark.driver.cores - Driver 프로세스에서 사용하는 코어수로 클러스터 모드에서만 사용
- spark.driver.maxResultSize - 개별 Spark Action 관련 함수(show, collect..)에 대한 모든 파티션의 직렬화된 결과의 총 크기 제한 (default: 1G)
- spark.driver.memory - SparkContext가 초기화 되는 Driver 프로세스에서 사용하는 메모리 (default : 1G)
- spark.executor.cores - Executor 프로세스에서 사용되는 코어수. (default : Yarn 모드에서는 1, stand-alone과 mesos에서는 이용가능한 모든 코어 수)
- spark.executor.memory - Executor 당 사용하는 메모리 (``default: 1G)

spark.executor.cores 를 제외한 properteis는 app 수행시 필요한 속성값이며, spark.executor.cores 는 실행 시 적용된다. 

Spark에서 제공하는 Dynamic Allocation를 통해 spark.executor.cores 속성값을 동적으로 핸들링 할 수 있기 때문에 실행 후 executor 의 core 수가 결정된다.



나머지는 http://spark.apache.org/docs/latest/configuration.html



**Spark를 Yarn모드로 동작할 시 추가로 설정해야 하는 Properties가 있다.**

Driver가 AM(Application Master) 내부가 아닌 개별 클라이언트로 수행하는 'yarn-client' 경우에는 spark.yarn.am.xxxxx' 설정값을 확인해야 한다.

- **spark.yarn.am.memory** : yarn-client로 수행시 AM(Application Master) 가 사용하는 메모리 (default : 512m)
- **spark.yarn.am.cores** : yarn-client로 수행시 AM(Application Master) 가 사용하는 코어수 (default : 1)
- **spark.executor.instances** : Executor의 수로 Dynamic Allocation 를 활용할 시 동적으로 늘어날 수 있다.(default : 2)
- **spark.yarn.executor.memoryOverhead** : Executor당 할당할 off-heap memory의 양 (default:`executorMemory * 0.10, with minimum of 384)
- **spark.yarn.driver.memoryOverhead** : Driver당 할당할 off-heap memory의 양 (default: driverMemory * 0.10, with minimum of 384)
- **spark.yarn.am.memoryOverhead** : yarn-client로 수행시 AM(Application Master) 할당할 off-heap memory의 양 (default: `AM memory * 0.10, with minimum of 384)
- **spark.yarn.jars** : Yarn Container에 배포할 Spark코드가 포함된 라이브러리로 일반적으로는 로컬의 jar를 사용하지만, HDFS에 위치시키면 Yarn에서 캐싱되어 app 실행시 배포할 필요가 없다. 따라서 HDFS에 올리는 것이 좋다.

\* **off-heap memory** 는 In-Memory 아키텍처에서 나오는 용어로, http://d2.naver.com/helloworld/106824 를 참고하기 바란다.



#### Hadoop측 AM 관련 yarn configuration

- **yarn.app.mapreduce.am.resource.mb** : spark.yarn.am.memory' 와 같은 의미. 지정하지 않을 시 Hadoop mapred-site.xml설정에` 있는 1536m으로 설정 (default: 1536)
- **yarn.app.mapreduce.am.resource.cpu-vcores** : spark.yarn.am.cores' 와 같은 의미. 지정하지 않을 시 Hadoop mapred-site.xml설정에 있는 1로 설정 (default: 1)`
- **yarn.app.mapreduce.am.command-opts** : AM(Application Master) 를 위한 자바 옵션 (default: -Xmx1024m) `



참고 : https://www.slideshare.net/FerranGalReniu/yarn-by-default-spark-on-yarn  
[http://egloos.zum.com/tobby48/v/4413044](http://egloos.zum.com/tobby48/v/4413044)
