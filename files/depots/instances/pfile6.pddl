(define (problem depotprob5656) (:domain depot)
(:objects
	depot0 - depot
	distributor0 distributor1 - distributor
	truck0 truck1 - truck
	pallet0 pallet1 pallet2 - pallet
	crate0 crate1 crate2 crate3 crate4 crate5 crate6 crate7 crate8 crate9 crate10 crate11 crate12 crate13 crate14 - crate
	hoist0 hoist1 hoist2 - hoist)
(:init
	(located pallet0 depot0)
	(clear crate11)
	(located pallet1 distributor0)
	(clear crate14)
	(located pallet2 distributor1)
	(clear crate10)
	(located truck0 distributor1)
	(= (current_load truck0) 0)
	(= (load_limit truck0) 301)
	(located truck1 depot0)
	(= (current_load truck1) 0)
	(= (load_limit truck1) 268)
	(located hoist0 depot0)
	(available hoist0)
	(located hoist1 distributor0)
	(available hoist1)
	(located hoist2 distributor1)
	(available hoist2)
	(located crate0 distributor1)
	(on crate0 pallet2)
	(= (weight crate0) 89)
	(located crate1 depot0)
	(on crate1 pallet0)
	(= (weight crate1) 62)
	(located crate2 distributor1)
	(on crate2 crate0)
	(= (weight crate2) 42)
	(located crate3 distributor0)
	(on crate3 pallet1)
	(= (weight crate3) 37)
	(located crate4 distributor0)
	(on crate4 crate3)
	(= (weight crate4) 11)
	(located crate5 distributor1)
	(on crate5 crate2)
	(= (weight crate5) 91)
	(located crate6 depot0)
	(on crate6 crate1)
	(= (weight crate6) 58)
	(located crate7 distributor0)
	(on crate7 crate4)
	(= (weight crate7) 58)
	(located crate8 distributor0)
	(on crate8 crate7)
	(= (weight crate8) 20)
	(located crate9 distributor0)
	(on crate9 crate8)
	(= (weight crate9) 15)
	(located crate10 distributor1)
	(on crate10 crate5)
	(= (weight crate10) 95)
	(located crate11 depot0)
	(on crate11 crate6)
	(= (weight crate11) 75)
	(located crate12 distributor0)
	(on crate12 crate9)
	(= (weight crate12) 53)
	(located crate13 distributor0)
	(on crate13 crate12)
	(= (weight crate13) 73)
	(located crate14 distributor0)
	(on crate14 crate13)
	(= (weight crate14) 70)
	(= (fuel-cost) 0)
)

(:goal (and
		(on crate0 crate8)
		(on crate1 crate9)
		(on crate2 crate1)
		(on crate3 crate12)
		(on crate4 crate11)
		(on crate5 crate0)
		(on crate8 pallet0)
		(on crate9 pallet1)
		(on crate10 crate4)
		(on crate11 crate5)
		(on crate12 pallet2)
	)
)

); minimize (total-time)))