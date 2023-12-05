(define (problem mprime-x-9)
	(:domain mystery-prime-typed)
	(:objects
		apple flounder haroset hamburger wurst hotdog guava - food
		entertainment intoxication curiosity excitement - pleasure
		dread sciatica abrasion prostatitis loneliness anger hangover anxiety laceration boils jealousy angina grief - pain
	)
	(:init
		(craves angina guava)
		(craves laceration wurst)
		(craves curiosity hotdog)
		(eats apple guava)
		(= (locale haroset) 2.0)
		(eats flounder wurst)
		(craves intoxication haroset)
		(craves dread flounder)
		(eats apple hotdog)
		(= (locale guava) 4.0)
		(craves boils guava)
		(eats hamburger haroset)
		(= (locale wurst) 1.0)
		(craves sciatica flounder)
		(= (locale flounder) 2.0)
		(craves jealousy guava)
		(craves abrasion haroset)
		(eats hotdog wurst)
		(eats wurst hotdog)
		(eats wurst flounder)
		(eats hamburger flounder)
	)
	(:goal
			(and
				(craves sciatica hamburger)
				(craves jealousy wurst)
			)
	)
)