(define

;;@problem_name@v1_nb_45_001
(problem v1_nb_45_001)

(:domain motion_planning_v1)

(:objects b_0 b_1 b_2 b_3 b_4 b_5 b_6 b_7 b_8 b_9 b_10 b_11 b_12 b_13 b_14 b_15 b_16 b_17 b_18 b_19 b_20 b_21 b_22 b_23 b_24 b_25 b_26 b_27 b_28 b_29 b_30 b_31 b_32 b_33 b_34 b_35 b_36 b_37 b_38 b_39 b_40 b_41 b_42 b_43 b_44 - box)

(:init

    ;;@initial_location@[-48, -50]
(= (x) -48) (= (y) -50)

    ;;@bounding_box@ {"coordinates": [[54.0819432706837, -54.16348170858503], [-52.916661797183195, -54.16348170858503], [-52.916661797183195, 54.445473841168514], [54.0819432706837, 54.445473841168514]]}
(= (maxx) 54.0819432706837) (= (maxy) 54.445473841168514) (= (minx) -52.916661797183195) (= (miny) -54.16348170858503)

    ;;@box@ {"coordinates": [[47.89493950819961, -27.39146843053023], [37.909374606973316, -27.39146843053023], [37.909374606973316, -8.699921902331631], [47.89493950819961, -8.699921902331631]]}
(= (a1 b_0) 0.0) (= (b1 b_0) -9.985564901226297) (= (c1 b_0) 273.51928575295085)
(= (a2 b_0) -18.6915465281986) (= (b2 b_0) 0.0) (= (c2 b_0) -708.5848393211522)
(= (a3 b_0) 0.0) (= (b3 b_0) 9.985564901226297) (= (c3 b_0) -86.87363479133266)
(= (a4 b_0) 18.6915465281986) (= (b4 b_0) 0.0) (= (c4 b_0) 895.2304902827705)
;;@box@ {"coordinates": [[8.611979774890997, 43.47293446805303], [-0.7780581450463302, 43.47293446805303], [-0.7780581450463302, 54.445473841168514], [8.611979774890997, 54.445473841168514]]}
(= (a1 b_1) 0.0) (= (b1 b_1) -9.390037919937328) (= (c1 b_1) -408.21250314596847)
(= (a2 b_1) -10.972539373115481) (= (b2 b_1) 0.0) (= (c2 b_1) 8.537273631094054)
(= (a3 b_1) 0.0) (= (b3 b_1) 9.390037919937328) (= (c3 b_1) 511.2450639375282)
(= (a4 b_1) 10.972539373115481) (= (b4 b_1) 0.0) (= (c4 b_1) 94.49528716046567)
;;@box@ {"coordinates": [[12.086243945729084, -18.786587457395015], [9.454670377108737, -18.786587457395015], [9.454670377108737, -14.034845531467496], [12.086243945729084, -14.034845531467496]]}
(= (a1 b_2) 0.0) (= (b1 b_2) -2.6315735686203467) (= (c1 b_2) 49.43828699745524)
(= (a2 b_2) -4.751741925927519) (= (b2 b_2) 0.0) (= (c2 b_2) -44.92615362673253)
(= (a3 b_2) 0.0) (= (b3 b_2) 2.6315735686203467) (= (c3 b_2) -36.93372854027925)
(= (a4 b_2) 4.751741925927519) (= (b4 b_2) 0.0) (= (c4 b_2) 57.43071208390853)
;;@box@ {"coordinates": [[-25.951828658308447, -54.16348170858503], [-34.12918051422996, -54.16348170858503], [-34.12918051422996, -39.96013189012714], [-25.951828658308447, -39.96013189012714]]}
(= (a1 b_3) 0.0) (= (b1 b_3) -8.177351855921511) (= (c1 b_3) 442.91384767286866)
(= (a2 b_3) -14.203349818457895) (= (b2 b_3) 0.0) (= (c2 b_3) 484.7486898609048)
(= (a3 b_3) 0.0) (= (b3 b_3) 8.177351855921511) (= (c3 b_3) -326.7680586745995)
(= (a4 b_3) 14.203349818457895) (= (b4 b_3) 0.0) (= (c4 b_3) -368.60290086263564)
;;@box@ {"coordinates": [[-30.30207248173078, -47.9333565722833], [-49.747853493407874, -47.9333565722833], [-49.747853493407874, -40.92865902263949], [-30.30207248173078, -40.92865902263949]]}
(= (a1 b_4) 0.0) (= (b1 b_4) -19.445781011677095) (= (c1 b_4) 932.1015550592541)
(= (a2 b_4) -7.004697549643808) (= (b2 b_4) 0.0) (= (c2 b_4) 348.4686674653133)
(= (a3 b_4) 0.0) (= (b3 b_4) 19.445781011677095) (= (c3 b_4) -795.8897404558495)
(= (a4 b_4) 7.004697549643808) (= (b4 b_4) 0.0) (= (c4 b_4) -212.25685286190864)
;;@box@ {"coordinates": [[-9.04779157961978, 43.44046352182344], [-22.961061516261044, 43.44046352182344], [-22.961061516261044, 52.49634088059138], [-9.04779157961978, 52.49634088059138]]}
(= (a1 b_5) 0.0) (= (b1 b_5) -13.913269936641264) (= (c1 b_5) -604.3988951519475)
(= (a2 b_5) -9.055877358767944) (= (b2 b_5) 0.0) (= (c2 b_5) 207.93255711838634)
(= (a3 b_5) 0.0) (= (b3 b_5) 13.913269936641264) (= (c3 b_5) 730.3957613576039)
(= (a4 b_5) 9.055877358767944) (= (b4 b_5) 0.0) (= (c4 b_5) -81.93569091273001)
;;@box@ {"coordinates": [[49.58452877138752, -40.66398171264075], [30.922199341693833, -40.66398171264075], [30.922199341693833, -26.08332550485497], [49.58452877138752, -26.08332550485497]]}
(= (a1 b_6) 0.0) (= (b1 b_6) -18.662329429693685) (= (c1 b_6) 758.8846226443412)
(= (a2 b_6) -14.580656207785779) (= (b2 b_6) 0.0) (= (c2 b_6) -450.86595778985753)
(= (a3 b_6) 0.0) (= (b3 b_6) 18.662329429693685) (= (c3 b_6) -486.77561319353475)
(= (a4 b_6) 14.580656207785779) (= (b4 b_6) 0.0) (= (c4 b_6) 722.974967240664)
;;@box@ {"coordinates": [[19.398031910369756, 41.563381583421126], [-0.0781137631485116, 41.563381583421126], [-0.0781137631485116, 42.73156533104633], [19.398031910369756, 42.73156533104633]]}
(= (a1 b_7) 0.0) (= (b1 b_7) -19.476145673518268) (= (c1 b_7) -809.4944744027362)
(= (a2 b_7) -1.168183747625207) (= (b2 b_7) 0.0) (= (c2 b_7) 0.09125122857593607)
(= (a3 b_7) 0.0) (= (b3 b_7) 19.476145673518268) (= (c3 b_7) 832.2461912449212)
(= (a4 b_7) 1.168183747625207) (= (b4 b_7) 0.0) (= (c4 b_7) 22.660465613609095)
;;@box@ {"coordinates": [[51.745320585011704, 3.7516730381267474], [33.45769649582375, 3.7516730381267474], [33.45769649582375, 18.124304848850308], [51.745320585011704, 18.124304848850308]]}
(= (a1 b_8) 0.0) (= (b1 b_8) -18.287624089187958) (= (c1 b_8) -68.60918622680367)
(= (a2 b_8) -14.372631810723561) (= (b2 b_8) 0.0) (= (c2 b_8) -480.87515296941064)
(= (a3 b_8) 0.0) (= (b3 b_8) 18.287624089187958) (= (c3 b_8) 331.450473953621)
(= (a4 b_8) 14.372631810723561) (= (b4 b_8) 0.0) (= (c4 b_8) 743.7164406962279)
;;@box@ {"coordinates": [[-28.587410219021862, -13.952412787611387], [-32.553006924544576, -13.952412787611387], [-32.553006924544576, 4.542069627582272], [-28.587410219021862, 4.542069627582272]]}
(= (a1 b_9) 0.0) (= (b1 b_9) -3.9655967055227137) (= (c1 b_9) 55.3296421846447)
(= (a2 b_9) -18.49448241519366) (= (b2 b_9) 0.0) (= (c2 b_9) 602.051014127667)
(= (a3 b_9) 0.0) (= (b3 b_9) 3.9655967055227137) (= (c3 b_9) 18.012016351395037)
(= (a4 b_9) 18.49448241519366) (= (b4 b_9) 0.0) (= (c4 b_9) -528.7093555916273)
;;@box@ {"coordinates": [[-11.632552249157785, -28.391667895904014], [-21.08811558526635, -28.391667895904014], [-21.08811558526635, -17.85666256317704], [-11.632552249157785, -17.85666256317704]]}
(= (a1 b_10) 0.0) (= (b1 b_10) -9.455563336108566) (= (c1 b_10) 268.4592140074806)
(= (a2 b_10) -10.535005332726975) (= (b2 b_10) 0.0) (= (c2 b_10) 222.16341014794384)
(= (a3 b_10) 0.0) (= (b3 b_10) 9.455563336108566) (= (c3 b_10) -168.84480383763923)
(= (a4 b_10) 10.535005332726975) (= (b4 b_10) 0.0) (= (c4 b_10) -122.54899997810243)
;;@box@ {"coordinates": [[27.500511807037135, -4.866943154128997], [9.611190120215687, -4.866943154128997], [9.611190120215687, 3.576826419541227], [27.500511807037135, 3.576826419541227]]}
(= (a1 b_11) 0.0) (= (b1 b_11) -17.889321686821447) (= (c1 b_11) 87.06631171568704)
(= (a2 b_11) -8.443769573670224) (= (b2 b_11) 0.0) (= (c2 b_11) -81.15467470383707)
(= (a3 b_11) 0.0) (= (b3 b_11) 17.889321686821447) (= (c3 b_11) 63.98699843709478)
(= (a4 b_11) 8.443769573670224) (= (b4 b_11) 0.0) (= (c4 b_11) 232.2079848566189)
;;@box@ {"coordinates": [[49.87259606126304, 37.17138144810113], [44.166465848520374, 37.17138144810113], [44.166465848520374, 43.60924152719795], [49.87259606126304, 43.60924152719795]]}
(= (a1 b_12) 0.0) (= (b1 b_12) -5.706130212742664) (= (c1 b_12) -212.10474273039202)
(= (a2 b_12) -6.437860079096822) (= (b2 b_12) 0.0) (= (c2 b_12) -284.3375273209825)
(= (a3 b_12) 0.0) (= (b3 b_12) 5.706130212742664) (= (c3 b_12) 248.84001063313627)
(= (a4 b_12) 6.437860079096822) (= (b4 b_12) 0.0) (= (c4 b_12) 321.0727952237267)
;;@box@ {"coordinates": [[47.892685855506436, 39.44038099604718], [43.897722852896244, 39.44038099604718], [43.897722852896244, 44.858982173306075], [47.892685855506436, 44.858982173306075]]}
(= (a1 b_13) 0.0) (= (b1 b_13) -3.9949630026101914) (= (c1 b_13) -157.5628628880586)
(= (a2 b_13) -5.418601177258893) (= (b2 b_13) 0.0) (= (c2 b_13) -237.8642527296882)
(= (a3 b_13) 0.0) (= (b3 b_13) 3.9949630026101914) (= (c3 b_13) 179.2099741171079)
(= (a4 b_13) 5.418601177258893) (= (b4 b_13) 0.0) (= (c4 b_13) 259.5113639587375)
;;@box@ {"coordinates": [[-3.128687618183117, -11.239664674095618], [-10.85179353259206, -11.239664674095618], [-10.85179353259206, 0.0934858685742439], [-3.128687618183117, 0.0934858685742439]]}
(= (a1 b_14) 0.0) (= (b1 b_14) -7.723105914408944) (= (c1 b_14) 86.80512072048114)
(= (a2 b_14) -11.333150542669863) (= (b2 b_14) 0.0) (= (c2 b_14) 122.98500976283701)
(= (a3 b_14) 0.0) (= (b3 b_14) 7.723105914408944) (= (c3 b_14) 0.7220012644994003)
(= (a4 b_14) 11.333150542669863) (= (b4 b_14) 0.0) (= (c4 b_14) -35.45788777785647)
;;@box@ {"coordinates": [[27.544093469611912, 13.835062553369308], [16.096399215072065, 13.835062553369308], [16.096399215072065, 29.653258248907466], [27.544093469611912, 29.653258248907466]]}
(= (a1 b_15) 0.0) (= (b1 b_15) -11.447694254539847) (= (c1 b_15) -158.3795661034052)
(= (a2 b_15) -15.818195695538158) (= (b2 b_15) 0.0) (= (c2 b_15) -254.6159927775167)
(= (a3 b_15) 0.0) (= (b3 b_15) 11.447694254539847) (= (c3 b_15) 339.46143408440435)
(= (a4 b_15) 15.818195695538158) (= (b4 b_15) 0.0) (= (c4 b_15) 435.69786075851584)
;;@box@ {"coordinates": [[15.818689691787991, 18.550178525498534], [13.473205908069477, 18.550178525498534], [13.473205908069477, 24.193770895807337], [15.818689691787991, 24.193770895807337]]}
(= (a1 b_16) 0.0) (= (b1 b_16) -2.345483783718514) (= (c1 b_16) -43.50914291664022)
(= (a2 b_16) -5.643592370308802) (= (b2 b_16) 0.0) (= (c2 b_16) -76.03728206638039)
(= (a3 b_16) 0.0) (= (b3 b_16) 2.345483783718514) (= (c3 b_16) 56.74609730311705)
(= (a4 b_16) 5.643592370308802) (= (b4 b_16) 0.0) (= (c4 b_16) 89.27423645285721)
;;@box@ {"coordinates": [[50.777426334890244, 11.34397126985402], [40.55384882645273, 11.34397126985402], [40.55384882645273, 27.154658810852457], [50.777426334890244, 27.154658810852457]]}
(= (a1 b_17) 0.0) (= (b1 b_17) -10.223577508437515) (= (c1 b_17) -115.97596953084091)
(= (a2 b_17) -15.810687540998437) (= (b2 b_17) 0.0) (= (c2 b_17) -641.1842323799302)
(= (a3 b_17) 0.0) (= (b3 b_17) 10.223577508437515) (= (c3 b_17) 277.61775906792576)
(= (a4 b_17) 15.810687540998437) (= (b4 b_17) 0.0) (= (c4 b_17) 802.826021917015)
;;@box@ {"coordinates": [[40.15423216156809, -1.7718579245497104], [23.33865980476339, -1.7718579245497104], [23.33865980476339, 5.446364249005786], [40.15423216156809, 5.446364249005786]]}
(= (a1 b_18) 0.0) (= (b1 b_18) -16.815572356804697) (= (c1 b_18) 29.794805136243454)
(= (a2 b_18) -7.218222173555496) (= (b2 b_18) 0.0) (= (c2 b_18) -168.4636317038115)
(= (a3 b_18) 0.0) (= (b3 b_18) 16.815572356804697) (= (c3 b_18) 91.58373211067106)
(= (a4 b_18) 7.218222173555496) (= (b4 b_18) 0.0) (= (c4 b_18) 289.84216895072603)
;;@box@ {"coordinates": [[-11.572489947023495, 20.02744270117114], [-27.87980683536679, 20.02744270117114], [-27.87980683536679, 33.990639062389704], [-11.572489947023495, 33.990639062389704]]}
(= (a1 b_19) 0.0) (= (b1 b_19) -16.307316888343294) (= (c1 b_19) -326.59385459113577)
(= (a2 b_19) -13.963196361218564) (= (b2 b_19) 0.0) (= (c2 b_19) 389.29121735507)
(= (a3 b_19) 0.0) (= (b3 b_19) 16.307316888343294) (= (c3 b_19) 554.2961224276889)
(= (a4 b_19) 13.963196361218564) (= (b4 b_19) 0.0) (= (c4 b_19) -161.5889495185169)
;;@box@ {"coordinates": [[-27.622670168382815, -17.715324345148314], [-43.816636050737245, -17.715324345148314], [-43.816636050737245, -7.195087745470832], [-27.622670168382815, -7.195087745470832]]}
(= (a1 b_20) 0.0) (= (b1 b_20) -16.19396588235443) (= (c1 b_20) 286.88135804017463)
(= (a2 b_20) -10.520236599677482) (= (b2 b_20) 0.0) (= (c2 b_20) 460.9613782557137)
(= (a3 b_20) 0.0) (= (b3 b_20) 16.19396588235443) (= (c3 b_20) -116.51700547070111)
(= (a4 b_20) 10.520236599677482) (= (b4 b_20) 0.0) (= (c4 b_20) -290.5970256862402)
;;@box@ {"coordinates": [[-17.679801267461084, -2.9516127387396125], [-22.044015106807212, -2.9516127387396125], [-22.044015106807212, 0.6503989089971893], [-17.679801267461084, 0.6503989089971893]]}
(= (a1 b_21) 0.0) (= (b1 b_21) -4.364213839346128) (= (c1 b_21) 12.881469162797744)
(= (a2 b_21) -3.602011647736802) (= (b2 b_21) 0.0) (= (c2 b_21) 79.4027991776056)
(= (a3 b_21) 0.0) (= (b3 b_21) 4.364213839346128) (= (c3 b_21) 2.8384799197411565)
(= (a4 b_21) 3.602011647736802) (= (b4 b_21) 0.0) (= (c4 b_21) -63.6828500950667)
;;@box@ {"coordinates": [[-15.185777664211006, 35.47743596691002], [-31.40886314499978, 35.47743596691002], [-31.40886314499978, 47.89809812070207], [-15.185777664211006, 47.89809812070207]]}
(= (a1 b_22) 0.0) (= (b1 b_22) -16.223085480788775) (= (c1 b_22) -575.5534763303915)
(= (a2 b_22) -12.420662153792051) (= (b2 b_22) 0.0) (= (c2 b_22) 390.11887775873276)
(= (a3 b_22) 0.0) (= (b3 b_22) 16.223085480788775) (= (c3 b_22) 777.0549401793579)
(= (a4 b_22) 12.420662153792051) (= (b4 b_22) 0.0) (= (c4 b_22) -188.6174139097663)
;;@box@ {"coordinates": [[6.718222621615718, 28.519960340044108], [-12.317901259040434, 28.519960340044108], [-12.317901259040434, 45.85649954977178], [6.718222621615718, 45.85649954977178]]}
(= (a1 b_23) 0.0) (= (b1 b_23) -19.036123880656152) (= (c1 b_23) -542.90949810448)
(= (a2 b_23) -17.336539209727675) (= (b2 b_23) 0.0) (= (c2 b_23) 213.5497781589084)
(= (a3 b_23) 0.0) (= (b3 b_23) 19.036123880656152) (= (c3 b_23) 872.9300061627088)
(= (a4 b_23) 17.336539209727675) (= (b4 b_23) 0.0) (= (c4 b_23) 116.47072989932035)
;;@box@ {"coordinates": [[-24.88016454604295, -33.048830250485004], [-29.06282360768838, -33.048830250485004], [-29.06282360768838, -17.00104728290514], [-24.88016454604295, -17.00104728290514]]}
(= (a1 b_24) 0.0) (= (b1 b_24) -4.182659061645431) (= (c1 b_24) 138.23198932397275)
(= (a2 b_24) -16.047782967579863) (= (b2 b_24) 0.0) (= (c2 b_24) 466.3938856812395)
(= (a3 b_24) 0.0) (= (b3 b_24) 4.182659061645431) (= (c3 b_24) -71.10958447530562)
(= (a4 b_24) 16.047782967579863) (= (b4 b_24) 0.0) (= (c4 b_24) -399.2714808325724)
;;@box@ {"coordinates": [[32.71493268005663, 24.70805200205783], [30.44542364719364, 24.70805200205783], [30.44542364719364, 41.39363461724898], [32.71493268005663, 41.39363461724898]]}
(= (a1 b_25) 0.0) (= (b1 b_25) -2.269509032862988) (= (c1 b_25) -56.07514720311868)
(= (a2 b_25) -16.685582615191148) (= (b2 b_25) 0.0) (= (c2 b_25) -507.9996315197437)
(= (a3 b_25) 0.0) (= (b3 b_25) 2.269509032862988) (= (c3 b_25) 93.94322766687664)
(= (a4 b_25) 16.685582615191148) (= (b4 b_25) 0.0) (= (c4 b_25) 545.8677119835016)
;;@box@ {"coordinates": [[-4.7601878651549, -30.089495924802428], [-16.426575208632745, -30.089495924802428], [-16.426575208632745, -26.336942464790596], [-4.7601878651549, -26.336942464790596]]}
(= (a1 b_26) 0.0) (= (b1 b_26) -11.666387343477844) (= (c1 b_26) 351.0357144287432)
(= (a2 b_26) -3.752553460011832) (= (b2 b_26) 0.0) (= (c2 b_26) 61.64160163529939)
(= (a3 b_26) 0.0) (= (b3 b_26) 11.666387343477844) (= (c3 b_26) -307.2569722371372)
(= (a4 b_26) 3.752553460011832) (= (b4 b_26) 0.0) (= (c4 b_26) -17.862859443693356)
;;@box@ {"coordinates": [[-22.96999258753297, 20.54752655760273], [-34.618307010839224, 20.54752655760273], [-34.618307010839224, 24.32488206834106], [-22.96999258753297, 24.32488206834106]]}
(= (a1 b_27) 0.0) (= (b1 b_27) -11.648314423306253) (= (c1 b_27) -239.34404996419215)
(= (a2 b_27) -3.7773555107383316) (= (b2 b_27) 0.0) (= (c2 b_27) 130.76565275982497)
(= (a3 b_27) 0.0) (= (b3 b_27) 11.648314423306253) (= (c3 b_27) 283.3438746418808)
(= (a4 b_27) 3.7773555107383316) (= (b4 b_27) 0.0) (= (c4 b_27) -86.7658280821363)
;;@box@ {"coordinates": [[8.215666859476038, -22.3277772091303], [-4.528432704258144, -22.3277772091303], [-4.528432704258144, -8.415514940503943], [8.215666859476038, -8.415514940503943]]}
(= (a1 b_28) 0.0) (= (b1 b_28) -12.744099563734181) (= (c1 b_28) 284.54741579003144)
(= (a2 b_28) -13.912262268626357) (= (b2 b_28) 0.0) (= (c2 b_28) 63.000743447464195)
(= (a3 b_28) 0.0) (= (b3 b_28) 12.744099563734181) (= (c3 b_28) -107.24816028187479)
(= (a4 b_28) 13.912262268626357) (= (b4 b_28) 0.0) (= (c4 b_28) 114.29851206069247)
;;@box@ {"coordinates": [[7.653465343634934, -50.85902684022078], [3.0186077473159125, -50.85902684022078], [3.0186077473159125, -45.609725965341525], [7.653465343634934, -45.609725965341525]]}
(= (a1 b_29) 0.0) (= (b1 b_29) -4.634857596319021) (= (c1 b_29) 235.72434689179025)
(= (a2 b_29) -5.249300874879253) (= (b2 b_29) 0.0) (= (c2 b_29) -15.845580288902712)
(= (a3 b_29) 0.0) (= (b3 b_29) 4.634857596319021) (= (c3 b_29) -211.39458485649206)
(= (a4 b_29) 5.249300874879253) (= (b4 b_29) 0.0) (= (c4 b_29) 40.175342324200905)
;;@box@ {"coordinates": [[22.200017605595303, -53.57548635311664], [14.299768418568862, -53.57548635311664], [14.299768418568862, -44.21039866148383], [22.200017605595303, -44.21039866148383]]}
(= (a1 b_30) 0.0) (= (b1 b_30) -7.900249187026441) (= (c1 b_30) 423.2596925057559)
(= (a2 b_30) -9.365087691632809) (= (b2 b_30) 0.0) (= (c2 b_30) -133.9185852099388)
(= (a3 b_30) 0.0) (= (b3 b_30) 7.900249187026441) (= (c3 b_30) -349.2731660835025)
(= (a4 b_30) 9.365087691632809) (= (b4 b_30) 0.0) (= (c4 b_30) 207.90511163219222)
;;@box@ {"coordinates": [[48.81674039121825, 10.34209355443246], [39.792096609146284, 10.34209355443246], [39.792096609146284, 19.354781634664], [48.81674039121825, 19.354781634664]]}
(= (a1 b_31) 0.0) (= (b1 b_31) -9.024643782071962) (= (c1 b_31) -93.33371028961541)
(= (a2 b_31) -9.012688080231541) (= (b2 b_31) 0.0) (= (c2 b_31) -358.6337547966746)
(= (a3 b_31) 0.0) (= (b3 b_31) 9.024643782071962) (= (c3 b_31) 174.6700097326311)
(= (a4 b_31) 9.012688080231541) (= (b4 b_31) 0.0) (= (c4 b_31) 439.97005423969034)
;;@box@ {"coordinates": [[32.594643644889096, 20.346445761023713], [21.742451937867166, 20.346445761023713], [21.742451937867166, 35.73035762511291], [32.594643644889096, 35.73035762511291]]}
(= (a1 b_32) 0.0) (= (b1 b_32) -10.85219170702193) (= (c1 b_32) -220.80352995515304)
(= (a2 b_32) -15.383911864089196) (= (b2 b_32) 0.0) (= (c2 b_32) -334.4839643213438)
(= (a3 b_32) 0.0) (= (b3 b_32) 10.85219170702193) (= (c3 b_32) 387.7526907081781)
(= (a4 b_32) 15.383911864089196) (= (b4 b_32) 0.0) (= (c4 b_32) 501.4331250743689)
;;@box@ {"coordinates": [[14.934860041830383, -51.383053557916924], [3.226012144988055, -51.383053557916924], [3.226012144988055, -44.57899656398308], [14.934860041830383, -44.57899656398308]]}
(= (a1 b_33) 0.0) (= (b1 b_33) -11.708847896842329) (= (c1 b_33) 601.6363585849523)
(= (a2 b_33) -6.804056993933841) (= (b2 b_33) 0.0) (= (c2 b_33) -21.94997049762149)
(= (a3 b_33) 0.0) (= (b3 b_33) 11.708847896842329) (= (c3 b_33) -521.9686901615347)
(= (a4 b_33) 6.804056993933841) (= (b4 b_33) 0.0) (= (c4 b_33) 101.61763892103907)
;;@box@ {"coordinates": [[54.0819432706837, 5.525666097981706], [39.81605424618183, 5.525666097981706], [39.81605424618183, 8.87055860391623], [54.0819432706837, 8.87055860391623]]}
(= (a1 b_34) 0.0) (= (b1 b_34) -14.265889024501874) (= (c1 b_34) -78.82853934025931)
(= (a2 b_34) -3.3448925059345243) (= (b2 b_34) 0.0) (= (c2 b_34) -133.18042146393609)
(= (a3 b_34) 0.0) (= (b3 b_34) 14.265889024501874) (= (c3 b_34) 126.54640462880921)
(= (a4 b_34) 3.3448925059345243) (= (b4 b_34) 0.0) (= (c4 b_34) 180.898286752486)
;;@box@ {"coordinates": [[-21.349192816492142, -11.123258671303658], [-36.7748069548324, -11.123258671303658], [-36.7748069548324, -2.613994589854828], [-21.349192816492142, -2.613994589854828]]}
(= (a1 b_35) 0.0) (= (b1 b_35) -15.425614138340258) (= (c1 b_35) 171.58309622447757)
(= (a2 b_35) -8.50926408144883) (= (b2 b_35) 0.0) (= (c2 b_35) 312.92654392297)
(= (a3 b_35) 0.0) (= (b3 b_35) 15.425614138340258) (= (c3 b_35) -40.32247190280958)
(= (a4 b_35) 8.50926408144883) (= (b4 b_35) 0.0) (= (c4 b_35) -181.66591960130197)
;;@box@ {"coordinates": [[37.23355855054437, 6.537865326141304], [34.11462009557978, 6.537865326141304], [34.11462009557978, 15.377616766292203], [37.23355855054437, 15.377616766292203]]}
(= (a1 b_36) 0.0) (= (b1 b_36) -3.118938454964592) (= (c1 b_36) -20.39119957908174)
(= (a2 b_36) -8.839751440150899) (= (b2 b_36) 0.0) (= (c2 b_36) -301.56476212010216)
(= (a3 b_36) 0.0) (= (b3 b_36) 3.118938454964592) (= (c3 b_36) 47.961840278097014)
(= (a4 b_36) 8.839751440150899) (= (b4 b_36) 0.0) (= (c4 b_36) 329.1354028191174)
;;@box@ {"coordinates": [[37.85425144821099, 17.424801698303117], [19.516494941631123, 17.424801698303117], [19.516494941631123, 32.122761434298994], [37.85425144821099, 32.122761434298994]]}
(= (a1 b_37) 0.0) (= (b1 b_37) -18.337756506579865) (= (c1 b_37) -319.53177071892185)
(= (a2 b_37) -14.697959735995877) (= (b2 b_37) 0.0) (= (c2 b_37) -286.8526568398614)
(= (a3 b_37) 0.0) (= (b3 b_37) 18.337756506579865) (= (c3 b_37) 589.0593775011291)
(= (a4 b_37) 14.697959735995877) (= (b4 b_37) 0.0) (= (c4 b_37) 556.3802636220687)
;;@box@ {"coordinates": [[-9.326149069233976, -38.399983995010786], [-14.687925981967128, -38.399983995010786], [-14.687925981967128, -36.19786604722157], [-9.326149069233976, -36.19786604722157]]}
(= (a1 b_38) 0.0) (= (b1 b_38) -5.361776912733152) (= (c1 b_38) 205.89214763377137)
(= (a2 b_38) -2.202117947789219) (= (b2 b_38) 0.0) (= (c2 b_38) 32.3445454206894)
(= (a3 b_38) 0.0) (= (b3 b_38) 5.361776912733152) (= (c3 b_38) -194.08488246219983)
(= (a4 b_38) 2.202117947789219) (= (b4 b_38) 0.0) (= (c4 b_38) -20.537280249117856)
;;@box@ {"coordinates": [[7.752439657310506, 29.28472525766976], [-6.0695605372850165, 29.28472525766976], [-6.0695605372850165, 30.831323308834772], [7.752439657310506, 30.831323308834772]]}
(= (a1 b_39) 0.0) (= (b1 b_39) -13.822000194595523) (= (c1 b_39) -404.7734782101878)
(= (a2 b_39) -1.546598051165013) (= (b2 b_39) 0.0) (= (c2 b_39) 9.387170498393075)
(= (a3 b_39) 0.0) (= (b3 b_39) 13.822000194595523) (= (c3 b_39) 426.1505567743517)
(= (a4 b_39) 1.546598051165013) (= (b4 b_39) 0.0) (= (c4 b_39) 11.989908065770791)
;;@box@ {"coordinates": [[-38.046577557367, 44.02119303824716], [-52.916661797183195, 44.02119303824716], [-52.916661797183195, 45.357201865336435], [-38.046577557367, 45.357201865336435]]}
(= (a1 b_40) 0.0) (= (b1 b_40) -14.870084239816194) (= (c1 b_40) -654.5988488159455)
(= (a2 b_40) -1.3360088270892732) (= (b2 b_40) 0.0) (= (c2 b_40) 70.69712726113447)
(= (a3 b_40) 0.0) (= (b3 b_40) 14.870084239816194) (= (c3 b_40) 674.465412619901)
(= (a4 b_40) 1.3360088270892732) (= (b4 b_40) 0.0) (= (c4 b_40) -50.830563457178954)
;;@box@ {"coordinates": [[39.09643276766032, -34.59466092313902], [37.518436145315675, -34.59466092313902], [37.518436145315675, -19.265394207504144], [39.09643276766032, -19.265394207504144]]}
(= (a1 b_41) 0.0) (= (b1 b_41) -1.5779966223446422) (= (c1 b_41) 54.590258087871554)
(= (a2 b_41) -15.329266715634873) (= (b2 b_41) 0.0) (= (c2 b_41) -575.1301144250599)
(= (a3 b_41) 0.0) (= (b3 b_41) 1.5779966223446422) (= (c3 b_41) -30.400726987579574)
(= (a4 b_41) 15.329266715634873) (= (b4 b_41) 0.0) (= (c4 b_41) 599.3196455253519)
;;@box@ {"coordinates": [[45.715050329380446, -31.633436754518264], [32.88475027908039, -31.633436754518264], [32.88475027908039, -19.687595224747277], [45.715050329380446, -19.687595224747277]]}
(= (a1 b_42) 0.0) (= (b1 b_42) -12.830300050300053) (= (c1 b_42) 405.86648518265923)
(= (a2 b_42) -11.945841529770988) (= (b2 b_42) 0.0) (= (c2 b_42) -392.8360155799866)
(= (a3 b_42) 0.0) (= (b3 b_42) 12.830300050300053) (= (c3 b_42) -252.59775400236208)
(= (a4 b_42) 11.945841529770988) (= (b4 b_42) 0.0) (= (c4 b_42) 546.1047467602838)
;;@box@ {"coordinates": [[-3.396632339552834, 21.15313466742757], [-13.117107717635935, 21.15313466742757], [-13.117107717635935, 27.156750762489278], [-3.396632339552834, 27.156750762489278]]}
(= (a1 b_43) 0.0) (= (b1 b_43) -9.720475378083101) (= (c1 b_43) -205.61852470400575)
(= (a2 b_43) -6.003616095061709) (= (b2 b_43) 0.0) (= (c2 b_43) 78.75007901425725)
(= (a3 b_43) 0.0) (= (b3 b_43) 9.720475378083101) (= (c3 b_43) 263.9765271355165)
(= (a4 b_43) 6.003616095061709) (= (b4 b_43) 0.0) (= (c4 b_43) -20.3920765827465)
;;@box@ {"coordinates": [[-15.325478100101044, 14.858622446318794], [-26.247985527595937, 14.858622446318794], [-26.247985527595937, 16.039794081894126], [-15.325478100101044, 16.039794081894126]]}
(= (a1 b_44) 0.0) (= (b1 b_44) -10.922507427494892) (= (c1 b_44) -162.29341403225936)
(= (a2 b_44) -1.181171635575332) (= (b2 b_44) 0.0) (= (c2 b_44) 31.003375996188133)
(= (a3 b_44) 0.0) (= (b3 b_44) 10.922507427494892) (= (c3 b_44) 175.1947699949772)
(= (a4 b_44) 1.181171635575332) (= (b4 b_44) 0.0) (= (c4 b_44) -18.102020033470282)
)
(:goal (and
        ;;@goal_location@[44, 29]
(= (x) 44) (= (y) 29)
	     )
)
)

