;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_4_2)
  (:domain fn-counters-rnd)
  (:objects
    c0 c1 c2 c3 - counter
  )

  (:init
    (= (max_int) 8)
	(= (value c0) 1)
	(= (value c1) 7)
	(= (value c2) 0)
	(= (value c3) 7)
  )

  (:goal (and 
(<= (+ (value c0) 1) (value c1))
(<= (+ (value c1) 1) (value c2))
(<= (+ (value c2) 1) (value c3))
  ))

  
)
