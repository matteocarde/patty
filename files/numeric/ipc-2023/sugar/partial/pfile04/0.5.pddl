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
		(connected depot3 mill2)
		(connected depot1 depot3)
		(= (cost-process mill2) 3.0)
		(change-process brand1 brand4)
		(connected mill1 depot1)
		(= (max-service-time crane1) 10.0)
		(connected depot2 depot1)
		(current-process mill2 brand3)
		(= (in-truck-sugar brand2 truck2) 0.0)
		(connected mill3 mill2)
		(connected depot1 depot2)
		(at-location crane3 mill3)
		(connected mill2 mill1)
		(current-process mill1 brand1)
		(current-process mill1 brand1)
		(available mill2)
		(= (has-resource sugar-cane mill3) 10.0)
		(change-process brand2 brand3)
		(= (capacity crane2) 10.0)
		(produce mill3 brand2)
		(produce mill2 brand2)
		(change-process brand3 brand4)
		(connected mill3 depot1)
		(change-process brand1 brand3)
		(= (in-storage mill1 brand3) 0.0)
		(= (handling-cost) 0.0)
		(ready-crane crane3)
		(connected depot2 mill2)
		(connected depot1 mill3)
		(connected mill1 mill2)
		(= (max-produce mill2) 8.0)
		(produce mill1 brand4)
		(connected depot1 mill2)
		(= (cost-process mill3) 6.0)
		(= (has-resource sugar-cane mill1) 0.0)
		(produce mill1 brand3)
		(= (max-service-time crane2) 15.0)
		(connected mill1 depot3)
		(connected depot2 mill3)
		(change-process brand4 brand1)
		(= (inventory-cost) 0.0)
		(= (in-storage mill2 brand1) 0.0)
		(= (capacity crane3) 10.0)
		(= (in-truck-sugar brand4 truck2) 0.0)
		(= (service-time crane3) 5.0)
		(= (max-produce mill1) 5.0)
		(at-location truck2 depot2)
		(change-process brand4 brand2)
		(= (has-resource sugar-cane mill2) 5.0)
		(connected depot1 mill1)
		(= (in-storage depot2 brand4) 0.0)
		(= (in-truck-sugar brand4 truck1) 0.0)
		(= (cost-process mill1) 1.0)
		(connected depot2 depot3)
		(= (in-storage depot1 brand2) 0.0)
		(= (in-storage depot1 brand3) 0.0)
		(= (in-storage mill3 brand2) 0.0)
		(= (in-storage depot3 brand1) 0.0)
		(connected mill3 mill1)
		(= (in-storage depot3 brand2) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 5.0)
				(>= (in-storage depot2 brand2) 3.0)
			)
	)
)