# MusicMoodRecognition

![image](https://github.com/FW2022/MusicMoodRecognition/blob/main/Pic/Diagram_MusicMoodRecog.jpg)

Music Mood Recognition은 입력받은 건반음을 5가지의 무드(분위기) 중 하나로 분류하고, 분류된 무드로 저장되어있는 Spotify 플레이리스트 중 하나를 랜덤으로 틀어주는 프로그램이다.

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
 
 (Spotify Happy Playlist : https://open.spotify.com/playlist/)
 
 (Spotify Relax Playlist : https://open.spotify.com/playlist/)
 
 (Spotify Happy Playlist : https://open.spotify.com/playlist/)
 
 (Spotify Happy Playlist : https://open.spotify.com/playlist/)
 
 (Spotify Happy Playlist : https://open.spotify.com/playlist/)
 
 ![image](https://github.com/FW2022/MusicMoodRecognition/blob/main/Pic/MusicMoodClassify.png)
 ![image](https://github.com/FW2022/MusicMoodRecognition/blob/main/Pic/MusicMoodClassify2.png)
 
 Dark나 Sad의 Mood 같은 경우에는 훈련과 테스트 모두 같은 Mood로 분류가 잘되는 데에 반해, Happy, Romance, Relaxing은 분류가 잘못되는 경우가 있다. 특히 Relaxing의 경우에는 Happy, Romance, Dark 등으로 다양하게 분류되는 경우가 많았다. 
 
 ## 추가 계획
 - Galaxy Fit에서 추출한 데이터를 Smart Phone의 Samsung Health에서 csv 내보내기를 하여 Heart Rate를 측정할 수 있다. 이 Heart Rate를 건반음의 Tempo로 설정하여 곡을 만들고자 한다.
 - 그러나 현재, Samsung Health에서 csv 파일 내보내기와 csv 파일 최상단 1열을 자동으로 지워주는 프로그램이 요구된다.
 
