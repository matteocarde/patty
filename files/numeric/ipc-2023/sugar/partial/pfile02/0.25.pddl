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
		(= (in-truck-sugar brand4 truck1) 0.0)
		(= (max-changing mill2) 2.0)
		(connected depot1 mill1)
		(= (in-storage depot3 brand2) 0.0)
		(= (max-produce mill1) 5.0)
		(available mill2)
		(= (has-resource sugar-cane mill1) 10.0)
		(change-process brand3 brand1)
		(change-process brand3 brand4)
		(connected depot3 mill1)
		(change-process brand4 brand3)
		(change-process brand2 brand3)
		(change-process brand1 brand2)
		(at-location truck1 depot1)
		(= (in-storage depot3 brand1) 0.0)
		(= (in-truck-sugar brand2 truck2) 0.0)
		(= (in-truck-sugar brand1 truck2) 0.0)
		(= (in-storage depot2 brand4) 0.0)
		(connected depot1 depot3)
		(connected mill1 depot3)
		(= (in-storage mill3 brand1) 0.0)
		(= (max-service-time crane3) 10.0)
		(= (service-time crane2) 15.0)
		(= (max-changing mill1) 2.0)
		(produce mill3 brand4)
		(connected depot2 mill1)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 10.0)
				(>= (in-storage depot2 brand3) 5.0)
			)
	)
)