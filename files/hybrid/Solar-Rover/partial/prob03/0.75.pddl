(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 0.0)
		(off b3)
		(= (SoC b1) 40.0)
		(night)
		(datatosend)
		(off b1)
		(= (SoC b2) 80.0)
		(= (SoC b3) 100.0)
		(= (time) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)