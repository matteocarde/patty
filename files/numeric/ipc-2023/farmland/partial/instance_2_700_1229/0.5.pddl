(define (problem instance_2_700_1229_ladder)
	(:domain farmland)
	(:objects
		farm0 farm1 - farm
	)
	(:init
		(= (x farm0) 700.0)
		(= (cost) 0.0)
	)
	(:goal
			(and
				(>= (x farm0) 1.0)
				(>= (x farm1) 1.0)
				(>= (+ (* 1.0 (x farm0)) (+ (* 1.7 (x farm1)) 0.0)) 980.0)
			)
	)
)