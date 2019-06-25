



# 병렬 연산 모델



병렬 데이터 처리를 수행할 수 있는 클러스터 시스템 위에서 구동되는 드라이버(Driver)혹은 마스터 노드를 위한 프로그램을 사용자가 만들어야 한다. 스파크는 대용량 데이터세트를 **RDD(변경할 수 없는 형태의 분산된 객체들의 모음)** 표현하는데, 이들은 executor 혹은 slave 에 저장된다. RDD를 구성하는 객체를 파티션(Partition)이라고 하는데,  경우에 따라 다르지만 저장된 노드가 아닌 다른 노드에서 계산될 수도 있다

- . **스파크 클러스터 매니저** 은 스파크 애플리케이션에서 설정한 파라미터에 따라 분산 시스템에 이그제큐터를 실행하고 분산해 주는 역할.
- 드라이버 프로그램이 RDD의 각 데이터들의 처리 단계를 결정하자마자 연산을 수행하는 것이 아니라 연산 시점을 뒤로 미루어 실제로 최종 RDD를 계산해야 하는 시점에 RDD변형을 수행한다.(보통 저장 장치에 써야 할 시점이나 결과 데이터를 드라이버에 보내야 할 때)

- 스파크는 더 빠른 접근과 반복 연산을 위해 스파크 애플리케이션이 동작하는 동안 로드된 RDD를 이그제큐너 노드들의 메모리에 가지고 있을 수 있다. 이들은 스파크에서 변경 불가능(immutable)하도록 구현되었기 때문에 데이터 변형의 결과는 기존 RDD가 아닌 새로운 RDD를 리턴한다. 이 장을 살펴보는 동안 이런 지연 평가, 인메모리 저장소, 불변셩의 패러다임이 스파크를 쓰기 쉽고 장애에 강하며 쉽게 확장 가능하고 효과적으로 만들어 준다는 것을 꺠닫게 



## 지연 평가

인메모리 저장소를 쓰는 다른 많은 시스템들은 변경 가능한 객체를 '잘게 쪼개어서'업데이트하지만, RDD의 연산은 완전히 게으른 방식을 채택. 파티션은 액션이 호출되기 전까지는 계산되지 않는다. 액션은 RD가 아닌 다른 타입의 결과를 리턴하는 스파크 연산 종류의 하나로, 파티션 연산을 시작하게 하고 스파크 외의 시스템으로 결과를 보낼 수도 있다.