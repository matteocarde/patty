(define

;;@problem_name@v1_nb_15_001
(problem v1_nb_15_001)

(:domain motion_planning_v1)

(:objects b_0 b_1 b_2 b_3 b_4 b_5 b_6 b_7 b_8 b_9 b_10 b_11 b_12 b_13 b_14 - box)

(:init

    ;;@initial_location@[-3, -52]
(= (x) -3) (= (y) -52)

    ;;@bounding_box@ {"coordinates": [[47.71252707614703, -54.195798308192764], [-43.09040364303266, -54.195798308192764], [-43.09040364303266, 52.09067701554898], [47.71252707614703, 52.09067701554898]]}
(= (maxx) 47.71252707614703) (= (maxy) 52.09067701554898) (= (minx) -43.09040364303266) (= (miny) -54.195798308192764)

    ;;@box@ {"coordinates": [[46.04888315959025, 39.77381758887147], [41.96073159974827, 39.77381758887147], [41.96073159974827, 50.262722132196515], [46.04888315959025, 50.262722132196515]]}
(= (a1 b_0) 0.0) (= (b1 b_0) -4.088151559841975) (= (c1 b_0) -162.60139441681508)
(= (a2 b_0) -10.488904543325049) (= (b2 b_0) 0.0) (= (c2 b_0) -440.12210831784256)
(= (a3 b_0) 0.0) (= (b3 b_0) 4.088151559841975) (= (c3 b_0) 205.48162588664295)
(= (a4 b_0) 10.488904543325049) (= (b4 b_0) 0.0) (= (c4 b_0) 483.00233978767045)
;;@box@ {"coordinates": [[13.81559866415705, -41.00379052590826], [10.156763717411806, -41.00379052590826], [10.156763717411806, -29.889828636835087], [13.81559866415705, -29.889828636835087]]}
(= (a1 b_1) 0.0) (= (b1 b_1) -3.6588349467452446) (= (c1 b_1) 150.02610172521472)
(= (a2 b_1) -11.11396188907317) (= (b2 b_1) 0.0) (= (c2 b_1) -112.88188487163595)
(= (a3 b_1) 0.0) (= (b3 b_1) 3.6588349467452446) (= (c3 b_1) -109.361949568679)
(= (a4 b_1) 11.11396188907317) (= (b4 b_1) 0.0) (= (c4 b_1) 153.54603702817167)
;;@box@ {"coordinates": [[-24.05957536119101, -2.16805149688169], [-43.09040364303266, -2.16805149688169], [-43.09040364303266, 3.454377479747438], [-24.05957536119101, 3.454377479747438]]}
(= (a1 b_2) 0.0) (= (b1 b_2) -19.03082828184165) (= (c1 b_2) 41.25981574334519)
(= (a2 b_2) -5.622428976629128) (= (b2 b_2) 0.0) (= (c2 b_2) 242.27273405723216)
(= (a3 b_2) 0.0) (= (b3 b_2) 19.03082828184165) (= (c3 b_2) 65.73966463773442)
(= (a4 b_2) 5.622428976629128) (= (b4 b_2) 0.0) (= (c4 b_2) -135.27325367615254)
;;@box@ {"coordinates": [[40.615265790001814, -25.1974429439214], [30.020197267193737, -25.1974429439214], [30.020197267193737, -9.5019238507214], [40.615265790001814, -9.5019238507214]]}
(= (a1 b_3) 0.0) (= (b1 b_3) -10.595068522808077) (= (c1 b_3) 266.9686345903941)
(= (a2 b_3) -15.695519093199998) (= (b2 b_3) 0.0) (= (c2 b_3) -471.1825793888697)
(= (a3 b_3) 0.0) (= (b3 b_3) 10.595068522808077) (= (c3 b_3) -100.67353429689763)
(= (a4 b_3) 15.695519093199998) (= (b4 b_3) 0.0) (= (c4 b_3) 637.4776796823662)
;;@box@ {"coordinates": [[10.736282132679543, 4.083553016526342], [-3.720036692778871, 4.083553016526342], [-3.720036692778871, 15.75627893807707], [10.736282132679543, 15.75627893807707]]}
(= (a1 b_4) 0.0) (= (b1 b_4) -14.456318825458414) (= (c1 b_4) -59.03314434756726)
(= (a2 b_4) -11.672725921550729) (= (b2 b_4) 0.0) (= (c2 b_4) 43.42296873291977)
(= (a3 b_4) 0.0) (= (b3 b_4) 14.456318825458414) (= (c3 b_4) 227.77779183169747)
(= (a4 b_4) 11.672725921550729) (= (b4 b_4) 0.0) (= (c4 b_4) 125.32167875121044)
;;@box@ {"coordinates": [[47.71252707614703, 22.258720058206706], [38.23210963995826, 22.258720058206706], [38.23210963995826, 30.32109091956613], [47.71252707614703, 30.32109091956613]]}
(= (a1 b_5) 0.0) (= (b1 b_5) -9.480417436188773) (= (c1 b_5) -211.02195774706763)
(= (a2 b_5) -8.062370861359426) (= (b2 b_5) 0.0) (= (c2 b_5) -308.2414467294983)
(= (a3 b_5) 0.0) (= (b3 b_5) 9.480417436188773) (= (c3 b_5) 287.45659903811986)
(= (a4 b_5) 8.062370861359426) (= (b4 b_5) 0.0) (= (c4 b_5) 384.6760880205505)
;;@box@ {"coordinates": [[17.324985590394107, -51.82974950975297], [3.483464709043103, -51.82974950975297], [3.483464709043103, -33.98983862370446], [17.324985590394107, -33.98983862370446]]}
(= (a1 b_6) 0.0) (= (b1 b_6) -13.841520881351004) (= (c1 b_6) 717.4025601144377)
(= (a2 b_6) -17.839910886048514) (= (b2 b_6) 0.0) (= (c2 b_6) -62.14469998402387)
(= (a3 b_6) 0.0) (= (b3 b_6) 13.841520881351004) (= (c3 b_6) -470.4710610637561)
(= (a4 b_6) 17.839910886048514) (= (b4 b_6) 0.0) (= (c4 b_6) 309.0761990347055)
;;@box@ {"coordinates": [[-12.716098950067607, 35.83329159947624], [-18.046636148863325, 35.83329159947624], [-18.046636148863325, 52.09067701554898], [-12.716098950067607, 52.09067701554898]]}
(= (a1 b_7) 0.0) (= (b1 b_7) -5.330537198795717) (= (c1 b_7) -191.01069382630217)
(= (a2 b_7) -16.257385416072736) (= (b2 b_7) 0.0) (= (c2 b_7) 293.39111933570166)
(= (a3 b_7) 0.0) (= (b3 b_7) 5.330537198795717) (= (c3 b_7) 277.6712915418369)
(= (a4 b_7) 16.257385416072736) (= (b4 b_7) 0.0) (= (c4 b_7) -206.73052162016697)
;;@box@ {"coordinates": [[6.324589122292908, -48.863217604302164], [-7.767404519659253, -48.863217604302164], [-7.767404519659253, -40.64726937124996], [6.324589122292908, -40.64726937124996]]}
(= (a1 b_8) 0.0) (= (b1 b_8) -14.091993641952161) (= (c1 b_8) 688.580151805151)
(= (a2 b_8) -8.215948233052202) (= (b2 b_8) 0.0) (= (c2 b_8) 63.81659343869613)
(= (a3 b_8) 0.0) (= (b3 b_8) 14.091993641952161) (= (c3 b_8) -572.8010615423713)
(= (a4 b_8) 8.215948233052202) (= (b4 b_8) 0.0) (= (c4 b_8) 51.962496824083594)
;;@box@ {"coordinates": [[-15.926876609797871, 41.667460953155086], [-25.440313831099843, 41.667460953155086], [-25.440313831099843, 44.19084137230948], [-15.926876609797871, 44.19084137230948]]}
(= (a1 b_9) 0.0) (= (b1 b_9) -9.513437221301972) (= (c1 b_9) -396.40077394889215)
(= (a2 b_9) -2.5233804191543925) (= (b2 b_9) 0.0) (= (c2 b_9) 64.19558977854001)
(= (a3 b_9) 0.0) (= (b3 b_9) 9.513437221301972) (= (c3 b_9) 420.4067951519801)
(= (a4 b_9) 2.5233804191543925) (= (b4 b_9) 0.0) (= (c4 b_9) -40.18956857545204)
;;@box@ {"coordinates": [[16.98388423637529, 12.376058110979926], [13.173898261669407, 12.376058110979926], [13.173898261669407, 26.2374877601751], [16.98388423637529, 26.2374877601751]]}
(= (a1 b_10) 0.0) (= (b1 b_10) -3.8099859747058815) (= (c1 b_10) -47.15260782497848)
(= (a2 b_10) -13.861429649195173) (= (b2 b_10) 0.0) (= (c2 b_10) -182.6090639597851)
(= (a3 b_10) 0.0) (= (b3 b_10) 3.8099859747058815) (= (c3 b_10) 99.96446037778436)
(= (a4 b_10) 13.861429649195173) (= (b4 b_10) 0.0) (= (c4 b_10) 235.42091651259096)
;;@box@ {"coordinates": [[-6.29166492129448, -21.56927758460848], [-22.386596431133672, -21.56927758460848], [-22.386596431133672, -4.148410893919452], [-6.29166492129448, -4.148410893919452]]}
(= (a1 b_11) 0.0) (= (b1 b_11) -16.094931509839192) (= (c1 b_11) 347.1560454409832)
(= (a2 b_11) -17.420866690689024) (= (b2 b_11) 0.0) (= (c2 b_11) 389.99391208503437)
(= (a3 b_11) 0.0) (= (b3 b_11) 16.094931509839192) (= (c3 b_11) -66.76838921230437)
(= (a4 b_11) 17.420866690689024) (= (b4 b_11) 0.0) (= (c4 b_11) -109.60625585635559)
;;@box@ {"coordinates": [[-26.61945840163121, -36.929580939398775], [-30.926397574514713, -36.929580939398775], [-30.926397574514713, -23.780515665857838], [-26.61945840163121, -23.780515665857838]]}
(= (a1 b_12) 0.0) (= (b1 b_12) -4.306939172883503) (= (c1 b_12) 159.05345878606855)
(= (a2 b_12) -13.149065273540938) (= (b2 b_12) 0.0) (= (c2 b_12) 406.6532203827721)
(= (a3 b_12) 0.0) (= (b3 b_12) 4.306939172883503) (= (c3 b_12) -102.42123447265294)
(= (a4 b_12) 13.149065273540938) (= (b4 b_12) 0.0) (= (c4 b_12) -350.0209960693565)
;;@box@ {"coordinates": [[32.970581307221025, -6.208447729570153], [13.158827382300432, -6.208447729570153], [13.158827382300432, 6.5795640851132475], [32.970581307221025, 6.5795640851132475]]}
(= (a1 b_13) 0.0) (= (b1 b_13) -19.811753924920595) (= (c1 b_13) 123.00023867397584)
(= (a2 b_13) -12.7880118146834) (= (b2 b_13) 0.0) (= (c2 b_13) -168.27524003223738)
(= (a3 b_13) 0.0) (= (b3 b_13) 19.811753924920595) (= (c3 b_13) 130.35270458750895)
(= (a4 b_13) 12.7880118146834) (= (b4 b_13) 0.0) (= (c4 b_13) 421.62818329372215)
;;@box@ {"coordinates": [[16.883394436744005, -54.195798308192764], [13.365886408214172, -54.195798308192764], [13.365886408214172, -35.90233844691538], [16.883394436744005, -35.90233844691538]]}
(= (a1 b_14) 0.0) (= (b1 b_14) -3.517508028529834) (= (c1 b_14) 190.63415566165165)
(= (a2 b_14) -18.293459861277384) (= (b2 b_14) 0.0) (= (c2 b_14) -244.5083065190589)
(= (a3 b_14) 0.0) (= (b3 b_14) 3.517508028529834) (= (c3 b_14) -126.28676373002017)
(= (a4 b_14) 18.293459861277384) (= (b4 b_14) 0.0) (= (c4 b_14) 308.85569845069034)
)
(:goal (and
        ;;@goal_location@[44, 33]
(= (x) 44) (= (y) 33)
	     )
)
)

