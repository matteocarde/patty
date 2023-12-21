

(define (problem turnandopen-2-8-10)
  (:domain turnandopen-strips)
  (:objects
    robot1 robot2 - robot
    rgripper1 lgripper1 rgripper2 lgripper2 - gripper
    room1 room2 room3 room4 room5 room6 room7 room8 - room
    door1 door2 door3 door4 door5 door6 door7 - door
    ball1 ball2 ball3 ball4 ball5 ball6 ball7 ball8 ball9 ball10 - object
  )
  (:init
    (closed door1)
    (closed door2)
    (closed door3)
    (closed door4)
    (closed door5)
    (closed door6)
    (closed door7)
    (connected room1 room2 door1)
    (connected room2 room1 door1)
    (connected room2 room3 door2)
    (connected room3 room2 door2)
    (connected room3 room4 door3)
    (connected room4 room3 door3)
    (connected room4 room5 door4)
    (connected room5 room4 door4)
    (connected room5 room6 door5)
    (connected room6 room5 door5)
    (connected room6 room7 door6)
    (connected room7 room6 door6)
    (connected room7 room8 door7)
    (connected room8 room7 door7)
    (at-robby robot1 room5)
    (free robot1 rgripper1)
    (free robot1 lgripper1)
    (at-robby robot2 room6)
    (free robot2 rgripper2)
    (free robot2 lgripper2)
    (at ball1 room6)
    (at ball2 room7)
    (at ball3 room4)
    (at ball4 room5)
    (at ball5 room1)
    (at ball6 room1)
    (at ball7 room4)
    (at ball8 room7)
    (at ball9 room6)
    (at ball10 room2)
  )
  (:goal
    (and
      (at ball1 room1)
      (at ball2 room8)
      (at ball3 room7)
      (at ball4 room4)
      (at ball5 room2)
      (at ball6 room7)
      (at ball7 room7)
      (at ball8 room6)
      (at ball9 room7)
      (at ball10 room2)
    )
  )
  (:metric minimize
    (total-time)
  )

)