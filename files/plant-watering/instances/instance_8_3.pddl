;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_8_3)
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
	(= (x agent1) 6)
	(= (y agent1) 3)
	(= (x plant6) 2)
	(= (y plant6) 2)
	(= (x plant1) 7)
	(= (y plant1) 7)
	(= (x plant4) 6)
	(= (y plant4) 6)
	(= (x plant3) 1)
	(= (y plant3) 1)
	(= (x tap1) 5)
	(= (y tap1) 5)
	(= (x plant5) 5)
	(= (y plant5) 5)
	(= (x plant2) 6)
	(= (y plant2) 6)
  )

  (:goal (and 
    (= (poured plant1) 6)
	(= (poured plant2) 9)
	(= (poured plant3) 1)
	(= (poured plant4) 7)
	(= (poured plant5) 9)
	(= (poured plant6) 10)
	(= (total_poured) (+ (+ (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) (poured plant5)) (poured plant6)) )
  ))

  
  

  
)
