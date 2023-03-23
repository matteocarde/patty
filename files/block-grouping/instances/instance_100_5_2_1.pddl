;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_100_5_2_1)
  (:domain mt-block-grouping)
  (:objects
    b1 b2 b3 b4 b5 - block
  )

  (:init
    (= (x b3) 3)
	(= (y b3) 14)
	(= (x b4) 74)
	(= (y b4) 5)
	(= (x b2) 68)
	(= (y b2) 11)
	(= (x b1) 28)
	(= (y b1) 46)
	(= (x b5) 28)
	(= (y b5) 49)
	(= (max_x) 100 )
	(= (min_x) 1 )
	(= (max_y) 100 )
	(= (min_y) 1 )
  )

  (:goal (and 
    (= (x b1) (x b2))
(= (y b1) (y b2))
	(or (not (= (x b1) (x b3))) (not (= (y b1) (y b3))))
	(or (not (= (x b1) (x b4))) (not (= (y b1) (y b4))))
	(= (x b1) (x b5))
(= (y b1) (y b5))
	(or (not (= (x b2) (x b3))) (not (= (y b2) (y b3))))
	(or (not (= (x b2) (x b4))) (not (= (y b2) (y b4))))
	(= (x b2) (x b5))
(= (y b2) (y b5))
	(= (x b3) (x b4))
(= (y b3) (y b4))
	(or (not (= (x b3) (x b5))) (not (= (y b3) (y b5))))
	(or (not (= (x b4) (x b5))) (not (= (y b4) (y b5))))
  ))

  
  

  
)
