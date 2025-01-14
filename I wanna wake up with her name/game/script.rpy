define JunHo = Character("박준호", color="#000000", window_background=Transform(Image("gui/JunHo_text.png", xalign=0.5, yalign=0.5), zoom=0.6))
define Geonhee = Character("강건희", color="#000000", window_background=Transform(Image("gui/Geonhee_text.png", xalign=0.5, yalign=0.5), zoom=0.6))
define Heeseol = Character("심희설", color="#000000", window_background=Transform(Image("gui/Heeseol_text.png", xalign=0.5, yalign=0.5), zoom=0.6))
define Yeha = Character("진예하", color="#000000", window_background=Transform(Image("gui/Yeha_text.png", xalign=0.5, yalign=0.5), zoom=0.6))
define Sungjae = Character("조성제", color="#000000", window_background=Transform(Image("gui/Sungjae_text.png", xalign=0.5, yalign=0.5), zoom=0.6))
define system = Character("시스템", color="#000000", window_background=Transform(Image("gui/JunHo_text.png", xalign=0.5, yalign=0.5), zoom=0.6))
define info = Character("정보!", color="#000000", window_background=Transform(Image("gui/JunHo_text.png", xalign=0.5, yalign=0.5), zoom=0.6))

image main_bg = "gui/main_menu.png"
image campus = "images/campus.png"
image evening_campus = "images/evening_campus.png"
image calssroom = "images/classroom.png"
image department_store = "images/department_store.png"
image cafe = "images/cafe.png"
image beach = "images/beach.png"
image mansroom_night = "images/mansroom_night.png"
image sports_field = "images/sports_field.png"
image sports_field_evening = "images/sports_field_evening.png"
image bar = "images/bar.png"

image JunHo1 = "JunHo1.png"
image JunHo2 = "JunHo2.png"
image JunHo3 = "JunHo3.png"
image JunHo4 = "JunHo4.png"
image JunHo5 = "JunHo5.png"
image JunHo6 = "JunHo6.png"
image JunHo7 = "JunHo7.png"

image Geonhee = "Geonhee.png"
image Geonhee_happy = "Geonhee_happy.png"
image Geonhee_unhappy = "Geonhee_unhappy.png"

image Heeseol = "Heeseol.png"
image Heeseol_happy = "Heeseol_happy.png"
image Heeseol_unhappy = "Heeseol_unhappy.png"

image Yeha = "Yeha.png"
image Yeha_happy = "Yeha_happy.png"
image Yeha_unhappy = "Yeha_unhappy.png"

image Sungjae1 = "Sungjae1.png"
image Sungjae2 = "Sungjae2.png"
image Sungjae3 = "Sungjae3.png"
image Sungjae4 = "Sungjae4.png"

default love_Geonhee = 0
default love_Heeseol = 0
default love_Yeha = 0
default current_character = None
default dated_with = ""
define ending = 404

screen affection_display():
    if current_character == "Geonhee":
        frame:
            xalign 0.83
            yalign 0.03
            background None  # 배경 제거
            xsize 150  # 프레임 너비
            ysize 300  # 프레임 높이
            ypadding 10

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10

                hbox:
                    spacing 20
                    bar:
                        value VariableValue("love_Geonhee", 100)
                        xsize 240  # 막대 너비
                        ysize 40  # 막대 높이
                        yalign 0.5
                        left_bar Solid("#ff69b4")  # 핑크색
                        right_bar Solid("#ffffff")  # 빈 부분 흰색
                        thumb None  # 썸 제거
                    text "[love_Geonhee]%" size 40 color "#ff69b4" yalign 0.5 bold True

    elif current_character == "Heeseol":
        frame:
            xalign 0.83
            yalign 0.03
            background None
            xsize 150
            ysize 300
            ypadding 10

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10

                hbox:
                    spacing 20
                    bar:
                        value VariableValue("love_Heeseol", 100)
                        xsize 240
                        ysize 40
                        yalign 0.5
                        left_bar Solid("#ff69b4")  # 핑크색
                        right_bar Solid("#ffffff")  # 빈 부분 흰색
                        thumb None
                    text "[love_Heeseol]%" size 40 color "#ff69b4" yalign 0.5 bold True

    elif current_character == "Yeha":
        frame:
            xalign 0.83
            yalign 0.03
            background None
            xsize 150
            ysize 300
            ypadding 10

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10

                hbox:
                    spacing 20
                    bar:
                        value VariableValue("love_Yeha", 100)
                        xsize 240
                        ysize 40
                        yalign 0.5
                        left_bar Solid("#ff69b4")  # 핑크색
                        right_bar Solid("#ffffff")  # 빈 부분 흰색
                        thumb None
                    text "[love_Yeha]%" size 40 color "#ff69b4" yalign 0.5 bold True

