(define (problem p_8_3)

	(:domain new)

	(:objects
		i0 i1 i2 - Item
		t0 t1 t2 t3 t4 t5 t6 t7 last_t - Treatment
	)

        (:init
              (not_busy)
              (not_treated i0 t0)
              (not_treated i0 t1)
              (not_treated i0 t2)
              (not_treated i0 t3)
              (not_treated i0 t4)
              (not_treated i0 t5)
              (not_treated i0 t6)
              (not_treated i0 t7)
              (not_treated i1 t0)
              (not_treated i1 t1)
              (not_treated i1 t2)
              (not_treated i1 t3)
              (not_treated i1 t4)
              (not_treated i1 t5)
              (not_treated i1 t6)
              (not_treated i1 t7)
              (not_treated i2 t0)
              (not_treated i2 t1)
              (not_treated i2 t2)
              (not_treated i2 t3)
              (not_treated i2 t4)
              (not_treated i2 t5)
              (not_treated i2 t6)
              (not_treated i2 t7)
              (not_started i0 t0)
              (not_started i0 t1)
              (not_started i0 t2)
              (not_started i0 t3)
              (not_started i0 t4)
              (not_started i0 t5)
              (not_started i0 t6)
              (not_started i0 t7)
              (not_started i1 t0)
              (not_started i1 t1)
              (not_started i1 t2)
              (not_started i1 t3)
              (not_started i1 t4)
              (not_started i1 t5)
              (not_started i1 t6)
              (not_started i1 t7)
              (not_started i2 t0)
              (not_started i2 t1)
              (not_started i2 t2)
              (not_started i2 t3)
              (not_started i2 t4)
              (not_started i2 t5)
              (not_started i2 t6)
              (not_started i2 t7)
              (= (item_id i0) 0)
              (= (item_id i1) 1)
              (= (item_id i2) 2)
              (consecutive t0 t1)
              (consecutive t1 t2)
              (consecutive t2 t3)
              (consecutive t3 t4)
              (consecutive t4 t5)
              (consecutive t5 t6)
              (consecutive t6 t7)
              (consecutive t7 last_t)
              (started i0 last_t)
              (ready i0 t0)
              (started i1 last_t)
              (ready i1 t0)
              (started i2 last_t)
              (ready i2 t0)
              (= (counter t0) 0)
              (= (counter t1) 0)
              (= (counter t2) 0)
              (= (counter t3) 0)
              (= (counter t4) 0)
              (= (counter t5) 0)
              (= (counter t6) 0)
              (= (counter t7) 0)
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
              (treated i0 t6)
              (treated i0 t7)
              (treated i1 t0)
              (treated i1 t1)
              (treated i1 t2)
              (treated i1 t3)
              (treated i1 t4)
              (treated i1 t5)
              (treated i1 t6)
              (treated i1 t7)
              (treated i2 t0)
              (treated i2 t1)
              (treated i2 t2)
              (treated i2 t3)
              (treated i2 t4)
              (treated i2 t5)
              (treated i2 t6)
              (treated i2 t7)
              )
	)
)
