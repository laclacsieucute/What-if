#chuyển video thành image để chạy loop

image intro 2 = Movie(play = "images/Intro/intro 2.webm")
image intro 3 = Movie(play = "images/Intro/intro 3.webm")
image intro 6 = Movie(play = "images/Intro/intro 6.webm")
image LoadingScreen = Movie(play = "images/gtnv/loadingScreen.webm")
image gtnv 1 = Movie(play = "images/gtnv/gtnv 1.webm")
image gtnv 2 = Movie(play = "images/gtnv/gtnv 2.webm")
image a2 10loop = Movie(play = "images/a2/a2 10loop.webm")



#tên nhân vật
define A = Character("Amber", color="#ff3535")
define D = Character("Dana", color="#1aff53")





#nội dung chính
label AmberNDana:
    scene black
    #intro
    "6H tối"
    #play sound "audio/sfx/sfx.ogg" fadein 1.0 loop
    window hide
    $ renpy.movie_cutscene("images/Intro/intro 1.webm")
    show intro 2
    window show
    voice "audio/Voice/A1/Dana.ogg"
    D "á! {w=0.7}nhẹ thôi anh ưi..."
    show intro 3
    voice "audio/Voice/A1/Dana-001.ogg"
    D "người ta đã bảo nhẹ thôi mà..."
    show intro 4
    play sound "audio/sfx/door.ogg"
    "!"

    show intro 5
    voice "audio/Voice/A1/Amber.ogg"
    A "hai đứa{w=1.0} rửa tay rồi nhanh dọn cơm ăn tối, đến bữa rồi."

    #play sound "audio/sfx/sfx.ogg" loop
    voice "audio/Voice/A1/Dana-002.ogg"
    show intro 6
    "dạ... bọn con sắp xong rồi ạ..."

    #giới thiệu nhân vật
    scene black
    show gtnv 1
    "đây là bạn{w=1.0}{nw}"
    "đúng vậy,{w=0.5} thanh niên này chính là bạn{w=1.0}{nw}"
    "đừng hỏi tôi tại mặt thanh niên này lại trông buồn cười như thế,{w=2}{nw}"
    "tôi chỉ tạo ra ngẫu nghiên thôi{w=1}{nw}"
    show gtnv amber stand
    "bạn đang sống với mẹ{w=1.5}{nw}"
    show gtnv 2
    "và em gái{w=1.5}{nw}"
    "cách chơi game này rất đơn giản{w=1}{nw}"
    "bạn ngồi nghe tôi nói linh tinh về triết lí nhân sinh{w=2}{nw}"
    "sau đó đưa ra lựa chọn{w=1}{nw}"
    "rồi lại tiếp tục ngồi nghe tôi nói gì đó về khoa học vũ trụ{w=2}{nw}"
    
    menu Lc_gtnv:
        "bắt đầu với lựa chọn đầu tiên của bạn nào."
        "bắn vào trong":
            show gtnv lc b 1
            play sound "audio/sfx/gun.ogg"
            D "a..."
            "không,{w=0.7} tôi đùa thôi,{w=0.7} game này chỉ có chịch với chịch thôi.{w=0.7} chẳng có triết lý gì đâu."
            "hình như bạn làm em gái mình cáu rồi thì phải"
            show gtnv lc b 2
            voice "audio/Voice/A1/Dana-003.ogg"
            D "cái ông này nữa...{w=1} lần nào cũng thế {w=1.7} {nw}"

            voice "audio/Voice/A1/Dana-004.ogg"
            D "cứ bắn tùm lum ra xong rồi nguời ta lại phải dọn. {w=2}{nw}"

            voice "audio/Voice/A1/Dana-005.ogg"
            D "lần sau nhá...{w=1.5} đeo cái bao vào, không thì người ta không chơi nữa đâu đấy"
        
        "bắn ra ngoài":
            show gtnv lc a 1
            play sound "audio/sfx/gun.ogg"
            D "a..."
            "không,{w=0.7} tôi đùa thôi,{w=0.7} game này chỉ có chịch với chịch thôi.{w=0.7} chẳng có triết lý gì đâu."
            "hình như bạn làm em gái mình cáu rồi thì phải"
            show gtnv lc a 2
            voice "audio/Voice/A1/Dana-003.ogg"
            D "cái ông này nữa...{w=1} lần nào cũng thế {w=1.7} {nw}"

            voice "audio/Voice/A1/Dana-004.ogg"
            D "cứ bắn tùm lum ra xong rồi nguời ta lại phải dọn. {w=2}{nw}"

            voice "audio/Voice/A1/Dana-005.ogg"
            D "lần sau nhá...{w=1.5} đeo cái bao vào, không thì người ta không chơi nữa đâu đấy"
        
    show gtnv amber angry3
    voice "audio/Voice/A1/Amber-001.ogg"

    A "ơ{w=0.7} hai cái đứa này,{w=1.0} mẹ đã bảo là đi dọn cơm rồi cơ mà."

    #cắt cảnh sang A2
    scene black
    show LoadingScreen
    "Loading screen"
    "Không tôi đùa đấy"
    "game này làm gì có Loading Screen, tôi chỉ không biết chuyển cảnh kiểu gì thôi."
    "dù sao thì"
    "chào mừng bạn tới Bữa tối côn trùng."
    jump A2
    