screen affection_event(name, amount):
    modal False

    frame:
        xalign 0.5
        yalign 0.5
        #background None
        background Solid("#ffffffa5")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            add Image("gui/heart.png") align (0.5, 0.5) zoom 0.5
            text name + "의 호감도가 " + str(amount) + "만큼 상승!" size 54 color "#000000" xalign 0.5
    
    timer 2.0 action Hide("affection_event")

init python:
    config.overlay_screens.append("affection_display")

    def show_affection_event(name, amount):
        renpy.show_screen("affection_event", name=name, amount=amount)
        renpy.pause(2.3)
    
    def choose_ending(fin_Geonhee,fin_Heeseol,fin_Yeha):
        love = [fin_Geonhee, fin_Heeseol, fin_Yeha]
        max_love = max(love)
        if max_love < 100:
            return 404
        else:
            return love.index(max_love)

screen react_screen(react_function):
    button:
        background None
        action [
            Function(react_function),
            Hide("react_screen"),
            Return(True)
        ]

label eye_game:
    $ results = []
    $ rounds = 5
    $ flag = False

    show Sungjae1
    $ current_character = "Sungjae"
    system "야생의 조성제가 눈웃음을 시전했다!"
    system "눈웃음을 보고 빠르게 반응하지 못하면 매혹되고 말거야!"

    python:
        import random
        import time

        def react():
            if not timer_reacted[0]:
                timer_reacted[0] = True
                reaction_time = time.time() - start_time
                results.append(reaction_time)
                renpy.hide("Sungjae2")
                renpy.show("Sungjae1")

        for i in range(rounds):
            if flag:
                break

            wait_time = random.uniform(2, 5)
            renpy.pause(wait_time)

            renpy.hide("Sungjae1")
            renpy.show("Sungjae2")

            start_time = time.time()
            timer_reacted = [False]

            renpy.call_screen("react_screen", react_function=react)

            if results[-1]>0.7:
                flag=True

    hide Sungjae1

    if flag:
        show Sungjae4
        system "효과는 굉장했다!"
        system "모든 호감도가 0으로 돌아갑니다."
        $ love_Geonhee = 0
        $ love_Heeseol = 0
        $ love_Yeha = 0
        hide Sungjae4
    else:
        show Sungjae3
        system "효과는 별로였다.."
        system "호감도를 성공적으로 지켜냈습니다."
        hide Sungjae3

    jump scene2

