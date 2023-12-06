(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(night)
		(datatosend)
		(= (SoC b2) 80.0)
		(gboff GB)
		(= (time) 0.0)
		(= (SoC b1) 40.0)
		(= (SoC b3) 100.0)
		(off b3)
		(off b1)
	)
	(:goal
			(and
				(datasent)
			)
	)
)