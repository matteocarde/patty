(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) -23.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 80.0)
		(off b1)
		(off b2)
		(= (SoC b2) 73.0)
		(off b3)
		(= (SoC b3) 137.0)
		(= (sunexposure_time) 89.0)
		(= (time) -25.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)