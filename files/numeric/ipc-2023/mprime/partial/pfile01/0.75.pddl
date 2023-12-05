(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats okra pork)
		(eats pear rice)
		(eats rice flounder)
		(eats rice pear)
		(= (locale rice) 1.0)
		(craves rest pork)
		(= (harmony rest) 3.0)
		(= (locale flounder) 4.0)
		(eats okra pear)
		(eats flounder rice)
		(eats pork lamb)
		(eats pear okra)
		(= (locale pear) 2.0)
		(eats pork okra)
		(craves depression flounder)
		(= (locale pork) 5.0)
		(eats lamb flounder)
		(eats rice rice)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)