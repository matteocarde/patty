(define (problem instance_10_5_2_1)
	(:domain ext-plant-watering)
	(:objects
		plant1 plant2 plant3 plant4 plant5 - plant
		tap1 - tap
		agent1 agent2 - agent
	)
	(:init
		(= (maxx) -1.0)
		(= (minx) -7.0)
		(= (maxy) -8.0)
		(= (miny) -8.0)
		(= (total_poured) 18.0)
		(= (total_loaded) -5.0)
		(= (water_reserve) 21.0)
		(= (carrying agent1) 0.0)
		(= (max_carry agent1) 20.0)
		(= (carrying agent2) -1.0)
		(= (max_carry agent2) -6.0)
		(= (poured plant1) -19.0)
		(= (poured plant2) 11.0)
		(= (poured plant3) 13.0)
		(= (poured plant4) 4.0)
		(= (poured plant5) -1.0)
		(= (x plant1) -8.0)
		(= (y plant1) -3.0)
		(= (x plant2) 14.0)
		(= (y plant2) -10.0)
		(= (x plant3) -10.0)
		(= (y plant3) -17.0)
		(= (x plant4) 20.0)
		(= (y plant4) 14.0)
		(= (x plant5) 16.0)
		(= (y plant5) 18.0)
		(= (x tap1) 22.0)
		(= (y tap1) 17.0)
		(= (x agent1) 6.0)
		(= (y agent1) 20.0)
		(= (x agent2) 11.0)
		(= (y agent2) 23.0)
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