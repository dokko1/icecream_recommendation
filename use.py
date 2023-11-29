import streamlit as st
import pandas as pd

def next_page():
    st.session_state.page += 1

def back_page():
    st.session_state.page -= 1

def start_page():
    st.session_state.page = 1

# 1페이지
def main_screen():
    st.title('Baskin Robbins 32🍦🍧')
    st.image("https://drive.google.com/uc?export=view&id=1k1jXAWwkUg-U9uBHbQQuAMzl_BM9ZFOY", width=432)
    st.subheader("시작 버튼을 눌러주세요.")

    if st.button('👉 시작'):
        next_page()

# 기존메뉴 이미지 주소 딕셔너리 
options_with_images = {
    "도라에몽의 팥붕! 슈붕!":"https://www.baskinrobbins.co.kr/upload/product/1752137961.png",
    "둘세 데 레체" : "https://www.baskinrobbins.co.kr/upload/product/1733881175.png",
    "나는 딸기치오" : "https://www.baskinrobbins.co.kr/upload/product/1739109691.png",
    "엄마는 외계인" : "https://www.baskinrobbins.co.kr/upload/product/1528197022.png",
    "아몬드 봉봉" : "https://www.baskinrobbins.co.kr/upload/product/1452062933.png",
    "뉴욕치즈케이크" : "https://www.baskinrobbins.co.kr/upload/product/1530775918.png",
    "핑크 베리 하츄핑" : "https://www.baskinrobbins.co.kr/upload/product/1720614645.png",
    "레인보우 샤베트" : "https://www.baskinrobbins.co.kr/upload/product/1530778136.png",
    "슈팅스타" : "https://www.baskinrobbins.co.kr/upload/product/1530775807.png",
    "사랑에 빠진 딸기": "https://www.baskinrobbins.co.kr/upload/product/1530779443.png",
    "오레오 쿠키 앤 크림" : "https://www.baskinrobbins.co.kr/upload/product/1670827140.png",
    "31 요거트" : "https://www.baskinrobbins.co.kr/upload/product/1530778368.png",
    "바람과 함께 사라지다" : "https://www.baskinrobbins.co.kr/upload/product/1530777439.png",
    "바닐라" : "https://www.baskinrobbins.co.kr/upload/product/1530775244.png",
    "이상한 나라의 솜사탕" : "https://www.baskinrobbins.co.kr/upload/product/1670827275.png",
    "그린티" : "https://www.baskinrobbins.co.kr/upload/product/1670827328.png",
    "치즈나무숲" : "https://i.namu.wiki/i/VOiGfj1FfoUlNj42PXfNX8ICHl-q-PxEqQ2O-t2UVo1z4WeCx59HVi_NyKyY14o9DCvYNcggMTgSGojGArS3gVL7jTczb6HMn780rYyvRH7AT0MxVrfRu4ucAR8WfhdWW5S33yk28b82CuZKJswEXtWuLQLtYoyl0dQ1MqmsC24.webp",
    "초콜릿" : "https://www.baskinrobbins.co.kr/upload/product/1530771632.png",
    "자모카 아몬드 훠지" : "https://www.baskinrobbins.co.kr/upload/product/1530775514.png",
    "마법사의 비밀 레시피" : "https://www.baskinrobbins.co.kr/upload/product/1547103366.png",
    "초코, 우리 이제 헤이즐넛" : "https://www.baskinrobbins.co.kr/upload/product/1739109254.png",
    "민트 초콜릿칩" : "https://www.baskinrobbins.co.kr/upload/product/1670827206.png",
    "체리쥬빌레" : "https://www.baskinrobbins.co.kr/upload/product/1452062882.png",
    "베리베리스트로베리" : "https://www.baskinrobbins.co.kr/upload/product/1554261647.png",
    "초코나무숲" : "https://www.baskinrobbins.co.kr/upload/product/1720525374.png",
    "피스타치오 아몬드" : "https://www.baskinrobbins.co.kr/upload/product/1720525397.png",
    "알폰소망고" : "https://www.baskinrobbins.co.kr/upload/product/1467791176.png",
    "쫀떡궁합" : "https://i.namu.wiki/i/VOiGfj1FfoUlNj42PXfNXyFYvEkHtWWxRBV58YvT6TWS1XMvrA12GDQ0aPV70KTOx2U_NgBtxLUdKkGorBA0axLfBcFSWWLfflbPfVVcyHrO406JBdkS-vnZ2spBwYlwSk4T9QGx0SgLUlaIvOoX7ER2q0Ts6N21uimh8vxr9Lg.webp",
    "밤이 옥수로 맛있구마" :"https://i.namu.wiki/i/VOiGfj1FfoUlNj42PXfNXzEsH_Pzpn9GLYf8O_SvCQneaqSpRWdACjp-CXXj2TkG5OurHpPbgltISt5KtzJEUie1S9acgP6YUQ31ew6NO09r5nD-597EWpBKmqiXUEFBsCwg3W4-Ib8utoJpnkOCyMJnwve4DZ5KkM3RbJ1N-dk.webp",
    "아빠는 딸바봉" : "https://i.namu.wiki/i/VOiGfj1FfoUlNj42PXfNXypXgZyHFaOiSgeHKZq6p7ac0hIIPjzBsxdF74t081Cs_aIiyOGWX3WX_LlNLMhOc-X9uLnM82Ef6aBRYnaKVCdzIHL_fMH5sqUD9v31e__E0Q_GsvJ5tRYDK83YjyxqulgnFd6Z9cYXkolWf-hVx-4.webp",
    "피카피카피카츄" : "https://i.namu.wiki/i/VOiGfj1FfoUlNj42PXfNXyCkJs9DqGKL-B9PIuICFk1iu14xwsUo3W-z2dDUcV5o-QrudRoWk6M3fVHWhHr_SmFiouNyboQnrHzJmlE-ASTjbfxf2GDoaebbF37NP_a_o0-oMI5jy3G4ZYs9beLj0Q5HWe7FCdXD660GYlSRXR8.webp"
}

