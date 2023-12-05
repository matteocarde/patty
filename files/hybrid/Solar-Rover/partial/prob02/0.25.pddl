(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 0.0)
		(gboff GB)
		(off b2)
	)
	(:goal
			(and
				(datasent)
			)
	)
)