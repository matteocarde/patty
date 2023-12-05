(define (problem ZTRAVEL-1-3)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(= (capacity plane1) 6830.0)
		(located person2 city1)
		(= (distance city1 city0) 627.0)
		(= (distance city0 city1) 627.0)
		(located person3 city2)
		(= (distance city1 city2) 631.0)
		(= (total-fuel-used) 0.0)
		(= (fast-burn plane1) 11.0)
		(= (slow-burn plane1) 3.0)
		(located plane1 city0)
	)
	(:goal
			(and
				(located plane1 city2)
				(located person1 city1)
				(located person3 city2)
			)
	)
)