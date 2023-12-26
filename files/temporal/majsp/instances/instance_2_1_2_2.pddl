
(define (problem instance2_2_1)

(:domain majsp)

(:objects
	r0 r1 - Robot
	p0 p1 - Position
	t0 t1 - Treatment
	b0 - Pallet
)

(:init
	(robot-at r0 p1)
	(robot-at r1 p1)

	(robot-free r0)
	(robot-free r1)

	(= (battery-level r0) 4.0)
	(= (battery-level r1) 4.0)


	(pallet-at b0 p1)
	(is-depot p1)

	(position-free p0)
	(position-free p1)

	(can-do p0 t1)
	(can-do p0 t0)

	(= (distance p1 p0) 1)
	(= (distance p0 p1) 1)

	
)

(:goal
	(and
	(treated b0 t0)
	(treated b0 t1)

	)
)
)

