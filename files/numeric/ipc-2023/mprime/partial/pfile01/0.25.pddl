(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats rice rice)
		(eats rice pear)
		(craves depression flounder)
		(eats pear rice)
		(eats pork okra)
		(craves abrasion pork)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)