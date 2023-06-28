(define

;;@problem_name@v1_nb_35_001
(problem v1_nb_35_001)

(:domain motion_planning_v1)

(:objects b_0 b_1 b_2 b_3 b_4 b_5 b_6 b_7 b_8 b_9 b_10 b_11 b_12 b_13 b_14 b_15 b_16 b_17 b_18 b_19 b_20 b_21 b_22 b_23 b_24 b_25 b_26 b_27 b_28 b_29 b_30 b_31 b_32 b_33 b_34 - box)

(:init

    ;;@initial_location@[-43, -29]
(= (x) -43) (= (y) -29)

    ;;@bounding_box@ {"coordinates": [[51.9823044605346, -54.74158932964849], [-52.11816462393129, -54.74158932964849], [-52.11816462393129, 53.352668418523294], [51.9823044605346, 53.352668418523294]]}
(= (maxx) 51.9823044605346) (= (maxy) 53.352668418523294) (= (minx) -52.11816462393129) (= (miny) -54.74158932964849)

    ;;@box@ {"coordinates": [[-28.81199255724878, 36.96363942710018], [-47.569528245488705, 36.96363942710018], [-47.569528245488705, 45.5465052519254], [-28.81199255724878, 45.5465052519254]]}
(= (a1 b_0) 0.0) (= (b1 b_0) -18.757535688239926) (= (c1 b_0) -693.3467857210641)
(= (a2 b_0) -8.58286582482522) (= (b2 b_0) 0.0) (= (c2 b_0) 408.282878281263)
(= (a3 b_0) 0.0) (= (b3 b_0) 18.757535688239926) (= (c3 b_0) 854.340197737598)
(= (a4 b_0) 8.58286582482522) (= (b4 b_0) 0.0) (= (c4 b_0) -247.28946626472913)
;;@box@ {"coordinates": [[-35.70855725629508, 0.6436619905206733], [-52.11816462393129, 0.6436619905206733], [-52.11816462393129, 15.105483605145434], [-35.70855725629508, 15.105483605145434]]}
(= (a1 b_1) 0.0) (= (b1 b_1) -16.409607367636212) (= (c1 b_1) -10.56224054191543)
(= (a2 b_1) -14.46182161462476) (= (b2 b_1) 0.0) (= (c2 b_1) 753.7235996729411)
(= (a3 b_1) 0.0) (= (b3 b_1) 16.409607367636212) (= (c3 b_1) 247.87505505870251)
(= (a4 b_1) 14.46182161462476) (= (b4 b_1) 0.0) (= (c4 b_1) -516.410785156154)
;;@box@ {"coordinates": [[44.009457854816574, 22.38519721600443], [35.649076923793686, 22.38519721600443], [35.649076923793686, 28.046510560196253], [44.009457854816574, 28.046510560196253]]}
(= (a1 b_2) 0.0) (= (b1 b_2) -8.360380931022888) (= (c1 b_2) -187.14877594187007)
(= (a2 b_2) -5.661313344191825) (= (b2 b_2) 0.0) (= (c2 b_2) -201.82059489679406)
(= (a3 b_2) 0.0) (= (b3 b_2) 8.360380931022888) (= (c3 b_2) 234.47951206919683)
(= (a4 b_2) 5.661313344191825) (= (b4 b_2) 0.0) (= (c4 b_2) 249.1513310241208)
;;@box@ {"coordinates": [[-28.31758383253085, 41.162912226929905], [-44.69237466292545, 41.162912226929905], [-44.69237466292545, 45.76932689295461], [-28.31758383253085, 45.76932689295461]]}
(= (a1 b_3) 0.0) (= (b1 b_3) -16.374790830394602) (= (c1 b_3) -674.0340776858696)
(= (a2 b_3) -4.606414666024705) (= (b2 b_3) 0.0) (= (c2 b_3) 205.87161010677073)
(= (a3 b_3) 0.0) (= (b3 b_3) 16.374790830394602) (= (c3 b_3) 749.4631543200862)
(= (a4 b_3) 4.606414666024705) (= (b4 b_3) 0.0) (= (c4 b_3) -130.44253347255417)
;;@box@ {"coordinates": [[-12.761689935415143, 1.624794306618112], [-26.902460427331143, 1.624794306618112], [-26.902460427331143, 2.890043264368048], [-12.761689935415143, 2.890043264368048]]}
(= (a1 b_4) 0.0) (= (b1 b_4) -14.140770491916) (= (c1 b_4) -22.975843386458514)
(= (a2 b_4) -1.2652489577499357) (= (b2 b_4) 0.0) (= (c2 b_4) 34.03831001658962)
(= (a3 b_4) 0.0) (= (b3 b_4) 14.140770491916) (= (c3 b_4) 40.86743851313628)
(= (a4 b_4) 1.2652489577499357) (= (b4 b_4) 0.0) (= (c4 b_4) -16.146714889911856)
;;@box@ {"coordinates": [[-18.696052052092426, -24.354281350232505], [-22.166570225150508, -24.354281350232505], [-22.166570225150508, -12.552459121273138], [-18.696052052092426, -12.552459121273138]]}
(= (a1 b_5) 0.0) (= (b1 b_5) -3.470518173058082) (= (c1 b_5) 84.52197601775143)
(= (a2 b_5) -11.801822228959367) (= (b2 b_5) 0.0) (= (c2 b_5) 261.6059212229701)
(= (a3 b_5) 0.0) (= (b3 b_5) 3.470518173058082) (= (c3 b_5) -43.563537496947106)
(= (a4 b_5) 11.801822228959367) (= (b4 b_5) 0.0) (= (c4 b_5) -220.64748270216577)
;;@box@ {"coordinates": [[30.849060938590704, 1.7599173829032604], [21.3073518806467, 1.7599173829032604], [21.3073518806467, 7.279675184268378], [30.849060938590704, 7.279675184268378]]}
(= (a1 b_6) 0.0) (= (b1 b_6) -9.541709057944004) (= (c1 b_6) -16.792619633681145)
(= (a2 b_6) -5.519757801365117) (= (b2 b_6) 0.0) (= (c2 b_6) -117.6114217696313)
(= (a3 b_6) 0.0) (= (b3 b_6) 9.541709057944004) (= (c3 b_6) 69.46054264462377)
(= (a4 b_6) 5.519757801365117) (= (b4 b_6) 0.0) (= (c4 b_6) 170.27934478057392)
;;@box@ {"coordinates": [[-13.565134800271586, -37.92553974768577], [-22.838196108338423, -37.92553974768577], [-22.838196108338423, -34.38120874117761], [-13.565134800271586, -34.38120874117761]]}
(= (a1 b_7) 0.0) (= (b1 b_7) -9.273061308066836) (= (c1 b_7) 351.68585522181576)
(= (a2 b_7) -3.544331006508159) (= (b2 b_7) 0.0) (= (c2 b_7) 80.94612659949784)
(= (a3 b_7) 0.0) (= (b3 b_7) 9.273061308066836) (= (c3 b_7) -318.8190565023834)
(= (a4 b_7) 3.544331006508159) (= (b4 b_7) 0.0) (= (c4 b_7) -48.07932788006545)
;;@box@ {"coordinates": [[-24.44187827319609, -32.71892717555578], [-40.74198741074867, -32.71892717555578], [-40.74198741074867, -25.431565266599957], [-24.44187827319609, -25.431565266599957]]}
(= (a1 b_8) 0.0) (= (b1 b_8) -16.30010913755258) (= (c1 b_8) 533.3220838251942)
(= (a2 b_8) -7.28736190895582) (= (b2 b_8) 0.0) (= (c2 b_8) 296.9016071522474)
(= (a3 b_8) 0.0) (= (b3 b_8) 16.30010913755258) (= (c3 b_8) -414.5372893843708)
(= (a4 b_8) 7.28736190895582) (= (b4 b_8) 0.0) (= (c4 b_8) -178.11681271142402)
;;@box@ {"coordinates": [[33.51769235086329, 9.819603145509738], [27.582381525284625, 9.819603145509738], [27.582381525284625, 17.6751341737287], [33.51769235086329, 17.6751341737287]]}
(= (a1 b_9) 0.0) (= (b1 b_9) -5.935310825578668) (= (c1 b_9) -58.28239685243029)
(= (a2 b_9) -7.855531028218962) (= (b2 b_9) 0.0) (= (c2 b_9) -216.67425390404685)
(= (a3 b_9) 0.0) (= (b3 b_9) 5.935310825578668) (= (c3 b_9) 104.90741520488743)
(= (a4 b_9) 7.855531028218962) (= (b4 b_9) 0.0) (= (c4 b_9) 263.29927225650397)
;;@box@ {"coordinates": [[6.589356110169707, -51.73990965352948], [0.18535459151116696, -51.73990965352948], [0.18535459151116696, -32.1326256317664], [6.589356110169707, -32.1326256317664]]}
(= (a1 b_10) 0.0) (= (b1 b_10) -6.404001518658539) (= (c1 b_10) 331.3424599964584)
(= (a2 b_10) -19.60728402176308) (= (b2 b_10) 0.0) (= (c2 b_10) -3.634300120497326)
(= (a3 b_10) 0.0) (= (b3 b_10) 6.404001518658539) (= (c3 b_10) -205.77738334431834)
(= (a4 b_10) 19.60728402176308) (= (b4 b_10) 0.0) (= (c4 b_10) 129.1993767726374)
;;@box@ {"coordinates": [[-23.22183534859579, 29.691010235011206], [-31.73642442376847, 29.691010235011206], [-31.73642442376847, 38.24356240147945], [-23.22183534859579, 38.24356240147945]]}
(= (a1 b_11) 0.0) (= (b1 b_11) -8.51458907517268) (= (c1 b_11) -252.80675137786662)
(= (a2 b_11) -8.552552166468246) (= (b2 b_11) 0.0) (= (c2 b_11) 271.4274254614568)
(= (a3 b_11) 0.0) (= (b3 b_11) 8.51458907517268) (= (c3 b_11) 325.62821861932156)
(= (a4 b_11) 8.552552166468246) (= (b4 b_11) 0.0) (= (c4 b_11) -198.6059582200018)
;;@box@ {"coordinates": [[-32.476163463395466, -39.251074403833705], [-40.29190100212817, -39.251074403833705], [-40.29190100212817, -33.393726385508465], [-32.476163463395466, -33.393726385508465]]}
(= (a1 b_12) 0.0) (= (b1 b_12) -7.815737538732705) (= (c1 b_12) 306.77609565363355)
(= (a2 b_12) -5.85734801832524) (= (b2 b_12) 0.0) (= (c2 b_12) 236.0036864893722)
(= (a3 b_12) 0.0) (= (b3 b_12) 7.815737538732705) (= (c3 b_12) -260.99660086938735)
(= (a4 b_12) 5.85734801832524) (= (b4 b_12) 0.0) (= (c4 b_12) -190.224191705126)
;;@box@ {"coordinates": [[5.369979077515151, -15.106854236815632], [-13.974222068298285, -15.106854236815632], [-13.974222068298285, 2.222188580629105], [5.369979077515151, 2.222188580629105]]}
(= (a1 b_13) 0.0) (= (b1 b_13) -19.344201145813436) (= (c1 b_13) 292.2300270374455)
(= (a2 b_13) -17.329042817444737) (= (b2 b_13) 0.0) (= (c2 b_13) 242.15989256202215)
(= (a3 b_13) 0.0) (= (b3 b_13) 19.344201145813436) (= (c3 b_13) 42.98646288761906)
(= (a4 b_13) 17.329042817444737) (= (b4 b_13) 0.0) (= (c4 b_13) 93.05659736304243)
;;@box@ {"coordinates": [[-38.78349069840779, -23.461325004989437], [-47.258708861988396, -23.461325004989437], [-47.258708861988396, -15.016108137014275], [-38.78349069840779, -15.016108137014275]]}
(= (a1 b_14) 0.0) (= (b1 b_14) -8.475218163580607) (= (c1 b_14) 198.83984782395436)
(= (a2 b_14) -8.445216867975162) (= (b2 b_14) 0.0) (= (c2 b_14) 399.1100452399917)
(= (a3 b_14) 0.0) (= (b3 b_14) 8.475218163580607) (= (c3 b_14) -127.26479242911392)
(= (a4 b_14) 8.445216867975162) (= (b4 b_14) 0.0) (= (c4 b_14) -327.53498984515124)
;;@box@ {"coordinates": [[-39.16612664164325, 18.812042479380835], [-51.624346142999734, 18.812042479380835], [-51.624346142999734, 20.84988358525473], [-39.16612664164325, 20.84988358525473]]}
(= (a1 b_15) 0.0) (= (b1 b_15) -12.458219501356481) (= (c1 b_15) -234.36455447696886)
(= (a2 b_15) -2.0378411058738948) (= (b2 b_15) 0.0) (= (c2 b_15) 105.20221463406732)
(= (a3 b_15) 0.0) (= (b3 b_15) 12.458219501356481) (= (c3 b_15) 259.75242628283286)
(= (a4 b_15) 2.0378411058738948) (= (b4 b_15) 0.0) (= (c4 b_15) -79.8143428282033)
;;@box@ {"coordinates": [[-25.83092502737552, -38.69039944371169], [-28.12301873795488, -38.69039944371169], [-28.12301873795488, -24.052011011729956], [-25.83092502737552, -24.052011011729956]]}
(= (a1 b_16) 0.0) (= (b1 b_16) -2.2920937105793584) (= (c1 b_16) 88.68202122473467)
(= (a2 b_16) -14.638388431981735) (= (b2 b_16) 0.0) (= (c2 b_16) 411.67567216608427)
(= (a3 b_16) 0.0) (= (b3 b_16) 2.2920937105793584) (= (c3 b_16) -55.1294631667717)
(= (a4 b_16) 14.638388431981735) (= (b4 b_16) 0.0) (= (c4 b_16) -378.1231141081213)
;;@box@ {"coordinates": [[32.2478651061057, 24.12824047364043], [18.014904584904148, 24.12824047364043], [18.014904584904148, 26.582301043856347], [32.2478651061057, 26.582301043856347]]}
(= (a1 b_17) 0.0) (= (b1 b_17) -14.232960521201552) (= (c1 b_17) -343.4162941073817)
(= (a2 b_17) -2.4540605702159155) (= (b2 b_17) 0.0) (= (c2 b_17) -44.20966701801518)
(= (a3 b_17) 0.0) (= (b3 b_17) 14.232960521201552) (= (c3 b_17) 378.3448413199022)
(= (a4 b_17) 2.4540605702159155) (= (b4 b_17) 0.0) (= (c4 b_17) 79.13821423053568)
;;@box@ {"coordinates": [[-29.94411749854583, -9.3462069998686], [-42.02911026180556, -9.3462069998686], [-42.02911026180556, -1.3773666110630085], [-29.94411749854583, -1.3773666110630085]]}
(= (a1 b_18) 0.0) (= (b1 b_18) -12.084992763259734) (= (c1 b_18) 112.94884395733952)
(= (a2 b_18) -7.968840388805592) (= (b2 b_18) 0.0) (= (c2 b_18) 334.92327135983976)
(= (a3 b_18) 0.0) (= (b3 b_18) 12.084992763259734) (= (c3 b_18) -16.645465527052043)
(= (a4 b_18) 7.968840388805592) (= (b4 b_18) 0.0) (= (c4 b_18) -238.6198929295523)
;;@box@ {"coordinates": [[-4.439683219967442, -10.074058372942872], [-7.309692971685756, -10.074058372942872], [-7.309692971685756, 5.49133315320303], [-4.439683219967442, 5.49133315320303]]}
(= (a1 b_19) 0.0) (= (b1 b_19) -2.870009751718314) (= (c1 b_19) 28.91264576972557)
(= (a2 b_19) -15.565391526145902) (= (b2 b_19) 0.0) (= (c2 b_19) 113.77823304020572)
(= (a3 b_19) 0.0) (= (b3 b_19) 2.870009751718314) (= (c3 b_19) 15.760179699626773)
(= (a4 b_19) 15.565391526145902) (= (b4 b_19) 0.0) (= (c4 b_19) -69.10540757085337)
;;@box@ {"coordinates": [[-31.375964481182518, -3.10985505947776], [-40.86340415111806, -3.10985505947776], [-40.86340415111806, 7.721024698142068], [-31.375964481182518, 7.721024698142068]]}
(= (a1 b_20) 0.0) (= (b1 b_20) -9.487439669935544) (= (c1 b_20) 29.504562259039062)
(= (a2 b_20) -10.830879757619828) (= (b2 b_20) 0.0) (= (c2 b_20) 442.58661684778264)
(= (a3 b_20) 0.0) (= (b3 b_20) 9.487439669935544) (= (c3 b_20) 73.25275601370515)
(= (a4 b_20) 10.830879757619828) (= (b4 b_20) 0.0) (= (c4 b_20) -339.8292985750384)
;;@box@ {"coordinates": [[-19.610847724049247, 37.117248782018905], [-39.115945973323036, 37.117248782018905], [-39.115945973323036, 53.352668418523294], [-19.610847724049247, 53.352668418523294]]}
(= (a1 b_21) 0.0) (= (b1 b_21) -19.50509824927379) (= (c1 b_21) -723.9755842360166)
(= (a2 b_21) -16.23541963650439) (= (b2 b_21) 0.0) (= (c2 b_21) 635.0637973557336)
(= (a3 b_21) 0.0) (= (b3 b_21) 19.50509824927379) (= (c3 b_21) 1040.6490393642237)
(= (a4 b_21) 16.23541963650439) (= (b4 b_21) 0.0) (= (c4 b_21) -318.39034222752656)
;;@box@ {"coordinates": [[43.77181731793956, -39.977747788655726], [33.25957755864227, -39.977747788655726], [33.25957755864227, -34.48859641016468], [43.77181731793956, -34.48859641016468]]}
(= (a1 b_22) 0.0) (= (b1 b_22) -10.512239759297287) (= (c1 b_22) 420.25566979106594)
(= (a2 b_22) -5.489151378491044) (= (b2 b_22) 0.0) (= (c2 b_22) -182.56685600405103)
(= (a3 b_22) 0.0) (= (b3 b_22) 10.512239759297287) (= (c3 b_22) -362.55239442529086)
(= (a4 b_22) 5.489151378491044) (= (b4 b_22) 0.0) (= (c4 b_22) 240.2701313698261)
;;@box@ {"coordinates": [[39.51427054069873, -45.9661129286062], [31.755936380192455, -45.9661129286062], [31.755936380192455, -44.93714543818391], [39.51427054069873, -44.93714543818391]]}
(= (a1 b_23) 0.0) (= (b1 b_23) -7.758334160506276) (= (c1 b_23) 356.6204641596947)
(= (a2 b_23) -1.0289674904222892) (= (b2 b_23) 0.0) (= (c2 b_23) -32.675826163136506)
(= (a3 b_23) 0.0) (= (b3 b_23) 7.758334160506276) (= (c3 b_23) -348.637390528701)
(= (a4 b_23) 1.0289674904222892) (= (b4 b_23) 0.0) (= (c4 b_23) 40.658899794130164)
;;@box@ {"coordinates": [[44.0565678124373, 17.581012813690766], [40.23140746198677, 17.581012813690766], [40.23140746198677, 34.277784656930834], [44.0565678124373, 34.277784656930834]]}
(= (a1 b_24) 0.0) (= (b1 b_24) -3.825160350450531) (= (c1 b_24) -67.25019313569265)
(= (a2 b_24) -16.696771843240068) (= (b2 b_24) 0.0) (= (c2 b_24) -671.7346313252191)
(= (a3 b_24) 0.0) (= (b3 b_24) 3.825160350450531) (= (c3 b_24) 131.1180227709734)
(= (a4 b_24) 16.696771843240068) (= (b4 b_24) 0.0) (= (c4 b_24) 735.6024609604998)
;;@box@ {"coordinates": [[-16.244009636100667, -23.865832963381948], [-21.318474135422047, -23.865832963381948], [-21.318474135422047, -8.481308636316216], [-16.244009636100667, -8.481308636316216]]}
(= (a1 b_25) 0.0) (= (b1 b_25) -5.07446449932138) (= (c1 b_25) 121.10632211941565)
(= (a2 b_25) -15.384524327065732) (= (b2 b_25) 0.0) (= (c2 b_25) 327.97458395232206)
(= (a3 b_25) 0.0) (= (b3 b_25) 5.07446449932138) (= (c3 b_25) -43.03809958277446)
(= (a4 b_25) 15.384524327065732) (= (b4 b_25) 0.0) (= (c4 b_25) -249.9063614156809)
;;@box@ {"coordinates": [[-36.91879393151644, -26.768180551852574], [-50.01938273612908, -26.768180551852574], [-50.01938273612908, -18.319105256442356], [-36.91879393151644, -18.319105256442356]]}
(= (a1 b_26) 0.0) (= (b1 b_26) -13.100588804612642) (= (c1 b_26) 350.6789264574497)
(= (a2 b_26) -8.449075295410218) (= (b2 b_26) 0.0) (= (c2 b_26) 422.6175309674966)
(= (a3 b_26) 0.0) (= (b3 b_26) 13.100588804612642) (= (c3 b_26) -239.99106523306932)
(= (a4 b_26) 8.449075295410218) (= (b4 b_26) 0.0) (= (c4 b_26) -311.9296697431162)
;;@box@ {"coordinates": [[-4.6525797701581855, -45.88486008074814], [-17.543853466858096, -45.88486008074814], [-17.543853466858096, -27.86696489041492], [-4.6525797701581855, -27.86696489041492]]}
(= (a1 b_27) 0.0) (= (b1 b_27) -12.89127369669991) (= (c1 b_27) 591.5142898357042)
(= (a2 b_27) -18.01789519033322) (= (b2 b_27) 0.0) (= (c2 b_27) 316.10331300041327)
(= (a3 b_27) 0.0) (= (b3 b_27) 12.89127369669991) (= (c3 b_27) -359.24067149866573)
(= (a4 b_27) 18.01789519033322) (= (b4 b_27) 0.0) (= (c4 b_27) -83.82969466337481)
;;@box@ {"coordinates": [[4.079425122819126, -54.74158932964849], [2.4755523418597587, -54.74158932964849], [2.4755523418597587, -37.896173679741395], [4.079425122819126, -37.896173679741395]]}
(= (a1 b_28) 0.0) (= (b1 b_28) -1.6038727809593674) (= (c1 b_28) 87.79854511227896)
(= (a2 b_28) -16.845415649907096) (= (b2 b_28) 0.0) (= (c2 b_28) -41.70170816172854)
(= (a3 b_28) 0.0) (= (b3 b_28) 1.6038727809593674) (= (c3 b_28) -60.78064146744601)
(= (a4 b_28) 16.845415649907096) (= (b4 b_28) 0.0) (= (c4 b_28) 68.71961180656149)
;;@box@ {"coordinates": [[16.430437170816223, -2.3153409191496817], [12.537933485907642, -2.3153409191496817], [12.537933485907642, 6.807927340320438], [16.430437170816223, 6.807927340320438]]}
(= (a1 b_29) 0.0) (= (b1 b_29) -3.892503684908581) (= (c1 b_29) 9.012473059609757)
(= (a2 b_29) -9.12326825947012) (= (b2 b_29) 0.0) (= (c2 b_29) -114.38693061132874)
(= (a3 b_29) 0.0) (= (b3 b_29) 3.892503684908581) (= (c3 b_29) 26.49988225878718)
(= (a4 b_29) 9.12326825947012) (= (b4 b_29) 0.0) (= (c4 b_29) 149.89928592972566)
;;@box@ {"coordinates": [[43.09782842708292, 26.944589968912155], [24.9965421816379, 26.944589968912155], [24.9965421816379, 38.9435353270858], [43.09782842708292, 38.9435353270858]]}
(= (a1 b_30) 0.0) (= (b1 b_30) -18.101286245445024) (= (c1 b_30) -487.73173579342557)
(= (a2 b_30) -11.998945358173643) (= (b2 b_30) 0.0) (= (c2 b_30) -299.9321437807557)
(= (a3 b_30) 0.0) (= (b3 b_30) 18.101286245445024) (= (c3 b_30) 704.9280803651806)
(= (a4 b_30) 11.998945358173643) (= (b4 b_30) 0.0) (= (c4 b_30) 517.1284883525107)
;;@box@ {"coordinates": [[-13.775153688739717, -23.360331555257236], [-25.98103561179399, -23.360331555257236], [-25.98103561179399, -14.072601766514676], [-13.775153688739717, -14.072601766514676]]}
(= (a1 b_31) 0.0) (= (b1 b_31) -12.205881923054271) (= (c1 b_31) 285.13344864686854)
(= (a2 b_31) -9.28772978874256) (= (b2 b_31) 0.0) (= (c2 b_31) 241.3048383940403)
(= (a3 b_31) 0.0) (= (b3 b_31) 12.205881923054271) (= (c3 b_31) -171.76851551224308)
(= (a4 b_31) 9.28772978874256) (= (b4 b_31) 0.0) (= (c4 b_31) -127.93990525941483)
;;@box@ {"coordinates": [[28.778241052332117, -39.636657594025145], [16.144718129269126, -39.636657594025145], [16.144718129269126, -24.71035462728326], [28.778241052332117, -24.71035462728326]]}
(= (a1 b_32) 0.0) (= (b1 b_32) -12.63352292306299) (= (c1 b_32) 500.75062230771545)
(= (a2 b_32) -14.926302966741886) (= (b2 b_32) 0.0) (= (c2 b_32) -240.98095411012127)
(= (a3 b_32) 0.0) (= (b3 b_32) 12.63352292306299) (= (c3 b_32) -312.1788316207987)
(= (a4 b_32) 14.926302966741886) (= (b4 b_32) 0.0) (= (c4 b_32) 429.55274479703803)
;;@box@ {"coordinates": [[0.5790063872523152, 41.09611316558818], [-11.053905659885169, 41.09611316558818], [-11.053905659885169, 48.89824566288138], [0.5790063872523152, 48.89824566288138]]}
(= (a1 b_33) 0.0) (= (b1 b_33) -11.632912047137484) (= (c1 b_33) -478.0674699344961)
(= (a2 b_33) -7.802132497293201) (= (b2 b_33) 0.0) (= (c2 b_33) 86.24403657100332)
(= (a3 b_33) 0.0) (= (b3 b_33) 11.632912047137484) (= (c3 b_33) 568.828991055621)
(= (a4 b_33) 7.802132497293201) (= (b4 b_33) 0.0) (= (c4 b_33) 4.51748455012162)
;;@box@ {"coordinates": [[51.9823044605346, -10.729572032453532], [32.048890624569715, -10.729572032453532], [32.048890624569715, 0.22238914577376168], [51.9823044605346, 0.22238914577376168]]}
(= (a1 b_34) 0.0) (= (b1 b_34) -19.933413835964885) (= (c1 b_34) 213.8769996056911)
(= (a2 b_34) -10.951961178227293) (= (b2 b_34) 0.0) (= (c2 b_34) -350.99820592554016)
(= (a3 b_34) 0.0) (= (b3 b_34) 19.933413835964885) (= (c3 b_34) 4.432974875335113)
(= (a4 b_34) 10.951961178227293) (= (b4 b_34) 0.0) (= (c4 b_34) 569.3081804065664)
)
(:goal (and
        ;;@goal_location@[-42, 49]
(= (x) -42) (= (y) 49)
	     )
)
)

