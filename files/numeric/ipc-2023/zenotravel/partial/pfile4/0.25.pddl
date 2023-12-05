(define (problem ZTRAVEL-2-5)
	(:domain zenotravel)
	(:objects
		plane1 plane2 - aircraft
		person1 person2 person3 person4 person5 - person
		city0 city1 city2 - city
	)
	(:init
		(= (distance city0 city0) 0.0)
		(= (zoom-limit plane1) 2.0)
		(located person5 city2)
		(located person1 city0)
		(= (distance city0 city1) 834.0)
		(= (onboard plane1) 0.0)
		(= (distance city2 city0) 743.0)
	)
	(:goal
			(and
				(located plane1 city0)
				(located person2 city2)
				(located person3 city0)
				(located person4 city1)
				(located person5 city2)
			)
	)
)