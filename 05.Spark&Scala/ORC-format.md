# ORC

**Optimized Row Columnar** file format

- 하이브 파일 포맷의 한계를 극복하기 위해서 나온 포맷으로 퍼포먼스가 좋음
- [RCFile](https://en.wikipedia.org/wiki/RCFile) 비해 장점은 다음과 같다.
  - NameNode의 부하를 줄이는 각 작업의 출력으로 단일 파일로 만든다.
  - 좀 더 다양한 타입을 지원(datatime, decimal, complex type(list, struct, map and union))
  - light-weight 인덱스를 파일안에 저장한다.
    - 조건부 필터링을 통과하지 않는 행 그룹 건너 뛰기
    - seek to a given row
  - 데이터 유형에 기반한 블록 모드 압축
    - run-length encoding for integer columns
    - dictionary encoding for string columns
  - 별도의 RecordReaders를 사용하여 동일한 파일의 동시 읽기
  - Markers를 스캔하지 않고 파일을 분할하는 기능
  - 읽기 또는 쓰기에 필요한 메모리 양을 제한한다.
  - 프로토콜 버퍼를 사용하여 메타 데이터 저장, 필드 추가 및 제거 가능



### 파일 구조

ORC 파일에는 file footer의 보조 정보와 함께 stripes 라고하는 groups of row data이 포함되어 있습니다. 파일의 끝에는 postscript가 압축 매개 변수와 압축 된 footer 글의 크기를 저장합니다.



기본 default stripe 사이즈는 250MB, 큰 사이즈가 가능하므로, HDFS에서 읽는 것이 효과적이다.

File footer에는 file의 strips 목록들과, strips의 한 개당 행 수 및 각 열의 데이터 유형을 포함합니다. 또한 Columns수준에서 집계 수, 최소, 최대 및 합계를 포함합니다.



![img](http://ww1.sinaimg.cn/large/006tNc79gy1g4c7qp3w3gj30g40frwho.jpg)



