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
		(= (max-service-time crane3) 10.0)
		(change-process brand4 brand1)
		(= (service-time crane1) 5.0)
		(= (max-produce mill1) 5.0)
		(change-process brand2 brand4)
		(produce mill2 brand3)
		(connected mill1 depot3)
		(= (in-storage depot3 brand4) 0.0)
		(= (in-storage mill3 brand2) 0.0)
		(connected depot1 mill3)
		(= (in-storage depot3 brand1) 0.0)
		(= (cost-process mill1) 1.0)
		(change-process brand1 brand2)
		(connected depot3 mill2)
		(change-process brand4 brand3)
		(= (in-truck-sugar brand3 truck2) 0.0)
		(= (in-storage depot3 brand3) 0.0)
		(= (in-storage mill1 brand4) 0.0)
		(connected mill2 mill1)
		(produce mill2 brand4)
		(= (capacity crane1) 10.0)
		(at-location truck1 depot1)
		(connected depot3 mill1)
		(= (in-truck-sugar brand2 truck2) 0.0)
		(= (max-changing mill2) 2.0)
		(= (in-storage mill2 brand2) 0.0)
		(= (max-service-time crane2) 15.0)
		(connected mill1 depot2)
		(= (in-storage mill3 brand1) 0.0)
		(= (in-truck-sugar brand4 truck1) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 5.0)
				(>= (in-storage depot2 brand2) 3.0)
			)
	)
)