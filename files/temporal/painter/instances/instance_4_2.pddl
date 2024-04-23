(define (problem p_4_2)

	(:domain new)

	(:objects
		i0 i1 - Item
		t0 t1 t2 t3 last_t - Treatment
	)

        (:init
              (not_busy)
              (not_treated i0 t0)
              (not_treated i0 t1)
              (not_treated i0 t2)
              (not_treated i0 t3)
              (not_treated i1 t0)
              (not_treated i1 t1)
              (not_treated i1 t2)
              (not_treated i1 t3)
              (not_started i0 t0)
              (not_started i0 t1)
              (not_started i0 t2)
              (not_started i0 t3)
              (not_started i1 t0)
              (not_started i1 t1)
              (not_started i1 t2)
              (not_started i1 t3)
              (= (item_id i0) 0)
              (= (item_id i1) 1)
              (consecutive t0 t1)
              (consecutive t1 t2)
              (consecutive t2 t3)
              (consecutive t3 last_t)
              (started i0 last_t)
              (ready i0 t0)
              (started i1 last_t)
              (ready i1 t0)
              (= (counter t0) 0)
              (= (counter t1) 0)
              (= (counter t2) 0)
              (= (counter t3) 0)
              (= (counter last_t) 0)
        )

	(:goal
              (and
              (treated i0 t0)
              (treated i0 t1)
              (treated i0 t2)
              (treated i0 t3)
              (treated i1 t0)
              (treated i1 t1)
              (treated i1 t2)
              (treated i1 t3)
              )
	)
)