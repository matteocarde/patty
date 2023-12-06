(define (problem mprime-x-4)
	(:domain mystery-prime-typed)
	(:objects
		muffin ham scallion shrimp cherry grapefruit bacon arugula scallop wurst - food
		aesthetics - pleasure
		hangover dread sciatica jealousy loneliness abrasion anger - pain
	)
	(:init
		(craves sciatica grapefruit)
		(eats muffin cherry)
		(= (locale scallop) 3.0)
		(craves hangover muffin)
		(eats muffin arugula)
		(eats cherry ham)
		(eats bacon arugula)
		(eats bacon wurst)
		(craves dread ham)
		(eats ham cherry)
		(craves loneliness arugula)
	)
	(:goal
			(and
				(craves sciatica wurst)
			)
	)
)