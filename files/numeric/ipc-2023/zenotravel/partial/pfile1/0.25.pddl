(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located person3 city1)
		(= (slow-burn plane1) 4.0)
		(= (zoom-limit plane1) 8.0)
		(= (distance city0 city0) 0.0)
		(located plane1 city0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)