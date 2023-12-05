(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b3) 100.0)
		(= (roverenergy) 0.0)
		(off b2)
		(off b1)
		(gboff GB)
		(off b3)
		(datatosend)
		(= (sunexposure_time) 200.0)
		(night)
	)
	(:goal
			(and
				(datasent)
			)
	)
)