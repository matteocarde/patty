(define (problem problem1)
  (:domain robots)
  (:objects
    robot1 robot2 - robot
    roomA roomB roomC - room
    ball1 - obj
  )
  (:init
    (atRobot robot1 roomA)
    (atRobot robot2 roomB)
    (atObject ball1 roomA)
    (allowed robot1 roomA)
    (allowed robot1 roomB)
    (allowed robot2 roomC)
    (allowed robot2 roomB)
    (link roomA roomB)
    (link roomB roomA)
    (link roomC roomB)
    (link roomB roomC)
    (= (distance roomA roomB) 12)
    (= (distance roomB roomA) 12)
    (= (distance roomC roomB) 120)
    (= (distance roomB roomC) 120)
    (= (speed robot1) 1.0)
    (= (speed robot2) 1.0)
    (= (battery robot1) 100)
    (= (battery robot2) 100)
    (= (dischargeRate robot1) 20.0)
    (= (dischargeRate robot2) 2.0)
  )

  (:goal
    (and
      (atObject ball1 roomC))
    )
  )
)