label A2:
    scene black
    window hide
    play sound "audio/sfx/kitchensound.ogg"
    show a2 1 with Pause(2.0)
    play sound "audio/sfx/kitchensound-001.ogg"
    show a2 2 with Pause(2.0)
    show a2 3 with Pause(0.5)

    voice "audio/Voice/A1/Dana-006.ogg"
    D "ủa..{w=0.7} sao hôm nay mẹ về sớm vậy?"

    show a2 4
    voice "audio/Voice/A1/Amber-002.ogg"
    A "chứ...{w=0.7} bình thường thì là mấy giờ?"

    show a2 5
    voice "audio/Voice/A1/Dana-007.ogg"
    D "mọi khi là...{w=0.7} 7H mẹ mới về mà"

    show a2 6
    voice "audio/Voice/A1/Amber-003.ogg"
    A "thế nhìn lại đồng hồ xem là mấy giờ rồi"

    show a2 7
    voice "audio/Voice/A1/Dana-008.ogg"
    D "ờ... {w=0.7}6h59"

    show a2 8
    voice "audio/Voice/A1/Amber-004.ogg"
    A "thôi thôi thôi... {w=0.7} mày đừng có lôi thôi nữa"

    show a2 9
    voice "audio/Voice/A1/Amber-005.ogg"
    A " nhanh cái tay lên,{w=0.7} mẹ đói lắm rồi"
    window hide
    show a2 10 with dissolve
    with Pause(1.0)
    show a2 10loop with dissolve
    
    menu A2menu:
        "xúc cát":
            jump A5
        "bật Tivi":
            jump A3


label A3:
    menu A3menu:
        "bro thật sự muốn mở tivi???"
        "không, thực ra tôi nứng lắm rồi":
            jump A5
        "đúng vậy, tôi muốn xem chung kết, VN vô địch":
            window hide

            play sound "audio/sfx/tvClick.ogg"
            show a3 1 with Pause(0.7)

            play sound "audio/sfx/chungkethighlight.ogg" fadein 1.0
            show a3 2 with dissolve
            with Pause(7.0)
            "highlight chung kết"
            jump A4

    

label A4:
    scene black
    window hide
    show a4 1 with Pause(1.0)

    voice "audio/Voice/A1/Amber-006.ogg"
    A "nào {w=0.7}mày ngồi lui ra cho mẹ xem nào"

    show a4 2
    voice "audio/Voice/A1/Amber-007.ogg"
    A "đã không phụ được cái gì thì chớ"
    voice "audio/Voice/A1/Amber-008.ogg"
    A "lại còn cứ ngồi chình ình ra đây"
    show a4 3 with dissolve
    window hide
    menu A4menu:
        "xúc cát":
            jump A6
        "xúc cát":
            jump A6
        "xúc cát":
            jump A6
        "cương lắm rồi, không chọn được cái khác đâu":
            jump A6
    

label A5:
    scene black
    window hide
    show a5 1 with dissolve
    with Pause(1.0)
    show a6 4 with dissolve
    voice "audio/Voice/A1/Amber-009.ogg"
    A "cái thằng này...{w=0.7} đến bữa rồi mà còn không chịu thôi"
    voice "audio/Voice/A1/Amber-010.ogg"
    A "mày đúng là..."
    
    show a6 5 with dissolve
    voice "audio/Voice/A1/Amber-011.ogg"
    A "thôi mày ngồi im cho mẹ xem nào..."

    show a6 6 with dissolve
    with Pause(0.5)   
    show a6 7 with dissolve 
    with Pause(1.0)
    jump A7

