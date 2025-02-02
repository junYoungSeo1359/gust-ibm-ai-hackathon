# Linux 핸즈온 가이드 (CentOS 9.0)

## 교육 개요
- 교육 시간
  - 오전: 09:30 ~ 11:30 (2시간)
  - 오후: 13:00 ~ 17:30 (4.5시간)
- 실습 환경: CentOS 9.0
- 대상: Linux 입문자

## 타임 테이블
| 시간 | 내용 |
|------|------|
| 09:30 - 10:00 | Linux 기초 개념 |
| 10:00 - 11:30 | 기본 명령어 실습 |
| 13:00 - 14:30 | 파일 시스템과 권한 관리 |
| 14:30 - 16:00 | vi 에디터 사용법 |
| 16:00 - 17:30 | 텍스트 처리와 프로세스 관리 기초 |

## Part 1: Linux 기초 개념 (09:30 - 10:00)

### Linux 디렉토리 구조
```plaintext
/     : 루트 디렉토리
/bin  : 기본 명령어
/boot : 부팅 관련 파일
/dev  : 장치 파일
/etc  : 설정 파일
/home : 사용자 홈 디렉토리
/lib  : 라이브러리
/tmp  : 임시 파일
/usr  : 응용 프로그램
/var  : 가변 데이터
```

## Part 2: 기본 명령어 실습 (10:00 - 11:30)

### 기본 탐색 명령어
```bash
# 현재 디렉토리 확인
pwd

# 디렉토리 내용 확인
ls
ls -l    # 상세 정보
ls -la   # 숨김 파일 포함
ls -lh   # 파일 크기 읽기 쉽게
ls -ltr  # 시간 역순 정렬

# 디렉토리 이동
cd /etc          # 절대 경로
cd ../test      # 상대 경로
cd ~            # 홈 디렉토리
cd ..           # 상위 디렉토리
cd -            # 이전 디렉토리
```

### 파일과 디렉토리 조작
```bash
# 디렉토리 생성
mkdir test
mkdir -p test1/test2   # 부모 디렉토리 포함 생성

# 파일 생성 및 보기
touch file.txt
echo "Hello" > file.txt    # 덮어쓰기
echo "World" >> file.txt   # 추가하기
cat file.txt
head -n 5 file.txt        # 앞 5줄
tail -n 5 file.txt        # 뒤 5줄
tail -f log.txt           # 실시간 로그 보기

# 파일/디렉토리 복사
cp file.txt file2.txt
cp -r test test_backup    # 디렉토리 복사

# 파일/디렉토리 이동/이름변경
mv file.txt newfile.txt
mv test test_new

# 파일/디렉토리 삭제
rm file.txt
rm -r test               # 디렉토리 삭제
rm -rf test              # 강제 삭제
```

## Part 3: 파일 시스템과 권한 관리 (13:00 - 14:30)

### 파일 권한
```bash
# 파일 권한 확인
ls -l file.txt

# 권한 형식
# r(읽기:4) w(쓰기:2) x(실행:1)
# 예: chmod 755 = rwxr-xr-x

# 권한 변경
chmod 644 file.txt
chmod u+x file.txt     # 소유자에게 실행 권한 추가
chmod g-w file.txt     # 그룹의 쓰기 권한 제거
chmod o-rwx file.txt   # 기타 사용자의 모든 권한 제거

# 소유자/그룹 변경
chown user:group file.txt
chown -R user:group directory  # 디렉토리 전체 변경
```

### 파일 시스템 관리
```bash
# 디스크 사용량 확인
df -h
du -sh *     # 현재 디렉토리 파일/폴더 크기
du -sh .[!.]* # 숨김 파일 포함
```

## Part 4: vi 에디터 사용법 (14:30 - 16:00)

### vi 기본 모드
1. 명령 모드 (기본)
2. 입력 모드 (i, a, o)
3. Ex 모드 (:)

### 기본 조작법
```plaintext
# 입력 모드 전환
i    # 현재 커서 위치에서 입력
I    # 현재 줄 맨 앞에서 입력
a    # 현재 커서 다음 위치에서 입력
A    # 현재 줄 맨 끝에서 입력
o    # 현재 줄 다음에 새 줄 추가
O    # 현재 줄 이전에 새 줄 추가

# 커서 이동
h    # 왼쪽
j    # 아래
k    # 위
l    # 오른쪽
w    # 다음 단어의 시작으로
b    # 이전 단어의 시작으로
^    # 줄의 시작으로
$    # 줄의 끝으로
gg   # 파일의 처음으로
G    # 파일의 끝으로

# 복사 및 붙여넣기
yy   # 현재 줄 복사
3yy  # 3줄 복사
p    # 현재 커서 다음에 붙여넣기
P    # 현재 커서 이전에 붙여넣기

# 삭제
x    # 현재 커서의 문자 삭제
dd   # 현재 줄 삭제
3dd  # 3줄 삭제
dw   # 단어 삭제

# 되돌리기/다시하기
u    # 되돌리기
Ctrl + r  # 다시하기

# 저장 및 종료
:w        # 저장
:q        # 종료
:wq or :x # 저장 후 종료
:q!       # 강제 종료
```

## Part 5: 텍스트 처리와 프로세스 관리 기초 (16:00 - 17:30)

### 텍스트 처리
```bash
# 파일 내용 검색
grep "error" log.txt
grep -i "ERROR" log.txt   # 대소문자 무시
grep -r "error" .         # 현재 디렉토리 하위 모든 파일 검색
grep -v "error" log.txt   # 패턴이 없는 줄 검색
grep -n "error" log.txt   # 줄 번호 표시

# 파일 내용 정렬
sort file.txt
sort -r file.txt          # 역순 정렬
sort -n file.txt          # 숫자 정렬

# 중복 제거
uniq file.txt
sort file.txt | uniq      # 정렬 후 중복 제거
sort file.txt | uniq -c   # 중복 횟수 표시

# 파일 비교
diff file1.txt file2.txt
```

### 프로세스 관리 기초
```bash
# 프로세스 강제 종료
kill -9 1234   # PID가 1234인 프로세스 강제 종료
```

## 유용한 단축키
- Ctrl + C: 현재 실행 중인 프로세스 중단
- Ctrl + Z: 프로세스를 백그라운드로 보내기
- Ctrl + D: 현재 셸 세션 종료
- Ctrl + R: 명령어 히스토리 검색
- Ctrl + L: 화면 지우기 (clear)

## 실무 팁
1. vi 에디터 사용 시 자주 저장하기
2. 파일 수정 전 백업하기
3. rm 명령어 사용 시 주의하기
4. 파일명에 공백 사용 피하기
5. 상대경로보다 절대경로 사용하기

## 참고 자료
- CentOS 공식 문서: https://docs.centos.org
- Vim 튜토리얼: vimtutor 명령어로 실행
