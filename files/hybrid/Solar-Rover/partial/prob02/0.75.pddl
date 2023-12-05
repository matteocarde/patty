(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b2) 80.0)
		(off b2)
		(datatosend)
		(off b3)
		(off b1)
		(= (SoC b3) 100.0)
		(night)
		(= (roverenergy) 0.0)
		(= (SoC b1) 40.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)