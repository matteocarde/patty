(define (problem ZTRAVEL-1-3)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(= (distance city1 city2) 631.0)
		(= (onboard plane1) 0.0)
		(= (fast-burn plane1) 11.0)
		(= (total-fuel-used) 0.0)
		(= (distance city2 city2) 0.0)
	)
	(:goal
			(and
				(located plane1 city2)
				(located person1 city1)
				(located person3 city2)
			)
	)
)