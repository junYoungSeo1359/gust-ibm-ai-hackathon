
## Windows 사용자 
Windows 사용자는 PowerShell을 admin으로 권한으로 실행하고 다음 명령어를 실행합니다.
```bash
Set-ExecutionPolicy Unrestricted


```
A를 입력하고 엔터

## python 가상환경 생성
VS-Code에서 Terminal > New Terminal 선택 

cloud-native-gen-ai-enablement를 선택합니다.

```bash
python -m venv .venv 
.venv/Scripts/activate
 
python -m pip uninstall pyzmq 


pip install pyzmq==25.1.2

python -m pip install --upgrade pip
```

# virtualenv 

