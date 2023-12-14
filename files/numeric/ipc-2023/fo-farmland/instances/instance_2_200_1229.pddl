;;Setting seed to 1229
;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_2_200_1229_ladder)
(:domain farmland_ln)
	(:objects
		farm0 farm1  - farm
	)
  (:init

                (= (num-of-cars) 0)
		(= (x farm0) 200)
		(= (x farm1) 1)
		
		(adj farm0 farm1)
		(adj farm1 farm0)
		
		(= (cost) 0)
	)
	(:goal
		(and
			(>= (x farm0) 1)
			(>= (x farm1) 1)
			
			(>= (- (+ (* 1.0 (x farm0))(+ (* 1.7 (x farm1)) 0)) (cost)) 280.0)		)
	)
)


