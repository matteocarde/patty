(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(gboff GB)
		(datatosend)
		(night)
		(off b3)
		(= (roverenergy) 0.0)
		(off b1)
	)
	(:goal
			(and
				(datasent)
			)
	)
)