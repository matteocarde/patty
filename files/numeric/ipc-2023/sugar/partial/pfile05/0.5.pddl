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
		(at-location crane2 mill2)
		(current-process mill2 brand3)
		(= (cost-process mill2) 3.0)
		(connected depot1 mill2)
		(produce mill2 brand3)
		(connected mill1 depot2)
		(connected mill2 depot1)
		(change-process brand4 brand1)
		(= (in-storage mill2 brand2) 0.0)
		(produce mill3 brand1)
		(connected depot2 mill1)
		(= (max-changing mill3) 2.0)
		(= (max-service-time crane2) 15.0)
		(at-location crane1 mill1)
		(current-process mill1 brand1)
		(at-location truck1 depot1)
		(= (has-resource sugar-cane mill3) 10.0)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(connected mill3 depot2)
		(= (max-changing mill2) 2.0)
		(produce mill2 brand4)
		(change-process brand2 brand4)
		(change-process brand3 brand1)
		(= (in-storage depot3 brand4) 0.0)
		(= (capacity crane2) 5.0)
		(at-location truck2 depot2)
		(= (max-service-time crane1) 10.0)
		(= (handling-cost) 0.0)
		(= (in-storage mill2 brand1) 0.0)
		(change-process brand2 brand3)
		(connected mill3 mill2)
		(produce mill1 brand4)
		(available mill2)
		(= (unharvest-field) 3.0)
		(= (in-storage mill1 brand4) 0.0)
		(= (max-produce mill3) 10.0)
		(= (service-time crane1) 10.0)
		(= (has-resource sugar-cane mill2) 10.0)
		(= (capacity crane1) 5.0)
		(= (max-service-time crane3) 10.0)
		(connected mill1 mill3)
		(connected depot1 depot2)
		(= (in-storage depot2 brand2) 0.0)
		(= (in-truck-sugar brand3 truck2) 0.0)
		(= (in-storage mill3 brand1) 0.0)
		(change-process brand4 brand3)
		(produce mill2 brand2)
		(= (cost-process mill1) 1.0)
		(= (in-truck-sugar brand1 truck2) 0.0)
		(= (in-storage depot3 brand3) 0.0)
		(= (in-storage mill2 brand3) 0.0)
		(ready-crane crane1)
		(connected depot3 depot2)
		(= (truck-cap truck1) 10.0)
		(= (service-time crane3) 10.0)
		(change-process brand2 brand1)
		(= (in-storage depot1 brand3) 0.0)
		(connected mill1 mill2)
		(= (in-storage depot1 brand1) 0.0)
		(connected depot2 depot3)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand4) 4.0)
				(>= (in-storage depot2 brand4) 4.0)
			)
	)
)