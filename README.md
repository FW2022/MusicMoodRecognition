<p align="middle">
    <img width="200px;" src="https://github.com/omizha/Space4U-client/blob/master/docs/img/logo.png?raw=true"/>
</p>
<h2 align="middle">Space for U</h2>
<p align="middle">WebGL(three.js) + AI를 활용한 인터랙티브 미디어 아트</p>
<p align="middle">https://space4-u-client.vercel.app/space</p>
<p align="middle">
    WebGL </br>
    <img src="https://img.shields.io/badge/tech-ReactJS-blue" />
    <img src="https://img.shields.io/badge/tech-ThreeJS-lightgrey" />
    <img src="https://img.shields.io/badge/tech-NestJS-red" />
    <img src="https://img.shields.io/badge/tech-GraphQL-purple" />
    </br>
    </br> AI </br>
    <img src="https://img.shields.io/badge/tech-Tenserflow-orange" />
    <img src="https://img.shields.io/badge/tech-Keras-red" />
    <img src="https://img.shields.io/badge/tech-Sklearn-blue" />    
    </br>
    </br> OpenCV </br>
    <img src="https://img.shields.io/badge/tech-Librosa-purple" />
    <img src="https://img.shields.io/badge/tech-pygame-green" />
    
</p>

## Exhibition Process
<img src="https://github.com/omizha/Space4U-client/blob/master/docs/img/ExhibitionProcess1.png?raw=true">
<img src="https://github.com/omizha/Space4U-client/blob/master/docs/img/ExhibitionProcess2.png?raw=true">


# MusicMoodRecognition

![image](https://github.com/FW2022/MusicMoodRecognition/blob/main/Pic/Diagram_MusicMoodRecog.jpg)

Music Mood Recognition은 입력받은 건반음을 5가지의 무드(분위기) 중 하나로 분류하고, 분류된 무드로 저장되어있는 Spotify 플레이리스트 중 하나를 랜덤으로 틀어주는 프로그램이다.

# 2022년 숭실대학교 글로벌미디어학부 졸업작품전시회 출품작

본 기술은 숭실대학교 글로벌미디어학부 2022년 졸업작품전시회 FROM_PROM의 출품작에 쓰였다. 컬러테라티 색채 심리검사, 미니어처 배치를 통한 놀이치료검사, 피아노 건반을 통한 음악치료검사 3개의 단계 중에 마지막 3단계에 적용됐다.

## 필요한 Open Source
 - Pygame.midi
 - Pygame
 - Python >=3.7
 - spotipy
 - heartpy
 - Librosa


## 현재 단계
 - 2022년 3월 30일 현재, Librosa를 통한 MFCC, Energy 등의 std, mean, min, max와 Spotify에서 기본적으로 제공하는 tempo, speechiness, loudness, danceability, acousticness, instrumentalness 등을 결합하여 5가지 Mood(Happy, Sad, Romance, Relaxing, Dark)로 곡을 분류할 수 있다.
 - 또한 해당 5가지 Spotify 플레이리스트 중 선택된 플리의 곡 하나를 랜덤으로 재생할 수 있다.
 
 (Spotify Happy Playlist : https://open.spotify.com/playlist/2mu4kG7W1LVjDh8SsxZBLF)
 
 (Spotify Relaxing Playlist : https://open.spotify.com/playlist/37i9dQZF1DWVFeEut75IAL)
 
 (Spotify Romance Playlist : https://open.spotify.com/playlist/37i9dQZF1DX4s3V2rTswzO)
 
 (Spotify Sad Playlist : https://open.spotify.com/playlist/37i9dQZF1DXbm0dp7JzNeL)
 
 (Spotify Dark Playlist : https://open.spotify.com/playlist/37i9dQZF1DWSw8liJZcPOI)
 
 ![image](https://github.com/FW2022/MusicMoodRecognition/blob/main/Pic/MusicMoodClassify.png)
 ![image](https://github.com/FW2022/MusicMoodRecognition/blob/main/Pic/MusicMoodClassify2.png)
 
 Dark나 Sad의 Mood 같은 경우에는 훈련과 테스트 모두 같은 Mood로 분류가 잘되는 데에 반해, Happy, Romance, Relaxing은 분류가 잘못되는 경우가 있다. 특히 Relaxing의 경우에는 Happy, Romance, Dark 등으로 다양하게 분류되는 경우가 많았다. 
 
 ## 추가 계획
 - Galaxy Fit에서 추출한 데이터를 Smart Phone의 Samsung Health에서 csv 내보내기를 하여 Heart Rate를 측정할 수 있다. 이 Heart Rate를 건반음의 Tempo로 설정하여 곡을 만들고자 한다.
 - 그러나 현재, Samsung Health에서 csv 파일 내보내기와 csv 파일 최상단 1열을 자동으로 지워주는 프로그램이 요구된다.
 

## Contributors
<table>
  <tr>
    <td align="center">
    <a href="https://github.com/Junst">
        <img src="https://avatars.githubusercontent.com/u/30133053?v=4" width="150px;" alt=""/>
        <br />
        <sub>
            <b>< 고준영 ></b>
            <br />
            음악 분류 모델 개발 <br />
            미니어처 분류 모델 개발
        </sub>
    </a>
</td>
    <td align="center">
        <a href="https://github.com/omizha">
            <img src="https://avatars.githubusercontent.com/u/4525704?v=4?s=100" width="150px;" alt=""/>
            <br />
            <sub>
                <b>< 하정훈 ></b>
                <br />
                WebGL 인터랙티브 웹 개발 <br />
                인공지능 파이프라인 서버 구축
            </sub>
        </a>
    </td>
    <td align="center">
    <a href="https://github.com/your-mistletoe">
        <img src="https://avatars.githubusercontent.com/u/84714861?v=4" width="150px;" alt=""/>
        <br />
        <sub>
            <b>< 박다인 ></b>
            <br />
            퍼지 추론 시스템 개발 <br />
            전시 연출 및 굿즈 디자인
        </sub>
    </a>
</td>
</table>
