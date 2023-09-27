
(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	;(:objects  )

	(:init
		(= (d) 10.0)
		(= (v) 0.0)
		(engine_stopped)
		(= (a) 0.0)
		(= (max_acceleration) 1)
		(= (min_acceleration) -1)
		(= (max_speed) 10.0)
	)

	(:goal
		(and
			(>= (d) 299.5)
			(<= (d) 300.5)
			(engine_stopped)
		)
	)
)

; Executed Wrong Plan: d=10
; 0: (start_car)
; 0: (accelerate)
; 0: -----waiting---- [1.0]
; 1.0: (decelerate)
; 1.0: -----waiting---- [290.0]
; 290.0: (decelerate)
; 290.0: -----waiting---- [291.0]
; 291.0: (stop_car)

; Correct given plan: d=0
; 0: (start_car)
; 0: (accelerate)
; 0: -----waiting---- [1.0]
; 1.0: (decelerate)
; 1.0: -----waiting---- [300.0]
; 300.0: (decelerate)
; 300.0: -----waiting---- [301.0]
; 301.0: (stop_car)