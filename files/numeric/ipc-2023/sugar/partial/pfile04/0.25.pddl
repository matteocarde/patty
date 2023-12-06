(define (problem prob1)
	(:domain supply-chain)
	(:objects
		brand1 brand2 brand3 brand4 - brand
		sugar-cane - raw-cane
		truck1 truck2 - truck
		depot1 depot2 depot3 - depot
		mill1 mill2 mill3 - mill
		crane1 crane2 crane3 - crane
	)
	(:init
		(= (max-service-time crane1) 10.0)
		(connected mill3 depot2)
		(ready-crane crane3)
		(= (max-produce mill3) 10.0)
		(= (in-truck-sugar brand4 truck1) 0.0)
		(produce mill2 brand2)
		(= (in-truck-sugar brand4 truck2) 0.0)
		(= (in-storage depot3 brand1) 0.0)
		(= (in-storage depot1 brand4) 0.0)
		(= (max-changing mill3) 2.0)
		(= (capacity crane2) 10.0)
		(= (in-storage depot1 brand2) 0.0)
		(connected mill2 depot3)
		(available mill1)
		(= (in-storage mill2 brand3) 0.0)
		(connected mill3 mill2)
		(= (capacity crane3) 10.0)
		(= (truck-cap truck1) 10.0)
		(= (in-storage mill2 brand2) 0.0)
		(= (in-storage depot2 brand4) 0.0)
		(at-location crane1 mill1)
		(connected mill1 depot3)
		(= (in-storage depot2 brand1) 0.0)
		(connected mill1 depot1)
		(connected depot2 mill1)
		(= (in-storage mill1 brand1) 0.0)
		(= (in-storage depot1 brand3) 0.0)
		(= (in-storage mill3 brand4) 2.0)
		(available mill2)
		(= (in-storage depot3 brand3) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 5.0)
				(>= (in-storage depot2 brand2) 3.0)
			)
	)
)