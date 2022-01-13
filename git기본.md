## # git 

> 분산버전관리시스템 (DVCS)

## 1. git 저장소 만들기

``` bash
$ git init
Initialized empty Git repository in C:/Users/minjae/Desktop/startcamp/first/.git/

```

- `.git` 폴더가 생성 => 버전이 기록되는 저장소 
  - 해당 폴더를 지우게 되면 모든 버전이 삭제되니 주의! 
- `(master)` 기본버전  

## 버전 기록하기 

### `add` 

```bash
$ git add 파일명
$ git add a.txt
$ git add my_folder/
$ git add a.txt b.txt
```

### `commit` 

```bash
$ git commit -m '커밋메시지'
```

- 커밋 메시지는 항상 버전의 내용(변경사항)에 대해서 나타낼 수 있도록 기록하다. / 알수있게

### `status` 

```bash
$ git status

#  b 커밋할 변경사항들 (staging area)
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    b.txt
# a 커밋을 위해 준비되지 않은 변경사항 (working directory) 한번이라도 커밋된적이 있음
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt
# 트래킹 되지 않은 파일들 (working directory)  한번도 커밋된적이 없음 
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c.txt
 
```

- 파일을 조작하는 방법 4가지 
  - 생성 Create
  - 읽기 ~~Read~~
  - 수정 Update
  - 삭제 Delete

### git에서 관리하는 파일 변경사항 상태 

- untracked : 커밋에 포함된 적 없는 파일
- tracked
  - modified 커밋에 비해서 수정된 경우
  - staged 커밋 되기 전 목록 (staging area)
  - commited 커밋된 상태

```bash
선생님이 깃 이동 정리사항있음 

마지막부분 .git 하위폴더에 .git 해도되는데 꼬인다 /지금수준에서는 안된다고 생각하자
```











### `log` 

```bash
$ git log
```







### 

### 처음 git 할때    저자 확인

```bash
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

### git log  확인

```bash
$ git config --global -l
```

### 

추가 메모는 학습자료 다운 추가



​    

에러 커맨드 잘확인하기 /대부분 답이있음

​    

git에서 HEAD 는 시간상 위치를 알려줌 참고

​    

git restore 마지막 커밋 내용으로 되돌리기

​    

git restore --staged <file name>  파일을 add전 상태로 전환    

​    

fetch 가져오는거 

push  보내는거 

​    

git push origin master하면  커밋된 최신 버전(git log에 찍힌 버전) 올라감

​    

git clone  / .git밑 레포 복사

​    

git pull / 클론한주소 최신화

​    

​    

​    

!!!!!(브랜치개념추가)

fetch / 받아오기만한다

pull /   fetch + merge  (병합)

​    

​    

끈기 + 끊어서 생각 잘하자

cs50강의 듣기 강추~~~





git commmit --amend >>> .git  안에 파일 편집기들어가서 커밋(이름)을 바꿀수있다

!!!!! 하지만  고유 커밋코드40자리 (그역사? 저장한시간은)는 안바뀜

```bash
commit 53825522ebafcf156e016dcce45f042d49598f89 ##커밋 해시값

```

  즉  push 하고나서는  커밋이름을 바꾸지않는것이좋다  코드가 다르기때문에 공동작업에서 에로사항 생길수있다
