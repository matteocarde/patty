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
	)
	(:goal
			(and
				(>= (in-storage depot1 brand1) 5.0)
				(>= (in-storage depot2 brand2) 3.0)
			)
	)
)