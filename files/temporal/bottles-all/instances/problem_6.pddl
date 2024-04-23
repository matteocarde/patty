(define (problem prob_6)
(:domain bottles-all)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (on-platform) 0)
		(= (litres l1) 16)
		(= (litres l2) 1)
		(= (litres l3) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped r1)
		(capped r2)
		(capped r3)
	)
	(:goal
		(and
			(= (litres r1) 2)
			(= (litres r2) 3)
			(= (litres r3) 13)
			(packed l1)
			(packed l2)
			(packed l3)
			(packed r1)
			(packed r2)
			(packed r3)
		)
	)
)