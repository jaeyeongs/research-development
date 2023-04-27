# ElasticSearch 기본 개념

## 1. ElasticSearch

ElasticSearch는 Apache Lucene(아파치 루씬) 기반의 Java 오픈소스 분산 검색 엔진

ElasticSearch를 통해 루씬 라이브러리를 단독으로 사용할 수 있게 되었으며, 방대한 양의 데이터를 신속하게, 거의 실시간(NRT, Near Real Time)으로 저장, 검색, 분석이 가능

Elasticsearch는 검색을 위해 단독으로 사용되기도 하며, ELK(Elasticsearch / Logstatsh / Kibana)스택으로 사용


- **Logstash**
    
    다양한 소스(DB, CSV 파일 등)의 로그 또는 트랜잭션 데이터를 수집, 집계, 파싱하여 Elasticsearch로 전달
    
- **ElasticSearch**
    
    Logstash로부터 받은 데이터를 검색 및 집계를 하여 필요한 관심 있는 정보를 획득
    
- **Kibana**
    
    ElasticSearch의 빠른 검색을 통해 데이터를 시각화 및 모니터링

![image](https://user-images.githubusercontent.com/87981867/203449976-0582c27c-ee9b-4b56-860b-af99f3b8a482.png)

## 2. ElasticSearch 특징

- **Scale out**
    
    샤드를 통해 규모가 수평적으로 늘어날 수 있음
    
- **고가용성**
    
    Replica를 통해 데이터의 안정성을 보장
    
- **Schema Free**
    
    JSON 문서를 통해 데이터 검색을 수행하므로 스키마 개념이 없음
    
    
 
 ## 3. ElasticSearch와 관계형 DB

흔히 사용하고 있는 관계형 DB는 ElasticSearch에서 각각 다음과 같이 대응시킬 수 있음

![image](https://user-images.githubusercontent.com/87981867/203668852-f41b23f3-81b9-472d-b9a8-96b293b4ca8c.png)
![image](https://user-images.githubusercontent.com/87981867/203668860-e09b187d-5694-463d-8038-333d63a6753b.png)

| Relational Database | CRUD | ElasticSearch Restful |
| :---: | :---: | :---: |
| SELECT | SELECT | GET |
| UPDATE | INSERT | PUT |
| INSERT | UPDATE | POST |
| DELETE | DELETE | DELETE |

## 4. ElasticSearch 아키텍쳐 및 용어

ElasticSearch에서 사용하는 대부분의 개념은 RDBMS에도 존재하는 개념

![image](https://user-images.githubusercontent.com/87981867/203902337-6a5d259f-8fbc-43c2-b9da-3dd2595f4ae8.png)

**(1) 클러스터(Cluseter)**

클러스터란 ElasticSearch에서 가장 큰 시스템 단위를 의미하며, 최소 하나 이상의 노드로 이루어진 노드들의 집합

서로 다른 클러스터는 데이터의 접근, 교환을 할 수 없는 독립적인 시스템으로 유지

여러 대의 서버가 하나의 클러스터를 구성할 수 있고, 한 서버에 여러 개의 클러스터가 존재할수도 있음

**(2) 노드(Node)**

ElasticSearch를 구성하는 하나의 단위 프로세스를 의미

역할에 따라 **Master-eligible Node**, **Data Node**, **Ingest Node**, **Tribe Node**로 구분

**1) Master-eligible Node**

클러스터를 제어하는 마스터로 선택할 수 있는 노드

Master 노드의 역할

- 인덱스 생성, 삭제
- 클러스더 노드들의 추적, 관리
- 데이터 입력 시 어떤 샤드(Shard)에 할당할 것인지

**2) Data Node**

데이터와 관련된 CRUD 작업과 관련있는 노드

CPU, 메모리 등 자원을 많이 소모하므로 모니터링이 필요하며, master 노드와 분리되는 것이 좋음

**3) Ingest Node**

데이터를 변환하는 등 사전 처리 파이프라인을 실행하는 역할

**4) Coordination only Node**

Data Node와 Master-eligible Node의 일을 대신 하여 대규모 클러스터에서 큰 이점

로드밸런서와 비슷한 역할

**(3) 인덱스(Index) / 샤드(Shard) / 복제(Replica)**

**1) Index**

ElasticSearch에서 **Index**는 RDBMS에서 Database와 대응하는 개념

**2) Shard**

데이터를 분산해서 저장하는 방법을 의미

Elasticsearch에서 scale out을 위해 index를 여러 Shard로 쪼갠 것

기본적으로 1개가 존재하며, 검색 성능 향상을 위해 클러스터의 샤드 갯수를 조정하는 튜닝을 하기도 함

**3) Replica** 

Replica는 또 다른 형태의 **Shard**라고 할 수 있음

노드를 손실했을 경우 데이터의 신뢰성을 위해 샤드들을 복제

![image](https://user-images.githubusercontent.com/87981867/203902360-c58a52bb-e5ac-4863-af63-25601c04c657.png)

## 5. 역색인(Inverted Index)

책에서 맨 앞에 볼 수 있는 목차가 index, 책 맨 뒤에 키워드마다 찾아볼 수 있도록 찾아보기가 inverted index

Elasticsearch는 텍스트를 파싱해서 검색어 사전을 만든 다음에 inverted index 방식으로 텍스트를 저장

![image](https://user-images.githubusercontent.com/87981867/204070510-dcb3b40f-6a0d-4a80-8883-c0c84640c7da.png)
![image](https://user-images.githubusercontent.com/87981867/204070514-904a7712-05ba-4c28-abab-bc0dad28916b.png)

> "Lorem Ipsum is simply dummy text of the printing and typesetting industry"


이 문장을 모두 파싱해서 각 단어들( Lorem, Ipsum, is, simply .... )을 저장하고,

대문자는 소문자 처리하고, 유사어도 체크 등의 작업을 통해 텍스트를 저장

때문에 RDBMS보다 전문검색(Full Text Search)에 빠른 성능을 보임
