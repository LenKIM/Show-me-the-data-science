# Kafka

OVERVIEW

Kafka® is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.



Kafka®는 실시간 데이터 파이프 라인 및 스트리밍 앱을 구축하는 데 사용됩니다. 수평적으로 확장 가능하고 내결함성이 있으며 사악하게 빠르며 수천 개의 회사에서 생산되고 있습니다.



1. Publish & Subscribe  
   Read and write streams of data like a messaging system.
2. Process  
   Write scalable stream processing applications that react to events in real-time.
3. Store  
   Store streams of data safely in a distributed, replicated, fault-tolerant cluster.



![](https://ws2.sinaimg.cn/large/006tNc79gy1g27sq7osqcj30de0dsabz.jpg)

---

### Apache Kafka® is *a distributed streaming platform*. What exactly does that mean?

A streaming platform has three key capabilities:

- Message queue 또는 엔터프라이즈 메시징 시스템과 유사하게 레코드 스트림을 게시하고 구독

- 내결함성이있는 방식으로 레코드 스트림을 저장
- 저장된 레코드 스트림을 처리한다.



First a few concepts:

- Kafka is run as a cluster on one or more servers that can span multiple datacenters.  
  (Kafka는 여러 데이터 센터로 확장 될 수있는 하나 이상의 서버에서 클러스터로 실행됩니다.)
- The Kafka cluster stores streams of records in categories called topics.  
  (카프카 클러스터는 Topic이라는 범주에 레코드 스트림을 저장합니다.)
- Each record consists of a key, a value, and a timestamp.  
  (각 레코드는 키, 값 및 타임 스탬프로 구성됩니다.)



#### Kafka 는 4가지 코어 API를 가짐.

1. Producer API  
   하나 또는 그 이상의 Kafka Topics 스트림을 Publish
2. Comsumer API  
   하나 이상의 Topic을 구독하고 생성된 레코드 스트림을 처리하는 API
3. Streams API  
   응용 프로그램이 하나 이상의 주제에서 입력 스트림을 소비하고 하나 이상의 출력 항목으로 출력 스트림을 생성하여 효과적으로 입력 스트림을 출력 스트림으로 변환하는 스트림 프로세서로 작동하도록합니다.
4. Connector API  
   Connector API를 사용하면 Kafka 주제를 기존 응용 프로그램이나 데이터 시스템에 연결하는 재사용 가능한 제작자 또는 소비자를 만들고 실행할 수 있습니다. 예를 들어, 관계형 데이터베이스에 대한 커넥터는 테이블에 대한 모든 변경 사항을 캡처 할 수 있습니다.



Kafka에서 클라이언트와 서버 간의 통신은 단순하고 고성능의 언어에 구애받지 않는 TCP 프로토콜로 수행됩니다. 



사용가능한 [Client](https://cwiki.apache.org/confluence/display/KAFKA/Clients) 는 여기.



### Topics and Logs

Topics는 레코드가 공개되는 카테고리 또는 피드 이름입니다. 카프카의 Topics는 항상 멀티 구독자입니다. 즉, Topics에는 기록 된 데이터를 구독하는 0, 1 또는 많은 사용자가있을 수 있습니다.

각 Topic에 대해 카프카 클러스터는 다음과 같은 파티션 로그를 유지합니다.

![](https://ws1.sinaimg.cn/large/006tNc79gy1g27tui4393j30bk07f0t6.jpg)

각 파티션은 계속해서 추가되는 순서화 된 불변의 레코드 순서로서 구조화 된 Commit log입니다. 파티션의 레코드에는 파티션 내의 각 레코드를 고유하게 식별하는 offset이라는 순차적 인 ID 번호가 각각 할당됩니다.



Kafka 클러스터는 구성 가능한 보존 기간을 사용하여 게시 된 모든 레코드 (사용 여부와 상관없이)를 영구히 유지합니다. 예를 들어 보존 정책(retention policy)을 2 일로 설정하면 레코드를 게시 한 후 2 일 동안 소비 정책을 사용할 수 있으며 그 이후에는 사용 가능한 공간을 늘리기 위해 폐기됩니다. Kafka의 성능은 데이터 크기와 관련하여 실질적으로 일정하므로 데이터를 오랫동안 저장하는 것은 문제가되지 않습니다.

![](https://ws4.sinaimg.cn/large/006tNc79gy1g27tyaqog5j31d90u0jvo.jpg)

사실, Consumer 기준으로 유지되는 유일한 메타 데이터는 로그에서 해당 Consumer's 오프셋 또는 위치입니다. 이 오프셋은 Consumer에 의해 제어됩니다. 일반적으로 Consumer는 레코드를 읽을 때 선형적으로 오프셋을 진행하지만, 실제로는 위치가 Consumer에 의해 제어되므로 좋아하는 순서대로 레코드를 소비할 수 있습니다. 예를 들어 소비자는 과거의 데이터를 다시 처리하기 위해 이전 오프셋으로 재설정하거나 가장 최근의 레코드로 건너 뛰고 "지금"에서 소비하기 시작할 수 있습니다.

This combination of features means that Kafka consumers are very cheap—they can come and go without much impact on the cluster or on other consumers. For example, you can use our command line tools to "tail" the contents of any topic without changing what is consumed by any existing consumers.

로그의 파티션은 여러 가지 용도로 사용됩니다. 

 첫째, 로그를 단일 서버에 맞는 크기 이상으로 확장 할 수 있습니다. 각 개별 파티션은 호스트하는 서버에 적합해야하지만 주제에 많은 파티션이있어 임의의 양의 데이터를 처리 할 수 있습니다.

두 번째는 병렬 처리 단위로 작동합니다.

### Distribution

로그의 파티션은 Kafka 클러스터의 서버를 통해 배포되며 각 서버는 데이터를 처리하고 파티션 공유에 대한 요청을 처리합니다. 각 파티션은 장애 허용을 위해 구성 가능한 수의 서버에 복제됩니다.

각 파티션에는 "리더"역할을하는 서버와 "팔로어"역할을하는 0 이상의 서버가 있습니다. 리더는 팔로워가 리더를 수동적으로 복제하는 동안 파티션에 대한 모든 읽기 및 쓰기 요청을 처리합니다. 

리더가 실패하면 추종자 중 하나가 자동으로 새로운 리더가 됩니다. 각 서버는 일부 파티션의 리더와 다른 서버의 팔로어로 작동하므로 로드가 클러스터 내에서 잘 균형을 이룹니다.



### Geo-Replication

Kafka MirrorMaker는 클러스터에 지리적 복제 지원을 제공합니다. MirrorMaker를 사용하면 메시지가 여러 데이터 센터 또는 클라우드 지역에 복제됩니다. 

백업 및 복구를 위해 능동 / 수동 시나리오에서 사용할 수 있습니다. 또는 데이터를 사용자 가까이에 배치하거나 데이터 지역성 요구 사항을 지원하는 활성 / 활성 시나리오에서 사용할 수 있습니다.

### Producers

Producers는 선택한 주제에 데이터를 게시합니다. Producer는 주제 내에서 어떤 파티션에 어떤 레코드를 할당할지 선택해야합니다. 이는 Load-balance을 맞추기 위해 라운드 로빈 방식으로 수행하거나 일부 의미적인 파티션 함수 (레코드의 일부 키를 기반으로 함)에 따라 수행 할 수 있습니다. 

두 번째로 파티셔닝으로 더 많이 사용합니다!

### Consumers

Consumers는 Consumers Group 이름을 사용하여 레이블을 지정하고 주제에 게시 된 각 레코드는 구독하는 각 Consumers Group 내의 하나의 Consumers Instance에 전달됩니다. Consumers Instance는 별도의 프로세스 또는 별도의 시스템에있을 수 있습니다.

모든 Consumers 인스턴스가 동일한 Consumers Group을 갖는 경우 레코드는 Consumers Instance보다 효과적으로 밸런싱됩니다.

모든 Consumers 인스턴스가 서로 다른 Consumers Group을 갖고 있으면 각 레코드가 모든 소비자 프로세스에 브로드 캐스팅됩니다.

![](https://ws3.sinaimg.cn/large/006tNc79gy1g27uddnwm8j30d60700tc.jpg)

2 개의  consumer groups이있는 4개의 파티션 (P0-P3)을 호스팅하는 2대의 서버 Kafka 클러스터. 소비자 그룹 A에는 두 개의 소비자 인스턴스가 있고 그룹 B에는 네 개의 인스턴스가 있습니다.

그러나 더 일반적으로, 우리는 Topic이 각각의 "logical subscriber"에 대해 하나씩 적은 수의 소비자 그룹을 가지고 있음을 발견했습니다. 각 그룹은 확장성 및 내결함성을 위해 많은 소비자 인스턴스로 구성됩니다. 구독자가 단일 프로세스 대신 소비자 클러스터 인 publish-subscribe semantics 불과합니다.

Kafka에서 consumption가 구현되는 방식은 로그의 파티션을 소비자 인스턴스로 나누어 각 인스턴스가 어느 시점에서든 파티션의 "fair share"를 독점적으로 사용하는 것입니다. 이 그룹 구성원을 유지하는이 프로세스는 Kafka 프로토콜에 의해 동적으로 처리됩니다. 새 인스턴스가 그룹에 참여하면 그룹의 다른 구성원으로부터 일부 파티션을 인계받습니다. 인스턴스가 종료되면 해당 파티션이 나머지 인스턴스에 배포됩니다.

카프카는 한 Topic의 다른 파티션 사이가 아니라 한 파티션 내의 레코드에 대해서만 전체 주문을 제공합니다. 대부분의 응용 프로그램에서는 키 단위로 데이터를 분할하는 기능과 함께 파티션 단위의 순서만으로 충분합니다. 그러나 레코드에 대한 전체 순서가 필요한 경우 이는 하나의 파티션 만있는 항목으로 달성 할 수 있습니다. 단, 이는 소비자 그룹당 하나의 소비자 프로세스를 의미합니다.

### Multi-tenancy(다중 임대)

카프카를 Multi-tenancy 솔루션으로 배포 할 수 있습니다. Multi-tenancy는 데이터를 produce or consume 할 수있는 Topic을 구성하여 활성화됩니다. 할당량에 대한 운영 지원도 있습니다. 관리자는 클라이언트가 사용하는 브로커 자원을 제어하는 요청에 대해 할당량을 정의하고 시행 할 수 있습니다. 자세한 내용은 보안 설명서를 참조하십시오.

### Guarnatees

- 생성자가 특정 주제 파티션으로 보낸 메시지는 전송 된 순서대로 추가됩니다. 즉, 레코드 M1이 레코드 M2와 동일한 생성자에 의해 보내지고 M1이 먼저 보내지면 M1은 M2보다 더 낮은 오프셋을 가지며 로그에서 더 일찍 나타납니다.

- 소비자 인스턴스는 로그에 저장된 순서대로 레코드를 봅니다.
- For a topic with replication factor N, we will tolerate up to N-1 server failures without losing any records committed to the log. (복제 인수가 N 인 항목의 경우 로그에 커밋 된 레코드를 손실하지 않고 최대 N-1 개의 서버 오류를 허용합니다.)



### kafka as a Messaging System

기존의 메세지 큐와 카프카의 메시지큐는 뭐가 다를까?

메시징에는 전통적으로 두 가지 모델이 있습니다. 

[Queuing](http://en.wikipedia.org/wiki/Message_queue)과  [Publish-subscribe](http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)입니다.

a quque에서는 소비자 풀은 서버에서 읽을 수 있으며, 각 레코드는 그 중 하나에 저장됩니다.

publish-subscribe에서 모든 소비자에게 레코드가 브로드 캐스트됩니다.

각각이 장단점이 있는데, 

Queuing을 사용하면 여러 소비자 인스턴스에서 데이터 처리를 나눌 수 있으므로 처리 규모를 확장 할 수 있습니다. 유감스럽게도Queuing은 multi-subscriber가 아닙니다. 일단 하나의 프로세스가 데이터를 읽으면 그것은 사라진다.

Publish-subscribe를 사용하면 데이터를 여러 프로세스에 브로드 캐스트 할 수 있지만 모든 메시지가 모든 구독자에게 전달되기 때문에 확장 처리 방법이 없습니다.

Kafka의 Consumer group 개념은이 두 개념을 일반화합니다. Queuing과 마찬가지로 소비자 그룹은 프로세스 모음 (소비자 그룹의 구성원)을 통해 처리를 나눌 수 있습니다. publish-subscribe와 마찬가지로 Kafka를 사용하면 여러 소비자 그룹에 메시지를 브로드 캐스트 할 수 있습니다.

Kafka의 모델의 장점은 모든 Topic이 이러한 속성을 모두 갖추고 있다는 것입니다. 즉, 처리 규모를 조정할 수 있고 다중 가입자이기도합니다. 하나 또는 둘 다를 선택할 필요가 없습니다.

Kafka has stronger ordering guarantees than a traditional messaging system, too.

전통적인 대기열은 서버에서 순서대로 레코드를 보유하고, 여러 소비자가 대기열에서 소모하는 경우 서버는 저장된 순서대로 레코드를 전달합니다. 그러나 서버가 레코드를 순서대로 전달하더라도 레코드는 비동기적으로 소비자에게 전달되므로 서로 다른 소비자에게 순서가 잘못 될 수 있습니다. 

이것은 실제로 병렬 소비가 발생하면 레코드의 순서가 손실된다는 것을 의미합니다. 메시징 시스템은 대기열에서 하나의 프로세스만 사용할 수있는 "exclusive consumer"라는 개념을 사용하여이 문제를 해결하기도 하지만 처리 과정에서 병렬 처리가 없다는 것을 의미합니다.



그러나, Kafka는 Topics 내에서 병렬 처리 개념 (파티션)을 가짐으로써 Kafka는  a pool of consumer processe에 대해 ordering guarantees과  load balancing을 모두 제공 할 수 있습니다.

이는 Topic의 파티션을 Consumer Groups의 Consumer에게 할당하여 각 파티션이 그룹의 정확히 한 Consumer에 의해 소비 되도록하여 수행됩니다.

이렇게 함으로써 우리는 Consumer가 해당 파티션의 유일한 reader임을 확인하고 순서대로 데이터를 소비합니다.

파티션이 많으므로 많은 소비자 인스턴스에 대해 로드 벨런싱을 유지합니다. 그러나 Consumer Groups에는 파티션보다 더 많은 소비자 인스턴스가 있을 수 없습니다.

### Kafka as a Storage System

분리된 공개 메시지가 메시지를 소비하지 못하게하는 메시지 대기열은 사실상 메시지의 저장 시스템 역할을합니다. 카프카가 다른 점은 그것이 매우 훌륭한 저장 시스템이라는 것입니다.

Kafka에 기록 된 데이터는 디스크에 기록되고 내결함성을 위해 복제됩니다. 카프카(Kafka)는 producers가 승인을 기다릴 수 있도록 하여,  a Write 서버가 완전히 실패 할 때까지 계속 복제 될 때까지 쓰기가 완료된 것으로 간주하지 않도록합니다. ( ? )

Kafka가 scale well-Kafka를 사용하는 디스크 구조는 서버에 50KB 또는 50TB의 영구 데이터를 가지고 있더라도 동일하게 수행합니다.

스토리지를 중요하게 생각하고 클라이언트가 읽기 위치를 제어 할 수있게 된 결과, Kafka는 고성능, 낮은 대기 시간의 커밋 로그 저장, 복제 및 전파 전용의 특수 목적 분산 파일 시스템으로 생각할 수 있습니다.



### Kafka for Stream Processing

### Putting the Pieces Together

메시징, 스토리지 및 스트림 처리의 이러한 결합은 드문 것처럼 보일 수 있지만 스트리밍 플랫폼으로서의 카프카의 역할에 필수적입니다.

HDFS와 같은 분산 파일 시스템을 사용하면 일괄 처리를 위해 정적 파일을 저장할 수 있습니다. 사실상 이와 같은 시스템은 과거의 과거 데이터를 저장하고 처리 할 수있게합니다.

기존의 엔터프라이즈 메시징 시스템을 사용하면 가입 후 도착할 예정인 메시지를 처리 할 수 있습니다. 이러한 방식으로 구축 된 응용 프로그램은 도착할 때 미래의 데이터를 처리합니다.

Kafka는이 두 가지 기능을 모두 갖추고 있으며 스트리밍 응용 프로그램 및 스트리밍 데이터 파이프 라인을위한 플랫폼으로 Kafka를 사용하는 데있어이 두 가지 기능이 모두 중요합니다.

스토리지 및 대기 시간이 짧은 구독을 결합하여 스트리밍 응용 프로그램은 과거 및 미래 데이터를 동일한 방식으로 처리 할 수 있습니다. 즉, 단일 응용 프로그램에서 기록 된 저장된 데이터를 처리 할 수 있지만 마지막 레코드에 도달 할 때 종료하지 않고 이후 데이터가 도착할 때 처리를 유지할 수 있습니다. 이는 메시지 처리 응용 프로그램뿐만 아니라 일괄 처리를 포함하는 스트림 처리의 일반화 된 개념입니다.

마찬가지로 스트리밍 데이터 파이프 라인의 경우 실시간 이벤트에 가입하면 매우 짧은 지연 시간의 파이프 라인에 Kafka를 사용할 수 있습니다. 데이터를 안정적으로 저장하는 기능을 통해 데이터 전달을 보장해야하는 중요한 데이터에 대해 또는 주기적으로 데이터를로드하거나 유지 관리를 위해 오랜 시간 동안 데이터를 다운시킬 수있는 오프라인 시스템과의 통합을 위해 데이터를 사용할 수 있습니다. 스트림 처리 설비는 도착한 데이터를 변환 할 수있게합니다.

기타

<https://console.bluemix.net/docs/services/EventStreams/eventstreams073.html#apache_kafka>

<https://console.bluemix.net/docs/services/EventStreams/eventstreams073.html?locale=ko#apache_kafka>