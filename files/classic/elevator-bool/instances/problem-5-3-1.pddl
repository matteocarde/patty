(define (problem pb1)
  (:domain elevator)
  (:objects
    personA - person
    floor1 floor2 - floor
    elevatorX - elevator

  )
  (:init
    (at-person personA floor1)
    (target personA floor2)

    (at-elevator elevatorX floor2)
    (above floor2 floor1)
  )
  (:goal
    (and
      (reached personA)
    )
  )
)