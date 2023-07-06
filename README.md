# Datescape
일상에서 벗어나 새로운 환경의 데이트 명소를 공유하는 서비스

# 👨‍💻 Information
### 서비스 소개
매번 똑같은 곳을 방문하고 똑같은 것을 먹다보면 일상이 지루해지기 마련입니다. 사람들은 자연스레 새로운 장소에 대한 정보를 얻고자 노력합니다. 하지만 너무나 많은 플랫폼과 정보의 양으로 인해 오히려 선택의 어려움을 겪습니다. 그래서 저희는 한 곳에서 다양한 정보를 얻을 수 있는 서비스를 제공하고자 하였습니다.
데이트스케이프는 자신이 방문한 명소를 리뷰할 수 있을 뿐만 아니라 다른 이들의 리뷰들을 보고 다양한 이모티콘을 활용해 소통하며 새로운 정보를 얻을 수 있습니다.
+ 소셜 로그인으로 회원가입의 번거로움을 줄였습니다.
+ 지도 api 사용으로 보다 쉽게 위치를 검색하고 명소에 대한 소개 글을 작성할 수 있습니다.
+ 대표 사진과 여러 장의 추가 사진으로 해당 명소를 소개할 수 있습니다.
+ 알림 기능으로 내가 접속하지 않았을 때 작성된 글과 댓글을 쉽게 확인할 수 있습니다.
+ 이모티콘 구매와 판매로 부가적인 수익창출이 가능합니다.
+ 스케줄러 사용으로 매일 추천 태그가 변경됩니다.
+ 신고(유저, 게시글, 댓글) 기능으로 불편한 글과 부적절한 글은 신고 후 관리자의 확인으로 접근금지 처리가 가능합니다.


### 팀 >_water💦
- 박종민 /[github](https://github.com/jmpop97), [blog](https://jmpop.tistory.com/)
  - 리더
  - 서버 배포
  - docker
  - throttling
  - 신고기능구현(유저,게시글,댓글)


- 박혜린 /[github](https://github.com/HyerinPark1998), [blog](https://hr1998.tistory.com/)
  - Articles 관련 메인 페이지 작업
  - tag 별로 메인 페이지 정렬
  - 게시글 관련 검색 기능 구현
  - 내 위치 기준으로 주변에 저장된 명소 보기 구현


- 유혜민 /[github](https://github.com/Namunllvo), [blog](https://yump.tistory.com/)
  - 회원가입(이메일 인증), 로그인, 로그아웃, 회원 탈퇴 기능 구현
  - 소셜 로그인 기능 구현 4종(카카오, 네이버, 구글, 깃허브)
  - 아이디 찾기, 비밀번호 변경, 재설정 구현
  - 프로필 수정 구현


- 이현식 /[github](https://github.com/hyeon5819), [blog](https://velog.io/@hyeon5819)
  - 이모티콘(CRUD, 신청/구매/제작자별 조회, 신청 승인시 이메일 알림)
  - 관리자 페이지(누적 판매량/월별 판매량 조회, 판매상태별 조회, 판매상태 수정)
  - PG사 결제 연동(포트원)
  - 댓글 / 대댓글(CRUD, 이모티콘 사용 기능, 댓글 좋아요)
  - 프론트 태그 입력 및 전달 data 처리
  - 게시글 북마크 기능
  - 게시글, 댓글, 이모티콘 알림 기능


- 최진규 /[github](https://github.com/kyuparfum), [blog](https://kyuparfum.tistory.com/)
  - Articles 작업 게시글(front, back) CRUD 작업
  - 지도 api(카카오, 네이버) 사용
  - 지도로 주소 받는 부분 작업
  - 주소 검색으로 게시글에 주소 입력(back, front) 작업
  - 전반적인 css 작업
  - 마이페이지(게시글 댓글 북마크 연결(front, back) 작업)
  - 평점별 게시글 리스트 분류



### 개발 기간
22.06.05(월) ~ 

### 개발 환경
- `Python 3.10.6`
- `django-rest-framework`
- `git`

### 배포 환경..도 적을까요?


# 📌 Features
- [공통모델](#공통모델)
- [유저](#유저)
- [게시글 및 댓글](#게시글-및-댓글)
- [이모티콘](#이모티콘)
- [신고](#신고)
- [알림](#알림)


## 공통모델
  - DB에 저장된 데이터를 즉각 삭제하는 방법이 아닌 삭제 상태 값을 변경하여 관리할 수 있도록 작성됐습니다.
    사용자에 의한 복구요청에 대응할 수 있으며 추후 기간설정을 통한 DB관리까지 고려하여 채택했습니다.
  - 전체 모델에 적용될 필드를 공통 모델에 작성한 후 이를 상속받아 모델작성을 진행했습니다.


## 유저
### 로그인 및 회원가입
- 로그인(JWT), 로그아웃(BLACKLIST)
- 일반 회원가입
  - 이메일 인증
  - 아이디찾기
  - 비밀번호 재설정
- 소셜 간편로그인
  - 네이버, 카카오
  - 구글, 깃허브
- 프로필 정보 수정
  - 닉네임
  - 프로필 사진
  - 일반회원 비밀번호 변경
- 회원탈퇴(계정 비활성화)
- throttling
  - 1/second throttling
  - 4/second not_active
  - 4/10second not_active




## 게시글 및 댓글
### 게시글 CRUD
- 다중 이미지, 태그, 지도검색 포함한 게시글 작성
- 게시글 수정, 삭제 기능
- 메인 페이지에 태그별로 게시글 리스트 호출
- 태그 사용으로 게시글 리스트 호출
- 게시글 북마크 설정 가능
- 

### 댓글 대댓글 CRUD
- 댓글/대댓글 작성시 이모티콘 사용 가능
- 댓글 좋아요 기능

### 검색
- 전체, 게시글, 태그, 주소, 글작성자 검색

### 페이지네이션
- django rest-framework PageNumberPagination

### 내 주변 명소
- 사용자의 위치를 기준으로 반경 nKm 내에 있는 데이터들 불러오기

## 이모티콘
### 이모티콘 CRUD
- 클라이언트-서버간의 수익모델로써 이모티콘 제작시 최초 신청상태 적용, 승인 이전까지 수정 및 삭제요청 가능
- 신청 승인 이후 상품화로 간주하여 상품 수정 및 삭제요청 불가
- 이미지 용량에 따른 가격 책정방식 채택


### 이모티콘 결제
- PG사 테스트 결제 연동(포트원)
- 구매시 구매리스트 DB추가
  - 결제 진행이 요구됨에 따라 결제시 받게되는 uid값을 사용
  - 프론트: 결제시 포트원으로부터 받는 uid값을 서버측에 전달
  -   백  : 전달받은 uid값을 사용하여 포트원 결제조회 API요청, 응답내용 검증 후 지불완료 상태인 경우 구매리스트 DB추가

## 신고
### 카테고리별 신고기능
- 신고시 카테고리 기능
  - 프론트에서 카테고리 수정가능
  - 카테고리 안에 카테고리 가능


## 알림
- 작성 게시글에 대한 댓글 / 작성 댓글에 대한 대댓글 / 이모티콘 신청 승인 3가지에 대한 알림기능
- 댓글과 대댓글 생성시 타겟 유저가 본인이 아닌 경우 알림 DB 생성
- 이모티콘 신청 승인시 제작자에 대한 알림 DB 생성
