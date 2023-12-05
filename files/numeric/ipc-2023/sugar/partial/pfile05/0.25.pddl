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
		(= (in-storage depot3 brand3) 0.0)
		(connected depot2 depot1)
		(= (in-storage depot3 brand1) 0.0)
		(at-location crane1 mill1)
		(= (cost-process mill3) 6.0)
		(= (max-changing mill1) 2.0)
		(= (max-produce mill3) 10.0)
		(= (in-storage depot2 brand1) 0.0)
		(change-process brand1 brand4)
		(change-process brand4 brand3)
		(connected mill3 mill1)
		(connected mill2 mill1)
		(connected depot2 mill1)
		(= (in-truck-sugar brand4 truck1) 0.0)
		(connected mill2 depot3)
		(= (in-storage mill3 brand2) 0.0)
		(= (max-service-time crane2) 15.0)
		(current-process mill3 brand1)
		(connected mill3 mill2)
		(ready-crane crane2)
		(= (unharvest-field) 3.0)
		(connected depot2 mill3)
		(= (in-storage depot1 brand3) 0.0)
		(= (truck-cap truck1) 10.0)
		(= (in-storage mill2 brand2) 0.0)
		(= (max-changing mill2) 2.0)
		(produce mill1 brand4)
		(produce mill1 brand1)
		(= (in-truck-sugar brand4 truck2) 0.0)
		(change-process brand3 brand4)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand4) 4.0)
				(>= (in-storage depot2 brand4) 4.0)
			)
	)
)