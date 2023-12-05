(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(datatosend)
		(= (SoC b1) 40.0)
		(off b1)
		(= (sunexposure_time) 50.0)
		(off b3)
		(night)
		(= (SoC b3) 100.0)
		(gboff GB)
		(= (time) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)