(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats lamb flounder)
		(= (locale okra) 6.0)
		(= (locale pork) 5.0)
		(eats pear rice)
		(eats okra pear)
		(= (harmony rest) 3.0)
		(eats okra pork)
		(eats rice flounder)
		(eats pork okra)
		(eats rice pear)
		(eats lamb pork)
		(eats rice rice)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)