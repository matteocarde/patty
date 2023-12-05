(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 5.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 48.0)
		(off b1)
		(off b2)
		(= (SoC b2) 74.0)
		(off b3)
		(= (SoC b3) 103.0)
		(= (sunexposure_time) 58.0)
		(= (time) -7.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)