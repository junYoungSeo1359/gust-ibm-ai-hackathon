## requirements.txt 만들기

pip freeze > requirements.txt 

## llm 애플리케이션 컨테이너화 using docker

docker build 
```
# docker build -t 자신의 docker hub 계정/llm-app .
docker build -t nexweb1/llm-app .
```

docker를 사용하는 경우
```
docker run --name demo -d -p 8000:8000 -e API_KEY="..." -e PROJECT_ID="..." nexweb1/llm-app
```


## llm 애플리케이션 컨테이너화 using podman

podman build 
```
podman build -t nexweb1/llm-app .
```

podman을 사용하는 경우
```
podman run --name demo -d -p 8000:8000 -e API_KEY="opuyTeiQdISa-wLUaprGjc7Ko4N1aG651j4HVX0rUEPg" -e PROJECT_ID="d0b685b9-04b2-4d61-a957-c017b6fa3613" nexweb1/llm-app
```