label start:

    scene campus with fade
    python:
        renpy.log("디버깅 테스트: 로그 출력 확인")
    show JunHo1
    $ current_character = "JunHo"
    JunHo "안녕? 난 박준호, 23세."
    JunHo "한국 최고의 명문대학교 KISST에\n재학 중인 전설적인 존재야."
    JunHo "완벽한 얼굴, 모델 뺨치는 키, 한 번 보면 빠져드는 눈빛, 거기다 다정함까지."
    hide JunHo1
    show JunHo4
    JunHo "이런 내가 못가진 게 있다면 딱 하나 ,,, 첫사랑"
    JunHo "맞아. 아직까지 내 심장을 뛰게 만든\n여자를 찾지 못했어!"
    JunHo "그런데 말이야, 운명의 장난처럼 내 앞에 사랑의 기회가 떨어졌다고?"
    JunHo "{i}몰입캠프에 참가하시겠습니까?{/i}"
    JunHo "혼자 들어가면 반드시 둘이 되어\n나온다는, 그 사랑의 몰입캠프?!"
    hide JunHo4
    show JunHo6
    JunHo "과연 나, 박준호, 드디어 사랑이라는 걸 느낄 수 있을까?"
    JunHo "핑크빛 세상 속에서, 매일 아침 그녀의\n이름으로 눈을 뜨고 싶어."
    hide JunHo6

    jump first_meeting

    label first_meeting:

        scene classroom with fade
        
        show JunHo2
        JunHo "난 준비됐어. 이 심장을 뛰게 해줄\n누군가를 만나기 위해."
        JunHo "몰입캠프... 내가 왔다!"
        hide JunHo2

        show Geonhee
        $ current_character = "Geonhee"
        Geonhee "처음 뵙겠습니다. 강건희라고 해요."
        Geonhee "제 이름, 오늘부터 기억하셔야 할걸요."
        Geonhee "왜냐면요, 이 캠프에서 가장 특별한\n순간은 제 옆자리에서 시작될 테니까요."
        Geonhee "어서 앉으세요."
        hide Geonhee

        show Heeseol
        $ current_character = "Heeseol"
        Heeseol "안녕하세요. 저는 심희설이에요."
        Heeseol "솔직히 이런 데는 처음이라 조금\n긴장했는데…"
        Heeseol "준호 씨랑 얘기하면 괜찮아질 것 같아요."
        Heeseol "제 옆자리, 비어 있으니까 괜찮다면\n앉아주세요."
        hide Heeseol

        show Yeha
        $ current_character = "Yeha"
        Yeha "어머~ 준호 씨? 생각보다 더\n매력적이시네."
        Yeha "아, 나 진예하야."
        Yeha "여기 내 옆자리 비었는데, 같이 앉아서\n재미 좀 만들어볼래요?"
        hide Yeha

        show JunHo4
        $ current_character = "JunHo"
        system "누구 옆에 앉을까?"
        menu:
            "1. 강건희":
                hide JunHo4
                jump sit_Geonhee

            "2. 심희설":
                hide JunHo4
                jump sit_Heeseol

            "3. 진예하":
                hide JunHo4
                jump sit_Yeha

        label sit_Geonhee:
            show Geonhee_happy
            $ current_character = "Geonhee"
            Geonhee "그 선택이 후회되지 않게 만들어 줄게."
            $ love_Geonhee+=20
            $ show_affection_event("강건희", 20)
            hide Geonhee_happy
            jump scene1

        label sit_Heeseol:
            show Heeseol_happy
            $ current_character = "Heeseol"
            Heeseol "조금 부끄럽긴 하지만.. 옆에 있으니까\n기분은 좋네요."
            $ love_Heeseol+=20
            $ show_affection_event("심희설", 20)
            hide Heeseol_happy
            jump scene1

        label sit_Yeha:
            show Yeha_happy
            $ current_character = "Yeha"
            Yeha "아니, 나랑 앉을 줄 알았어! 그래도 고마워!"
            $ love_Yeha+=20
            $ show_affection_event("진예하", 20)
            hide Yeha_happy
            jump scene1
    
    return
    
label scene1:
    show Sungjae1
    $ current_character = "Sungjae"
    Sungjae "안녕하세요! 몰입캠프 운영진 \n조성제입니다."
    hide Sungjae1
    show Sungjae2
    Sungjae "그리고… 제 눈웃음 보셨죠? 저한테 \n빠져들지 마세요, 너무 매력적이니까요."
    hide Sungjae2

    jump eye_game

