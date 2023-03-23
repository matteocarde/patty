;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_11_5_2_1)
  (:domain mt-block-grouping)
  (:objects
    b1 b2 b3 b4 b5 - block
  )

  (:init
    (= (x b3) 4)
	(= (y b3) 10)
	(= (x b4) 9)
	(= (y b4) 9)
	(= (x b2) 1)
	(= (y b2) 5)
	(= (x b1) 1)
	(= (y b1) 3)
	(= (x b5) 9)
	(= (y b5) 8)
	(= (max_x) 11 )
	(= (min_x) 1 )
	(= (max_y) 11 )
	(= (min_y) 1 )
  )

  (:goal (and 
    (or (not (= (x b1) (x b2))) (not (= (y b1) (y b2))))
	(= (x b1) (x b3))
(= (y b1) (y b3))
	(or (not (= (x b1) (x b4))) (not (= (y b1) (y b4))))
	(or (not (= (x b1) (x b5))) (not (= (y b1) (y b5))))
	(or (not (= (x b2) (x b3))) (not (= (y b2) (y b3))))
	(= (x b2) (x b4))
(= (y b2) (y b4))
	(= (x b2) (x b5))
(= (y b2) (y b5))
	(or (not (= (x b3) (x b4))) (not (= (y b3) (y b4))))
	(or (not (= (x b3) (x b5))) (not (= (y b3) (y b5))))
	(= (x b4) (x b5))
(= (y b4) (y b5))
  ))

  
  

  
)
