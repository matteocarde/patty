(define (problem ZTRAVEL-2-5)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 person5 - person
		city0 city1 city2 - city
	)
	(:init
		(= (distance city1 city0) 834.0)
		(= (onboard plane2) 0.0)
		(= (fuel plane1) 1048.0)
		(= (distance city0 city0) 0.0)
		(located person4 city0)
		(= (distance city2 city0) 743.0)
		(= (distance city2 city2) 0.0)
		(= (distance city1 city2) 502.0)
		(located plane2 city2)
		(= (capacity plane1) 5304.0)
		(= (fast-burn plane2) 4.0)
		(= (slow-burn plane2) 2.0)
		(= (distance city2 city1) 502.0)
		(located person1 city0)
		(= (slow-burn plane1) 2.0)
		(= (distance city0 city2) 743.0)
		(= (onboard plane1) 0.0)
		(= (zoom-limit plane1) 2.0)
		(located person5 city2)
		(= (fast-burn plane1) 7.0)
		(located plane1 city2)
	)
	(:goal
			(and
				(located plane1 city0)
				(located person2 city2)
				(located person3 city0)
				(located person4 city1)
				(located person5 city2)
			)
	)
)