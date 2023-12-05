(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 1.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 40.0)
		(off b1)
		(off b2)
		(= (SoC b2) 83.0)
		(off b3)
		(= (SoC b3) 95.0)
		(= (sunexposure_time) 49.0)
		(= (time) -2.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)