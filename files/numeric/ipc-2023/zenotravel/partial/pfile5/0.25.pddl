(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 city3 - city
	)
	(:init
		(= (distance city0 city2) 607.0)
		(= (fuel plane1) 174.0)
		(located person3 city0)
		(= (onboard plane2) 0.0)
		(= (distance city1 city2) 504.0)
		(= (distance city2 city2) 0.0)
		(located person2 city0)
		(= (slow-burn plane2) 2.0)
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