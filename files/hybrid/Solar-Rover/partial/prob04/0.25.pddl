(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (time) 0.0)
		(off b3)
		(= (SoC b1) 40.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)