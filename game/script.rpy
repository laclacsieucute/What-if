# 1. Khai báo các đoạn video
image bg = Movie(play="movie/n1startfull.webm", loop=True)
image g = Movie(play="movie/n1starthafl1.webm", loop=True)
image f = Movie(play="movie/n1starthalf2.webm", loop=True)
image b = Movie(play="movie/n1startnude.webm", loop=True)
image s = Movie(play="movie/n1mouthtablefullcum.webm", loop=True)
image d = Movie(play="movie/n1mouthtablefull.webm", loop=True)
image c = Movie(play="movie/n1mouthtablehalf1cum.webm", loop=True)
image z = Movie(play="movie/n1mouthtablehalf1.webm", loop=True)
image x = Movie(play="movie/n1mouthtablehalf2cum.webm", loop=True)
image v = Movie(play="movie/n1mouthtablehalf2.webm", loop=True)
image n = Movie(play="movie/n1mouthtablenudecum.webm", loop=True)
image m = Movie(play="movie/n1mouthtablenude.webm", loop=True)
image h = Movie(play="movie/n1mouthendfull.webm", loop=True)
image j = Movie(play="movie/n1mouthendhalf1.webm", loop=True)
image k = Movie(play="movie/n1mouthendhalf2.webm", loop=True)
image r = Movie(play="movie/n1mouthendnude.webm", loop=True)

label start:
    stop audio
    play audio 'audio/Hikari_kuh.ogg'

    show bg
    "sẽ thế nào nếu như Ophelia bị trói tay trước mặt bạn?"

    menu:

        "cứ vậy mà chơi luôn":
            
            "..."
            menu:
                "liếm cu":
                    show d

                    play audio 'audio/Hikari_Con1.ogg'
                    "..."
                    menu:
                        "xuất":
                            hide d

                            play audio 'audio/Hikari_kuh.ogg'

                            scene n1mouthtableejectfull
                            "...."
                            menu:
                                "liếm tiếp":
                                    show s

                                    play audio 'audio/Hikari_Con1.ogg'
                                    "..."
                                    menu:
                                        "buông Ophelia ra":
                                            show h

        "cởi áo":
            show g

            play audio 'audio/Hikari_Mote2.ogg'
            "..."
            menu:
                "liếm cu":
                    show z

                    play audio 'audio/Hikari_Con1.ogg'
                    "..."
                    menu:
                        "xuất":
                            hide z

                            play audio 'audio/Hikari_kuh.ogg'

                            scene n1mouthtableejecthalf1
                            "...."
                            menu:
                                "liếm tiếp":
                                    show c

                                    queue audio 'audio/Hikari_Con1.ogg'
                                    "..."
                                    menu:
                                        "buông Ophelia ra":
                                            show j

        "vén hết lên":
            show f

            play audio 'audio/Hikari_kuh.ogg'
            "..."
            menu:
                "liếm cu":
                    show v

                    play audio 'audio/Hikari_Con1.ogg'
                    "..."
                    menu:
                        "xuất":
                            hide v

                            play audio 'audio/Hikari_kuh.ogg'

                            scene n1mouthtableejecthalf2
                            "...."
                            menu:
                                "Liếm tiếp":
                                    show x

                                    play audio 'audio/Hikari_Con1.ogg'
                                    "..."
                                    menu:
                                        "end":
                                            show k

        "cởi sạch":
            show b

            play audio 'audio/Hikari_Mote2.ogg'
            "..."
            menu:
                "liếm cu":
                    show m

                    play audio 'audio/Hikari_Con1.ogg'
                    "..."
                    menu:
                        "xuất":
                            hide m

                            stop audio
                            play audio 'audio/Hikari_kuh.ogg'

                            scene n1mouthtableejectnude
                            "...."
                            menu:
                                "Liếm tiếp":
                                    show n

                                    play audio 'audio/Hikari_Con1.ogg'
                                    "..."
                                    menu:
                                        "buông Ophelia ra":
                                            show r

    # Thêm câu thoại ở đây để người chơi kịp nhìn thấy video chuyển đổi
    play audio 'audio/ambulance-siren1.ogg'
    "..."
    "..."
    "hết rồi đấy"
    "..."
    "..."
    "chơi lại hoặc thoát game đi bạn"
    menu:
        "chơi lại":
            jump start 
    return