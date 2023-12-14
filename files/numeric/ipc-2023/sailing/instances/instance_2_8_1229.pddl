;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
;;Setting seed to 1229
(define (problem instance_2_8_1229)

	(:domain sailing)

	(:objects
		b0 b1  - boat
		p0 p1 p2 p3 p4 p5 p6 p7  - person
	)

  (:init
		(= (x b0) 0)
(= (y b0) 0)
(= (x b1) -5)
(= (y b1) 0)


		(= (d p0) -370)
(= (d p1) -58)
(= (d p2) 63)
(= (d p3) 483)
(= (d p4) 223)
(= (d p5) 316)
(= (d p6) -394)
(= (d p7) -242)


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

		)
	)
)