label A6:
    scene black
    window hide
    play sound "audio/sfx/sniff.ogg"
    show a6 1 with Pause(3.0)
    stop sound
    show a6 2 with dissolve
    with Pause(0.5) 
    show a6 3 with dissolve
    with Pause(1.0)

    show a6 4 with dissolve
    voice "audio/Voice/A1/Amber-009.ogg"
    A "cái thằng này...{w=0.7} đến bữa rồi mà còn không chịu thôi"
    voice "audio/Voice/A1/Amber-010.ogg"
    A "mày đúng là..."

    show a6 5 with dissolve
    voice "audio/Voice/A1/Amber-011.ogg"
    A "thôi mày ngồi im cho mẹ xem nào..."
    
    show a6 6 with dissolve
    voice "audio/Voice/A1/Amber-012.ogg"
    A "con đang xem gì đấy?"
    
    show a6 7 with dissolve
    voice "audio/Voice/A1/Amber-013.ogg"
    A "suốt ngày bóng với bánh" 
    with Pause(1.0)
    jump A7


label A7:
    scene black
    show a7 1
    play sound "audio/sfx/introthoisu.ogg" fadein 2.0
    "intro huyền thoại"

    show a7 2
    stop sound
    play sound "audio/sfx/idolphuongHang.ogg"
    "trội ôi... giọng idol!!!"

    show a7 3
    stop sound
    voice "audio/Voice/A1/Amber-014.ogg"
    A "kìa ăn đi con. cái con này. học không lo học, cứ cắm mặt vào cái điện thoại, rồi á đến lòi mắt ra như hai con ốc nhồi đấy con ạ."

    show a7 4
    voice "audio/Voice/A1/Dana-009.ogg"
    D "xời ơi...{w=0.7} con xem có tý, thì có sao đâu mà."

    show a7 5
    voice "audio/Voice/A1/Dana-010.ogg"
    D " hôm trước con thi lại vẫn đủ điểm ấy thây."

    show a7 6
    voice "audio/Voice/A1/Dana-011.ogg"
    D " à! mẹ ơi,{w=1.0} con mới mua lọ nước hoa trên TikTok này."
    voice "audio/Voice/A1/Dana-012.ogg"
    D " đúng hàng cao cấp luôn...{w=1.5} thơm lắm luôn mẹ ơi..."

    show a7 8
    voice "audio/Voice/A1/Amber-015.ogg"
    A "mày. mua cái gì không mua lại đi mua nước hoa."

    show a7 7
    voice "audio/Voice/A1/Amber-015.ogg"
    A "Ba cái thứ linh ta linh tinh, bổ béo gì đâu."

    show a7 9
    voice "audio/Voice/A1/Dana-013.ogg"
    D "kìa mẹ...{w=1.0} cái này nó là nước hoa cao cấp mà.{w=2.5}không ấy mai mẹ dùng thử đi."

    show a7 10
    voice "audio/Voice/A1/Narator.ogg"
    "thời sự: theo thông tin mới nhất chúng tôi vừa nhận được, lực lượng chức năng địa phương vừa triệt phá đường dây chiết nước hoa lậu lớn nhất quận Cam"

    show a7 11
    voice "audio/Voice/A1/Narator-001.ogg"
    "thời sự: theo ước tính từ các chuyên gia trà đá vỉa hè, thì tổng giá trị các lô nước hoa lậu đã lên tới 300 tỷ Mĩ kim"

    show a7 12
    voice "audio/Voice/A1/Narator-002.ogg"
    "thời sự: trên tay tôi là một lọ nước hoa lậu mà vợ tôi đã lỡ mua trên TikTok."
    voice "audio/Voice/A1/Narator-003.ogg"
    "thời sự: thật may là ở đây chúng ta có một giáo sư MÙI HỌC, ông Lôi Hách"
    voice "audio/Voice/A1/Narator-004.ogg"
    "thời sự: tôi có thể nhờ giáo sư mùi học Lôi Hách kiểm tra giúp tôi lọ nước hoa này được không ạ?"

    show a7 13
    voice "audio/Voice/A1/Narator-005.ogg"
    "Lôi Hách: tôi là tôi nói thật với anh, cái lọ này tôi còn không cần ngửi, nhìn là thấy đồ dở rồi. "

    show a7 14
    voice "audio/Voice/A1/Narator-006.ogg"
    "Hôi Lách: không hiểu sao vẫn có người mua nó về, có khi là vợ anh ghét anh lắm đấy."
   
    play sound "audio/sfx/tvClick.ogg"
    scene black
    
    D "{i}tắt Tivi{/i} {w=1.0} mẹ kiếp... toàn tin vịt!"

    

        




return