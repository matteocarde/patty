;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_20_10_2_2)
  (:domain mt-block-grouping)
  (:objects
    b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 - block
  )

  (:init
    (= (x b9) 15)
	(= (y b9) 20)
	(= (x b5) 13)
	(= (y b5) 3)
	(= (x b4) 11)
	(= (y b4) 18)
	(= (x b2) 12)
	(= (y b2) 2)
	(= (x b1) 6)
	(= (y b1) 16)
	(= (x b10) 17)
	(= (y b10) 8)
	(= (x b8) 7)
	(= (y b8) 18)
	(= (x b3) 1)
	(= (y b3) 14)
	(= (x b6) 17)
	(= (y b6) 5)
	(= (x b7) 19)
	(= (y b7) 11)
	(= (max_x) 20 )
	(= (min_x) 1 )
	(= (max_y) 20 )
	(= (min_y) 1 )
  )

  (:goal (and 
    (= (x b1) (x b2))
(= (y b1) (y b2))
	(or (not (= (x b1) (x b3))) (not (= (y b1) (y b3))))
	(or (not (= (x b1) (x b4))) (not (= (y b1) (y b4))))
	(or (not (= (x b1) (x b5))) (not (= (y b1) (y b5))))
	(or (not (= (x b1) (x b6))) (not (= (y b1) (y b6))))
	(or (not (= (x b1) (x b7))) (not (= (y b1) (y b7))))
	(= (x b1) (x b8))
(= (y b1) (y b8))
	(= (x b1) (x b9))
(= (y b1) (y b9))
	(= (x b1) (x b10))
(= (y b1) (y b10))
	(or (not (= (x b2) (x b3))) (not (= (y b2) (y b3))))
	(or (not (= (x b2) (x b4))) (not (= (y b2) (y b4))))
	(or (not (= (x b2) (x b5))) (not (= (y b2) (y b5))))
	(or (not (= (x b2) (x b6))) (not (= (y b2) (y b6))))
	(or (not (= (x b2) (x b7))) (not (= (y b2) (y b7))))
	(= (x b2) (x b8))
(= (y b2) (y b8))
	(= (x b2) (x b9))
(= (y b2) (y b9))
	(= (x b3) (x b4))
(= (y b3) (y b4))
	(= (x b3) (x b5))
(= (y b3) (y b5))
	(= (x b3) (x b6))
(= (y b3) (y b6))
	(= (x b3) (x b7))
(= (y b3) (y b7))
	(or (not (= (x b3) (x b8))) (not (= (y b3) (y b8))))
	(or (not (= (x b3) (x b9))) (not (= (y b3) (y b9))))
	(= (x b4) (x b5))
(= (y b4) (y b5))
	(= (x b4) (x b6))
(= (y b4) (y b6))
	(= (x b4) (x b7))
(= (y b4) (y b7))
	(or (not (= (x b4) (x b8))) (not (= (y b4) (y b8))))
	(or (not (= (x b4) (x b9))) (not (= (y b4) (y b9))))
	(= (x b5) (x b6))
(= (y b5) (y b6))
	(= (x b5) (x b7))
(= (y b5) (y b7))
	(or (not (= (x b5) (x b8))) (not (= (y b5) (y b8))))
	(or (not (= (x b5) (x b9))) (not (= (y b5) (y b9))))
	(= (x b6) (x b7))
(= (y b6) (y b7))
	(or (not (= (x b6) (x b8))) (not (= (y b6) (y b8))))
	(or (not (= (x b6) (x b9))) (not (= (y b6) (y b9))))
	(or (not (= (x b7) (x b8))) (not (= (y b7) (y b8))))
	(or (not (= (x b7) (x b9))) (not (= (y b7) (y b9))))
	(= (x b8) (x b9))
(= (y b8) (y b9))
	(= (x b10) (x b2))
(= (y b10) (y b2))
	(or (not (= (x b10) (x b3))) (not (= (y b10) (y b3))))
	(or (not (= (x b10) (x b4))) (not (= (y b10) (y b4))))
	(or (not (= (x b10) (x b5))) (not (= (y b10) (y b5))))
	(or (not (= (x b10) (x b6))) (not (= (y b10) (y b6))))
	(or (not (= (x b10) (x b7))) (not (= (y b10) (y b7))))
	(= (x b10) (x b8))
(= (y b10) (y b8))
	(= (x b10) (x b9))
(= (y b10) (y b9))
  ))

  
  

  
)