label scene2:
    show JunHo1
    $ current_character = "JunHo"
    JunHo "안녕하세요, 저는 박준호라고 합니다."
    hide JunHo1
    show JunHo4
    JunHo "음… 사실 저는 연애 경험이 \n부족한 편이라,"
    JunHo "이번 캠프에서 진지하게 사랑을 \n배워보고 싶어요. 잘 부탁드립니다…"
    hide JunHo4

    show Geonhee
    $ current_character = "Geonhee"
    Geonhee "그렇다면, 이번 캠프에서 어떤 사람을 \n만나고 싶으신가요?"
    hide Geonhee
    show JunHo3
    $ current_character = "JunHo"

    menu:
        "어 ... 아직 잘 모르겠어요.":
            hide JunHo3
            show Geonhee_unhappy
            $ current_character = "Geonhee"
            info "건희는 답답하거나 돌려말하는 사람을 싫어합니다."
            hide Geonhee_unhappy
        
        "너.":
            hide JunHo3
            show Geonhee_happy
            $ love_Geonhee+=20
            $ current_character = "Geonhee"
            $ show_affection_event("강건희", 20)
            info "건희는 직설적으로 말하는 사람을 좋아합니다."
            hide Geonhee_happy

        "그냥 착하고 따뜻한 사람이면 좋지 않을까요?":
            hide JunHo3
            show Geonhee_unhappy
            $ current_character = "Geonhee"
            info "건희는 답답하거나 돌려말하는 사람을 싫어합니다."
            hide Geonhee_unhappy
    
    show Heeseol
    $ current_character = "Heeseol"
    Heeseol "연애에 대해서는 잘 모르신다고 했지만… 평소에 무엇을 좋아하세요?"
    hide Heeseol

    show JunHo6
    $ current_character = "JunHo"

    menu:
        "도서관에서 조용히 책을 읽는 걸 좋아합니다.":
            hide JunHo6
            show Heeseol_happy
            $ love_Heeseol+=20
            $ current_character = "Heeseol"
            $ show_affection_event("심희설", 20)
            info "희설이는 조용한 장소를 좋아합니다."
            hide Heeseol_happy

        "노래방 가는 걸 즐겨요.":
            hide JunHo6
            show Heeseol_unhappy
            $ current_character = "Heeseol"
            info "희설이는 시끄러운 장소나 액티비티를 싫어합니다."
            hide Heeseol_unhappy

        "운동하는 걸 좋아해요.":
            hide JunHo6
            show Heeseol_unhappy
            $ current_character = "Heeseol"
            info "희설이는 시끄러운 장소나 액티비티를 싫어합니다."
            hide Heeseol_unhappy
    
    show Yeha
    $ current_character = "Yeha"
    Yeha "준호씨.  혹시 정치색 있어요?"
    hide Yeha

    show JunHo3
    $ current_character = "JunHo"

    menu:
        "나의 아버지. 윤석열.":
            hide JunHo3
            show Yeha_unhappy
            $ current_character = "Yeha"
            info "예하는 정치 이야기를 싫어합니다."
            hide Yeha_unhappy

        "아이 러브 이재명!":
            hide JunHo3
            show Yeha_unhappy
            $ current_character = "Yeha"
            info "예하는 정치 이야기를 싫어합니다."
            hide Yeha_unhappy

        "딱히 없습니다.":
            hide JunHo3
            show Yeha_happy
            $ love_Yeha+=20
            $ current_character = "Yeha"
            $ show_affection_event("진예하", 20)
            info "예하는 정치 이야기를 싫어합니다."
            hide Yeha_happy

    show Sungjae1
    $ current_character = "Sungjae"
    Sungjae "이제 각자 선택한 장소에 따라 데이트가 진행됩니다."
    Sungjae "선택이 끝나면, 같은 장소를 고른 \n사람끼리만 데이트를 떠나게 되죠."
    hide Sungjae1
    show Sungjae2
    Sungjae "이 눈웃음처럼, 여러분의 선택도 아주 \n달콤한 결과를 낳을 거라고 믿어요!"
    hide Sungjae2

    show JunHo2
    $ current_character = "JunHo"
    JunHo "어디가 좋을까… 아, 이런 기분 처음이야!"
    
    menu:
        "윤슬이 예쁜 바닷가":
            hide JunHo2
            jump date_Yeha
        
        "둘만의 조용한 카페":
            hide JunHo2
            jump date_Heeseol
        
        "모든 게 다 있는 대형 백화점":
            hide JunHo2
            jump date_Geonhee

    return

label date:

    label date_Geonhee:
        scene department_store with fade
        show Geonhee_happy
        $ dated_with = "Geonhee"
        $ current_character = "Geonhee"
        Geonhee "예상보다 더 잘 맞는 선택을 했네요. 좋은 선택입니다."
        $ love_Geonhee+=20
        $ show_affection_event("강건희", 20)
        hide Geonhee_happy
        jump evening

    label date_Heeseol:
        scene cafe with fade
        show Heeseol_happy
        $ dated_with = "Heeseol"
        $ current_character = "Heeseol"
        Heeseol "준호씨랑 이렇게 데이트할 줄은 몰랐어요. 조금 떨리네요…"
        $ love_Heeseol+=20
        $ show_affection_event("심희설", 20)
        hide Heeseol_happy
        jump evening

    label date_Yeha:
        scene beach with fade
        show Yeha_happy
        $ dated_with = "Yeha"
        $ current_character = "Yeha"
        Yeha "어머, 이곳에 나랑 같은 장소를 고른 거야? 너무 운명적인 거 아니야?"
        $ love_Yeha+=20
        $ show_affection_event("진예하", 20)
        hide Yeha_happy
        jump evening

