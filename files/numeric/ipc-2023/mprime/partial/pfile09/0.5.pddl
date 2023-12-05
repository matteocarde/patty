(define (problem mprime-x-9)
	(:domain mystery-prime-typed)
	(:objects
		apple flounder haroset hamburger wurst hotdog guava - food
		entertainment intoxication curiosity excitement - pleasure
		dread sciatica abrasion prostatitis loneliness anger hangover anxiety laceration boils jealousy angina grief - pain
	)
	(:init
		(= (locale hotdog) 1.0)
		(= (harmony intoxication) 1.0)
		(eats haroset guava)
		(craves jealousy guava)
		(craves entertainment flounder)
		(eats flounder wurst)
		(= (harmony excitement) 1.0)
		(craves grief guava)
		(craves abrasion haroset)
		(eats apple hotdog)
		(eats haroset hamburger)
		(eats apple guava)
		(= (harmony entertainment) 3.0)
		(eats flounder hamburger)
		(= (locale wurst) 1.0)
		(craves anger haroset)
		(craves curiosity hotdog)
		(craves sciatica flounder)
		(eats hamburger flounder)
		(craves laceration wurst)
		(craves excitement guava)
	)
	(:goal
			(and
				(craves sciatica hamburger)
				(craves jealousy wurst)
			)
	)
)