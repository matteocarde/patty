

(define (problem turnandopen-2-9-22)
  (:domain turnandopen-strips)
  (:objects
    robot1 robot2 - robot
    rgripper1 lgripper1 rgripper2 lgripper2 - gripper
    room1 room2 room3 room4 room5 room6 room7 room8 room9 - room
    door1 door2 door3 door4 door5 door6 door7 door8 - door
    ball1 ball2 ball3 ball4 ball5 ball6 ball7 ball8 ball9 ball10 ball11 ball12 ball13 ball14 ball15 ball16 ball17 ball18 ball19 ball20 ball21 ball22 - object
  )
  (:init
    (closed door1)
    (closed door2)
    (closed door3)
    (closed door4)
    (closed door5)
    (closed door6)
    (closed door7)
    (closed door8)
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
    (connected room8 room9 door8)
    (connected room9 room8 door8)
    (at-robby robot1 room3)
    (free robot1 rgripper1)
    (free robot1 lgripper1)
    (at-robby robot2 room4)
    (free robot2 rgripper2)
    (free robot2 lgripper2)
    (at ball1 room4)
    (at ball2 room6)
    (at ball3 room8)
    (at ball4 room1)
    (at ball5 room8)
    (at ball6 room2)
    (at ball7 room2)
    (at ball8 room6)
    (at ball9 room3)
    (at ball10 room2)
    (at ball11 room7)
    (at ball12 room8)
    (at ball13 room3)
    (at ball14 room1)
    (at ball15 room8)
    (at ball16 room7)
    (at ball17 room5)
    (at ball18 room2)
    (at ball19 room1)
    (at ball20 room4)
    (at ball21 room9)
    (at ball22 room1)
  )
  (:goal
    (and
      (at ball1 room5)
      (at ball2 room3)
      (at ball3 room2)
      (at ball4 room9)
      (at ball5 room5)
      (at ball6 room3)
      (at ball7 room5)
      (at ball8 room7)
      (at ball9 room7)
      (at ball10 room9)
      (at ball11 room4)
      (at ball12 room5)
      (at ball13 room9)
      (at ball14 room3)
      (at ball15 room7)
      (at ball16 room1)
      (at ball17 room8)
      (at ball18 room1)
      (at ball19 room3)
      (at ball20 room5)
      (at ball21 room9)
      (at ball22 room6)
    )
  )
  (:metric minimize
    (total-time)
  )

)