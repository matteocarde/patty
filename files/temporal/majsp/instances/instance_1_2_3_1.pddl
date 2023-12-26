
(define (problem instance1_3_2)

(:domain majsp)

(:objects
	r0 - Robot
	p0 p1 p2 - Position
	t0 - Treatment
	b0 b1 - Pallet
)

(:init
	(robot-at r0 p2)

	(robot-free r0)

	(= (battery-level r0) 12.0)


	(pallet-at b0 p2)
	(pallet-at b1 p2)
	(is-depot p2)

	(position-free p0)
	(position-free p1)
	(position-free p2)

	(can-do p0 t0)

	(= (distance p1 p0) 1)
	(= (distance p1 p2) 1)
	(= (distance p0 p2) 2)
	(= (distance p0 p1) 1)
	(= (distance p2 p1) 1)
	(= (distance p2 p0) 2)

	
)

(:goal
	(and
	(treated b0 t0)
	(treated b1 t0)

	)
)
)

