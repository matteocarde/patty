(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 5993.0)
		(= (fuel plane1) 4014.0)
		(= (slow-burn plane1) 15.0)
		(= (fast-burn plane1) 14.0)
		(= (onboard plane1) 20.0)
		(= (zoom-limit plane1) -9.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) -21.0)
		(= (distance city0 city1) 701.0)
		(= (distance city0 city2) 773.0)
		(= (distance city1 city0) 688.0)
		(= (distance city1 city1) -9.0)
		(= (distance city1 city2) 788.0)
		(= (distance city2 city0) 773.0)
		(= (distance city2 city1) 799.0)
		(= (distance city2 city2) -14.0)
		(= (total-fuel-used) -15.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)