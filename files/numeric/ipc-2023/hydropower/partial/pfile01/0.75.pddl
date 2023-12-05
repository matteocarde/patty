(define (problem power1)
	(:domain hydropower)
	(:objects
		n0 n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18 n19 n20 n21 n22 n23 n24 n25 n26 - turnvalue
		t0000 t0030 t0100 t0130 t0200 t0230 t0300 t0330 t0400 t0430 t0500 t0530 t0600 t0630 t0700 t0730 t0800 t0830 t0900 t0930 t1000 t1030 t1100 t1130 t1200 t1230 t1300 t1330 t1400 t1430 t1500 t1530 t1600 t1630 t1700 t1730 t1800 t1830 t1900 t1930 t2000 t2030 t2100 t2130 t2200 t2230 t2300 t2330 t2400 t2430 t2500 - time
	)
	(:init
		(= (value n11) 11.0)
		(= (value n19) 19.0)
		(demand t1530 n20)
		(before t2300 t2330)
		(before t1300 t1330)
		(before t0330 t0400)
		(demand t0100 n7)
		(before t0830 t0900)
		(= (value n24) 24.0)
		(demand t1200 n19)
		(before t0700 t0730)
		(before t1030 t1100)
		(demand t1730 n25)
		(= (value n7) 7.0)
		(before t1530 t1600)
		(timenow t0000)
		(= (value n9) 9.0)
		(before t1630 t1700)
		(demand t0630 n13)
		(demand t0530 n5)
		(= (value n5) 5.0)
		(demand t0830 n19)
		(= (value n8) 8.0)
		(before t1000 t1030)
		(before t2000 t2030)
		(demand t1630 n25)
		(before t0800 t0830)
		(= (value n12) 12.0)
		(before t0530 t0600)
		(before t0100 t0130)
		(demand t1330 n18)
		(demand t1430 n18)
		(demand t1500 n19)
		(before t0230 t0300)
		(= (value n17) 17.0)
		(before t1800 t1830)
		(= (value n10) 10.0)
		(demand t0730 n19)
		(demand t2330 n3)
		(before t0000 t0030)
		(demand t2300 n6)
		(demand t1130 n19)
		(demand t0430 n3)
		(demand t0500 n4)
		(demand t0600 n9)
		(demand t0000 n7)
		(demand t1830 n22)
		(= (value n20) 20.0)
		(= (value n2) 2.0)
		(demand t0030 n7)
		(before t1230 t1300)
		(demand t1030 n19)
		(demand t2030 n18)
		(before t1600 t1630)
		(demand t1700 n26)
		(before t1100 t1130)
		(before t1700 t1730)
		(= (value n22) 22.0)
		(= (value n18) 18.0)
		(= (value n25) 25.0)
		(before t0600 t0630)
		(demand t2000 n19)
		(before t1730 t1800)
		(= (value n26) 26.0)
		(demand t1400 n18)
		(demand t2500 n1)
		(before t0500 t0530)
		(demand t2400 n1)
		(before t0400 t0430)
		(demand t1300 n18)
		(demand t2230 n10)
		(before t0630 t0700)
		(before t0300 t0330)
		(before t0730 t0800)
		(before t0200 t0230)
		(before t1130 t1200)
		(before t1330 t1400)
		(= (value n14) 14.0)
		(= (value n21) 21.0)
		(demand t2130 n14)
		(before t2100 t2130)
		(before t1900 t1930)
		(demand t2100 n16)
		(before t0130 t0200)
		(before t0030 t0100)
		(before t2030 t2100)
		(demand t0330 n4)
		(before t0430 t0500)
		(before t0900 t0930)
		(= (value n6) 6.0)
		(demand t0900 n19)
		(demand t0700 n18)
		(= (stored_units) 0.0)
		(demand t1800 n24)
		(before t1430 t1500)
		(demand t1600 n23)
		(demand t1930 n20)
	)
	(:goal
			(and
				(>= (funds) 1010.0)
			)
	)
)