label evening:

    scene evening_campus with fade
    show Sungjae1
    $ current_character = "Sungjae"
    Sungjae "드디어 1:1 대화 시간입니다!"
    Sungjae "각자 데이트 후에 나누고 싶은 \n이야기나 궁금한 점들을"
    Sungjae "상대방과 자유롭게 이야기할 수 있는\n시간이죠."
    hide Sungjae1
    show Sungjae2
    Sungjae "눈웃음처럼 설레는 시간이 될 거예요."
    hide Sungjae2

    if dated_with == "Geonhee":
        jump evening_with_Geonhee
    elif dated_with == "Heeseol":
        jump evening_with_Heeseol
    elif dated_with == "Yeha":
        jump evening_with_Yeha

    return

    label evening_with_Geonhee:

        show Geonhee
        $ current_character = "Geonhee"
        Geonhee "준호씨, 첫 데이트는 어땠어요?"
        hide Geonhee
        show JunHo1
        $ current_character = "JunHo"

        menu:
            "좋은 데이트였습니다.":
                hide JunHo1
                show Geonhee
                Geonhee "그렇게 생각해 주셔서 다행이에요."
                hide Geonhee
                jump post_evening

            "떨려서 기억이 잘 안 나네요...":
                hide JunHo1
                show Geonhee_unhappy
                $ current_character = "Geonhee"
                Geonhee "좀 더 생각해보고 말해도 좋을 것 같아요."
                hide Geonhee_unhappy
                jump post_evening

            "매일 너랑 데이트 하고싶다.":
                hide JunHo1
                show Geonhee_happy
                $ current_character = "Geonhee"
                Geonhee "솔직한 대답, 마음에 들어요."
                $ love_Geonhee += 20
                $ show_affection_event("강건희", 20)
                hide Geonhee_happy
                jump post_evening

    label evening_with_Heeseol:

        show Heeseol
        $ current_character = "Heeseol"
        Heeseol "준호씨는 연락을 자주 하시는 편인가요?"
        hide Heeseol
        show JunHo4
        $ current_character = "JunHo"

        menu:
            "매일 1분만에 답하는 편입니다.":
                hide JunHo4
                show Heeseol_happy
                $ current_character = "Heeseol"
                Heeseol "정말요? 저도 그렇게 생각해요."
                $ love_Heeseol += 20
                $ show_affection_event("심희설", 20)
                hide Heeseol_happy
                jump post_evening

            "문자보단 전화를 선호합니다.":
                hide JunHo4
                show Heeseol_unhappy
                $ current_character = "Heeseol"
                Heeseol "그렇군요. 그럼, 저는 조금 더 생각해볼게요."
                hide Heeseol_unhappy
                jump post_evening

            "연락을 중요하게 생각하진 않아요.":
                hide JunHo4
                show Heeseol_unhappy
                $ current_character = "Heeseol"
                Heeseol "그렇군요. 그럼, 저는 조금 더 생각해볼게요."
                hide Heeseol_unhappy
                jump post_evening

    label evening_with_Yeha:

        show Yeha
        $ current_character = "Yeha"
        Yeha "준호씨~ 술은 좀 드시는 편이세요?"
        hide Yeha
        show JunHo1
        $ current_character = "JunHo"

        menu:
            "아니요. 술을 별로 안 좋아합니다.":
                hide JunHo1
                show Yeha_unhappy
                $ current_character = "Yeha"
                Yeha "설마... 농담이지?"
                hide Yeha_unhappy
                jump post_evening

            "컨디션에 따라 다른 거 같아요.":
                hide JunHo1
                show Yeha_unhappy
                $ current_character = "Yeha"
                Yeha "설마... 농담이지?"
                hide Yeha_unhappy
                jump post_evening

            "혼자 8병 먹어도 안 취해요!":
                hide JunHo1
                show Yeha_happy
                $ current_character = "Yeha"
                Yeha "역시 준호 씨, 내가 느낀 대로 맞네!\n멋지다!"
                $ love_Yeha += 20
                $ show_affection_event("진예하", 20)
                hide Yeha_happy
                jump post_evening

    label post_evening:
        scene mansroom_night with fade
        show JunHo1
        $ current_character = "JunHo"
        JunHo "휴 .. 오늘 하루 정말 바빴어"
        JunHo "내일도 파이팅이야!"
        hide JunHo1
        jump sports_day

