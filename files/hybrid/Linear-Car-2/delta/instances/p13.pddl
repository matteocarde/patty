
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
	(= (max_acceleration) 1)
	(= (min_acceleration) -1)
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
