# Genome Sequencing

## Week 1 - How do we aseemble genomes? part I
<p align="center"><img src="https://github.com/yeojingi/genome-sequencing/blob/main/img/gluing_tg.png" width="70%"></p>

<p>Shotgun Sequencing을 하기 위해 적절한 데이터 구조를 알아보자. <br>

### 과제 사례
|파일명|내용|결과|비고|
|------|---|---|---|
|[OverlapGraph.py](https://github.com/yeojingi/genome-sequencing/blob/main/week1/OverlapGraph.py)|주어진 k-mers 데이터에서 뒤의 k-1과 앞의 k-1가 겹치는 k-mer끼리 묶어서 output을 출력한다 |ATGCG GCATG CATGC AGGCA GGCAT GGCAC| CATGC: ATGCG \ GCATG: CATGC \ GGCAT: GCATG \ AGGCA: GGCAC GGCAT|
|[DeBrujinGraphFromKMers.py](https://github.com/yeojingi/genome-sequencing/blob/main/week1/DeBrujinGraphFromKMers.py)|위의 OverlapGraph.py와 달리 k-mers와 k-mers 간의 연결 관계를 표시하는 것이 아니라, k-mer의 앞의 k-1 부분(prefix)과 뒤의 k-1(suffix)를 edge로 만든다. 즉, k-mer가 노드가 되는 것이 아니라 엣지로서 표현된다.|GAGG CAGG GGGG GGGA CAGG AGGG GGAG|AGG: GGG \ CAG: AGG AGG \ GAG: AGG \ GGA: GAG \ GGG: GGA GGG|

## Week 2 - How do we aseemble genomes? part II

<p>오일러 경로와, d 간격을 두고 읽은 k-mer를 통해 error를 교정하는 sequencing을 해보자.<br>

### 과제 사례
|파일명|내용|결과|비고|
|------|---|---|---|
|[EulerianCycle.py](https://github.com/yeojingi/genome-sequencing/blob/main/week2/lesson2/EulerianCycle.py)|주어진 edge 데이터에서 오일러 회로를 만들었다. |-|-|
|[EulerianPath.py](https://github.com/yeojingi/genome-sequencing/blob/main/week2/lesson2/EulerianPath.py)|주어진 edge 데이터에서 오일러 경로를 만들었다.| - | - |
|[kUniversalCircularString.py](https://github.com/yeojingi/genome-sequencing/blob/main/week2/lesson2/kUniversalCircularString.py)| 길이 k의 모든 이진수에서, 오일러 회로를 만들었다.|-|-|

## Week 3 - How do we sequence antibiotics? part I

<p align="center"><img src="https://github.com/yeojingi/genome-sequencing/blob/main/img/mass_spectrometer.jpeg" width="70%"></p>
<p>Mass spectrometer를 통해 읽어 들인 단백질의 질량 데이터를 통해 단백질의 아미노산 서열을 sequencing해보자.<br>

### 과제 사례
|파일명|내용|결과|비고|
|------|---|---|---|
|[CycloPeptideSequencing.py](https://github.com/yeojingi/genome-sequencing/blob/main/week3/lesson4/CycloPeptideSequencing.py)|Mass spectromter를 통해 알게 된 단백질의 질량 데이터를 통해, 단백질의 아미노산 서열(각 서열의 질량)을 sequencing하였다 |186-147-114-128-163-99-128-113-147-97 147-114-128-163-99-128-113-147-97-186 ... [결과](https://github.com/yeojingi/genome-sequencing/blob/main/week3/lesson4/data/output_Tyrocidine_B1_theoretical_spectrum.txt)|[Tyrocidine_B1_theoretical_spectrum](https://github.com/yeojingi/genome-sequencing/blob/main/week3/lesson4/data/Tyrocidine_B1_theoretical_spectrum.txt)|