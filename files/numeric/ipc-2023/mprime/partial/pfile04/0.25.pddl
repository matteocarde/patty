(define (problem mprime-x-4)
	(:domain mystery-prime-typed)
	(:objects
		muffin ham scallion shrimp cherry grapefruit bacon arugula scallop wurst - food
		aesthetics - pleasure
		hangover dread sciatica jealousy loneliness abrasion anger - pain
	)
	(:init
		(eats cherry shrimp)
		(eats cherry arugula)
		(= (locale ham) 2.0)
		(eats muffin scallion)
		(= (locale scallop) 3.0)
		(= (locale arugula) 4.0)
		(eats bacon arugula)
		(craves dread ham)
		(= (locale scallion) 1.0)
		(eats grapefruit wurst)
		(eats scallop grapefruit)
	)
	(:goal
			(and
				(craves sciatica wurst)
			)
	)
)