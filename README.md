# Easy Portable Chrome 1.0 for window

## 구성 요소

`start_easy_portable_chrome.bat` : 설치된 크롬을 가져와서 포터블 크롬으로 만듭니다.

`start_portable_chrome.bat` : 포터블 크롬을 실행합니다.

## 사용 방법

`start_easy_portable_chrome.bat`를 실행하면 C 드라이브 기본 경로에 설치된 크롬 감지합니다.

설치된 크롬을 Portable Chrome에 가져오겠습니까? [y/n] : y를 선택하면 현재 디렉토리로 가져올 수 있습니다.

`start_portable_chrome.bat`를 통해 포터블 크롬을 실행할 수 있습니다.

여기에서 주의해야할 점은 `User Data` 디렉토리가 포터블 크롬의 프로필 정보 및 히스토리를 모두 포함합니다. 절대로 삭제하지 마세요.

## 2024.10.06 ver 1.0

### Ver Log

윈도우 전용입니다.

간단하게 개발했습니다. 불안정하여 어떤 문제가 발생할 수 있으니 이 점은 감수해야 합니다.

### 예외 처리

- Chrome이 설치되지 않는 경우
- 시스템 폴더(system32, SysWOW64)로 경로가 잡히는 경우
- 크롬이 설치된 폴더로 경로가 잡히는경우