label sports_day:
    scene sports_field with fade
    show Sungjae4
    $ current_character = "Sungjae"
    Sungjae "자, 오늘 체육대회는 여러분의 체력과 함께\n운명도 시험해볼 기회!"
    Sungjae "같은 종목을 고른 사람과 데이트로 \n이어질 수 있답니다!"
    hide Sungjae4
    show Sungjae2
    Sungjae "내 눈웃음처럼… 여러분의 선택도 \n매력적이고 빛날 거라고 믿어요."
    hide Sungjae2

    show JunHo2
    $ current_character = "JunHo"
    JunHo "어떤 종목을 나갈까?"

    menu:
        "섬세함이 필요한 배드민턴":
            hide JunHo2
            jump badminton_event

        "집중력이 필요한 양궁":
            hide JunHo2
            jump archery_event

        "협력이 필요한 2인3각":
            hide JunHo2
            jump two_leg_race_event
    
    label badminton_event:
        show Geonhee_happy
        $ current_character = "Geonhee"
        Geonhee "준호 씨 저랑 같이 호흡을 맞춰봐요."
        $ love_Geonhee += 20
        $ show_affection_event("강건희", 20)
        hide Geonhee_happy
        jump post_sports

    label archery_event:
        show Heeseol_happy
        $ current_character = "Heeseol"
        Heeseol "잘할 수 있을 거라고 믿어요."
        $ love_Heeseol += 20
        $ show_affection_event("심희설", 20)
        hide Heeseol_happy
        jump post_sports

    label two_leg_race_event:
        show Yeha_happy
        $ current_character = "Yeha"
        Yeha "이제부터는 우리 팀이 최고야!"
        $ love_Yeha += 20
        $ show_affection_event("진예하", 20)
        hide Yeha_happy
        jump post_sports
    
    label post_sports:
        scene sports_field_evening with fade
        show Sungjae4
        $ current_character = "Sungjae"
        Sungjae "우리 2분반이 체육대회 우승을 했다는 기쁜 소식을 전하게 됐네요!"
        hide Sungjae4
        show Sungjae2
        Sungjae "오늘 회식은 눈웃음이 가득한 곳에서,"
        Sungjae "우승의 기쁨을 한껏 더 만끽할 수 있는 특별한 장소로 갑니다."
        hide Sungjae2

        show JunHo2
        $ current_character = "JunHo"
        JunHo "야호~ 회식이다! 어디로 갈까?"

        menu:
            "신나는 노래가 나오는 클럽":
                hide JunHo2
                jump drinking

            "조용한 분위기의 칵테일바":
                hide JunHo2
                jump drinking

            "고급스러운 다이닝룸":
                hide JunHo2
                jump drinking

