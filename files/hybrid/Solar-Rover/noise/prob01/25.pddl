(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 0.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 23.0)
		(off b1)
		(off b2)
		(= (SoC b2) 69.0)
		(off b3)
		(= (SoC b3) 75.0)
		(= (sunexposure_time) 47.0)
		(= (time) -20.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)