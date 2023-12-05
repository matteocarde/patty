(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(off b2)
		(night)
		(= (time) 0.0)
		(gboff GB)
		(datatosend)
		(= (SoC b2) 80.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)