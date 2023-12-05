(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 city3 - city
	)
	(:init
		(= (slow-burn plane1) 1.0)
		(= (fast-burn plane1) 3.0)
		(= (zoom-limit plane1) 3.0)
		(located plane1 city1)
		(= (distance city0 city0) 0.0)
		(= (capacity plane1) 2990.0)
		(located person1 city3)
		(= (distance city2 city0) 607.0)
		(= (capacity plane2) 4839.0)
		(= (slow-burn plane2) 2.0)
		(located person3 city0)
		(= (distance city3 city1) 557.0)
		(= (fuel plane1) 174.0)
		(= (distance city3 city3) 0.0)
		(= (distance city1 city0) 569.0)
		(= (distance city0 city1) 569.0)
		(= (distance city2 city1) 504.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city3)
				(located person3 city3)
				(located person4 city3)
			)
	)
)