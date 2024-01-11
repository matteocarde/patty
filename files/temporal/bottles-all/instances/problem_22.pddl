(define (problem prob_22)
(:domain bottles-all)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 - bottleright
	)
	(:init
		(= (on-platform) 0)
		(= (litres l1) 25)
		(= (litres l2) 3)
		(= (litres l3) 6)
		(= (litres l4) 6)
		(= (litres l5) 2)
		(= (litres l6) 3)
		(= (litres l7) 5)
		(= (litres l8) 2)
		(= (litres l9) 5)
		(= (litres l10) 6)
		(= (litres l11) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
		(= (litres r7) 0)
		(= (litres r8) 0)
		(= (litres r9) 0)
		(= (litres r10) 0)
		(= (litres r11) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped l4)
		(capped l5)
		(capped l6)
		(capped l7)
		(capped l8)
		(capped l9)
		(capped l10)
		(capped l11)
		(capped r1)
		(capped r2)
		(capped r3)
		(capped r4)
		(capped r5)
		(capped r6)
		(capped r7)
		(capped r8)
		(capped r9)
		(capped r10)
		(capped r11)
	)
	(:goal
		(and
			(= (litres r1) 5)
			(= (litres r2) 2)
			(= (litres r3) 2)
			(= (litres r4) 5)
			(= (litres r5) 4)
			(= (litres r6) 3)
			(= (litres r7) 5)
			(= (litres r8) 1)
			(= (litres r9) 4)
			(= (litres r10) 31)
			(= (litres r11) 4)
			(packed l1)
			(packed l2)
			(packed l3)
			(packed l4)
			(packed l5)
			(packed l6)
			(packed l7)
			(packed l8)
			(packed l9)
			(packed l10)
			(packed l11)
			(packed r1)
			(packed r2)
			(packed r3)
			(packed r4)
			(packed r5)
			(packed r6)
			(packed r7)
			(packed r8)
			(packed r9)
			(packed r10)
			(packed r11)
		)
	)
)