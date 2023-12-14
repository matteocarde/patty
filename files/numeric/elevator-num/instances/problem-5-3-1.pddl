(define (problem pb1)
  (:domain elevator)
  (:objects
    personA personB personC personD personE - person
    elevatorX - elevator

  )
  (:init
    (= (floors) 3)

    (= (at-person personA) 1)
    (= (target personA) 2)
    (= (weight personA) 60)

    (= (at-person personB) 1)
    (= (target personB) 3)
    (= (weight personB) 70)

    (= (at-person personC) 2)
    (= (target personC) 3)
    (= (weight personC) 75)

    (= (at-person personD) 1)
    (= (target personD) 2)
    (= (weight personD) 55)

    (= (at-person personE) 3)
    (= (target personE) 1)
    (= (weight personE) 100)

    (= (at-elevator elevatorX) 3)

    (= (passengers elevatorX) 0)
    (= (capacity elevatorX) 2)

    (= (max-load elevatorX) 150)
    (= (load elevatorX) 0)
  )
  (:goal
    (and
      (reached personA)
      (reached personB)
      (reached personC)
      (reached personD)
      (reached personE)
    )
  )
)