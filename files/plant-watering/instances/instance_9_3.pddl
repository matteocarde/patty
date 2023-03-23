;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_9_3)
  (:domain mt-plant-watering-constrained)
  (:objects
    tap1 - tap
	agent1 - agent
	plant2 plant3 plant1 plant8 plant6 plant5 plant7 plant4 - plant
  )

  (:init
    (= (max_int) 160)
	(= (maxx) 9)
	(= (minx) 1)
	(= (maxy) 9)
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
	(= (poured plant7) 0)
	(= (poured plant8) 0)
	(= (x agent1) 7)
	(= (y agent1) 7)
	(= (x plant3) 1)
	(= (y plant3) 1)
	(= (x plant1) 2)
	(= (y plant1) 2)
	(= (x plant8) 7)
	(= (y plant8) 7)
	(= (x plant6) 5)
	(= (y plant6) 5)
	(= (x plant4) 1)
	(= (y plant4) 1)
	(= (x plant7) 8)
	(= (y plant7) 8)
	(= (x tap1) 4)
	(= (y tap1) 4)
	(= (x plant5) 7)
	(= (y plant5) 7)
	(= (x plant2) 9)
	(= (y plant2) 9)
  )

  (:goal (and 
    (= (poured plant1) 7)
	(= (poured plant2) 10)
	(= (poured plant3) 2)
	(= (poured plant4) 1)
	(= (poured plant5) 10)
	(= (poured plant6) 8)
	(= (poured plant7) 2)
	(= (poured plant8) 2)
	(= (total_poured) (+ (+ (+ (+ (+ (+ (+ (poured plant1) (poured plant2)) (poured plant3)) (poured plant4)) (poured plant5)) (poured plant6)) (poured plant7)) (poured plant8)) )
  ))

  
  

  
)
