;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_8_1)
  (:domain mt-plant-watering-constrained)
  (:objects
    tap1 - tap
	agent1 - agent
	plant2 plant3 plant1 plant6 plant5 plant4 - plant
  )

  (:init
    (= (max_int) 120)
	(= (maxx) 8)
	(= (minx) 1)
	(= (maxy) 8)
	(= (miny) 1)
	(= (carrying) 0)
	(= (total_poured) 0)
	(= (total_loaded) 0)
	(= (poured plant1) 0)
	(= (poured plant2) 0)
	(= (poured plant3) 0)
	(= (poured plant4) 0)
	(= (poured plant5) 0)
	(= (poured plant6) 0)
	(= (x agent1) 1)
	(= (y agent1) 3)
	(= (x plant6) 5)
	(= (y plant6) 5)
	(= (x plant1) 3)
	(= (y plant1) 3)
	(= (x plant4) 2)
	(= (y plant4) 2)
	(= (x plant3) 8)
	(= (y plant3) 8)
	(= (x tap1) 2)
	(= (y tap1) 2)
	(= (x plant5) 8)
	(= (y plant5) 8)
	(= (x plant2) 1)
	(= (y plant2) 1)
  )

  (:goal (and 
    (= (poured plant1) 9)
	(= (poured plant2) 6)
	(= (poured plant3) 6)
	(= (poured plant4) 3)
	(= (poured plant5) 9)
	(= (poured plant6) 2)
	(= (total_poured) (+ (+ (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) (poured plant5)) (poured plant6)) )
  ))

  
  

  
)
