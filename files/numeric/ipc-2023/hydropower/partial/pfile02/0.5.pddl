(define (problem power1)
	(:domain hydropower)
	(:objects
		n0 n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18 n19 n20 n21 n22 n23 n24 n25 n26 - turnvalue
		t0000 t0030 t0100 t0130 t0200 t0230 t0300 t0330 t0400 t0430 t0500 t0530 t0600 t0630 t0700 t0730 t0800 t0830 t0900 t0930 t1000 t1030 t1100 t1130 t1200 t1230 t1300 t1330 t1400 t1430 t1500 t1530 t1600 t1630 t1700 t1730 t1800 t1830 t1900 t1930 t2000 t2030 t2100 t2130 t2200 t2230 t2300 t2330 t2400 t2430 t2500 - time
	)
	(:init
		(before t2030 t2100)
		(demand t0030 n7)
		(demand t1400 n18)
		(= (value n9) 9.0)
		(demand t1630 n25)
		(= (stored_capacity) 1.0)
		(= (value n1) 1.0)
		(demand t1500 n19)
		(demand t2500 n1)
		(before t1930 t2000)
		(= (value n25) 25.0)
		(= (value n19) 19.0)
		(demand t1030 n19)
		(demand t2000 n19)
		(= (value n8) 8.0)
		(before t2130 t2200)
		(before t0930 t1000)
		(before t0600 t0630)
		(= (value n17) 17.0)
		(before t0100 t0130)
		(demand t1930 n20)
		(demand t0630 n13)
		(demand t1000 n19)
		(demand t0730 n19)
		(demand t1300 n18)
		(demand t1730 n25)
		(demand t1230 n18)
		(= (value n22) 22.0)
		(before t1030 t1100)
		(before t1300 t1330)
		(demand t2230 n10)
		(before t2200 t2230)
		(= (value n21) 21.0)
		(= (value n14) 14.0)
		(= (value n6) 6.0)
		(timenow t0000)
		(= (value n13) 13.0)
		(demand t1700 n26)
		(demand t0130 n6)
		(before t1500 t1530)
		(demand t0100 n7)
		(demand t0200 n6)
		(demand t2200 n12)
		(before t1230 t1300)
		(= (value n12) 12.0)
		(before t2300 t2330)
		(before t0300 t0330)
		(before t0730 t0800)
		(demand t0830 n19)
		(demand t2300 n6)
		(before t1730 t1800)
		(= (value n18) 18.0)
		(before t2000 t2030)
		(demand t0530 n5)
		(before t1000 t1030)
		(before t1430 t1500)
		(demand t0930 n19)
		(demand t2100 n16)
		(demand t0500 n4)
		(before t1630 t1700)
		(= (value n26) 26.0)
		(demand t1430 n18)
		(= (value n5) 5.0)
		(before t0330 t0400)
		(= (value n23) 23.0)
	)
	(:goal
			(and
				(>= (funds) 1020.0)
			)
	)
)