(define (problem mprime-x-4)
	(:domain mystery-prime-typed)
	(:objects
		muffin ham scallion shrimp cherry grapefruit bacon arugula scallop wurst - food
		aesthetics - pleasure
		hangover dread sciatica jealousy loneliness abrasion anger - pain
	)
	(:init
		(craves abrasion scallop)
		(eats scallion muffin)
		(eats bacon wurst)
		(= (locale bacon) 1.0)
		(eats shrimp cherry)
		(eats ham cherry)
		(eats arugula scallop)
		(eats cherry ham)
		(craves aesthetics shrimp)
		(eats cherry shrimp)
		(eats wurst bacon)
		(eats grapefruit scallop)
		(craves hangover muffin)
		(eats bacon arugula)
		(= (locale grapefruit) 0.0)
		(= (locale shrimp) 2.0)
		(= (locale scallop) 3.0)
		(= (locale wurst) 0.0)
		(eats shrimp scallion)
		(eats ham muffin)
		(craves dread ham)
		(craves jealousy bacon)
		(craves sciatica grapefruit)
	)
	(:goal
			(and
				(craves sciatica wurst)
			)
	)
)