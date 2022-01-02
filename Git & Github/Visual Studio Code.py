# control backtick ( ` ) 을 눌러서 터미널을 열 수 있음

# TIL => Today I Learned

# MD => Mark Down ( 개발자들의 문서 작성 양식 & 문법 )

# git init  =>  git initiation ( 특정 폴더를 깃으로 관리를 시작하겠다는 의미 )
# 중요 : 홈폴더에서는 이 명령어를 사용하지 않는다 ( git init )
# git init 을 치면 파일 옆에 U 라고 뜸. 이는 untracked 라는 의미
# 최초에 한번만 친다

# git status : 현재 상황을 알려줌 ( ex. untracked ). 매 단계마다 쳐보는게 좋음

# git add mulcam.txt : 분장실에서 무대로 올리는 것
# git add .  => 그 폴더 안에 있는 모든 파일들을 다 무대로 올림

# git commit -m '커밋메세지' : 메세지를 작성하여 무대에서 사진촬영저장소로 가는 것
#                            주로 변동사항을 메세지로 작성함

# touch => '파일'을 만듬
# ex. touch a.txt => a라는 이름의 text파일을 만든다

# mkdir => '폴더'를 만듬 ( = make directory )

# git log  =>  어떤 과정이 지나갔는 지 보여줌

# rm => 파일을 지울 때는 rm a.txt
#    => 폴더를 지울 때는 rm -r test
# rm *.txt => txt확장자를 가지고 있는 모든 파일을 지움
# rm -rf * => 이 폴더안에 있는 모든 파일을 싹 다 지움.  f = force ( 강제로 )
# * = 에스터레스크 ( git에서는 all을 의미 )

# notion은 마크다운 문법을 지원하는 웹 형태의 서비스 에디터
# notion에서 " / " 누르면 어떤 기능을 지원해주는지 확인할 수 있음

# git config --global --user.name"이름"
# git config --global user.email"이메일"

# 1. git init
# 2. git add a.txt / git add .
# 3. git status  => on branch master 확인한다
#                   ls -a를 쳐서 .git 을 확인한다
# 4. git commit -m 'message'
# 5. git log / git log --oneline ( 한 줄로 로그 변화를 보여줌 )
# 수정하고나서는 반드시 save하고 넘어가야함

# gitbash에서 code . 입력하면 그 폴더의 vs code 가 열림

# config의 뜻은 configuration으로 git의 환경 설정과 관련된 정보를 저장하는 겁니다.
# 그래서 user.name이나 user.email같이 작성자에 대한 설정 정보를 git config로 저장해준다고
# 생각하시면 됩니다

# 항상 수정을 하고 나면 ctrl s 로 save 하기

#주의 : git commit 메시지를 안적은 경우는 -> VIM 에디터가 열리게 됩니다.
# i -> insert 모드로의 변경 => 끼워넣기
# 메시지를 직접!! 수정하시고
# esc -> insert 모드를 종료해 주시고
# :wq
# -> 메시지가 정상적으로 적히게 됩니다.

# git checkout 해쉬번호 : 해쉬번호 과정으로 돌아가보는 것
# git checkout master : 다시 현재 상태로 되돌아옴

# git config --global --list : 확인용
# git config --global user.name "clock18" : 설정용
# git config --global user.email "clock4772@gmail.com" : 설정용
# git config --global --unset user.email : 삭제용
# git config --global --unset user.name : 삭제용

# local 이 붙으면 내 컴퓨터 안에서 활동하는 것

# git remote add origin : 멀리 잇는 주소를 등록합니다

# 1. git remote add origin https://github.com/clock18/lifecycle.git
# 2. git remote -v : 긁어 온 주소 확인
# 3. git push origin master : 자격 증명

# touch README.md : typora 파일 생성

# gitignore  =>  올리기 싫은 파일이나 폴더를 지정하면 허브에 올라가지 않고
#                깃의 추적을 피하고 싶을 때 작성한다. ex. touch .gitignore
#                깃의 추적을 받기 전에 작성해야함.

# git clone 카피주소
# 1. 로컬에서 시작한다  => git init  => add commit  => 온라인으로 가서 방을 받고
#   주소를 받는다  => git remote add로 연결한다
# 2. 온라인에서 시작한다  => gitbash 에서 git clone 카피주소  =>
#    해당 클론 받은 곳에 폴더가 생기며
#    그 폴더는 이미 깃의 관리를 받고 있다
# git init과 git clone 은 한번만 작성하는 명령어이다.

# 셋팅  => 매니지 엑세스  => add people  => 상대방 깃허브 아이디 입력  =>
# 상대방은 메일에서 초대장 수락

# 올릴때는 git push origin master
# 받을때는 git pull origin master
# 수정할 때는 수정하고나서 git add, git commit -m 과정을 거친 후 git push

# push 에러가 떴을 때는 git pull origin master 입력
# 웹에서의 변화와 local에서의 변화가 일치하지 않을 경우 발생
# git pull origin master 입력했을 때 나오는 부분 중 필요없는 부분을 다 지우고 저장
# 그 다음 git add, git commit, git push origin master 순으로 입력하면 됨

# git branch 브랜치명 : '브랜치명' 브랜치를 생성
# git switch 이름 : '이름' 브랜치로 이동
# git branch : 현재 어떤 브랜치가 내 작업 공간에 있는 지 확인 (ls 같은거)
# git branch -D {브랜치 이름} : 삭제
# git merge 합칠브랜드명 : 지금 위치해있는 브랜드와 합칠브랜드를 결합함