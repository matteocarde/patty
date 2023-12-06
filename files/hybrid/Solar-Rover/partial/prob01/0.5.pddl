(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(off b2)
		(= (sunexposure_time) 50.0)
		(gboff GB)
		(off b1)
		(off b3)
		(= (roverenergy) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)