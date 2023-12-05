(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 5994.0)
		(= (fuel plane1) 3997.0)
		(= (slow-burn plane1) 43.0)
		(= (fast-burn plane1) 35.0)
		(= (onboard plane1) -1.0)
		(= (zoom-limit plane1) -31.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) 32.0)
		(= (distance city0 city1) 715.0)
		(= (distance city0 city2) 803.0)
		(= (distance city1 city0) 651.0)
		(= (distance city1 city1) -4.0)
		(= (distance city1 city2) 839.0)
		(= (distance city2 city0) 758.0)
		(= (distance city2 city1) 825.0)
		(= (distance city2 city2) 26.0)
		(= (total-fuel-used) 8.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)