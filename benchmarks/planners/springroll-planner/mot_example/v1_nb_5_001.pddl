(define

    ;;@problem_name@v1_nb_5_001 (problem v1_nb_5_001)

    (:domain motion_planning_v1)

    (:objects
        b_0 b_1 b_2 b_3 b_4 - box
    )

    (:init

        ;;@initial_location@[-46, -36]
        (= (x) -46)
        (= (y) -36)

        ;;@bounding_box@ {"coordinates": [[14.114171389566636, -40.95012553534849], [-50.10532213816799, -40.95012553534849], [-50.10532213816799, 12.384517922561324], [14.114171389566636, 12.384517922561324]]}
        (= (maxx) 14.114171389566636)
        (= (maxy) 12.384517922561324)
        (= (minx) -50.10532213816799)
        (= (miny) -40.95012553534849)

        ;;@box@ {"coordinates": [[13.775383383817074, -4.523485768452313], [-5.5577462735910235, -4.523485768452313], [-5.5577462735910235, -2.296802429885777], [13.775383383817074, -2.296802429885777]]}
        (= (a1 b_0) 0.0)
        (= (b1 b_0) -19.333129657408097)
        (= (c1 b_0) 87.45313686492888)
        (= (a2 b_0) -2.226683338566536)
        (= (b2 b_0) 0.0)
        (= (c2 b_0) 12.375341027385385)
        (= (a3 b_0) 0.0)
        (= (b3 b_0) 19.333129657408097)
        (= (c3 b_0) -44.4043791744317)
        (= (a4 b_0) 2.226683338566536)
        (= (b4 b_0) 0.0)
        (= (c4 b_0) 30.67341666311179)
        ;;@box@ {"coordinates": [[14.114171389566636, -24.386273502966468], [1.6863658479066572, -24.386273502966468], [1.6863658479066572, -21.696625733143883], [14.114171389566636, -21.696625733143883]]}
        (= (a1 b_1) 0.0)
        (= (b1 b_1) -12.427805541659978)
        (= (c1 b_1) 303.06786498060256)
        (= (a2 b_1) -2.689647769822585)
        (= (b2 b_1) 0.0)
        (= (c2 b_1) -4.535730141927114)
        (= (a3 b_1) 0.0)
        (= (b3 b_1) 12.427805541659978)
        (= (c3 b_1) -269.641445521688)
        (= (a4 b_1) 2.689647769822585)
        (= (b4 b_1) 0.0)
        (= (c4 b_1) 37.96214960084164)
        ;;@box@ {"coordinates": [[3.8897464619358892, -21.100110480395347], [-7.682472188632207, -21.100110480395347], [-7.682472188632207, -7.8520600310079764], [3.8897464619358892, -7.8520600310079764]]}
        (= (a1 b_2) 0.0)
        (= (b1 b_2) -11.572218650568097)
        (= (c1 b_2) 244.1750920302784)
        (= (a2 b_2) -13.248050449387371)
        (= (b2 b_2) 0.0)
        (= (c2 b_2) 101.7777791310149)
        (= (a3 b_2) 0.0)
        (= (b3 b_2) 11.572218650568097)
        (= (c3 b_2) -90.86575553621081)
        (= (a4 b_2) 13.248050449387371)
        (= (b4 b_2) 0.0)
        (= (c4 b_2) 51.53155736305269)
        ;;@box@ {"coordinates": [[-1.7942528994191633, -6.3522765402432615], [-7.528143205282134, -6.3522765402432615], [-7.528143205282134, 12.384517922561324], [-1.7942528994191633, 12.384517922561324]]}
        (= (a1 b_3) 0.0)
        (= (b1 b_3) -5.733890305862971)
        (= (c1 b_3) 36.42325687426161)
        (= (a2 b_3) -18.736794462804585)
        (= (b2 b_3) 0.0)
        (= (c2 b_3) 141.05327192393025)
        (= (a3 b_3) 0.0)
        (= (b3 b_3) 5.733890305862971)
        (= (c3 b_3) 71.0114672589606)
        (= (a4 b_3) 18.736794462804585)
        (= (b4 b_3) 0.0)
        (= (c4 b_3) -33.61854779070805)
        ;;@box@ {"coordinates": [[-48.738630378283375, -40.95012553534849], [-50.10532213816799, -40.95012553534849], [-50.10532213816799, -30.296188945532435], [-48.738630378283375, -30.296188945532435]]}
        (= (a1 b_4) 0.0)
        (= (b1 b_4) -1.3666917598846169)
        (= (c1 b_4) 55.96619913540142)
        (= (a2 b_4) -10.653936589816055)
        (= (b2 b_4) 0.0)
        (= (c2 b_4) 533.8189248723484)
        (= (a3 b_4) 0.0)
        (= (b3 b_4) 1.3666917598846169)
        (= (c3 b_4) -41.4055517877666)
        (= (a4 b_4) 10.653936589816055)
        (= (b4 b_4) 0.0)
        (= (c4 b_4) -519.2582775247135)
    )
    (:goal
        (and
            ;;@goal_location@[9, 7]
            (= (x) 9) (= (y) 7)
        )
    )
)