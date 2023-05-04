(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 - person
		city0 - city
		city1 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 60)
		(= (fuel plane1) 4)
		(= (slow-burn plane1) 1)
		(= (fast-burn plane1) 3)
		(= (onboard plane1) 0)
		(= (zoom-limit plane1) 8)
		(located person1 city0)
		(= (distance city0 city0) 0)
		(= (distance city0 city1) 6)
		(= (distance city1 city0) 6)
		(= (distance city1 city1) 0)
		(= (total-fuel-used) 0)

	)
	(:goal
		(and
			(located person1 city1)
		)
	)
	;(:metric  minimize (total-fuel-used) )

)