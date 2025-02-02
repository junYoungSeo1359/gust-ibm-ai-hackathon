#  Python 개발 환경 설정:

이 섹션에서는 향후 실습에 사용할 개발 환경을 설정합니다. 여기에는 다음과 같은 내용이 포함 됩니다.
이 환경은 향후 python을 사용하는 모든 실습에서 동일하게 사용됩니다. 개별 실습내에 별도의 실행환경 설정 내용이 포함되어 있고 그 내용이 중복되는 경우 이 섹션의 내용이 우선 합니다.


## 1. Python 실행 환경 만들기

Python 실행 환경은 python을 설치하고 내장 모듈인 venv를 사용해서 만든다.

### 1-1. Python 설치하기
이 교육 과정의 소스코드는 Python 3.12.5 기준으로 작성되어 있으나 3.12.x 버전과 호환된다. 현재 실습용 서버에는 Python 3.9.12가 설치되어 있지만 여기서는 3.12.5를 추가로 설치한 후에 기본 python 명령이 3.9.12가 아니라 3.12.5를 가리키도록 수정해 준다. 

#### Step1
실습용 서버에서 Terminal 창을 실행 한 후 다음 명령으로 python 3.12를 설치한다. 
```
sudo dnf install python3.12
```
passsword를 물어보는 경우 user01의 password를 입력한다.

#### Step2

아래 두 명령을 실행한다.
``` 
sudo alternatives --install /usr/bin/python python /usr/bin/python3.12 1
sudo alternatives --set python /usr/bin/python3.12
```
그런 후 아래 명령을 실행해서 python version을 확인한다.
```
[user01@virtualserver02 ~]$ python -V
Python 3.12.5
```

### 1-2. Usecase 실습을 위한 가상환경 만들기

#### Step1
Terminal 창에서 user01 사용자 홈 디랙토리에서 다음 명령으로 myenvs 라는 directory를 만든다.

```
mkdir ~/myenvs
````
그런 후에 다음 명령으로 myenvs 아래에 4가지 가상 환경을 생성한다.
```
[user01@virtualserver02 ~]$ python -m venv ~/myenvs/06-prompt
[user01@virtualserver02 ~]$ 
[user01@virtualserver02 ~]$ python -m venv ~/myenvs/07-app
[user01@virtualserver02 ~]$ 
[user01@virtualserver02 ~]$ python -m venv ~/myenvs/08-rag
[user01@virtualserver02 ~]$ 
[user01@virtualserver02 ~]$ python -m venv ~/myenvs/09-usercase
```
myenvs 아래에 네개의 directory가 만들어졌는지 확인한다.
```
[user01@virtualserver02 ~]$ ls -ltr ./myenvs/
합계 16
drwxr-xr-x. 5 user01 user01 4096  1월 27 12:15 06-prompt
drwxr-xr-x. 5 user01 user01 4096  1월 27 12:15 07-app
drwxr-xr-x. 5 user01 user01 4096  1월 27 12:15 08-rag
drwxr-xr-x. 5 user01 user01 4096  1월 27 12:15 09-usecase
[user01@virtualserver02 ~]$ 
```

#### Step2

06-prompt 가상 환경을 activation, deactivation 시켜서 제대로 생성되었는지 확인한다.
```
[user01@virtualserver02 ~]$ 
[user01@virtualserver02 ~]$ source ./myenvs/06-prompt/bin/activate
(06-prompt) [user01@virtualserver02 ~]$ 
(06-prompt) [user01@virtualserver02 ~]$ 
(06-prompt) [user01@virtualserver02 ~]$ python -V
Python 3.12.5
(06-prompt) [user01@virtualserver02 ~]$ 
(06-prompt) [user01@virtualserver02 ~]$ 
(06-prompt) [user01@virtualserver02 ~]$ deactivate
[user01@virtualserver02 ~]$ 
```

위 확인 과정을 07-app, 08-rag, 09-usecase에 대해서도 동일하게 수행한다.

