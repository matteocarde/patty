(define (problem instance_10_11_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 plant6 plant7 plant8 plant9 plant10 plant11 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (minx) 1.0)
		(= (x plant8) 10.0)
		(= (total_poured) 0.0)
		(= (carrying agent1) 0.0)
		(= (y plant4) 10.0)
		(= (poured plant1) 0.0)
		(= (total_loaded) 0.0)
		(= (x agent2) 3.0)
		(= (x plant11) 10.0)
		(= (y plant1) 8.0)
		(= (y plant6) 7.0)
		(= (miny) 1.0)
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