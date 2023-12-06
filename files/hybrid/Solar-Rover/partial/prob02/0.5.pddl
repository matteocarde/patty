(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(off b1)
		(off b2)
		(datatosend)
		(= (SoC b2) 80.0)
		(= (time) 0.0)
		(= (roverenergy) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)