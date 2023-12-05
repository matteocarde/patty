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
		(= (SoC b1) 22.0)
		(off b1)
		(off b2)
		(= (SoC b2) 70.0)
		(off b3)
		(= (SoC b3) 92.0)
		(= (sunexposure_time) 59.0)
		(= (time) -6.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)