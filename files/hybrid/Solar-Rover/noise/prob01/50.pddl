(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) -12.0)
		(night)
		(datatosend)
		(gboff GB)
		(= (SoC b1) 35.0)
		(off b1)
		(off b2)
		(= (SoC b2) 101.0)
		(off b3)
		(= (SoC b3) 148.0)
		(= (sunexposure_time) 31.0)
		(= (time) 22.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)