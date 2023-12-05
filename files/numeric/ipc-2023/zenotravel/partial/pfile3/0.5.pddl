(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 - city
	)
	(:init
		(located plane1 city0)
		(= (distance city1 city1) 0.0)
		(= (fast-burn plane1) 7.0)
		(located person2 city0)
		(= (distance city0 city2) 532.0)
		(= (zoom-limit plane1) 8.0)
		(located person4 city1)
		(= (onboard plane2) 0.0)
		(= (slow-burn plane1) 3.0)
		(located person3 city1)
		(= (fast-burn plane2) 10.0)
		(= (total-fuel-used) 0.0)
		(located plane2 city2)
		(= (slow-burn plane2) 4.0)
	)
	(:goal
			(and
				(located plane2 city2)
				(located person1 city1)
				(located person2 city0)
				(located person3 city0)
				(located person4 city1)
			)
	)
)