label drinking:
    scene bar with fade
    show JunHo4
    $ current_character = "JunHo"
    JunHo "결국 자리가 없어서 여기를 왔네. \n다들 취한 것 같아..."
    hide JunHo4
    show JunHo5
    JunHo "그래도 오늘이 마지막이니까 모두와 \n대화를 해봐야겠어!"
    hide JunHo5

    show Geonhee
    $ current_character = "Geonhee"
    Geonhee "준호 씨, 혹시... 나랑 좀 더 친해지고 \n싶지 않아?"
    hide Geonhee
    show JunHo3
    $ current_character = "JunHo"

    menu:
        "너무너무! 항상 그 말을 기다렸어":
            hide JunHo3
            show Geonhee_happy
            $ current_character = "Geonhee"
            Geonhee "다행이네요. 나도 그런 대답을 \n듣고 싶었어요."
            $ love_Geonhee += 20
            $ show_affection_event("강건희", 20)
            hide Geonhee_happy

        "아직 반말은 좀 불편하네요...":
            hide JunHo3
            show Geonhee_unhappy
            $ current_character = "Geonhee"
            Geonhee "그렇게 생각하는 거면, 더 이상 말하지 않겠습니다."
            hide Geonhee_unhappy

        "차근차근 친해지면 되죠.":
            hide JunHo3
            show Geonhee_unhappy
            $ current_character = "Geonhee"
            Geonhee "그렇게 생각하는 거면, 더 이상 말하지 않겠습니다."
            hide Geonhee_unhappy

    show Heeseol
    $ current_character = "Heeseol"
    Heeseol "준호 씨... 오늘 너무 재미있었어요. \n고마워요."
    hide Heeseol
    show JunHo4
    $ current_character = "JunHo"

    menu:
        "저희 클럽으로 2차 어때요?":
            hide JunHo4
            show Heeseol_unhappy
            $ current_character = "Heeseol"
            Heeseol "언젠가 시간이 지나면 자연스럽게 친해질 수 있겠죠..?"
            hide Heeseol_unhappy

        "취하니까 더 귀여우시네요..":
            hide JunHo4
            show Heeseol_unhappy
            $ current_character = "Heeseol"
            Heeseol "언젠가 시간이 지나면 자연스럽게 친해질 수 있겠죠..?"
            hide Heeseol_unhappy

        "희설 씨랑 함께 해서 저도 좋았어요.":
            hide JunHo4
            show Heeseol_happy
            $ current_character = "Heeseol"
            Heeseol "아, 정말요? 저도 그런 마음이에요. \n기뻐요..."
            $ love_Heeseol += 20
            $ show_affection_event("심희설", 20)
            hide Heeseol_happy

    show Yeha
    $ current_character = "Yeha"
    Yeha "준호 씨, 취했나요? 그런 눈빛, \n너무 매력적인데요."
    hide Yeha
    show JunHo6
    $ current_character = "JunHo"

    menu:
        "정말요? 좋게 봐주셔서 감사합니다.":
            hide JunHo6
            show Yeha_unhappy
            $ current_character = "Yeha"
            Yeha "준호 씨 유머 감각은 없으시네요."
            hide Yeha_unhappy

        "\n제가 원래 취하면 차은우,\n안 취하면 송강입니다.":
            hide JunHo6
            show Yeha_happy
            $ current_character = "Yeha"
            Yeha "하하! 그런 말 듣고 싶었어요!"
            $ love_Yeha += 20
            $ show_affection_event("진예하", 20)
            hide Yeha_happy

        "이런 말 처음이라 조금 부끄럽네요...":
            hide JunHo6
            show Yeha_unhappy
            $ current_character = "Yeha"
            Yeha "준호 씨 유머 감각은 없으시네요."
            hide Yeha_unhappy

    jump epilogue

label epilogue:
    scene mansroom_night with fade
    show JunHo2
    $ current_character = "JunHo"
    JunHo "내일... 진짜 중요한 선택이구나..."
    JunHo "이렇게 설레는 기분은 처음이라, 조금 떨린다."
    JunHo "다들 너무 매력적이라서 \n한 명을 고른다는 게 너무 어려워."
    JunHo "내일 나는 누구의 이름으로 하루를 시작할까?"
    JunHo "이제 나도 모솔 탈출이다!!"
    hide JunHo2

    $ ending = choose_ending(love_Geonhee,love_Heeseol,love_Yeha)

    if ending == 0:
        show Geonhee_happy #Geonhee_ending
        Geonhee "준호 씨, 평생을 함께하며, 서로의 소중함을 느끼고 살아가고 싶어요."
    elif ending == 1:
        show Heeseol_happy #Heeseol_ending
        Heeseol "오빠, 처음 만났을 때부터 항상 따뜻하게 대해줘서, 제 옆에 있어줘서 고마워요."
    elif ending == 2:
        show Yeha_happy #Yeha_ending
        Yeha "준호야, 이렇게 멋진 날, 함께할 수 있다는 게 정말 행복해!"
    else:
        show Sungjae2 #bad_ending
        Sungjae "이렇게 멋진 결정을 해줘서 너무 고마워. 내 눈웃음을 평생 선물할게."