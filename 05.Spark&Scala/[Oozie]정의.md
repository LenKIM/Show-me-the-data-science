# Oozie

hue를 통해서 잘 활용하긴 하는데, 정작 Oozie가 뭔지 몰라서 정리.

한국말로 잘 정의된 사이트가 있어서 보고 정리합니다.

출석 - https://seamless.tistory.com/31?category=704553



정식 사이트 - http://oozie.apache.org/



Oozie에서 제공하는 기능 3가지

- Scheduling
  - 특정 시간에 액션 수행
  - 주기적인 간격 이후에 액션 수행
  - 이벤트가 발생하면 액션 수행
- Coordinating
  - 이전 액션이 성공적으로 끝나면 다음 액션 시작
- Managing
  - 액션이 성고하거나 실패했을 때 이메일 발송
  - 액션 수행시간이나 액션의 단계를 저장



## Oozie Terminology

- Action
  - 우지에서 실행할 수 있는 하나의 작업 단위
  - MapReduce, Spark, Shell script 등의 작업 수행
- Workflow
  - Action들의 제어와 의존 관계를 DAG(Directed acyclic graph) 표현
- Coodrinator
  - Data sets과 Workflow를 실행하는 스케쥴을 정의
- Bundle
  - 코디네이터의 모임



## Oozie Architecure - Client&Sever Model

![img](http://ww1.sinaimg.cn/large/006tNc79gy1g4eo0koliaj30g40do0u3.jpg)



## Oozie 구성 요소

**Workflow Engine**

- 워크플로우를 실행
- 하나의 워크플로우는 여러개의 액션을 포함

**Coordinator(Scheduler)**

- 미리 지정된 위치의 데이터셋의 존재 여부나 frequency에 따라 워크플로우를 스케줄링

**REST API**

- 실행, 스케줄, 워크플로우 모니터링하는 API가 있음

**CLI**

- 커맨드라인을 통하여 작업을 실행하거나 스케줄링, 모니터링 가능

**Bundle**

- 코디네이터를 모아서 한번에 제어하게 해주는 단위

**Notifications**

- 작업 상태가 변경 여부에 따라 이벤트를 보내줌

**SLA(Service Level Agreement) monitoring**

- 시작, 종료 시간이나 지속 시간을 기반으로 하여 작업에 대한 SLA를 추적하는데 어떤 작업이 SLA를 달성하거나 못하는지 체크하여 사용자에게 통지해줌

**Database**

- 코디네이터, 번들 SLA 및 workflow 이력 등을 저장



## Oozie 실행 순서

![img](http://ww2.sinaimg.cn/large/006tNc79gy1g4eo21z6d7j30g40a0t9l.jpg)



(1) 클라이언트는 우지 서버에 연결하여 job properties을 제출

- job properties는 key-value 행태로 작업에 피요한 파라미터를 정의
- workflow.xml(Action들과 그들을 연결하는 로직은 Workflow를 정의) 파일의 NameNode와 Yarn ResourceManager(혹은 JobTracker)에 대한 URI를 포함하고 있음. 이 부분은 `[Hue] HiveTable-데이터 넣기` 를 보면 알 수 있습니다.

(2) Oozie 서버가 HDFS로 부터 workflow 파일을 읽는다.

(3) Oozie 서버에서 workflow를 파싱해서 액션을 수행한다.



## Oozie launcher

- 하나의 MapTask로 이루어진 MapReduce Job
- Oozie가 런처를 이용하는 이유는 모니터링과 관리와 같은 것을 Hadoop cluster에게 위임하기 위해서이다.