(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 5997.0)
		(= (fuel plane1) 4002.0)
		(= (slow-burn plane1) 7.0)
		(= (fast-burn plane1) 15.0)
		(= (onboard plane1) -2.0)
		(= (zoom-limit plane1) 11.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) -3.0)
		(= (distance city0 city1) 682.0)
		(= (distance city0 city2) 779.0)
		(= (distance city1 city0) 679.0)
		(= (distance city1 city1) -5.0)
		(= (distance city1 city2) 814.0)
		(= (distance city2 city0) 771.0)
		(= (distance city2 city1) 813.0)
		(= (distance city2 city2) 2.0)
		(= (total-fuel-used) 2.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)