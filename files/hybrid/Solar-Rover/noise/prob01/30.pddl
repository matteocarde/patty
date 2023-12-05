(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 24.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 45.0)
		(off b1)
		(off b2)
		(= (SoC b2) 99.0)
		(off b3)
		(= (SoC b3) 127.0)
		(= (sunexposure_time) 60.0)
		(= (time) 27.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)