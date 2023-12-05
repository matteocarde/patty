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
		(= (unharvest-field) -4.0)
		(= (mill-cost) -2.0)
		(= (inventory-cost) 26.0)
		(= (handling-cost) 43.0)
		(= (cost-process mill1) 10.0)
		(= (cost-process mill2) -3.0)
		(= (has-resource sugar-cane mill1) 31.0)
		(= (has-resource sugar-cane mill2) 25.0)
		(= (max-changing mill1) -47.0)
		(= (max-changing mill2) -48.0)
		(= (max-produce mill1) -12.0)
		(= (max-produce mill2) 26.0)
		(available mill1)
		(available mill2)
		(produce mill1 brand1)
		(produce mill1 brand3)
		(produce mill1 brand4)
		(current-process mill1 brand1)
		(produce mill2 brand2)
		(produce mill2 brand3)
		(current-process mill2 brand3)
		(= (in-storage mill1 brand1) -7.0)
		(= (in-storage mill1 brand3) 18.0)
		(= (in-storage mill1 brand4) 41.0)
		(= (in-storage mill2 brand1) -48.0)
		(= (in-storage mill2 brand2) 30.0)
		(= (in-storage mill2 brand3) -23.0)
		(change-process brand1 brand2)
		(change-process brand1 brand3)
		(change-process brand1 brand4)
		(change-process brand2 brand1)
		(change-process brand2 brand3)
		(change-process brand2 brand4)
		(change-process brand3 brand1)
		(change-process brand3 brand2)
		(change-process brand3 brand4)
		(change-process brand4 brand1)
		(change-process brand4 brand2)
		(change-process brand4 brand3)
		(at-location truck1 depot1)
		(at-location truck2 depot2)
		(= (truck-cap truck1) 9.0)
		(= (truck-cap truck2) 5.0)
		(at-location crane1 mill1)
		(at-location crane2 mill2)
		(ready-crane crane1)
		(ready-crane crane2)
		(= (capacity crane1) 5.0)
		(= (capacity crane2) 12.0)
		(= (service-time crane1) 19.0)
		(= (service-time crane2) 63.0)
		(= (service-time crane3) -26.0)
		(= (max-service-time crane1) -26.0)
		(= (max-service-time crane2) 23.0)
		(= (max-service-time crane3) -37.0)
		(= (in-truck-sugar brand1 truck1) 7.0)
		(= (in-truck-sugar brand2 truck1) -14.0)
		(= (in-truck-sugar brand3 truck1) -48.0)
		(= (in-truck-sugar brand4 truck1) 5.0)
		(= (in-truck-sugar brand1 truck2) -7.0)
		(= (in-truck-sugar brand2 truck2) -34.0)
		(= (in-truck-sugar brand3 truck2) -17.0)
		(= (in-truck-sugar brand4 truck2) 21.0)
		(= (in-storage depot1 brand1) -17.0)
		(= (in-storage depot1 brand2) 43.0)
		(= (in-storage depot1 brand3) 27.0)
		(= (in-storage depot1 brand4) -29.0)
		(= (in-storage depot2 brand1) 27.0)
		(= (in-storage depot2 brand2) -46.0)
		(= (in-storage depot2 brand3) -34.0)
		(= (in-storage depot2 brand4) -28.0)
		(= (in-storage depot3 brand1) -25.0)
		(= (in-storage depot3 brand2) 7.0)
		(= (in-storage depot3 brand3) -46.0)
		(= (in-storage depot3 brand4) -7.0)
		(connected mill1 mill2)
		(connected mill2 mill1)
		(connected mill1 depot1)
		(connected depot1 mill1)
		(connected mill1 depot2)
		(connected depot2 mill1)
		(connected mill1 depot3)
		(connected depot3 mill1)
		(connected mill2 depot2)
		(connected depot2 mill2)
		(connected mill2 depot3)
		(connected depot3 mill2)
		(connected mill2 depot1)
		(connected depot1 mill2)
		(connected depot3 depot1)
		(connected depot1 depot3)
		(connected depot3 depot2)
		(connected depot2 depot3)
		(connected depot1 depot2)
		(connected depot2 depot1)
	)
	(:goal
			(and
				(>= (in-storage depot1 brand3) 3.0)
			)
	)
)