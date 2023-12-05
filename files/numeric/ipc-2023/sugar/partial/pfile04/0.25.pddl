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
		(connected mill3 depot1)
		(ready-crane crane2)
		(connected mill1 mill2)
		(= (unharvest-field) 3.0)
		(= (mill-cost) 0.0)
		(change-process brand2 brand3)
		(= (in-storage mill1 brand1) 0.0)
		(= (in-storage mill3 brand4) 2.0)
		(change-process brand3 brand2)
		(connected mill3 mill2)
		(change-process brand3 brand1)
		(= (has-resource sugar-cane mill1) 0.0)
		(= (in-storage mill2 brand3) 0.0)
		(change-process brand3 brand4)
		(= (in-storage depot3 brand1) 0.0)
		(produce mill1 brand4)
		(= (in-storage depot3 brand2) 0.0)
		(= (in-storage depot1 brand1) 0.0)
		(= (cost-process mill1) 1.0)
		(at-location truck1 depot1)
		(= (max-service-time crane2) 15.0)
		(= (in-storage depot2 brand3) 0.0)
		(connected mill1 depot2)
		(= (in-truck-sugar brand1 truck1) 0.0)
		(connected depot2 mill2)
		(change-process brand4 brand1)
		(= (has-resource sugar-cane mill3) 10.0)
		(= (service-time crane3) 5.0)
		(= (in-storage depot2 brand1) 0.0)
		(= (max-changing mill3) 2.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 5.0)
				(>= (in-storage depot2 brand2) 3.0)
			)
	)
)