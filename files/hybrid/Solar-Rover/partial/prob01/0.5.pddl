(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(gboff GB)
		(= (roverenergy) 0.0)
		(off b3)
		(= (sunexposure_time) 50.0)
		(off b1)
		(= (time) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)