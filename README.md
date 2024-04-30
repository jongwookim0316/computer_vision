<특징점 검출>

1. 특징점 검출이란?
이미지 내의 주요한 특징점을 검출하는 방법입니다. 해당 특징점이 존재하는 위치를 알려주거나 해당 특징점을 부각 시킵니다. 픽셀의 색상 강도, 연속성, 변화량, 의존성, 유사성, 임계점등을 사용하여 특징을 파악합니다.

2. 특징점 검출 실습
   1) 해리스 검출
![해리스 검출1](https://github.com/jongwookim0316/computer_vision/assets/135306103/99dcd1bd-ed37-43fe-a8b9-2cd102b5ea29)
![해리스 검출2](https://github.com/jongwookim0316/computer_vision/assets/135306103/37dac3c7-44f3-42cf-8c41-aab3fc4df1ee)
![해리스 검출3](https://github.com/jongwookim0316/computer_vision/assets/135306103/a7f529f4-eed6-4fe8-9f11-3c6c69445ffc)

   2) SIFT
![SIFT](https://github.com/jongwookim0316/computer_vision/assets/135306103/868cf345-3d2a-45ab-b73c-df778ce2b644)

   3) FLANN
![FLANN](https://github.com/jongwookim0316/computer_vision/assets/135306103/55625610-966f-422a-9ee2-7f847e0d0867)

   4) RANSAC
![RANSAC](https://github.com/jongwookim0316/computer_vision/assets/135306103/27ad3371-e743-44c7-b112-75a408c34d31)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<edge_detection>

1. edge_detection 란?
   디지털 이미지 처리에서 중요한 작업 중 하나입니다. 이미지의 에지는 이미지에서 갑작스럽게 밝기가 변하는 부분으로, 대상의 형태나 구조를 나타내는 중요한 정보를 제공합니다.
   에지 검출은 이러한 에지를 식별하고 감지하는 과정을 말합니다.
  
2. edge_detection 실습
   1) edge 검출 

![original_soccer](https://github.com/jongwookim0316/computer_vision/assets/135306103/5a695c5f-fbc8-4fb0-a55f-e3feefb4c7a5)

![sobelx](https://github.com/jongwookim0316/computer_vision/assets/135306103/3e221b80-2856-41e7-be5a-a4995b4781da)

![sobely](https://github.com/jongwookim0316/computer_vision/assets/135306103/185c009f-6141-49fc-b593-f2b8c2a47006)

![edge_strength](https://github.com/jongwookim0316/computer_vision/assets/135306103/9c7d35d9-da98-4bd9-b7c6-3bc4f10c060a)


   2) 캐니 edge

![original_happy](https://github.com/jongwookim0316/computer_vision/assets/135306103/4a0adc14-b44f-4ca2-8dfe-c2010ae02ff7)

![canny1](https://github.com/jongwookim0316/computer_vision/assets/135306103/0afc1817-d356-44ae-99f9-8b3eecb8c5b2)

![canny2](https://github.com/jongwookim0316/computer_vision/assets/135306103/bde58878-ff0c-4107-9521-aaca7e0f0a03)

   3) 직선 검출1

![사과 검출](https://github.com/jongwookim0316/computer_vision/assets/135306103/0af6bb76-cb23-46ed-8bc9-fed893220436)

   4) 직선 검출2

![image](https://github.com/jongwookim0316/computer_vision/assets/135306103/b6be7ce6-120e-4497-832b-9618a75a9969)

![image](https://github.com/jongwookim0316/computer_vision/assets/135306103/be32d7a0-84e5-4a17-b7ab-3b62a9c9bab5)

   5) 영역 분할

![영역분할](https://github.com/jongwookim0316/computer_vision/assets/135306103/f3b5060a-2219-44e3-96bd-dc1bc03f157d)

   6) 최적화 분할

![최적화 분할](https://github.com/jongwookim0316/computer_vision/assets/135306103/fea18101-2885-4c5a-b62f-51f1c5bc8902)

   7) GrabCut을 이용한 대화식 분활

![grabcut](https://github.com/jongwookim0316/computer_vision/assets/135306103/9f1bfa8c-4dab-43a0-8688-1bfdba6774b9)

   8) 이진 영역의 특징

![영역 특징](https://github.com/jongwookim0316/computer_vision/assets/135306103/8ca28bce-4a00-45f2-97c7-5ce1040bcc1b)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<OPEN CV>

1. open cv 란?

OpenCV는 Open Source Computer Vision의 약자로 영상 처리에 사용할 수 있는 오픈 소스 라이브러리 입니다. 
컴퓨터가 사람의 눈처럼 인식할 수 있게 처리해주는 역할을 하기도 하며, 우리가 많이 사용하는 카메라 어플에서도 OpenCV가 사용하기도 합니다.

2. open cv 구조

![image](https://github.com/jongwookim0316/computer_vision/assets/135306103/7d4ca9ff-277f-4253-a011-7b57a191cfdf)

![image](https://github.com/jongwookim0316/computer_vision/assets/135306103/38b3708d-8516-4f04-90c8-325c17858177)
사진 출처 : https://studium-anywhere.tistory.com/22

3. open cv 실습

1) 영상을 읽고 표시하기
![결과3](https://github.com/jongwookim0316/computer_vision/assets/135306103/96e16ee6-d431-4b77-80b8-8bfa46c9535f)
![결과3-1](https://github.com/jongwookim0316/computer_vision/assets/135306103/c018ea8f-a101-4594-829a-1e9f553c6b23)



2) 영상 형태 변환하고 크기 축소하기
![결과4](https://github.com/jongwookim0316/computer_vision/assets/135306103/dd841a50-ff72-46a5-be5d-d9638996d5a3)



3) 웹 캠에서 비디오 읽기



4) 비디오에서 수집한 영상 이어 붙이기



5) 영상에 도형을 그리고 글씨 쓰기 1
![결과6](https://github.com/jongwookim0316/computer_vision/assets/135306103/ccf12be1-4760-42af-8916-9cc3d96bfee7)



6) 영상에 도형을 그리고 글씨 쓰기 2
![결과7-1](https://github.com/jongwookim0316/computer_vision/assets/135306103/c21f7d05-719a-44d5-b311-0d7a5c7ef1ea)



7) 마우스 드래그로 도형크기 조절하기
![결과8](https://github.com/jongwookim0316/computer_vision/assets/135306103/6d970367-740e-44a6-9a33-43c4546acb49)



8) 페인팅 기능 만들기
![결과9](https://github.com/jongwookim0316/computer_vision/assets/135306103/2dff9db1-f971-4898-97bd-2e8b1b13d673)
