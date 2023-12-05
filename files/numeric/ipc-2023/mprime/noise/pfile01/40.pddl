(define (problem mprime-x-1)
	(:domain mystery-prime-typed)
	(:objects
		rice pear flounder okra pork lamb - food
		rest - pleasure
		hangover depression abrasion - pain
	)
	(:init
		(eats lamb pork)
		(eats pork okra)
		(= (locale okra) 10.0)
		(= (locale pork) 28.0)
		(eats pork lamb)
		(= (harmony rest) 19.0)
		(eats lamb flounder)
		(craves depression flounder)
		(eats okra pear)
		(eats rice rice)
		(eats rice flounder)
		(craves abrasion pork)
		(= (locale rice) -37.0)
		(eats flounder lamb)
		(craves rest pork)
		(= (locale pear) 24.0)
		(craves hangover rice)
		(= (locale lamb) -4.0)
		(eats flounder rice)
		(eats rice pear)
		(eats pear okra)
		(eats pear rice)
		(eats okra pork)
		(= (locale flounder) 1.0)
	)
	(:goal
			(and
				(craves abrasion rice)
			)
	)
)