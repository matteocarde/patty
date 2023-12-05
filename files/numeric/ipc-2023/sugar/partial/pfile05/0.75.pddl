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
		(connected depot2 mill1)
		(= (max-service-time crane2) 15.0)
		(connected mill3 depot3)
		(produce mill1 brand3)
		(= (in-storage mill1 brand4) 0.0)
		(= (in-storage mill1 brand3) 0.0)
		(connected depot2 mill3)
		(= (cost-process mill1) 1.0)
		(= (in-storage mill2 brand2) 0.0)
		(= (capacity crane2) 5.0)
		(= (in-storage depot3 brand1) 0.0)
		(at-location crane1 mill1)
		(ready-crane crane1)
		(connected mill1 depot2)
		(= (cost-process mill3) 6.0)
		(= (in-storage mill3 brand4) 2.0)
		(= (in-storage mill3 brand2) 0.0)
		(produce mill1 brand4)
		(connected depot2 depot1)
		(connected mill3 depot2)
		(connected mill2 depot1)
		(connected mill2 mill3)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(= (in-truck-sugar brand3 truck1) 0.0)
		(= (in-storage depot1 brand1) 0.0)
		(= (max-produce mill2) 8.0)
		(change-process brand4 brand3)
		(= (in-truck-sugar brand2 truck2) 0.0)
		(= (truck-cap truck1) 10.0)
		(= (has-resource sugar-cane mill2) 10.0)
		(= (in-storage depot2 brand1) 0.0)
		(change-process brand1 brand2)
		(connected depot2 depot3)
		(connected depot3 mill2)
		(produce mill2 brand2)
		(= (service-time crane2) 15.0)
		(= (capacity crane1) 5.0)
		(at-location truck2 depot2)
		(connected mill2 depot2)
		(change-process brand2 brand1)
		(= (mill-cost) 0.0)
		(connected mill3 depot1)
		(change-process brand3 brand1)
		(available mill1)
		(available mill3)
		(= (max-produce mill3) 10.0)
		(produce mill3 brand1)
		(= (service-time crane1) 10.0)
		(at-location crane3 mill3)
		(= (in-storage mill2 brand1) 0.0)
		(connected depot3 mill3)
		(connected depot3 depot2)
		(connected depot3 mill1)
		(produce mill1 brand1)
		(= (in-truck-sugar brand1 truck2) 0.0)
		(= (has-resource sugar-cane mill1) 0.0)
		(change-process brand2 brand3)
		(connected depot3 depot1)
		(connected mill3 mill1)
		(connected mill2 mill1)
		(connected mill1 mill3)
		(connected mill1 depot3)
		(= (labour-cost) 0.0)
		(at-location truck1 depot1)
		(produce mill2 brand3)
		(= (service-time crane3) 10.0)
		(change-process brand3 brand4)
		(= (max-changing mill1) 2.0)
		(= (in-storage depot2 brand4) 0.0)
		(connected depot1 mill2)
		(change-process brand4 brand2)
		(change-process brand4 brand1)
		(available mill2)
		(connected depot1 mill3)
		(connected depot2 mill2)
		(ready-crane crane2)
		(= (in-storage mill3 brand1) 0.0)
		(= (in-truck-sugar brand1 truck1) 0.0)
		(produce mill3 brand2)
		(= (in-storage mill2 brand3) 0.0)
		(= (in-truck-sugar brand4 truck1) 0.0)
		(= (unharvest-field) 3.0)
		(= (max-produce mill1) 5.0)
		(= (in-storage depot3 brand4) 0.0)
		(change-process brand1 brand3)
		(= (max-service-time crane1) 10.0)
		(connected mill1 depot1)
		(at-location crane2 mill2)
		(connected mill3 mill2)
		(= (in-storage depot3 brand2) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand4) 4.0)
				(>= (in-storage depot2 brand4) 4.0)
			)
	)
)