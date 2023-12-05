(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) -32.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 64.0)
		(off b1)
		(off b2)
		(= (SoC b2) 78.0)
		(off b3)
		(= (SoC b3) 125.0)
		(= (sunexposure_time) 81.0)
		(= (time) -15.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)