(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats pork okra)
		(eats lamb flounder)
		(eats okra pear)
		(= (locale pork) 5.0)
		(eats pear rice)
		(eats rice flounder)
		(= (locale rice) 1.0)
		(eats rice pear)
		(= (harmony rest) 3.0)
		(eats rice rice)
		(craves rest pork)
		(eats pear okra)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)