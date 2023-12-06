(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 - city
	)
	(:init
		(= (distance city2 city0) 532.0)
		(= (distance city1 city1) 0.0)
		(= (slow-burn plane2) 4.0)
		(= (fuel plane1) 2328.0)
		(= (distance city1 city0) 750.0)
		(located plane2 city2)
		(= (distance city2 city1) 768.0)
		(located person4 city1)
		(= (distance city0 city1) 750.0)
		(= (distance city1 city2) 768.0)
		(located person1 city0)
		(= (capacity plane2) 9074.0)
		(= (distance city0 city2) 532.0)
		(= (zoom-limit plane1) 8.0)
	)
	(:goal
			(and
				(located plane2 city2)
				(located person1 city1)
				(located person2 city0)
				(located person3 city0)
				(located person4 city1)
			)
	)
)