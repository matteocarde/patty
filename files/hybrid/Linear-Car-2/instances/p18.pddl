
(define (problem instance_1_300_01_100)
  (:domain car_linear_mt_sc)
  ;(:objects  )

  (:init
  (= (d) 0.0)
	(= (v) 0.0)
	(engine_stopped)
	(= (a) 0.0)
	(= (max_acceleration) 6)
	(= (min_acceleration) -6)
	(= (max_speed) 100.0)
  )

  (:goal
    (and 
	(>= (d) 2000.5 )
	(<= (d) 2001.5 )
	(engine_stopped)
	)
  )
)
