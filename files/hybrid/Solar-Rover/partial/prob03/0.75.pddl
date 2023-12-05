(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 0.0)
		(= (SoC b1) 40.0)
		(off b3)
		(= (SoC b2) 80.0)
		(= (time) 0.0)
		(datatosend)
		(= (SoC b3) 100.0)
		(off b1)
		(off b2)
	)
	(:goal
			(and
				(datasent)
			)
	)
)