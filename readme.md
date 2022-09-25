# Genome Sequencing

## Week 1
<p align="center"><img src="https://github.com/yeojingi/genome-sequencing/blob/main/img/gluing_tg.png" width="40%"></p>

<p>Shotgun Sequencing을 하기 위해 적절한 데이터 구조를 알아보자. <br>

### 과제 사례
|파일명|내용|결과|비고|
|------|---|---|---|
|[OverlapGraph.py](https://github.com/yeojingi/genome-sequencing/blob/main/week1/OverlapGraph.py)|주어진 k-mers 데이터에서 뒤의 k-1과 앞의 k-1가 겹치는 k-mer끼리 묶어서 output을 출력한다 |ATGCG GCATG CATGC AGGCA GGCAT GGCAC| CATGC: ATGCG \ GCATG: CATGC \ GGCAT: GCATG \ AGGCA: GGCAC GGCAT|
|[DeBrujinGraphFromKMers.py](https://github.com/yeojingi/genome-sequencing/blob/main/week1/DeBrujinGraphFromKMers.py)|위의 OverlapGraph.py와 달리 k-mers와 k-mers 간의 연결 관계를 표시하는 것이 아니라, k-mer의 앞의 k-1 부분(prefix)과 뒤의 k-1(suffix)를 edge로 만든다. 즉, k-mer가 노드가 되는 것이 아니라 엣지로서 표현된다.|GAGG CAGG GGGG GGGA CAGG AGGG GGAG|AGG: GGG \ CAG: AGG AGG \ GAG: AGG \ GGA: GAG \ GGG: GGA GGG|
