(define (problem mprime-x-4)
	(:domain mystery-prime-typed)
	(:objects
		muffin ham scallion shrimp cherry grapefruit bacon arugula scallop wurst - food
		aesthetics - pleasure
		hangover dread sciatica jealousy loneliness abrasion anger - pain
	)
	(:init
		(craves aesthetics shrimp)
		(eats shrimp cherry)
		(eats cherry ham)
		(= (locale cherry) 4.0)
		(eats shrimp scallion)
		(eats arugula scallop)
		(eats scallion shrimp)
		(= (harmony aesthetics) 1.0)
		(eats scallion muffin)
		(= (locale scallop) 3.0)
		(eats bacon arugula)
		(eats ham cherry)
		(eats ham muffin)
		(eats scallop arugula)
		(craves dread ham)
		(craves sciatica grapefruit)
		(= (locale scallion) 1.0)
		(eats grapefruit scallop)
		(eats muffin arugula)
		(eats bacon wurst)
		(eats muffin cherry)
		(eats cherry muffin)
		(= (locale ham) 2.0)
	)
	(:goal
			(and
				(craves sciatica wurst)
			)
	)
)