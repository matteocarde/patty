
(define (problem instance_1_300_01_100)
  (:domain car_linear_mt_sc)
  ;(:objects  )

  (:init
(= (time) 0)
(= (tk ) 0)
(= (delta ) 1)
  (= (d) 0.0)
	(= (v) 0.0)
	(engine_stopped)
	(= (a) 0.0)
	(= (max_acceleration) 20)
	(= (min_acceleration) -20)
	(= (max_speed) 100.0)
  )

  (:goal
    (and 
	(>= (d) 1000.5 )
	(<= (d) 1001.5 )
	(engine_stopped)
	)
  )
)