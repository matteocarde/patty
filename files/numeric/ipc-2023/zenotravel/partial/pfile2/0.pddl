(define (problem ZTRAVEL-1-3)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
	)
	(:goal
			(and
				(located plane1 city2)
				(located person1 city1)
				(located person3 city2)
			)
	)
)