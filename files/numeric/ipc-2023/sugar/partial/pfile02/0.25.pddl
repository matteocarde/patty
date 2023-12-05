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
		(connected mill1 depot3)
		(connected mill2 depot1)
		(= (truck-cap truck2) 20.0)
		(= (unharvest-field) 3.0)
		(at-location crane3 mill3)
		(change-process brand4 brand2)
		(= (capacity crane1) 5.0)
		(= (in-storage depot1 brand4) 0.0)
		(current-process mill3 brand2)
		(= (in-storage mill2 brand3) 0.0)
		(current-process mill1 brand1)
		(= (max-service-time crane3) 10.0)
		(change-process brand4 brand3)
		(= (in-storage mill2 brand2) 0.0)
		(= (service-time crane2) 15.0)
		(at-location truck2 depot2)
		(at-location crane2 mill2)
		(produce mill1 brand1)
		(= (in-storage mill2 brand1) 0.0)
		(= (in-storage mill3 brand1) 0.0)
		(= (max-service-time crane2) 15.0)
		(= (in-truck-sugar brand4 truck1) 0.0)
		(= (in-storage depot1 brand1) 0.0)
		(change-process brand3 brand2)
		(produce mill1 brand4)
		(= (inventory-cost) 0.0)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 10.0)
				(>= (in-storage depot2 brand3) 5.0)
			)
	)
)