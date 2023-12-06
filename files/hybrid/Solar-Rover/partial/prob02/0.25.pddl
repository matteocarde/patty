(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(datatosend)
		(= (SoC b2) 80.0)
		(off b3)
	)
	(:goal
			(and
				(datasent)
			)
	)
)