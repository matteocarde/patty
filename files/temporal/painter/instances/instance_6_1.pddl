(define (problem p_6_1)

	(:domain new)

	(:objects
		i0 - Item
		t0 t1 t2 t3 t4 t5 last_t - Treatment
	)

        (:init
              (not_busy)
              (not_treated i0 t0)
              (not_treated i0 t1)
              (not_treated i0 t2)
              (not_treated i0 t3)
              (not_treated i0 t4)
              (not_treated i0 t5)
              (not_started i0 t0)
              (not_started i0 t1)
              (not_started i0 t2)
              (not_started i0 t3)
              (not_started i0 t4)
              (not_started i0 t5)
              (= (item_id i0) 0)
              (consecutive t0 t1)
              (consecutive t1 t2)
              (consecutive t2 t3)
              (consecutive t3 t4)
              (consecutive t4 t5)
              (consecutive t5 last_t)
              (started i0 last_t)
              (ready i0 t0)
              (= (counter t0) 0)
              (= (counter t1) 0)
              (= (counter t2) 0)
              (= (counter t3) 0)
              (= (counter t4) 0)
              (= (counter t5) 0)
              (= (counter last_t) 0)
        )

	(:goal
              (and
              (treated i0 t0)
              (treated i0 t1)
              (treated i0 t2)
              (treated i0 t3)
              (treated i0 t4)
              (treated i0 t5)
              )
	)
)
