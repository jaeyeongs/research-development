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
