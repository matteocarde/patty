(define (problem instance_10_17_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 plant6 plant7 plant8 plant9 plant10 plant11 plant12 plant13 plant14 plant15 plant16 plant17 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
	)
	(:goal
			(and
				(= (poured plant1) 10.0)
				(= (poured plant2) 4.0)
				(= (poured plant3) 8.0)
				(= (poured plant4) 6.0)
				(= (poured plant5) 6.0)
				(= (poured plant6) 9.0)
				(= (poured plant7) 1.0)
				(= (poured plant8) 7.0)
				(= (poured plant9) 9.0)
				(= (poured plant10) 10.0)
				(= (poured plant11) 10.0)
				(= (poured plant12) 6.0)
				(= (poured plant13) 10.0)
				(= (poured plant14) 1.0)
				(= (poured plant15) 4.0)
				(= (poured plant16) 9.0)
				(= (poured plant17) 3.0)
				(= (total_poured) (total_loaded))
			)
	)
)