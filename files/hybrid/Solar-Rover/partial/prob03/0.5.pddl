(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b3) 100.0)
		(= (time) 0.0)
		(off b1)
		(datatosend)
		(night)
		(= (roverenergy) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)