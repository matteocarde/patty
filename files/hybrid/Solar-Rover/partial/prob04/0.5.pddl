(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b3) 100.0)
		(= (SoC b1) 40.0)
		(off b3)
		(datatosend)
		(gboff GB)
		(night)
	)
	(:goal
			(and
				(datasent)
			)
	)
)