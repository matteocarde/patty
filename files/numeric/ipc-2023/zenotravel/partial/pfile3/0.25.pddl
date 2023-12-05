(define (problem ZTRAVEL-2-4)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 - person
		city0 city1 city2 - city
	)
	(:init
		(= (zoom-limit plane2) 2.0)
		(= (onboard plane1) 0.0)
		(= (fuel plane1) 2328.0)
		(located plane2 city2)
		(= (fast-burn plane1) 7.0)
		(= (fuel plane2) 3624.0)
		(= (zoom-limit plane1) 8.0)
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