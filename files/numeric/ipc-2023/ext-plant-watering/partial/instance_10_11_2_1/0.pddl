(define (problem instance_10_11_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 plant6 plant7 plant8 plant9 plant10 plant11 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
	)
	(:goal
			(and
				(= (poured plant1) 5.0)
				(= (poured plant2) 1.0)
				(= (poured plant3) 6.0)
				(= (poured plant4) 5.0)
				(= (poured plant5) 9.0)
				(= (poured plant6) 4.0)
				(= (poured plant7) 10.0)
				(= (poured plant8) 7.0)
				(= (poured plant9) 5.0)
				(= (poured plant10) 6.0)
				(= (poured plant11) 7.0)
				(= (total_poured) (total_loaded))
			)
	)
)