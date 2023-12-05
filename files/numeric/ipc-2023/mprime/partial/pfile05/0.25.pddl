(define (problem mprime-x-5)
	(:domain mystery-prime-typed)
	(:objects
		broccoli chocolate turkey tuna sweetroll shrimp cherry scallop - food
		satisfaction excitement intoxication lubricity - pleasure
		sciatica anxiety grief boils depression abrasion prostatitis angina jealousy laceration anger grief-2 dread loneliness hangover - pain
	)
	(:init
		(= (harmony intoxication) 2.0)
		(eats chocolate broccoli)
		(craves satisfaction broccoli)
		(eats scallop cherry)
		(craves abrasion turkey)
		(= (locale scallop) 0.0)
		(eats broccoli chocolate)
		(craves lubricity sweetroll)
		(eats scallop sweetroll)
		(= (locale shrimp) 1.0)
		(craves dread scallop)
		(eats cherry shrimp)
	)
	(:goal
			(and
				(craves loneliness shrimp)
				(craves grief shrimp)
			)
	)
)