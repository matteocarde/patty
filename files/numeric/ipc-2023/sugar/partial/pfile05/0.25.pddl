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
		(connected depot3 mill3)
		(current-process mill1 brand1)
		(connected depot3 mill1)
		(connected depot2 depot3)
		(= (truck-cap truck1) 10.0)
		(= (in-storage depot2 brand1) 0.0)
		(connected depot1 mill2)
		(change-process brand4 brand1)
		(= (max-changing mill1) 2.0)
		(= (in-truck-sugar brand2 truck2) 0.0)
		(connected depot2 mill2)
		(= (max-changing mill3) 2.0)
		(= (in-storage depot3 brand2) 0.0)
		(= (in-storage mill2 brand1) 0.0)
		(current-process mill2 brand3)
		(= (in-storage mill2 brand2) 0.0)
		(at-location crane1 mill1)
		(= (in-truck-sugar brand2 truck1) 0.0)
		(= (in-storage depot3 brand4) 0.0)
		(connected mill2 depot3)
		(produce mill3 brand1)
		(= (has-resource sugar-cane mill1) 0.0)
		(change-process brand3 brand1)
		(= (in-storage depot1 brand4) 0.0)
		(= (cost-process mill2) 3.0)
		(produce mill1 brand4)
		(connected mill2 mill1)
		(= (in-storage depot1 brand1) 0.0)
		(at-location crane2 mill2)
		(change-process brand1 brand2)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand4) 4.0)
				(>= (in-storage depot2 brand4) 4.0)
			)
	)
)