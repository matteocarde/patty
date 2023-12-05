(define (problem ZTRAVEL-1-3)
	(:domain zenotravel)
	(:objects
		plane1 - aircraft
		person1 person2 person3 - person
		city0 city1 city2 - city
	)
	(:init
		(= (distance city0 city1) 627.0)
		(= (total-fuel-used) 0.0)
		(= (zoom-limit plane1) 9.0)
		(= (capacity plane1) 6830.0)
		(= (distance city0 city2) 998.0)
	)
	(:goal
			(and
				(located plane1 city2)
				(located person1 city1)
				(located person3 city2)
			)
	)
)