# Node.js 애플리케이션을 위한 이미지 선택
FROM node:20-alpine

# 앱 디렉토리 생성
WORKDIR /usr/src/app

# 의존성 설치
COPY package*.json ./
RUN npm install

# 앱 소스 추가
COPY . .

# 앱 실행
CMD ["node", "index.js"]
