(define (problem power1)
	(:domain hydropower)
	(:objects
		n0 n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18 n19 n20 n21 n22 n23 n24 n25 n26 - turnvalue
		t0000 t0030 t0100 t0130 t0200 t0230 t0300 t0330 t0400 t0430 t0500 t0530 t0600 t0630 t0700 t0730 t0800 t0830 t0900 t0930 t1000 t1030 t1100 t1130 t1200 t1230 t1300 t1330 t1400 t1430 t1500 t1530 t1600 t1630 t1700 t1730 t1800 t1830 t1900 t1930 t2000 t2030 t2100 t2130 t2200 t2230 t2300 t2330 t2400 t2430 t2500 - time
	)
	(:init
		(demand t1900 n21)
		(= (value n17) 17.0)
		(demand t0130 n6)
		(before t2000 t2030)
		(before t1630 t1700)
		(= (value n14) 14.0)
		(demand t1130 n19)
		(= (stored_units) 0.0)
		(demand t0300 n5)
		(= (value n25) 25.0)
		(= (value n22) 22.0)
		(demand t0000 n7)
		(before t1900 t1930)
		(demand t2130 n14)
		(demand t0730 n19)
		(before t0200 t0230)
		(= (value n15) 15.0)
		(before t0900 t0930)
		(demand t0930 n19)
		(= (value n5) 5.0)
		(before t0830 t0900)
		(demand t0400 n3)
		(demand t2400 n1)
		(= (value n12) 12.0)
		(before t1930 t2000)
		(demand t1930 n20)
		(demand t1530 n20)
		(before t2200 t2230)
		(before t1530 t1600)
		(= (value n11) 11.0)
		(demand t1630 n25)
		(before t0000 t0030)
	)
	(:goal
			(and
				(>= (funds) 1020.0)
			)
	)
)