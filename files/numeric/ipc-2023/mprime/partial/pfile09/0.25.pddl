(define (problem mprime-x-9)
	(:domain mystery-prime-typed)
	(:objects
		apple flounder haroset hamburger wurst hotdog guava - food
		entertainment intoxication curiosity excitement - pleasure
		dread sciatica abrasion prostatitis loneliness anger hangover anxiety laceration boils jealousy angina grief - pain
	)
	(:init
		(eats flounder wurst)
		(= (harmony intoxication) 1.0)
		(eats flounder hamburger)
		(craves jealousy guava)
		(craves curiosity hotdog)
		(craves dread flounder)
		(eats haroset hamburger)
		(= (locale haroset) 2.0)
		(craves excitement guava)
		(craves intoxication haroset)
	)
	(:goal
			(and
				(craves sciatica hamburger)
				(craves jealousy wurst)
			)
	)
)