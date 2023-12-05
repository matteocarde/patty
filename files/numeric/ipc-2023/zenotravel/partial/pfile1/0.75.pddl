(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(= (capacity plane1) 6000.0)
		(= (distance city1 city0) 678.0)
		(= (fast-burn plane1) 15.0)
		(= (slow-burn plane1) 4.0)
		(= (distance city2 city2) 0.0)
		(= (distance city0 city0) 0.0)
		(= (total-fuel-used) 0.0)
		(= (fuel plane1) 4000.0)
		(= (distance city0 city1) 678.0)
		(= (distance city1 city1) 0.0)
		(located person2 city0)
		(= (onboard plane1) 0.0)
		(= (distance city2 city1) 810.0)
		(= (distance city0 city2) 775.0)
		(= (distance city2 city0) 775.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)