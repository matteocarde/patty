(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 city3 - city
	)
	(:init
		(= (slow-burn plane2) 2.0)
		(= (capacity plane2) 4839.0)
		(= (distance city3 city3) 0.0)
		(located person4 city1)
		(= (onboard plane1) 0.0)
		(= (onboard plane2) 0.0)
		(= (distance city1 city3) 557.0)
		(= (distance city0 city3) 754.0)
		(= (slow-burn plane1) 1.0)
		(= (distance city3 city0) 754.0)
		(= (distance city2 city0) 607.0)
		(= (distance city0 city1) 569.0)
		(= (distance city2 city3) 660.0)
		(= (distance city1 city1) 0.0)
		(= (distance city0 city2) 607.0)
		(located person3 city0)
		(located plane2 city2)
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