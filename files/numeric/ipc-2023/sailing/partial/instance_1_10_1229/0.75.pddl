(define (problem instance_1_10_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 p4 p5 p6 p7 p8 p9 - person
	)
	(:init
		(= (d p2) 63.0)
		(= (d p4) 223.0)
		(= (d p5) 316.0)
		(= (d p0) -370.0)
		(= (d p9) -338.0)
		(= (d p3) 483.0)
		(= (d p6) -394.0)
		(= (x b0) -5.0)
		(= (d p8) -160.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
				(saved p2)
				(saved p3)
				(saved p4)
				(saved p5)
				(saved p6)
				(saved p7)
				(saved p8)
				(saved p9)
			)
	)
)