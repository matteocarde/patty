(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 3.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 52.0)
		(off b1)
		(off b2)
		(= (SoC b2) 78.0)
		(off b3)
		(= (SoC b3) 86.0)
		(= (sunexposure_time) 48.0)
		(= (time) -3.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)