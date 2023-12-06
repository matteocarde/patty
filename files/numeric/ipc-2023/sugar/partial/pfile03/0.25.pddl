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
		(= (capacity crane1) 5.0)
		(= (in-storage mill1 brand3) 0.0)
		(connected mill2 mill1)
		(= (max-produce mill1) 5.0)
		(= (in-storage depot1 brand4) 0.0)
		(change-process brand3 brand2)
		(available mill1)
		(produce mill1 brand4)
		(= (in-storage depot2 brand2) 0.0)
		(change-process brand3 brand1)
		(connected depot2 mill2)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(= (max-service-time crane2) 15.0)
		(= (in-storage depot3 brand1) 0.0)
		(= (in-storage mill3 brand2) 0.0)
		(= (in-storage mill2 brand3) 0.0)
		(= (in-storage depot1 brand1) 0.0)
		(ready-crane crane3)
		(at-location crane1 mill1)
		(= (mill-cost) 0.0)
		(produce mill1 brand3)
		(= (cost-process mill1) 1.0)
		(connected mill2 depot1)
		(= (in-storage mill1 brand1) 0.0)
		(connected depot1 depot2)
		(produce mill3 brand4)
		(change-process brand2 brand1)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 7.0)
			)
	)
)