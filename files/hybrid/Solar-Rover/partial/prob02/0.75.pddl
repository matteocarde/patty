(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 0.0)
		(= (time) 0.0)
		(off b1)
		(gboff GB)
		(datatosend)
		(night)
		(off b2)
		(= (SoC b1) 40.0)
		(= (sunexposure_time) 100.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)