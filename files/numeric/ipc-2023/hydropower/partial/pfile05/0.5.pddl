(define (problem power1)
	(:domain hydropower)
	(:objects
		n0 n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18 n19 n20 n21 n22 n23 n24 n25 n26 - turnvalue
		t0000 t0030 t0100 t0130 t0200 t0230 t0300 t0330 t0400 t0430 t0500 t0530 t0600 t0630 t0700 t0730 t0800 t0830 t0900 t0930 t1000 t1030 t1100 t1130 t1200 t1230 t1300 t1330 t1400 t1430 t1500 t1530 t1600 t1630 t1700 t1730 t1800 t1830 t1900 t1930 t2000 t2030 t2100 t2130 t2200 t2230 t2300 t2330 t2400 t2430 t2500 - time
	)
	(:init
		(demand t2300 n6)
		(= (value n10) 10.0)
		(demand t2130 n14)
		(demand t1500 n19)
		(demand t1330 n18)
		(before t1530 t1600)
		(= (value n11) 11.0)
		(before t1930 t2000)
		(demand t0800 n19)
		(demand t1400 n18)
		(demand t0930 n19)
		(before t0630 t0700)
		(before t1700 t1730)
		(= (value n15) 15.0)
		(= (value n14) 14.0)
		(before t2100 t2130)
		(before t2030 t2100)
		(before t2200 t2230)
		(before t2330 t2400)
		(demand t2400 n1)
		(demand t1600 n23)
		(demand t2430 n1)
		(demand t1100 n19)
		(before t1630 t1700)
		(before t1030 t1100)
		(demand t1300 n18)
		(= (value n21) 21.0)
		(demand t1800 n24)
		(before t1830 t1900)
		(before t2300 t2330)
		(before t1000 t1030)
		(demand t2030 n18)
		(before t1230 t1300)
		(demand t0700 n18)
		(demand t1830 n22)
		(demand t0200 n6)
		(= (value n8) 8.0)
		(before t2130 t2200)
		(before t0330 t0400)
		(demand t2500 n1)
		(demand t0100 n7)
		(demand t1030 n19)
		(before t0100 t0130)
		(before t0800 t0830)
		(demand t1630 n25)
		(demand t0300 n5)
		(before t1200 t1230)
		(demand t0230 n6)
		(before t0400 t0430)
		(= (value n19) 19.0)
		(before t0430 t0500)
		(= (value n7) 7.0)
		(= (value n13) 13.0)
		(demand t0830 n19)
		(= (value n0) 0.0)
		(demand t2100 n16)
		(= (funds) 1000.0)
		(before t0830 t0900)
		(before t0130 t0200)
		(= (value n20) 20.0)
		(demand t1530 n20)
		(before t1430 t1500)
		(demand t0730 n19)
		(= (value n26) 26.0)
		(before t1600 t1630)
	)
	(:goal
			(and
				(>= (funds) 1050.0)
			)
	)
)