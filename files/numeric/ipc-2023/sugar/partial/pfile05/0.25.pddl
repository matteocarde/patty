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
		(at-location truck1 depot1)
		(= (service-time crane2) 15.0)
		(= (in-storage depot3 brand4) 0.0)
		(connected mill2 depot2)
		(= (in-truck-sugar brand3 truck2) 0.0)
		(= (in-storage mill3 brand2) 0.0)
		(= (labour-cost) 0.0)
		(available mill2)
		(change-process brand3 brand1)
		(change-process brand4 brand2)
		(= (max-service-time crane1) 10.0)
		(change-process brand2 brand3)
		(= (in-truck-sugar brand4 truck1) 0.0)
		(= (max-produce mill1) 5.0)
		(connected mill1 mill2)
		(connected mill1 depot3)
		(produce mill1 brand3)
		(connected depot3 mill1)
		(= (in-storage depot2 brand2) 0.0)
		(connected depot1 depot2)
		(= (in-truck-sugar brand4 truck2) 0.0)
		(connected depot2 mill1)
		(available mill3)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(= (cost-process mill3) 6.0)
		(produce mill2 brand4)
		(= (max-changing mill1) 2.0)
		(= (has-resource sugar-cane mill3) 10.0)
		(produce mill1 brand4)
		(connected depot2 depot1)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand4) 4.0)
				(>= (in-storage depot2 brand4) 4.0)
			)
	)
)