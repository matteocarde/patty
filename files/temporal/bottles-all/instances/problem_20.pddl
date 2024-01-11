(define (problem prob_20)
(:domain bottles-all)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 - bottleright
	)
	(:init
		(= (on-platform) 0)
		(= (litres l1) 35)
		(= (litres l2) 1)
		(= (litres l3) 3)
		(= (litres l4) 5)
		(= (litres l5) 4)
		(= (litres l6) 4)
		(= (litres l7) 3)
		(= (litres l8) 2)
		(= (litres l9) 1)
		(= (litres l10) 2)
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
	)
	(:goal
		(and
			(= (litres r1) 5)
			(= (litres r2) 20)
			(= (litres r3) 6)
			(= (litres r4) 3)
			(= (litres r5) 5)
			(= (litres r6) 2)
			(= (litres r7) 6)
			(= (litres r8) 3)
			(= (litres r9) 5)
			(= (litres r10) 5)
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
		)
	)
)