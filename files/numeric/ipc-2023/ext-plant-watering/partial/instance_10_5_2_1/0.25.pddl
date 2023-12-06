(define (problem instance_10_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (x plant2) 2.0)
		(= (y plant5) 1.0)
		(= (x agent2) 8.0)
		(= (total_loaded) 0.0)
		(= (poured plant2) 0.0)
		(= (poured plant5) 0.0)
		(= (max_carry agent2) 5.0)
		(= (y agent1) 7.0)
	)
	(:goal
			(and
				(= (poured plant1) 4.0)
				(= (poured plant2) 2.0)
				(= (poured plant3) 7.0)
				(= (poured plant4) 9.0)
				(= (poured plant5) 5.0)
				(= (total_poured) (total_loaded))
			)
	)
)