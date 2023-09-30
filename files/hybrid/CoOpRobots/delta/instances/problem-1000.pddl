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
    (= (distance roomC roomB) 12000)
    (= (distance roomB roomC) 12000)
    (= (speed robot1) 1.0)
    (= (speed robot2) 1.0)
    (= (deltaMovement robot1) 3)
    (= (deltaMovement robot2) 3000)
    (= (deltaCharging robot1) 30)
    (= (deltaCharging robot2) 30)
    (= (battery robot1) 100)
    (= (battery robot2) 100)
    (= (dischargeRate robot1) 20.0)
    (= (dischargeRate robot2) 0.02)
    (= (time) 0.0)
    (= (d robot1) 3.0)
    (= (tk robot1) 0.0)
    (= (d robot2) 3000.0)
    (= (tk robot2) 0.0)
  )

  (:goal
    (and
      (atObject ball1 roomC))
  )
)