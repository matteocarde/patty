(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 6012.0)
		(= (fuel plane1) 4011.0)
		(= (slow-burn plane1) 5.0)
		(= (fast-burn plane1) 19.0)
		(= (onboard plane1) -8.0)
		(= (zoom-limit plane1) -5.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) 8.0)
		(= (distance city0 city1) 674.0)
		(= (distance city0 city2) 779.0)
		(= (distance city1 city0) 665.0)
		(= (distance city1 city1) -9.0)
		(= (distance city1 city2) 797.0)
		(= (distance city2 city0) 783.0)
		(= (distance city2 city1) 796.0)
		(= (distance city2 city2) -11.0)
		(= (total-fuel-used) 6.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)