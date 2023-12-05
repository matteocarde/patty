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
		(available mill3)
		(= (cost-process mill2) 3.0)
		(= (truck-cap truck1) 10.0)
		(produce mill3 brand4)
		(produce mill1 brand1)
		(produce mill2 brand3)
		(at-location truck2 depot2)
		(= (in-storage depot3 brand2) 0.0)
		(change-process brand1 brand4)
		(= (has-resource sugar-cane mill2) 5.0)
		(at-location crane1 mill1)
		(current-process mill3 brand2)
		(= (service-time crane2) 15.0)
		(connected depot3 depot2)
		(connected depot2 depot1)
		(= (service-time crane3) 10.0)
		(= (max-changing mill2) 2.0)
		(= (handling-cost) 0.0)
		(= (in-storage depot1 brand2) 0.0)
		(= (max-service-time crane2) 15.0)
		(change-process brand1 brand3)
		(= (in-storage depot2 brand4) 0.0)
		(= (in-truck-sugar brand4 truck2) 0.0)
		(produce mill1 brand3)
		(= (has-resource sugar-cane mill3) 10.0)
		(= (max-service-time crane1) 10.0)
		(= (in-truck-sugar brand1 truck1) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 7.0)
			)
	)
)