# 원재료 딕셔너리
options_with_ingredient = {
    "도라에몽의 팥붕! 슈붕!":['custard', 'redbean'],
    "둘세 데 레체" : ['caramel','milk'],
    "나는 딸기치오" : ['pistachio', 'strawberry'],
    "엄마는 외계인" : ['chocolate', 'vanilla'],
    "아몬드 봉봉" : ['almond', 'chocolate', 'vanilla'],
    "뉴욕치즈케이크" : ['hwangcheese', 'vanilla'],
    "핑크 베리 하츄핑" : ['milk', 'strawberry','raspberry'],
    "레인보우 샤베트" : ['orange', 'pineapple', 'raspberry'],
    "슈팅스타" : ['blueberry', 'cherry', 'vanilla'],
    "사랑에 빠진 딸기": ['chocolate', 'hwangcheese', 'strawberry', 'vanilla'],
    "오레오 쿠키 앤 크림" : ['oreo', 'vanilla'],
    "31 요거트" : ['yogurt'],
    "바람과 함께 사라지다" : ['blueberry', 'strawberry', 'vanilla'],
    "바닐라" : ['vanilla'],
    "이상한 나라의 솜사탕" : ['cottoncandy','milk','custard'],
    "그린티" : ['matcha','milk'],
    "치즈나무숲" : ['chocolate', 'hwangcheese','matcha'],
    "초콜릿" : ['chocolate'],
    "자모카 아몬드 훠지" : ['almond', 'mocha','chocolate'],
    "마법사의 비밀 레시피" : ['chocolate', 'mint'],
    "초코, 우리 이제 헤이즐넛" : ['chocolate', 'hazelnut'],
    "민트 초콜릿칩" : ['chocolate', 'mint'],
    "체리쥬빌레" : ['cherry','milk'],
    "베리베리스트로베리" : ['matcha', 'strawberry'],
    "초코나무숲" : ['chocolate', 'matcha'],
    "피스타치오 아몬드" : ['almond', 'matcha', 'pistachio'],
    "알폰소망고" : ['mango', 'milk'],
    "쫀떡궁합" : ['blacksesame', 'injeolmi','pecan'],
    "밤이 옥수로 맛있구마" : ['montblanc', 'corn','sweetpotato'],
    "아빠는 딸바봉" : ['strawberry', 'vanilla'],
    "피카피카피카츄" : ['banana', 'chocolate','custard']
}

