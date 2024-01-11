(define (problem prob_2)
(:domain bottles-all)
	(:objects
		 l1 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (on-platform) 0)
		(= (litres l1) 6)
		(= (litres r1) 0)
		(capped l1)
		(capped r1)
	)
	(:goal
		(and
			(= (litres r1) 6)
			(packed l1)
			(packed r1)
		)
	)
)