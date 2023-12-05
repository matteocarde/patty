(define (problem instance_2_200_1229_ladder)
	(:domain farmland_ln)
	(:objects
		farm0 farm1 - farm
	)
	(:init
		(= (num-of-cars) -6.0)
		(= (x farm0) 195.0)
		(= (x farm1) 7.0)
		(adj farm0 farm1)
		(adj farm1 farm0)
		(= (cost) 1.0)
	)
	(:goal
			(and
				(>= (x farm0) 1.0)
				(>= (x farm1) 1.0)
				(>= (- (+ (* 1.0 (x farm0)) (+ (* 1.7 (x farm1)) 0.0)) (cost)) 280.0)
			)
	)
)