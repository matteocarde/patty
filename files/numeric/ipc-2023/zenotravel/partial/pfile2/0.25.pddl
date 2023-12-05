(define (problem ZTRAVEL-1-3)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(= (onboard plane1) 0.0)
		(= (distance city1 city1) 0.0)
		(located person1 city2)
		(= (distance city1 city0) 627.0)
		(= (capacity plane1) 6830.0)
	)
	(:goal
			(and
				(located plane1 city2)
				(located person1 city1)
				(located person3 city2)
			)
	)
)