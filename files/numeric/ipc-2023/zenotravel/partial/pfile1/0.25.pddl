(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(= (onboard plane1) 0.0)
		(= (distance city2 city0) 775.0)
		(= (distance city1 city2) 810.0)
		(= (distance city2 city1) 810.0)
		(located person3 city1)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)