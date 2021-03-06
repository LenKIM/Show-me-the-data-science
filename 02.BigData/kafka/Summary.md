# Kafka

Kafka® is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

Kafka®는 실시간 데이터 파이프 라인 및 스트리밍 앱을 구축하는 데 사용됩니다. 수평적으로 확장 가능하고 내결함성이 있으며 사악하게 빠르며 수천 개의 회사에서 생산되고 있습니다.



1. Publish & Subscribe Read and write streams of data like **a messaging system.**
2. Process Write scalable stream processing applications that react to **events in real-time**.
3. **Store Store streams of data** safely in a distributed, replicated, fault-tolerant cluster.

![img](https://ws2.sinaimg.cn/large/006tNc79gy1g27sq7osqcj30de0dsabz.jpg)



A streaming platform has three key capabilities:

- Message queue 또는 엔터프라이즈 메시징 시스템과 유사하게 레코드 스트림을 게시하고 구독  
- 내결함성이있는 방식으로 레코드 스트림을 저장  
- 저장된 레코드 스트림을 처리한다.  



*Cf, 카프카 용어*

```
- 카프카 -아파치프로젝트 애플리케이션 이름, 클러스터 구성이 가능하며, 카프카 클러스터라고 부름
- 브로커(Broker) - 카프카 애플리케이션이 설치되어 있는 서버 또는 노드를 말합니다.
- 토픽(Topic) - 프로튜서와 컨슈머들이 카프카로 보낸 자신들의 메시지를 구분하기 위한 네임으로 사용
- 파티션(Partition) - 병렬처리가 가능하도록 토픽을 나눌 수 있고, 많은 양의 메시지 처리를 위해 파티션의 수를 늘려줄 수 있음
- 프로튜서(Producer) - 메시지를 생산하여 브로커의 토픽 이름으로 보내는 서버 또는 애플리케이션 등을 말함
- 컨슈머(Comsumer) - 브로커의 토픽 이름으로 저장된 메시지를 가져가는 서버 또는 애플리케이션
```



**Kafka 는 4가지 코어 API를 가짐.**

1. Producer API 하나 또는 그 이상의 Kafka Topics 스트림을 Publish
2. Comsumer API 하나 이상의 Topic을 구독하고 생성된 레코드 스트림을 처리하는 API
3. Streams API 응용 프로그램이 하나 이상의 주제에서 입력 스트림을 소비하고 하나 이상의 출력 항목으로 출력 스트림을 생성하여 효과적으로 입력 스트림을 출력 스트림으로 변환하는 스트림 프로세서로 작동하도록합니다.
4. Connector API Connector API를 사용하면 Kafka 주제를 기존 응용 프로그램이나 데이터 시스템에 연결하는 재사용 가능한 제작자 또는 소비자를 만들고 실행할 수 있습니다. 예를 들어, 관계형 데이터베이스에 대한 커넥터는 테이블에 대한 모든 변경 사항을 캡처 할 수 있습니다.



Kafka에서 클라이언트와 서버 간의 통신은 단순하고 고성능의 언어에 구애받지 않는 **TCP 프로토콜**로 구현되어 있다.

사용가능한 [Client](https://cwiki.apache.org/confluence/display/KAFKA/Clients) 확인가능.



# 특징/디자인

> **프로튜서와 컨슈머의 분리**

링크드인에서는 메트릭 수집 방식을 폴링 방식으로 구현된 시스템을 사용했고, 메트릭 수집이 늦어지는 경우가 발생하면서 수집이나 처리 시간이 너무 늦어지는 문제점이 발견됨에 따라, 링크드인 개발자들은 데이터를 보내는 역할과 받는 역할을 완벽하게 분리하기를 원했다. 그래서 카프카는 메시징 전송방식 중 메시지를 보내는 역할과 받는 역할이 완벽하게 분리된 펍/섭 방식을 적용.

(그림 )

> **멀티 프로듀서, 멀티 컨슈머**

카프카는 하나의 토픽에 여러 프로듀서 또는 컨슈머들이 접근 가능한 구조로 되었습니다. 하나의 프로튜서가 하나의 토픽에만 메시지를 보내는 것이 아니라, 하나 또는 하나 이상의 토픽으로 메시지를 보낼 수 있다. 컨슈머는 역시 하나의 토픽에서만 메시지를 가져오는 것이 아니라, 하나 또는 하나 이상의 토픽으로부터 메시지를 가져올 수 있다. 이러한 멀티 기능은 데이터 분석 및 처리 프로세스에서 하나의 데이터를 다양한 용도로 사용하는 요구가 많아지기 시작했고, 이러한 요구 사항들을 손쉽게 충족할 수 있다.

(그림 )

> **디스크에 메시지 저장**

일반적인 메시징 시스템들은 컨슈머가 메시지를 읽어가면 큐에서 바로 메시지를 삭제합니다. 하지만 카프카는 컨슈머가 메시지를 읽어가더라도 정해져 있는 보관 주기 동안 디스크에 메시지를 저장해둡니다. 트래픽이 일시적으로 폭주해 컨슈머의 처리가 늦어지더라도 카프카의 디스크에 안전하게 보관되어 있기 때문에, 컨슈머는 메시지 손실없이 메시지를 가져갈 수 있다.

> **확장성**

카프카는 확장이 매우 용이하도록 설계, 하나의 카프카 클러스터는 3대의 브로커로 시작해 수십 대의 브로커로 확장 가능하다. 또한 확장 작업은 카프카 서비스의 중단 없이 온라인 상태에서 작업이 가능하다. 최초 카프카 클러스터 구성 시 적은 수로 시작하더라도 이후 트래픽 및 사용량 증가로 클러스터를 확장하는 작업은 매우 간단할 뿐만 아니라, 큰 부담없이 할 수 있음.

> **높은 성능**

내부적으로 분산 처리, 배치 처리등의 고성을을 유지하기 위한 다양한 기법을 활용한다.

> **Distribution**

로그의 파티션은 Kafka 클러스터의 서버를 통해 배포되며 각 서버는 데이터를 처리하고 파티션 공유에 대한 요청을 처리합니다. 각 파티션은 장애 허용을 위해 구성 가능한 수의 서버에 복제됩니다.

각 파티션에는 "리더"역할을하는 서버와 "팔로어"역할을하는 0 이상의 서버가 있습니다. 리더는 팔로워가 리더를 수동적으로 복제하는 동안 파티션에 대한 모든 읽기 및 쓰기 요청을 처리합니다. 

리더가 실패하면 추종자 중 하나가 자동으로 새로운 리더가 됩니다. 각 서버는 일부 파티션의 리더와 다른 서버의 팔로어로 작동하므로 로드가 클러스터 내에서 잘 균형을 이룹니다.

> **Geo-Replication**

Kafka MirrorMaker는 클러스터에 지리적 복제 지원을 제공합니다. MirrorMaker를 사용하면 메시지가 여러 데이터 센터 또는 클라우드 지역에 복제됩니다. 

백업 및 복구를 위해 능동 / 수동 시나리오에서 사용할 수 있습니다. 또는 데이터를 사용자 가까이에 배치하거나 데이터 지역성 요구 사항을 지원하는 활성 / 활성 시나리오에서 사용할 수 있습니다.

> **Producers**

Producers는 선택한 Topic 에 데이터를 게시합니다. Producer는 주제 내에서 어떤 파티션에 어떤 레코드를 할당할지 선택해야합니다. 이는 Load-balance을 맞추기 위해 라운드 로빈 방식으로 수행하거나 일부 의미적인 파티션 함수 (레코드의 일부 키를 기반으로 함)에 따라 수행 할 수 있습니다. 

두 번째로 파티셔닝으로 더 많이 사용합니다!

> **Consumers**

Consumers는 Consumer's Group 이름을 사용하여 레이블을 지정하고 주제에 게시 된 각 레코드는 구독하는 각 Consumer's Group 내의 하나의 Consumer's Instance에 전달됩니다. Consumers Instance는 별도의 프로세스 또는 별도의 시스템에있을 수 있습니다.

모든 Consumer 인스턴스가 동일한 Consumers Group을 갖는 경우 레코드는 Consumers Instance보다 효과적으로 밸런싱됩니다.

모든 Consumer 인스턴스가 서로 다른 Consumers Group을 갖고 있으면 각 레코드가 모든 소비자 프로세스에 브로드 캐스팅됩니다.

![](https://ws3.sinaimg.cn/large/006tNc79gy1g27uddnwm8j30d60700tc.jpg)

2 개의  consumer groups이있는 4개의 파티션 (P0-P3)을 호스팅하는 2대의 서버 Kafka 클러스터. 소비자 그룹 A에는 두 개의 소비자 인스턴스가 있고 그룹 B에는 네 개의 인스턴스가 있습니다.

그러나 더 일반적으로, 우리는 Topic이 각각의 "logical subscriber"에 대해 하나씩 적은 수의 소비자 그룹을 가지고 있음을 발견했습니다. 각 그룹은 확장성 및 내결함성을 위해 많은 소비자 인스턴스로 구성됩니다. 구독자가 단일 프로세스 대신 소비자 클러스터 인 publish-subscribe semantics 불과합니다.

Kafka에서 consumption가 구현되는 방식은 로그의 파티션을 소비자 인스턴스로 나누어 각 인스턴스가 어느 시점에서든 파티션의 "fair share"를 독점적으로 사용하는 것입니다. 이 그룹 구성원을 유지하는이 프로세스는 Kafka 프로토콜에 의해 동적으로 처리됩니다. 새 인스턴스가 그룹에 참여하면 그룹의 다른 구성원으로부터 일부 파티션을 인계받습니다. 인스턴스가 종료되면 해당 파티션이 나머지 인스턴스에 배포됩니다.

카프카는 한 Topic의 다른 파티션 사이가 아니라 한 파티션 내의 레코드에 대해서만 전체 주문을 제공합니다. 대부분의 응용 프로그램에서는 키 단위로 데이터를 분할하는 기능과 함께 파티션 단위의 순서만으로 충분합니다. 그러나 레코드에 대한 전체 순서가 필요한 경우 이는 하나의 파티션 만있는 항목으로 달성 할 수 있습니다. 단, 이는 소비자 그룹당 하나의 소비자 프로세스를 의미합니다.

> **Multi-tenancy(다중 임대)**

카프카를 Multi-tenancy 솔루션으로 배포 할 수 있습니다. Multi-tenancy는 데이터를 produce or consume 할 수있는 Topic을 구성하여 활성화됩니다. 할당량에 대한 운영 지원도 있습니다. 관리자는 클라이언트가 사용하는 브로커 자원을 제어하는 요청에 대해 할당량을 정의하고 시행 할 수 있습니다. 자세한 내용은 보안 설명서를 참조하십시오.

> **Guarnatees**

- 생성자가 특정 주제 파티션으로 보낸 메시지는 전송 된 순서대로 추가됩니다. 즉, 레코드 M1이 레코드 M2와 동일한 생성자에 의해 보내지고 M1이 먼저 보내지면 M1은 M2보다 더 낮은 오프셋을 가지며 로그에서 더 일찍 나타납니다.
- 소비자 인스턴스는 로그에 저장된 순서대로 레코드를 봅니다.
- For a topic with replication factor N, we will tolerate up to N-1 server failures without losing any records committed to the log. (복제 인수가 N 인 항목의 경우 로그에 커밋 된 레코드를 손실하지 않고 최대 N-1 개의 서버 오류를 허용합니다.)

---

## 디자인

### 분산 시스템

분산 시스템은 네트워크로 이루어진 컴퓨터들의 그룹으로서 시스템 전체가 공통의 목표를 가진다. 같은 역할을 하는 여러 대의 서버로 이뤄진 서버그룹은 분산 시스템이라고 한다. 

- 단일 시스템보다 더 높은 성능을 얻을 수있다.
- 분산 시스템 중 하나의 서버 또는 노드 등이 장애가 발생하면 다른 서버 또는 노드가 대신 처리한다.
- 시스템 확장이 용이.



### 페이지 캐시

카프카는 처리량을 높이기 위한 기능을 몇 가지 추가했고 그 기능 중 하나가 페이지 캐시를 이용하는 것.

OS는 물리적 메모리에 애플리케이션이 사용하는 부분을 할당하고 남은 잔여 메모리 일부를 페이지 캐시로 유지해 OS의 전체적인 성능 향상을 높이게 됩니다. 

### 배치 전송 처리

 서버와 클라이언트 사이 또는 서버 내부적으로 데이터를 주고받는 과정에서는 I/O가 발생. 빈번하게 일어날경우 속도가 저하될 수 있다.

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2a02h648aj30vv0u0b2a.jpg)



# UseCase

### kafka as a Messaging System

**여기서 질문!** 기존의 메세지 큐와 카프카의 메시지큐는 뭐가 다를까?

메시징에는 전통적으로 두 가지 모델이 있습니다.  [Queuing](http://en.wikipedia.org/wiki/Message_queue)과  [Publish-subscribe](http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)입니다.

Quque에서 소비자 풀은 서버에서 읽을 수 있으며, 각 레코드는 그 중 하나에 저장됩니다. 그리고 publish-subscribe에서 모든 소비자에게 레코드가 브로드 캐스트됩니다.

각각이 장단점이 있는데, 

Queuing을 사용하면 여러 소비자 인스턴스에서 데이터 처리를 나눌 수 있으므로 처리 규모를 확장 할 수 있습니다. 유감스럽게도Queuing은 multi-subscriber가 아닙니다. 일단 하나의 프로세스가 데이터를 읽으면 그것은 사라진다.

반면, Publish-subscribe를 사용하면 데이터를 여러 프로세스에 브로드 캐스트 할 수 있지만 모든 메시지가 모든 구독자에게 전달되기 때문에 확장 처리 방법이 없습니다.

Kafka의 Consumer group 개념은 앞에 두가지 개념을 일반화합니다. Queuing과 마찬가지로 소비자 그룹은 프로세스 모음 (소비자 그룹의 구성원)을 통해 처리를 나눌 수 있습니다. publish-subscribe와 마찬가지로 Kafka를 사용하면 여러 소비자 그룹에 메시지를 브로드캐스트 할 수 있습니다.

Kafka의 모델의 장점은 모든 Topic이 이러한 속성을 모두 갖추고 있다는 것입니다. 즉, 처리 규모를 조정할 수 있고 다중 가입자이기도합니다. 하나 또는 둘 다르게 선택할 필요가 없습니다.

**Kafka has stronger ordering guarantees than a traditional messaging system, too.**

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

---

- 다양한 시스템과 연동하기 위한 멀티 프로토콜과 데이터 타입 지원
- 느슨한 결합(Loosely coupled)을 위한 메시지 큐 지원
- 정기적으로 데이터를 가져오는 대신 이벤트 기반 통신 지원

![](https://ws3.sinaimg.cn/large/006tNc79gy1g2bb1hyqltj30o50hk0ts.jpg)

![넷플릭스](https://ws3.sinaimg.cn/large/006tNc79gy1g2bb3fhjuxj30iv0ahjse.jpg)

![링크드인](https://ws4.sinaimg.cn/large/006tNc79gy1g2bb5o68p7j316k0u0gqg.jpg)

![우버](https://ws2.sinaimg.cn/large/006tNc79gy1g2bb61n6o2j30sg0ergnn.jpg)

## Topic

카프카 클러스터는 Topic이라 불리는 곳에 데이터를 저장한다. 우리가 많이 사용하는 메일 시스템과 비교하면, 토픽은 메일주소라고 생각하면 쉽다.

카프카에서는 데이터를 구분하기 위한 단위로 토픽이라는 용어를 사용하는데, 249자 미만으로 영문,숫자, '-','.','_','-'를 조합하여 자유롭게 만들 수 있다.

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2a08c3o2mj313y0u01ky.jpg)



## Partition

파티션이란 토픽을 분할한 것이다. 그럼 왜 하나의 토픽을 파티셔닝하는 걸까?

계산해보자!

4개의 메시지를 한개의 파티션으로 보내면 4초,

여기에서는 소요시간계산이 용이하도록 메시지를 보내는 데 걸리는 시간은 1초라고 가정하고, 프로튜서만 4개로 변경하고 파티션은 1개로 유지하면, 4배의 성능을 보장할 수 있지만, 이렇게 되면 큐시스템의 제약조건으로 메시지의 순서를 보장할 수 없다.

결국, 카푸카에서 효율적인 메시지 전송과 속도를 높이려면 토픽의 파티션 수를 늘려줘야 한다. 뉴스 토픽에 대해 파티션 수를 1개에서 4개로 변경하고, 파티션 수와 동일하게 프로듀서 수도 4개로 늘린뒤. 각 프로듀서는 하나의 메시지를 뉴스토픽의 파티션으로 보내게 된다. 빠른 전송을 위해서는 토픽의 파티션을 늘려줘야 하며, 그 수만큼 프로튜서 수도 늘려야 제대로 된 효과를 볼 수 있다.



**그럼 반대로 무조건 파티션의 수가 늘려야하나??**



발생할 수 있는 문제점은 무엇일까?

- 파일 핸들러의 낭비
- 장애 복구 시간 증가

**그렇다면 내 토픽의 적절한 파티션 수는??**

일단 원하는 목표 처리량의 기준을 잡아야 한다.

프로튜서 입장에서 4개의 프로튜서를 통해 각각 초당 10개의 메시지를 카프카의 토픽으로 보낸다면, 카프카의 토픽에서 초당 40개의 메시지를 받아줘야 합니다. 만약 해당 토픽에서 파티션을 1로 했을 때 초당 10개의 메시지를 받아준다면 파티션을 4로 늘려서 목표 처리량을 처리할 수 있도록 변경합니다. 토픽의 파티션 수를 4개로 정해 프로튜서의 목표치는 달성 했다.

**하지만 카프카에서는 컨슈머도 있기 때문에 컨슈머의 입장도 고려해야 합니다.** 컨슈머 입장에서 8개의 컨슈머를 통해 각각 초당 5개의 메시지를 카프카의 토픽에서 가져올 수 있다면, 해당 토픽의 파티션 수는 컨슈머 수와 동일하게 8개로 맞추어 켠슈머마다 각각의 파티션에 접근할 수 있게 해야 합니다.





![](https://ws3.sinaimg.cn/large/006tNc79gy1g2bbr20hlkj30d30g0q3q.jpg)

## Offset

카프카에서는 각 파티션마다 메시지가 저장되는 위치를 오프셋이라고 부르고 오프셋은 파티션 내에서 유일하고 순차적으로 증가하는 숫자(64비트) 형태로 되어 있다.

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2bbb5lbsbj30bk07faal.jpg)

여기서 쓰기의 의미는 프로튜서가 메시지를 보내면 메시지가 각 파티션 별로 분산되어 데이터를 저장하는 상태를 나타낸다. 각각의 파티션에는 프로튜서가 전송한 메시지들이 저장되어 있으며, 저장된 위치를 유니크하고 순차적인 숫자 형태인 0,1,2 같은 형태로 나타내고 있다. 이러한 숫자는 파티션마다 유니크한 값을 가지며 카프카에서 이를 오프셋이라고 한다. 오프셋은 하나의 파티션 내에서만 유일한 숫자이다.

## 카프카의 고가용성과 리플리케이션

분산 애플리케이션으로 서버의 물리적 장애가 발생하는 경우에도 높은 가용성을 보장. 이를 위해 카프카는 리플리케이션(Replication) 기능을 제공합니다. 카프카의 리플리케이션은 토픽 자체를 리플리케이션하는 것이 아니라,

 **토픽을 이루는 각각의 파티션을 리플리케이션하는 것.**

![](https://ws3.sinaimg.cn/large/006tNc79gy1g2bbzf6e0vj30ln09qdgc.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79gy1g2bc01mtr1j30ln09qjs0.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79gy1g2bc16rolrj30ln09qjs2.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79gy1g2bc1lfjvpj30ln09q74x.jpg)

- 리플리케이션 팩터와 리더, 팔로워의 역할

  카프카에는 리플리케이션 팩터(Factor)라는 것이 있음. 카프카의 기본값은 1로, 변경하고 싶다면

  레플리는 2로 설정해주는 것이 좋다.

  리더와 팔로워는 각자 역할이 나뉘어 있는데 가장 중요한 핵심은 모든 읽기와 쓰기가 리더를 통해서만 일어난다는 점, 즉 팔로워는 리더의 데이터를 그대로 리플리케이션만 하고 읽기와 쓰기에는 관여하지 않습니다. 리더와 팔로워는 저장된 데이터의 순서도 일치하고 동일한 오프셋과 메시지를 갖게 됩니다.

  단점은,  100G이면, 리플리케이션을 하는 다른 브로커에도 100G 들어간다.

- 리더와 팔로워의 관리

  리더는 모든 데이터의 읽기 쓰기에 대한 요청에 응답하면서 데이터를 저장해나가고, 팔로워는 리더를 주기적으로 보면서 자신에게 없는 데이터를 리더로부터 주기적으로 가져오는 방법으로 리플리케이션을 유지합니다. 리더와 팔로워 모두 주어진 역할에 맞게 잘 동작하고 있다면 전혀 문제가 없지만 팔로워에 문제가 있어 리더로부터 데이터를 가져오지 못하면서 정합성이 맞지 않게 된다면 어떻게 될까요? 결국 리더가 다운되는 경우 팔로워가 새로운 리더로 승격되어야 하는데, 데이터가 읽치하지 않으므로 큰 문제가 발생할 수 있다. 카프카에서는 이러한 현상을 방지하고자 ISR(In Sync Replica)라는 개념을 도입했다.

  **ISR** - 현재 리플리케이션되고 있는 리플리케이션 그룹. ISR에는 중요한 규칙 하나가 있는데, 그 규칙은 ISR에 속해있는 구성원만이 리더의 자격을 가질 수 있다. 
  peter토픽이 리플리케이션 팩터2로 구성되어 리더는 1번 브로커, 팔로워는 2번 브로커에 위치하고 있다면, ISR구성원은 1,2입니다. 그런데 급작스러운 이유로 브로커 1이 다운되면, ISR의 구성원인 2번 브로커에 있는 팔로워가 새로운 리더로 승격.

## 모든 브로커가 다운된다면

1. 마지막 리더가 살아나기를 기다린다.
2. ISR에서 추방되었지만 자동으로 리더가 된다.

0.11.0.0 이하 버전에서는 기본값으로 2번 방안 / 그 이상 버전부터는 1번 방안을 고려한다.

## 카프카에서 사용하는 주키퍼 지노드 역할

주키퍼는 서버 여러 대를 앙상블로 구성하고, 분산 애플리케이션들이 각각 클라이언트가 되어 주키퍼 서버들과 커넥션을 맺은 후 상태 정보등을 주고받게 됩니다. 상태 정보들은 주키퍼의 znode라 불리는 곳에 키-값 형태로 저장하고, 지노드에 키-값이 저장된 것을 이용하여 분산 애플리케이션들은 서로 데이터를 주고받게 도비니다. 주키퍼에서 사용되는 지노드는 데이터를 저장하기 위한 공간 이름을 말하는 것으로,일반 컴퓨터의 파일이나 폴더 개념이라고 생각하면 된다.



**그럼 카프라에서 지노드의 역할은?**

만약 지노드를 확인하고 싶다면, 주키퍼 서버에 접속한 후 zkCli.sh를 실행

`/usr/local/zookeeper/bin/zkCli.sh`

접속한 후 리스트를 확인하는  ls / 명령어를 이용하여 지노드 확인



# 카프카가 말하는 벤치마크

RabbitMQ와 Kafa비교



참고사이트

<https://www.slideshare.net/ifkakao/ss-113145591>



---

실습

➜  ~ zkServer start
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Starting zookeeper ... STARTED
➜  ~ zkServer stop
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Stopping zookeeper ... STOPPED
➜  ~ zkServer start
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Starting zookeeper … STARTED