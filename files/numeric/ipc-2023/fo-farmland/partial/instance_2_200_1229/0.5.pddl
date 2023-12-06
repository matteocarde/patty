(define (problem instance_2_200_1229_ladder)
	(:domain farmland_ln)
	(:objects
		farm0 farm1 - farm
	)
	(:init
		(adj farm0 farm1)
		(= (x farm1) 1.0)
		(= (num-of-cars) 0.0)
	)
	(:goal
			(and
				(>= (x farm0) 1.0)
				(>= (x farm1) 1.0)
				(>= (- (+ (* 1.0 (x farm0)) (+ (* 1.7 (x farm1)) 0.0)) (cost)) 280.0)
			)
	)
)