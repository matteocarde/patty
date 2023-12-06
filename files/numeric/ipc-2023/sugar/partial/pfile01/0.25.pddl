(define (problem prob1)
	(:domain supply-chain)
	(:objects
		brand1 brand2 brand3 brand4 - brand
		sugar-cane - raw-cane
		truck1 truck2 - truck
		depot1 depot2 depot3 - depot
		mill1 mill2 - mill
		crane1 crane2 crane3 - crane
	)
	(:init
		(connected depot3 depot1)
		(connected depot2 mill1)
		(produce mill2 brand2)
		(= (service-time crane3) 10.0)
		(= (max-changing mill1) 2.0)
		(available mill2)
		(= (service-time crane1) 10.0)
		(= (max-service-time crane1) 10.0)
		(= (cost-process mill2) 3.0)
		(change-process brand2 brand1)
		(connected mill2 depot1)
		(= (in-storage depot1 brand3) 0.0)
		(change-process brand1 brand3)
		(= (max-service-time crane2) 15.0)
		(= (capacity crane2) 5.0)
		(change-process brand3 brand1)
		(connected mill1 depot3)
		(connected depot1 mill2)
		(at-location crane2 mill2)
		(connected mill1 depot1)
		(connected mill2 depot3)
		(= (capacity crane1) 3.0)
		(connected depot2 depot3)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand3) 3.0)
			)
	)
)