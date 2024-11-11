(define (problem prob_4)
(:domain bottles-all)
	(:objects
		 l1 l2 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (on-platform) 0)
		(= (litres l1) 2)
		(= (litres l2) 10)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(capped l1)
		(capped l2)
		(capped r1)
		(capped r2)
	)
	(:goal
		(and
			(= (litres r1) 6)
			(= (litres r2) 6)
			(packed l1)
			(packed l2)
			(packed r1)
			(packed r2)
		)
	)
)