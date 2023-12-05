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
		(= (fuel plane1) 3992.0)
		(= (slow-burn plane1) 1.0)
		(= (fast-burn plane1) 19.0)
		(= (onboard plane1) -3.0)
		(= (zoom-limit plane1) 13.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) 4.0)
		(= (distance city0 city1) 670.0)
		(= (distance city0 city2) 782.0)
		(= (distance city1 city0) 679.0)
		(= (distance city1 city1) 0.0)
		(= (distance city1 city2) 809.0)
		(= (distance city2 city0) 766.0)
		(= (distance city2 city1) 816.0)
		(= (distance city2 city2) -1.0)
		(= (total-fuel-used) -2.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)