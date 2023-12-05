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
		(change-process brand1 brand3)
		(= (handling-cost) 0.0)
		(change-process brand4 brand3)
		(produce mill3 brand1)
		(current-process mill2 brand3)
		(connected depot1 depot2)
		(produce mill3 brand4)
		(produce mill2 brand3)
		(change-process brand3 brand4)
		(connected mill1 mill2)
		(connected depot1 mill2)
		(= (in-storage depot1 brand1) 0.0)
		(= (capacity crane2) 5.0)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(produce mill2 brand2)
		(connected depot3 depot1)
		(= (in-storage depot2 brand2) 0.0)
		(change-process brand1 brand4)
		(= (service-time crane1) 10.0)
		(= (service-time crane3) 10.0)
		(= (in-storage mill1 brand3) 0.0)
		(= (capacity crane1) 5.0)
		(= (in-storage depot1 brand4) 0.0)
		(connected mill2 depot1)
		(at-location crane1 mill1)
		(connected depot3 mill1)
		(= (in-storage depot2 brand3) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 7.0)
			)
	)
)