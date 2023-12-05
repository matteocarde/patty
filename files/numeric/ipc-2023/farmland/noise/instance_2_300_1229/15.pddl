(define (problem instance_2_300_1229_ladder)
	(:domain farmland)
	(:objects
		farm0 farm1 - farm
	)
	(:init
		(= (x farm0) 303.0)
		(= (x farm1) -12.0)
		(adj farm0 farm1)
		(adj farm1 farm0)
		(= (cost) -14.0)
	)
	(:goal
			(and
				(>= (x farm0) 1.0)
				(>= (x farm1) 1.0)
				(>= (+ (* 1.0 (x farm0)) (+ (* 1.7 (x farm1)) 0.0)) 420.0)
			)
	)
)