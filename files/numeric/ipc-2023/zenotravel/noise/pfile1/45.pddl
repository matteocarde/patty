(define (problem ZTRAVEL-1-2)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (capacity plane1) 5957.0)
		(= (fuel plane1) 4030.0)
		(= (slow-burn plane1) 1.0)
		(= (fast-burn plane1) -27.0)
		(= (onboard plane1) -11.0)
		(= (zoom-limit plane1) -8.0)
		(located person1 city0)
		(located person2 city0)
		(located person3 city1)
		(= (distance city0 city0) -9.0)
		(= (distance city0 city1) 652.0)
		(= (distance city0 city2) 746.0)
		(= (distance city1 city0) 699.0)
		(= (distance city1 city1) 33.0)
		(= (distance city1 city2) 829.0)
		(= (distance city2 city0) 760.0)
		(= (distance city2 city1) 802.0)
		(= (distance city2 city2) -20.0)
		(= (total-fuel-used) 42.0)
	)
	(:goal
			(and
				(located person1 city2)
				(located person2 city1)
				(located person3 city2)
			)
	)
)