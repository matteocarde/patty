
(define (problem instance2_3_2)

(:domain majsp)

(:objects
	r0 r1 - Robot
	p0 p1 p2 - Position
	t0 t1 - Treatment
	b0 b1 - Pallet
)

(:init
	(robot-at r0 p2)
	(robot-at r1 p2)

	(robot-free r0)
	(robot-free r1)

	(= (battery-level r0) 12.0)
	(= (battery-level r1) 12.0)


	(pallet-at b0 p2)
	(pallet-at b1 p2)
	(is-depot p2)

	(position-free p0)
	(position-free p1)
	(position-free p2)

	(can-do p0 t0)
	(can-do p1 t1)

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
	(treated b0 t1)
	(treated b1 t1)

	)
)
)

