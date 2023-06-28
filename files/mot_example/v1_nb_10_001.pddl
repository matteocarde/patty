(define

;;@problem_name@v1_nb_10_001
(problem v1_nb_10_001)

(:domain motion_planning_v1)

(:objects b_0 b_1 b_2 b_3 b_4 b_5 b_6 b_7 b_8 b_9 - box)

(:init

    ;;@initial_location@[-22, -50]
(= (x) -22) (= (y) -50)

    ;;@bounding_box@ {"coordinates": [[48.59635568244984, -50.96145423596497], [-46.888606819551185, -50.96145423596497], [-46.888606819551185, 40.783011642255886], [48.59635568244984, 40.783011642255886]]}
(= (maxx) 48.59635568244984) (= (maxy) 40.783011642255886) (= (minx) -46.888606819551185) (= (miny) -50.96145423596497)

    ;;@box@ {"coordinates": [[20.748573207312965, 5.835830099001907], [10.529751300570702, 5.835830099001907], [10.529751300570702, 22.372776131336185], [20.748573207312965, 22.372776131336185]]}
(= (a1 b_0) 0.0) (= (b1 b_0) -10.218821906742264) (= (c1 b_0) -59.63530845970656)
(= (a2 b_0) -16.536946032334278) (= (b2 b_0) 0.0) (= (c2 b_0) -174.12992899143936)
(= (a3 b_0) 0.0) (= (b3 b_0) 10.218821906742264) (= (c3 b_0) 228.62341484553863)
(= (a4 b_0) 16.536946032334278) (= (b4 b_0) 0.0) (= (c4 b_0) 343.11803537727144)
;;@box@ {"coordinates": [[34.77487316256075, -41.45830153755733], [27.21324358367981, -41.45830153755733], [27.21324358367981, -27.107781505639164], [34.77487316256075, -27.107781505639164]]}
(= (a1 b_1) 0.0) (= (b1 b_1) -7.561629578880943) (= (c1 b_1) 313.4923191965588)
(= (a2 b_1) -14.350520031918169) (= (b2 b_1) 0.0) (= (c2 b_1) -390.5241971810657)
(= (a3 b_1) 0.0) (= (b3 b_1) 7.561629578880943) (= (c3 b_1) -204.9790024508829)
(= (a4 b_1) 14.350520031918169) (= (b4 b_1) 0.0) (= (c4 b_1) 499.0375139267416)
;;@box@ {"coordinates": [[-25.38943954370064, 30.989278030699474], [-43.641261306896105, 30.989278030699474], [-43.641261306896105, 37.10655500819902], [-25.38943954370064, 37.10655500819902]]}
(= (a1 b_2) 0.0) (= (b1 b_2) -18.251821763195466) (= (c1 b_2) -565.6107791864358)
(= (a2 b_2) -6.117276977499543) (= (b2 b_2) 0.0) (= (c2 b_2) 266.9656830617172)
(= (a3 b_2) 0.0) (= (b3 b_2) 18.251821763195466) (= (c3 b_2) 677.2622282558565)
(= (a4 b_2) 6.117276977499543) (= (b4 b_2) 0.0) (= (c4 b_2) -155.31423399229644)
;;@box@ {"coordinates": [[2.0082822340843203, -50.96145423596497], [-12.674149382894797, -50.96145423596497], [-12.674149382894797, -34.88376871626368], [2.0082822340843203, -34.88376871626368]]}
(= (a1 b_3) 0.0) (= (b1 b_3) -14.682431616979116) (= (c1 b_3) 748.2380669213665)
(= (a2 b_3) -16.07768551970129) (= (b2 b_3) 0.0) (= (c2 b_3) 203.77098800789872)
(= (a3 b_3) 0.0) (= (b3 b_3) 14.682431616979116) (= (c3 b_3) -512.1785487190568)
(= (a4 b_3) 16.07768551970129) (= (b4 b_3) 0.0) (= (c4 b_3) 32.28853019441083)
;;@box@ {"coordinates": [[-17.131840628574473, -47.15402580469022], [-25.641458583580018, -47.15402580469022], [-25.641458583580018, -45.2470551920145], [-17.131840628574473, -45.2470551920145]]}
(= (a1 b_4) 0.0) (= (b1 b_4) -8.509617955005545) (= (c1 b_4) 401.2627446383867)
(= (a2 b_4) -1.906970612675721) (= (b2 b_4) 0.0) (= (c2 b_4) 48.89750798502872)
(= (a3 b_4) 0.0) (= (b3 b_4) 8.509617955005545) (= (c3 b_4) -385.03515327309344)
(= (a4 b_4) 1.906970612675721) (= (b4 b_4) 0.0) (= (c4 b_4) -32.669916619735474)
;;@box@ {"coordinates": [[48.59635568244984, 18.605884867227825], [37.968773685511096, 18.605884867227825], [37.968773685511096, 21.271573047131387], [48.59635568244984, 21.271573047131387]]}
(= (a1 b_5) 0.0) (= (b1 b_5) -10.627581996938744) (= (c1 b_5) -197.73556705206545)
(= (a2 b_5) -2.6656881799035617) (= (b2 b_5) 0.0) (= (c2 b_5) -101.21291121890032)
(= (a3 b_5) 0.0) (= (b3 b_5) 10.627581996938744) (= (c3 b_5) 226.06538676226094)
(= (a4 b_5) 2.6656881799035617) (= (b4 b_5) 0.0) (= (c4 b_5) 129.54273092909582)
;;@box@ {"coordinates": [[-39.86587231307179, -33.735096076333924], [-46.888606819551185, -33.735096076333924], [-46.888606819551185, -14.77912574612651], [-39.86587231307179, -14.77912574612651]]}
(= (a1 b_6) 0.0) (= (b1 b_6) -7.022734506479395) (= (c1 b_6) 236.9126232946679)
(= (a2 b_6) -18.955970330207414) (= (b2 b_6) 0.0) (= (c2 b_6) 888.8190396961733)
(= (a3 b_6) 0.0) (= (b3 b_6) 7.022734506479395) (= (c3 b_6) -103.78987635292069)
(= (a4 b_6) 18.955970330207414) (= (b4 b_6) 0.0) (= (c4 b_6) -755.696292754426)
;;@box@ {"coordinates": [[-28.616826104572564, -14.885226931870672], [-31.0038193867702, -14.885226931870672], [-31.0038193867702, -5.785446029301657], [-28.616826104572564, -5.785446029301657]]}
(= (a1 b_7) 0.0) (= (b1 b_7) -2.3869932821976363) (= (c1 b_7) 35.53093669036263)
(= (a2 b_7) -9.099780902569016) (= (b2 b_7) 0.0) (= (c2 b_7) 282.12796356243047)
(= (a3 b_7) 0.0) (= (b3 b_7) 2.3869932821976363) (= (c3 b_7) -13.809820806460046)
(= (a4 b_7) 9.099780902569016) (= (b4 b_7) 0.0) (= (c4 b_7) -260.4068476785279)
;;@box@ {"coordinates": [[7.247948635771852, 22.92329814947614], [-7.144389683667416, 22.92329814947614], [-7.144389683667416, 40.783011642255886], [7.247948635771852, 40.783011642255886]]}
(= (a1 b_8) 0.0) (= (b1 b_8) -14.392338319439268) (= (c1 b_8) -329.9198623646367)
(= (a2 b_8) -17.859713492779747) (= (b2 b_8) 0.0) (= (c2 b_8) 127.59675283107138)
(= (a3 b_8) 0.0) (= (b3 b_8) 14.392338319439268) (= (c3 b_8) 586.9629012409772)
(= (a4 b_8) 17.859713492779747) (= (b4 b_8) 0.0) (= (c4 b_8) 129.44628604526912)
;;@box@ {"coordinates": [[5.435335429848931, 11.58402904621586], [-2.428500312397259, 11.58402904621586], [-2.428500312397259, 28.899066333216624], [5.435335429848931, 28.899066333216624]]}
(= (a1 b_9) 0.0) (= (b1 b_9) -7.86383574224619) (= (c1 b_9) -91.09490165285033)
(= (a2 b_9) -17.315037287000763) (= (b2 b_9) 0.0) (= (c2 b_9) 42.04957346065154)
(= (a3 b_9) 0.0) (= (b3 b_9) 7.86383574224619) (= (c3 b_9) 227.25751074869243)
(= (a4 b_9) 17.315037287000763) (= (b4 b_9) 0.0) (= (c4 b_9) 94.11303563519056)
)
(:goal (and
        ;;@goal_location@[16, 24]
(= (x) 16) (= (y) 24)
	     )
)
)
