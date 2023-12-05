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
		(produce mill1 brand4)
		(current-process mill2 brand3)
		(= (in-storage depot2 brand3) 0.0)
		(= (in-truck-sugar brand3 truck2) 0.0)
		(= (capacity crane1) 5.0)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(connected depot1 depot3)
		(= (max-produce mill3) 15.0)
		(at-location truck2 depot2)
		(= (max-changing mill3) 2.0)
		(= (in-storage depot2 brand1) 0.0)
		(change-process brand4 brand3)
		(change-process brand2 brand1)
		(connected depot3 mill1)
		(change-process brand2 brand4)
		(available mill1)
		(produce mill3 brand2)
		(= (inventory-cost) 0.0)
		(= (capacity crane2) 5.0)
		(= (in-storage depot1 brand3) 0.0)
		(available mill3)
		(change-process brand3 brand1)
		(= (in-storage mill2 brand1) 0.0)
		(connected depot1 mill2)
		(change-process brand1 brand2)
		(= (in-truck-sugar brand1 truck1) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 10.0)
				(>= (in-storage depot2 brand3) 5.0)
			)
	)
)