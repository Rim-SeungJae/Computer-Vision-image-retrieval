<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=OpenCV&logoColor=white"/>
# 소개
이 저장소는 OpenCV를 활용한 프로젝트를 담고 있습니다.

## A3_compute_descriptors.py

이미지 사이의 유사도를 비교하기 위해서 필요한 이미지의 descriptor를 계산하는 코드를 작성하였습니다.
프로그램의 자세한 동작 과정은 아래와 같습니다.
1. visual word dictionary 읽어오기
프로그램이 실행된 후에 처음으로 하는 일은 'codewords'라는 사전 저장 파일에서 visual word dictionary를 읽어오는 것입니다. visual word dictionary의 visual word들은 주어진 데이터셋의 SIFT feauture들을 Kmeans를 사용하여 클러스터링하고 중앙값을 취하여 얻었습니다. 클러스터링은 128개의 클래스로 나뉘었습니다. 따라서 visual dictionary의 차원은 128입니다.

2. SIFT 파일 읽기
데이터셋의 각 SIFT 파일을 반복하여 읽습니다. 읽은 데이터는 numpy 배열 형식으로 저장됩니다.

3. 해당 SIFT 파일에 대한 BOW(Bag Of Words) 벡터 구축
이미지의 SIFT feature과 visual word 간의 거리를 계산하여 해당 특징과 가장 유사한 visual word를 결정합니다. 모든 feature에 대해 이러한 계산을 반복하여 해당 이미지의 모든 visual word에 대한 빈도를 나타내는 BOW 벡터를 얻을 수 있습니다.

4. 모든 벡터를 .des 파일로 저장
이전 단계에서 얻은 모든 벡터를 수집하고 .des 파일로 저장합니다.
