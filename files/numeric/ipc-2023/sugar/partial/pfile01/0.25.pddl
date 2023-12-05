(define (problem prob1)
	(:domain supply-chain)
	(:objects
		brand1 brand2 brand3 brand4 - brand
		sugar-cane - raw-cane
		truck1 truck2 - truck
		depot1 depot2 depot3 - depot
		mill1 mill2 - mill
		crane1 crane2 crane3 - crane
	)
	(:init
		(= (handling-cost) 0.0)
		(ready-crane crane2)
		(= (max-changing mill1) 2.0)
		(= (in-storage depot2 brand3) 0.0)
		(= (in-storage depot1 brand4) 0.0)
		(= (in-storage mill1 brand4) 0.0)
		(= (in-storage depot2 brand1) 0.0)
		(change-process brand1 brand3)
		(= (has-resource sugar-cane mill1) 3.0)
		(= (max-produce mill2) 8.0)
		(= (in-storage depot2 brand4) 0.0)
		(connected depot2 depot3)
		(= (inventory-cost) 0.0)
		(= (truck-cap truck2) 6.0)
		(= (unharvest-field) 3.0)
		(= (in-storage depot1 brand2) 0.0)
		(connected depot1 depot2)
		(change-process brand2 brand3)
		(= (in-truck-sugar brand1 truck2) 0.0)
		(= (max-service-time crane2) 15.0)
		(= (in-truck-sugar brand2 truck2) 0.0)
		(connected mill2 depot1)
		(connected depot3 mill1)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand3) 3.0)
			)
	)
)