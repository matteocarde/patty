(define (problem power1)
	(:domain hydropower)
	(:objects
		n0 n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18 n19 n20 n21 n22 n23 n24 n25 n26 - turnvalue
		t0000 t0030 t0100 t0130 t0200 t0230 t0300 t0330 t0400 t0430 t0500 t0530 t0600 t0630 t0700 t0730 t0800 t0830 t0900 t0930 t1000 t1030 t1100 t1130 t1200 t1230 t1300 t1330 t1400 t1430 t1500 t1530 t1600 t1630 t1700 t1730 t1800 t1830 t1900 t1930 t2000 t2030 t2100 t2130 t2200 t2230 t2300 t2330 t2400 t2430 t2500 - time
	)
	(:init
		(before t1300 t1330)
		(= (value n11) 11.0)
		(before t1330 t1400)
		(before t1230 t1300)
		(= (value n19) 19.0)
		(before t0200 t0230)
		(demand t0330 n4)
		(before t0530 t0600)
		(demand t0630 n13)
		(timenow t0000)
		(= (funds) 1000.0)
		(before t2030 t2100)
		(demand t1200 n19)
		(= (value n15) 15.0)
		(demand t1400 n18)
		(before t1830 t1900)
		(demand t0030 n7)
		(demand t1900 n21)
		(= (value n5) 5.0)
		(demand t0400 n3)
		(= (value n7) 7.0)
		(demand t0730 n19)
		(demand t0230 n6)
		(demand t2400 n1)
		(before t1800 t1830)
		(demand t0600 n9)
		(demand t0930 n19)
		(before t1000 t1030)
		(before t0300 t0330)
		(= (value n4) 4.0)
		(before t0800 t0830)
		(demand t1230 n18)
		(= (value n9) 9.0)
		(demand t1530 n20)
		(= (value n6) 6.0)
		(demand t0830 n19)
		(demand t1730 n25)
		(before t0930 t1000)
		(before t2100 t2130)
		(before t1500 t1530)
		(demand t1830 n22)
		(before t1900 t1930)
		(before t0730 t0800)
		(before t0830 t0900)
		(= (value n17) 17.0)
		(before t1930 t2000)
		(= (value n24) 24.0)
		(= (value n23) 23.0)
		(= (value n18) 18.0)
		(demand t0200 n6)
		(demand t2130 n14)
		(demand t0100 n7)
		(before t1600 t1630)
		(= (value n25) 25.0)
		(demand t1000 n19)
		(demand t0430 n3)
		(demand t1430 n18)
		(before t0700 t0730)
		(demand t2000 n19)
		(demand t0130 n6)
		(= (stored_capacity) 1.0)
		(demand t0000 n7)
		(before t0430 t0500)
		(= (value n2) 2.0)
		(demand t2430 n1)
	)
	(:goal
			(and
				(>= (funds) 1020.0)
			)
	)
)