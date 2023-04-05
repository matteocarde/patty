(define (problem pb1)
  (:domain elevator)
  (:objects
    personA personB personC personD personE - person
    floor1 floor2 floor3 - floor
    elevator1 elevator2 elevator3 - elevator

  )
  (:init
    (at-person personA floor1)
    (target personA floor2)
    (at-person personB floor1)
    (target personB floor3)
    (at-person personC floor2)
    (target personC floor3)
    (at-person personD floor1)
    (target personD floor2)
    (at-person personE floor3)
    (target personE floor1)

    (at-elevator elevator1 floor3)
    (at-elevator elevator2 floor2)
    (at-elevator elevator3 floor1)
    (above floor3 floor2)
    (above floor2 floor1)
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