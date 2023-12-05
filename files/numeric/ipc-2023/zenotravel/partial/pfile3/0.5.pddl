(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 - city
	)
	(:init
		(= (capacity plane1) 8873.0)
		(located person1 city0)
		(= (distance city0 city2) 532.0)
		(located person3 city1)
		(= (distance city0 city0) 0.0)
		(located person2 city0)
		(= (distance city1 city2) 768.0)
		(= (fuel plane2) 3624.0)
		(= (distance city0 city1) 750.0)
		(= (fuel plane1) 2328.0)
		(= (distance city2 city0) 532.0)
		(= (slow-burn plane1) 3.0)
		(= (distance city2 city1) 768.0)
		(= (zoom-limit plane2) 2.0)
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