```
java.lang.IllegalStateException: Cannot call methods on a stopped SparkContext.
This stopped SparkContext was created at:

org.apache.spark.sql.SparkSession$Builder.getOrCreate(SparkSession.scala:935)
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
java.lang.reflect.Method.invoke(Method.java:498)
org.apache.zeppelin.spark.BaseSparkScalaInterpreter.spark2CreateContext(BaseSparkScalaInterpreter.scala:246)
org.apache.zeppelin.spark.BaseSparkScalaInterpreter.createSparkContext(BaseSparkScalaInterpreter.scala:178)
org.apache.zeppelin.spark.SparkScala211Interpreter.open(SparkScala211Interpreter.scala:89)
org.apache.zeppelin.spark.NewSparkInterpreter.open(NewSparkInterpreter.java:102)
org.apache.zeppelin.spark.SparkInterpreter.open(SparkInterpreter.java:62)
org.apache.zeppelin.interpreter.LazyOpenInterpreter.open(LazyOpenInterpreter.java:69)
org.apache.zeppelin.interpreter.remote.RemoteInterpreterServer$InterpretJob.jobRun(RemoteInterpreterServer.java:616)
org.apache.zeppelin.scheduler.Job.run(Job.java:188)
org.apache.zeppelin.scheduler.FIFOScheduler$1.run(FIFOScheduler.java:140)
java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
java.util.concurrent.FutureTask.run(FutureTask.java:266)
java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)

The currently active SparkContext was created at:

(No active SparkContext.)

  at org.apache.spark.SparkContext.assertNotStopped(SparkContext.scala:101)
  at org.apache.spark.SparkContext.defaultParallelism(SparkContext.scala:2379)
  at org.apache.spark.SparkContext.defaultMinPartitions(SparkContext.scala:2388)
  at org.apache.spark.SparkContext.textFile$default$2(SparkContext.scala:839)
  ... 115 elided
```

위같은 에러가 발생했을 때.



https://stackoverflow.com/questions/35515120/why-does-sparkcontext-randomly-close-and-how-do-you-restart-it-from-zeppelin



![](http://ww4.sinaimg.cn/large/006tNc79gy1g445s646ddj31gz0nldm1.jpg)



Spark 인터프리터를 재시작하면 거의 해결됨. 문제는 인터프리터 프로세스가 러닝중인데, 그 안에 Spark Context가 없는 경우 발생한다.(spark context는 알아서 생성됨.)

