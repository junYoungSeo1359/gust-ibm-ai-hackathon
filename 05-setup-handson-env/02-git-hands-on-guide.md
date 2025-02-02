# Git Hands-on 가이드

## 교육 일정
- 교육 시간: 1일
- 오전 세션: 09:30 ~ 11:30
- 오후 세션: 13:00 ~ 17:30

## 세션 1: Git 기본 설정 (09:30 ~ 10:30)
### Git 설치 확인
```bash
git --version
```

### Git 초기 설정
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Git 설정 확인
```bash
git config --list
```

## 세션 2: 기본 Git 명령어 (10:30 ~ 11:30)
### 저장소 생성 및 초기화
```bash
mkdir git-practice
cd git-practice
git init
```

### README.md 파일 생성 및 첫 번째 커밋
```bash
echo "# Git 실습" > README.md
git add README.md
git commit -m "첫 번째 커밋: README.md 파일 생성"
```

## 세션 3: 변경 이력 관리 (13:00 ~ 14:30)
### README.md 파일 수정 및 커밋
```bash
echo "## Git 명령어 연습" >> README.md
git add README.md
git commit -m "두 번째 커밋: Git 명령어 섹션 추가"
```

### 변경 이력 확인
```bash
git log
git log --oneline
```

## 세션 4: Branch 관리 (14:30 ~ 15:30)
### 브랜치 생성 및 전환
```bash
git branch feature
git checkout feature
# 또는
git checkout -b feature
```

### README.md 파일 수정 (feature 브랜치)
```bash
echo "### 브랜치 실습" >> README.md
git add README.md
git commit -m "세 번째 커밋: 브랜치 실습 섹션 추가"
```

## 세션 5: Reset과 Revert (15:30 ~ 16:30)
### Reset 실습
```bash
# soft reset (커밋만 취소)
git reset --soft HEAD^

# mixed reset (스테이징 취소)
git reset --mixed HEAD^

# hard reset (변경사항 완전 삭제)
git reset --hard HEAD^
```

### Revert 실습
```bash
# 특정 커밋 되돌리기
git revert <commit-hash>
```

## 세션 6: GitHub 연동 (16:30 ~ 17:30)
### 원격 저장소 연결
```bash
git remote add origin https://github.com/username/repository.git
```

### 변경사항 Push
```bash
git push -u origin main
```

## 실습 예제: README.md 파일 변경 이력 만들기

### 1. 첫 번째 커밋
```markdown
# Git 실습
Git 기초 학습을 위한 저장소입니다.
```

### 2. 두 번째 커밋
```markdown
# Git 실습
Git 기초 학습을 위한 저장소입니다.

## Git 명령어
- git init: 저장소 초기화
- git add: 파일 스테이징
- git commit: 변경사항 커밋
```

### 3. 세 번째 커밋
```markdown
# Git 실습
Git 기초 학습을 위한 저장소입니다.

## Git 명령어
- git init: 저장소 초기화
- git add: 파일 스테이징
- git commit: 변경사항 커밋

## Branch 실습
브랜치를 사용하여 독립적인 작업 공간을 만들어봅니다.
```

## 유용한 Git 명령어 정리
- 상태 확인: `git status`
- 변경사항 확인: `git diff`
- 브랜치 목록: `git branch`
- 브랜치 삭제: `git branch -d <branch-name>`
- 변경사항 임시 저장: `git stash`
- 임시 저장된 변경사항 복원: `git stash pop`
