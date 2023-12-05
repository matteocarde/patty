(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 city3 - city
	)
	(:init
		(located person1 city3)
		(= (slow-burn plane2) 2.0)
		(= (distance city2 city0) 607.0)
		(= (fuel plane2) 1617.0)
		(= (distance city0 city0) 0.0)
		(= (distance city3 city2) 660.0)
		(= (zoom-limit plane1) 3.0)
		(= (capacity plane1) 2990.0)
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