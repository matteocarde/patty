(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 5987.0)
		(= (fuel plane1) 3987.0)
		(= (slow-burn plane1) 29.0)
		(= (fast-burn plane1) 14.0)
		(= (onboard plane1) 29.0)
		(= (zoom-limit plane1) 8.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) -19.0)
		(= (distance city0 city1) 685.0)
		(= (distance city0 city2) 760.0)
		(= (distance city1 city0) 692.0)
		(= (distance city1 city1) -18.0)
		(= (distance city1 city2) 828.0)
		(= (distance city2 city0) 783.0)
		(= (distance city2 city1) 828.0)
		(= (distance city2 city2) -21.0)
		(= (total-fuel-used) -9.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)