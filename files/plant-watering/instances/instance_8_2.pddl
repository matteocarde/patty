;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_8_2)
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
	(= (x agent1) 8)
	(= (y agent1) 7)
	(= (x plant6) 4)
	(= (y plant6) 4)
	(= (x plant1) 2)
	(= (y plant1) 2)
	(= (x plant4) 3)
	(= (y plant4) 3)
	(= (x plant3) 6)
	(= (y plant3) 6)
	(= (x tap1) 5)
	(= (y tap1) 5)
	(= (x plant5) 8)
	(= (y plant5) 8)
	(= (x plant2) 6)
	(= (y plant2) 6)
  )

  (:goal (and 
    (= (poured plant1) 10)
	(= (poured plant2) 4)
	(= (poured plant3) 8)
	(= (poured plant4) 4)
	(= (poured plant5) 10)
	(= (poured plant6) 7)
	(= (total_poured) (+ (+ (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) (poured plant5)) (poured plant6)) )
  ))

  
  

  
)
