(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(off b2)
		(gboff GB)
		(= (time) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)