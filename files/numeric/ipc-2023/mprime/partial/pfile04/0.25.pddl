(define (problem mprime-x-4)
	(:domain mystery-prime-typed)
	(:objects
		muffin ham scallion shrimp cherry grapefruit bacon arugula scallop wurst - food
		aesthetics - pleasure
		hangover dread sciatica jealousy loneliness abrasion anger - pain
	)
	(:init
		(= (locale cherry) 4.0)
		(eats arugula wurst)
		(craves hangover muffin)
		(eats shrimp scallion)
		(eats wurst bacon)
		(eats ham muffin)
		(= (locale muffin) 4.0)
		(eats bacon arugula)
		(= (locale shrimp) 2.0)
		(= (harmony aesthetics) 1.0)
		(craves loneliness arugula)
	)
	(:goal
			(and
				(craves sciatica wurst)
			)
	)
)