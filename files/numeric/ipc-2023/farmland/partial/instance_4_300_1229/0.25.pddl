(define (problem instance_4_300_1229_ladder)
	(:domain farmland)
	(:objects
		farm0 farm1 farm2 farm3 - farm
	)
	(:init
		(= (x farm1) 1.0)
		(= (x farm0) 300.0)
		(= (x farm2) 0.0)
	)
	(:goal
			(and
				(>= (x farm0) 1.0)
				(>= (x farm1) 1.0)
				(>= (x farm2) 1.0)
				(>= (x farm3) 1.0)
				(>= (+ (* 1.0 (x farm0)) (+ (* 1.7 (x farm1)) (+ (* 1.3 (x farm2)) (+ (* 1.1 (x farm3)) 0.0)))) 420.0)
			)
	)
)