(define (problem instance_11_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
	)
	(:goal
			(and
				(= (poured plant1) 10.0)
				(= (poured plant2) 1.0)
				(= (poured plant3) 8.0)
				(= (poured plant4) 8.0)
				(= (poured plant5) 1.0)
				(= (total_poured) (total_loaded))
			)
	)
)