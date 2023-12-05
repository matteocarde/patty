(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (time) 0.0)
		(off b1)
		(off b2)
		(night)
		(gboff GB)
		(= (SoC b2) 80.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)