# 유사도 높은 재료 딕셔너리 만들기 (ingredient파일을 use.py가 있는 폴더에 함께 넣어주기)
options_with_new_ingredient=dict()
similar_df=pd.read_csv('ingredient_final.csv', index_col=1)
similar_df.drop('Unnamed: 0', axis=1, inplace=True)
for i in range(len(similar_df['new_ingredient'])):
    string=similar_df.iloc[i,1]
    clean_string=string.replace("[", "").replace("]", "").replace("'", "")
    result_list = clean_string.split(", ")
    options_with_new_ingredient[similar_df.index[i]]=result_list

# 신메뉴 이미지 주소 딕셔너리 (구글드라이브)
options_with_new_images = {
    "도라에몽의 팥붕! 슈붕!":"https://drive.google.com/uc?export=view&id=1XvGB1STSuysQ9VFc1mZ0mZOxMQlrymBH",
    "둘세 데 레체" : "https://drive.google.com/uc?export=view&id=1Z-crolDJngm_xK9NUbgIc42f_4t-uyMa",
    "나는 딸기치오" : "https://drive.google.com/uc?export=view&id=1-FLzIl2wCG99Me9fDIXpDsyS4S3G8fff",
    "엄마는 외계인" : "https://drive.google.com/uc?export=view&id=1kLlMUDvwsBAZZB_0jhRoDvSZB9hW4wfe",
    "아몬드 봉봉" : "https://drive.google.com/uc?export=view&id=1F2GgB4O71hWwo5_8Kl6inkuAUoi5SZdN",
    "뉴욕치즈케이크" : "https://drive.google.com/uc?export=view&id=12apeV0fq1ZxGAFBAURBbGaimrrVnfxUb",
    "핑크 베리 하츄핑" : "https://drive.google.com/uc?export=view&id=14TTk8shWF3GE7bMIUAOHb6SVUtiYmnqt",
    "레인보우 샤베트" : "https://drive.google.com/uc?export=view&id=13Er5THlZXRjPq9VC1RObkH86LIp5iJjW",
    "슈팅스타" : "https://drive.google.com/uc?export=view&id=1F5VzHvDuNf5SV_S5S_O2Xs2AE_KHnCpZ",
    "사랑에 빠진 딸기": "https://drive.google.com/uc?export=view&id=1iaB7E0yk68km0uh1zNcYsyFIMe-hrmdH",
    "오레오 쿠키 앤 크림" : "https://drive.google.com/uc?export=view&id=1jBZJAv6K_EWDcFFRht7TBTxtd2xc5ct8",
    "31 요거트" : "https://drive.google.com/uc?export=view&id=1TWVifCcoZsZXTSCFujhPHNFZNe26qQPG",
    "바람과 함께 사라지다" : "https://drive.google.com/uc?export=view&id=1XiViuHrJVJhrSeaCaGs477HmPU8yZq-p",
    "바닐라" : "https://drive.google.com/uc?export=view&id=1_cld3I3tWSkN4bh8m1xLvvQ4L3cImXvz",
    "이상한 나라의 솜사탕" : "https://drive.google.com/uc?export=view&id=1etmJbLhtIHNKrV9xLT_s_lBwof3kAbYw",
    "그린티" : "https://drive.google.com/uc?export=view&id=1DdRsT2zHCtuLFQuQdGO65VM7hyp2jDa7",
    "치즈나무숲" : "https://drive.google.com/uc?export=view&id=1yWh__fBgvpJkMH-JBivheKV0ePfaUliM",
    "초콜릿" : "https://drive.google.com/uc?export=view&id=1z4GnYAu7Q-4moURYA4-91Gy9mY2JYfI2",
    "자모카 아몬드 훠지" : "https://drive.google.com/uc?export=view&id=1mSwlgPIN6cVmIOV1dfqIUYQyiszr3Nb6",
    "마법사의 비밀 레시피" : "https://drive.google.com/uc?export=view&id=1B2EUA6d6kXlxJlug5xapgwOdIrsPWYdt",
    "초코, 우리 이제 헤이즐넛" : "https://drive.google.com/uc?export=view&id=1Odp2zZvVXVUiI0PBNfiMRrZdjiFJ9w-X",
    "민트 초콜릿칩" : "https://drive.google.com/uc?export=view&id=1SEktTi-Py54zj4ZThD67k4IsZRZBrQt6",
    "체리쥬빌레" : "https://drive.google.com/uc?export=view&id=1A80C7pzCr3U1QjAiI89E656oGK5XMHO7",
    "베리베리스트로베리" : "https://drive.google.com/uc?export=view&id=1Zgu3C_ldhLfLkjMfXceiaYy2kKyr9wlq",
    "초코나무숲" : "https://drive.google.com/uc?export=view&id=1dJEJve46VO-SebZSLx_lpyz_vh3z-rAY",
    "피스타치오 아몬드" : "https://drive.google.com/uc?export=view&id=14vAP4UXZ7thPl8xo06YzEUUBHBe_z5Zn",
    "알폰소망고" : "https://drive.google.com/uc?export=view&id=1IzG3a6RyHqEW9pRN-TPzEQDbkFX8i6ED",
    "쫀떡궁합" : "https://drive.google.com/uc?export=view&id=1So_RqKoGT62IQeU35ojCp8k_-TCDFAUJ",
    "밤이 옥수로 맛있구마" : "https://drive.google.com/uc?export=view&id=14RRfNLLUVEX-knNesbnMZeWruHbG0nGb",
    "아빠는 딸바봉" : "https://drive.google.com/uc?export=view&id=1lVYN00hwzqy144cOT_EmZPOGdZGtPFVo",
    "피카피카피카츄" : "https://drive.google.com/uc?export=view&id=13jWLttKBWF1CxC0ydlxt6uJol_lwXOaW"

}

