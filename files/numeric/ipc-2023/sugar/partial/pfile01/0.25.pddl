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
		(connected depot3 depot2)
		(= (in-truck-sugar brand3 truck1) 0.0)
		(= (inventory-cost) 0.0)
		(at-location truck2 depot2)
		(change-process brand1 brand2)
		(= (capacity crane2) 5.0)
		(ready-crane crane2)
		(= (mill-cost) 0.0)
		(current-process mill2 brand3)
		(= (max-service-time crane2) 15.0)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(= (service-time crane2) 15.0)
		(connected mill1 depot2)
		(= (in-truck-sugar brand1 truck1) 0.0)
		(connected mill2 mill1)
		(connected depot3 depot1)
		(change-process brand4 brand2)
		(= (in-storage depot1 brand4) 0.0)
		(change-process brand3 brand4)
		(connected depot2 depot1)
		(available mill1)
		(connected depot1 depot2)
		(produce mill1 brand3)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand3) 3.0)
			)
	)
)