(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 5999.0)
		(= (fuel plane1) 4015.0)
		(= (slow-burn plane1) 9.0)
		(= (fast-burn plane1) 20.0)
		(= (onboard plane1) -5.0)
		(= (zoom-limit plane1) 23.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) 6.0)
		(= (distance city0 city1) 691.0)
		(= (distance city0 city2) 763.0)
		(= (distance city1 city0) 664.0)
		(= (distance city1 city1) 12.0)
		(= (distance city1 city2) 820.0)
		(= (distance city2 city0) 784.0)
		(= (distance city2 city1) 824.0)
		(= (distance city2 city2) -12.0)
		(= (total-fuel-used) -7.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)