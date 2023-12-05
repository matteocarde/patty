(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b3) 100.0)
		(night)
		(off b1)
		(datatosend)
		(off b2)
		(= (sunexposure_time) 200.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)