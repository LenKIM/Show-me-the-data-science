결국 디펜더시를 해결해서 Hue에 넣지는 못했지만, Jar 파일을 만드는 것에는 성공했다.

멀티 모듈로 코딩을 하면서 이 부분을 신경쓰지는 못했던 것 같다.



일단 내가 만든 모듈은 다음과 같다.

```scala

name := "Trio"

version := "0.1"

ThisBuild / scalaVersion := "2.11.12"
ThisBuild / organization := "com.DaouTech"

lazy val global = project
  .in(file("."))
  .settings(
    libraryDependencies ++= commonDependencies
  )
  .aggregate(
    webhdfs,
    kafka,
    common,
    spark
  ).dependsOn(common)
  .dependsOn(kafka)
  .dependsOn(webhdfs)
  .dependsOn(spark)


val common = (project in file("common"))
  .settings(
    name := "common",
    libraryDependencies ++= commonDependencies

  )
lazy val webhdfs = (project in file("webhdfs"))
  .settings(
    name := "webhdfs",
    libraryDependencies ++= commonDependencies ++ Seq(
      dependencies.playJson,
      dependencies.scalaj
    )
  ).dependsOn(common)

lazy val kafka = (project in file("kafka"))
  .settings(
    name := "kafka",
    libraryDependencies ++= commonDependencies ++ Seq(
      dependencies.kafka,
      dependencies.kafkaClients,
      dependencies.kafkaStreams,
      dependencies.kafkaStreamsScala,
      dependencies.playJson
    )
  )
  .dependsOn(common)

lazy val spark = (project in file("spark"))
  .settings(
    name := "spark",
    libraryDependencies ++= commonDependencies ++ Seq(
      dependencies.elasticSearch,
      dependencies.sparkCore,
      dependencies.sparkStream,
      dependencies.sparkSql,
      dependencies.sparkHive,
      dependencies.sparkRepl
    )
  )
  .dependsOn(common)

lazy val dependencies =
  new {
    val scalajV            = "2.4.0"
    val scalatestV         = "3.0.5"
    val kafkaV             = "2.2.0"
    val kafkaClientsV      = "2.2.0"
    val kafkaStreamsV      = "2.2.0"
    val kafkaStreamsScalaV = "2.2.0"
    val playJsonV          = "2.7.2"
    val elasticV           = "6.7.1"
    val providedV          = "6.5.1"
    val sparkV             = "2.2.0"

    val scalaj = "org.scalaj"                  %% "scalaj-http"         % scalajV
    val scalatest = "org.scalatest"            %% "scalatest"           % scalatestV
    val kafka = "org.apache.kafka"             %% "kafka"               % kafkaV
    val kafkaClients = "org.apache.kafka"      % "kafka-clients"        % kafkaClientsV
    val kafkaStreams = "org.apache.kafka"      % "kafka-streams"        % kafkaStreamsV
    val kafkaStreamsScala = "org.apache.kafka" %% "kafka-streams-scala" % kafkaStreamsScalaV
    val playJson = "com.typesafe.play"         %% "play-json"           % playJsonV

    val elasticSearch = "org.elasticsearch"    % "elasticsearch-hadoop" % elasticV
    val sparkCore = "org.apache.spark"         %% "spark-core"          % sparkV
    val sparkStream = "org.apache.spark"       %% "spark-streaming"     % sparkV % "provided"
    val sparkSql = "org.apache.spark"          %% "spark-sql"           % sparkV
    val sparkHive = "org.apache.spark"         %% "spark-hive"          % sparkV
    val sparkRepl = "org.apache.spark"         %% "spark-repl"          % sparkV
  }
lazy val commonDependencies = Seq(
  "commons-net" % "commons-net" % "3.3",
  "commons-lang" % "commons-lang" % "2.6",
  "commons-io" % "commons-io" % "2.4",
  dependencies.scalatest % "test"
)

assemblyMergeStrategy in assembly := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}
```



그리고 사용한 모듈은 

`https://github.com/sbt/sbt-assembly`



하나의 jars를 만든다는 것에서는 위 Plugins을 쓰는 것이 맞지만, 문제는 라이브러리 중복되는 것에서 발생했다.

그래서 위 sbt에 

```scala
assemblyMergeStrategy in assembly := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}
```

를 넣어 해결할 수 있었다.



이후 프로젝트 디렉터리 터미널에서 `sbt clean assembly ` 를 해서 만들어진 `Trio-assembly-0.1.jar` 를 활용하면 된다. (근데.. 이게 200M가 정도 되니 본의 아니게 큰 프로젝트가 되버렸다라는...)