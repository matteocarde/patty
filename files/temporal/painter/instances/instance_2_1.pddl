(define (problem p_2_1)
	(:domain new)
	(:objects
		i0 - Item
		t0 t1 last_t - Treatment
	)

	(:init
		(not_busy)
		(not_treated i0 t0)
		(not_treated i0 t1)
		(not_started i0 t0)
		(not_started i0 t1)
		(= (item_id i0) 0)
		(consecutive t0 t1)
		(consecutive t1 last_t)
		(started i0 last_t)
		(ready i0 t0)
		(= (counter t0) 0)
		(= (counter t1) 0)
		(= (counter last_t) 0)
	)

	(:goal
		(and
			(treated i0 t0)
			(treated i0 t1)
		)
	)
)