# 신메뉴명 딕셔너리
new_names = {
    "도라에몽의 팥붕! 슈붕!" : "티타임 알몬드 블렌드",
    "둘세 데 레체" : "바나타치오 브라보",
    "나는 딸기치오" : "골든 드림 캐러멜 나이트",
    "엄마는 외계인" : "무화과에 바나나?",
    "아몬드 봉봉" : "골드피그나나",
    "뉴욕치즈케이크" : "꿀꿀한 헤이즐 피그",
    "핑크 베리 하츄핑" : "밤의 바나나 쉬폰",
    "레인보우 샤베트" : "그린 트리오 바나트",
    "슈팅스타" : '솔티쿠키팝 무화과',
    "사랑에 빠진 딸기": "바나헤몽의 퐁듀",
    "오레오 쿠키 앤 크림" : '무화과띠, 정신체리',
    "31 요거트" : '레몬셔벗',
    "바람과 함께 사라지다" :'무화과의 솔티한 밤' ,
    "바닐라" : '무화과',
    "이상한 나라의 솜사탕" : '더블얼그레이 무화과',
    "그린티" : '바나초콜릿의 숲',
    "치즈나무숲" : '바초헤누트 크림파이',
    "초콜릿" : '나는 바나나',
    "자모카 아몬드 훠지" : '바쑥이의 비밀',
    "마법사의 비밀 레시피" : '바나바나바날라',
    "초코, 우리 이제 헤이즐넛" : '치즈킥 바나나 러브',
    "민트 초콜릿칩" : '바나바나바날라',
    "체리쥬빌레" : '바나나크림드림',
    "베리베리스트로베리" : '초코밤멜로우',
    "초코나무숲" : '바나초콜릿의 숲',
    "피스타치오 아몬드" : '초코피스타치오봉봉',
    "알폰소망고" : '딸바스무디',
    "쫀떡궁합" : '사과팥당냥',
    "밤이 옥수로 맛있구마" : '피칸딸기피스타띠',
    "아빠는 딸바봉" : '밤에 빠진 무화과',
    "피카피카피카츄" :'바레그레이 프린세스'
}


