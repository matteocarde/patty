(define (problem pb1)
  (:domain elevator)
  (:objects
    personA personB personC personD personE - person
    elevator1 elevator2 elevator3 - elevator

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

    (= (at-elevator elevator1) 3)
    (= (at-elevator elevator2) 2)
    (= (at-elevator elevator3) 1)

    (= (passengers elevator1) 0)
    (= (passengers elevator2) 0)
    (= (passengers elevator3) 0)

    (= (load elevator1) 0)
    (= (load elevator2) 0)
    (= (load elevator3) 0)

    (= (capacity elevator1) 2)
    (= (capacity elevator2) 3)
    (= (capacity elevator3) 1)

    (= (max-load elevator1) 120)
    (= (max-load elevator2) 180)
    (= (max-load elevator3) 60)
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