# 2페이지 내용 
def select_icecream():
    col1, col2 = st.columns(2)

    with col1:
        st.title('BR 32🍦🍧')
        st.subheader('좋아하는 맛을 골라주세요.')

        selected_list=options_with_images.keys()

        selected_option = st.radio(
        '👇아이스크림 리스트',
        selected_list)

    with col2:
        for i in selected_list:
            if selected_option == i:
                # 공백 조절 때문에 넣은 것임
                st.text(" ") 
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.image(options_with_images[selected_option], caption=selected_option, use_column_width=True)
                st.write(i+"(을/를) 선택하셨습니다.")
                st.text(" ")
                st.write('##### ['+i+']의 원재료')
                for x in options_with_ingredient[i]: st.write('##### 👉'+ ' '+ x)
                st.text(" ")
    
        st.session_state.selected_option = selected_option
        if st.button('다음 (유사도 높은 새 재료 찾기)'):
            next_page()
        if st.button("시작 화면으로 돌아가기"):
            back_page()
        


# 3페이지 내용
def show_result():

    selected_ice_cream = st.session_state.selected_option


    st.title('🍦 선택 아이스크림 정보')
    st.image(options_with_images[selected_ice_cream], width=350)
    st.write(f'##### # {selected_ice_cream}')
    st.write('##### # 원재료')
    for x in options_with_ingredient[selected_ice_cream]: st.write('#####  👉'+ ' '+ x)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.title('🍦 새 재료 찾기')
    st.subheader('기존 원재료 ➡️ 코사인 유사도 기반 새 재료')
    st.text(" ")
    for i in range(len(options_with_ingredient[selected_ice_cream])):
        st.write('#### 👉 '+ options_with_ingredient[selected_ice_cream][i] +' → '+options_with_new_ingredient[selected_ice_cream][i])
    st.text(" ")
    st.text(" ")
    if st.button('다음 (새 재료로 새 메뉴 만들기)'):
        next_page()
    if st.button("이전으로 돌아가기"):
        back_page()

# 4페이지 내용
def result():
    selected_ice_cream = st.session_state.selected_option

    # 새로운 아이스크림 사진 가져오기
    for ice_cream, image_url in options_with_new_images.items():
        if ice_cream == selected_ice_cream:
            similar_icecream_image = image_url
            break
    
    st.title('🍦 유사도로 개발한 신메뉴')
    col1, col2, col3 = st.columns([4, 2, 4])

    with col1:
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.write('### [선택한 아이스크림]')
        st.write ('##### 👉 ' + selected_ice_cream)
        st.image (options_with_images[selected_ice_cream], use_column_width=True)
        for x in options_with_ingredient[selected_ice_cream]: st.write('######  #'+ ' '+ x)
        


    with col2:
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.markdown('<div style="display: flex; justify-content: center;"><h1 style="font-size:30px;">➡️</h1></div>', unsafe_allow_html=True)

    

    with col3:
        # new_name에 새로운 아이스크림 명 저장
        if selected_ice_cream in new_names:
            new_name=new_names[selected_ice_cream]
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.write('### [새로운 아이스크림]')
        st.write ('##### 👉 ' + new_name)
        st.image (options_with_new_images[selected_ice_cream], use_column_width=True)
        for x in options_with_new_ingredient[selected_ice_cream]: st.write('######  #'+ ' '+ x)
        st.text(" ")
        st.text(" ")
        if st.button("종료(시작 단계로 돌아가기)"):
            start_page()
        if st.button("이전으로 돌아가기"):
            back_page()
        

    



# st.session_state 초기화
if 'page' not in st.session_state:
    st.session_state.page = 1

# 페이지 전환
if st.session_state.page == 1:
    main_screen()
elif st.session_state.page == 2:
    select_icecream()
elif st.session_state.page == 3:
    show_result()
elif st.session_state.page == 4:
    result()