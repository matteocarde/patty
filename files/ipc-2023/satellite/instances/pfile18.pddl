(define (problem strips-sat-x-1)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	instrument2 - instrument
	satellite1 - satellite
	instrument3 - instrument
	instrument4 - instrument
	instrument5 - instrument
	instrument6 - instrument
	satellite2 - satellite
	instrument7 - instrument
	instrument8 - instrument
	instrument9 - instrument
	satellite3 - satellite
	instrument10 - instrument
	instrument11 - instrument
	satellite4 - satellite
	instrument12 - instrument
	image1 - mode
	thermograph3 - mode
	thermograph0 - mode
	thermograph2 - mode
	thermograph4 - mode
	groundstation2 - direction
	star4 - direction
	star0 - direction
	star1 - direction
	star3 - direction
	phenomenon5 - direction
	planet6 - direction
	planet7 - direction
	star8 - direction
	star9 - direction
	star10 - direction
	planet11 - direction
	phenomenon12 - direction
	phenomenon13 - direction
	planet14 - direction
	star15 - direction
	phenomenon16 - direction
	phenomenon17 - direction
	phenomenon18 - direction
	planet19 - direction
	planet20 - direction
	phenomenon21 - direction
	star22 - direction
	planet23 - direction
	phenomenon24 - direction
)
(:init
	(supports instrument0 thermograph4)
	(supports instrument0 thermograph0)
	(supports instrument0 thermograph2)
	(calibration_target instrument0 star4)
	(supports instrument1 thermograph3)
	(calibration_target instrument1 star0)
	(supports instrument2 image1)
	(calibration_target instrument2 star4)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument2 satellite0)
	(power_avail satellite0)
	(pointing satellite0 star8)
	(= (data_capacity satellite0) 1000)
	(= (fuel satellite0) 101)
	(supports instrument3 thermograph3)
	(calibration_target instrument3 star1)
	(supports instrument4 image1)
	(calibration_target instrument4 star1)
	(supports instrument5 thermograph3)
	(calibration_target instrument5 star3)
	(supports instrument6 thermograph2)
	(supports instrument6 thermograph0)
	(supports instrument6 image1)
	(calibration_target instrument6 star0)
	(on_board instrument3 satellite1)
	(on_board instrument4 satellite1)
	(on_board instrument5 satellite1)
	(on_board instrument6 satellite1)
	(power_avail satellite1)
	(pointing satellite1 phenomenon21)
	(= (data_capacity satellite1) 1000)
	(= (fuel satellite1) 143)
	(supports instrument7 thermograph0)
	(calibration_target instrument7 star3)
	(supports instrument8 thermograph4)
	(supports instrument8 thermograph3)
	(supports instrument8 thermograph2)
	(calibration_target instrument8 star3)
	(supports instrument9 thermograph2)
	(supports instrument9 thermograph3)
	(calibration_target instrument9 star1)
	(on_board instrument7 satellite2)
	(on_board instrument8 satellite2)
	(on_board instrument9 satellite2)
	(power_avail satellite2)
	(pointing satellite2 star4)
	(= (data_capacity satellite2) 1000)
	(= (fuel satellite2) 113)
	(supports instrument10 thermograph2)
	(calibration_target instrument10 star3)
	(supports instrument11 thermograph2)
	(supports instrument11 thermograph4)
	(supports instrument11 thermograph0)
	(calibration_target instrument11 star1)
	(on_board instrument10 satellite3)
	(on_board instrument11 satellite3)
	(power_avail satellite3)
	(pointing satellite3 phenomenon16)
	(= (data_capacity satellite3) 1000)
	(= (fuel satellite3) 137)
	(supports instrument12 thermograph4)
	(calibration_target instrument12 star3)
	(on_board instrument12 satellite4)
	(power_avail satellite4)
	(pointing satellite4 phenomenon18)
	(= (data_capacity satellite4) 1000)
	(= (fuel satellite4) 114)
	(= (data phenomenon5 image1) 71)
	(= (data planet6 image1) 76)
	(= (data planet7 image1) 138)
	(= (data star8 image1) 38)
	(= (data star9 image1) 191)
	(= (data star10 image1) 175)
	(= (data planet11 image1) 149)
	(= (data phenomenon12 image1) 87)
	(= (data phenomenon13 image1) 19)
	(= (data planet14 image1) 33)
	(= (data star15 image1) 58)
	(= (data phenomenon16 image1) 174)
	(= (data phenomenon17 image1) 8)
	(= (data phenomenon18 image1) 161)
	(= (data planet19 image1) 200)
	(= (data planet20 image1) 12)
	(= (data phenomenon21 image1) 120)
	(= (data star22 image1) 88)
	(= (data planet23 image1) 46)
	(= (data phenomenon24 image1) 143)
	(= (data phenomenon5 thermograph3) 184)
	(= (data planet6 thermograph3) 103)
	(= (data planet7 thermograph3) 118)
	(= (data star8 thermograph3) 112)
	(= (data star9 thermograph3) 105)
	(= (data star10 thermograph3) 1)
	(= (data planet11 thermograph3) 197)
	(= (data phenomenon12 thermograph3) 69)
	(= (data phenomenon13 thermograph3) 73)
	(= (data planet14 thermograph3) 173)
	(= (data star15 thermograph3) 19)
	(= (data phenomenon16 thermograph3) 20)
	(= (data phenomenon17 thermograph3) 156)
	(= (data phenomenon18 thermograph3) 31)
	(= (data planet19 thermograph3) 65)
	(= (data planet20 thermograph3) 129)
	(= (data phenomenon21 thermograph3) 113)
	(= (data star22 thermograph3) 49)
	(= (data planet23 thermograph3) 127)
	(= (data phenomenon24 thermograph3) 19)
	(= (data phenomenon5 thermograph0) 57)
	(= (data planet6 thermograph0) 108)
	(= (data planet7 thermograph0) 71)
	(= (data star8 thermograph0) 46)
	(= (data star9 thermograph0) 15)
	(= (data star10 thermograph0) 11)
	(= (data planet11 thermograph0) 196)
	(= (data phenomenon12 thermograph0) 170)
	(= (data phenomenon13 thermograph0) 138)
	(= (data planet14 thermograph0) 116)
	(= (data star15 thermograph0) 73)
	(= (data phenomenon16 thermograph0) 95)
	(= (data phenomenon17 thermograph0) 132)
	(= (data phenomenon18 thermograph0) 144)
	(= (data planet19 thermograph0) 132)
	(= (data planet20 thermograph0) 200)
	(= (data phenomenon21 thermograph0) 136)
	(= (data star22 thermograph0) 100)
	(= (data planet23 thermograph0) 146)
	(= (data phenomenon24 thermograph0) 49)
	(= (data phenomenon5 thermograph2) 162)
	(= (data planet6 thermograph2) 153)
	(= (data planet7 thermograph2) 192)
	(= (data star8 thermograph2) 56)
	(= (data star9 thermograph2) 11)
	(= (data star10 thermograph2) 15)
	(= (data planet11 thermograph2) 181)
	(= (data phenomenon12 thermograph2) 1)
	(= (data phenomenon13 thermograph2) 23)
	(= (data planet14 thermograph2) 55)
	(= (data star15 thermograph2) 67)
	(= (data phenomenon16 thermograph2) 19)
	(= (data phenomenon17 thermograph2) 52)
	(= (data phenomenon18 thermograph2) 136)
	(= (data planet19 thermograph2) 188)
	(= (data planet20 thermograph2) 15)
	(= (data phenomenon21 thermograph2) 12)
	(= (data star22 thermograph2) 59)
	(= (data planet23 thermograph2) 53)
	(= (data phenomenon24 thermograph2) 123)
	(= (data phenomenon5 thermograph4) 14)
	(= (data planet6 thermograph4) 134)
	(= (data planet7 thermograph4) 132)
	(= (data star8 thermograph4) 84)
	(= (data star9 thermograph4) 36)
	(= (data star10 thermograph4) 185)
	(= (data planet11 thermograph4) 134)
	(= (data phenomenon12 thermograph4) 120)
	(= (data phenomenon13 thermograph4) 116)
	(= (data planet14 thermograph4) 99)
	(= (data star15 thermograph4) 86)
	(= (data phenomenon16 thermograph4) 77)
	(= (data phenomenon17 thermograph4) 126)
	(= (data phenomenon18 thermograph4) 7)
	(= (data planet19 thermograph4) 175)
	(= (data planet20 thermograph4) 120)
	(= (data phenomenon21 thermograph4) 113)
	(= (data star22 thermograph4) 183)
	(= (data planet23 thermograph4) 108)
	(= (data phenomenon24 thermograph4) 193)
	(= (slew_time groundstation2 star0) 7.657)
	(= (slew_time star0 groundstation2) 7.657)
	(= (slew_time groundstation2 star1) 26.41)
	(= (slew_time star1 groundstation2) 26.41)
	(= (slew_time star4 star0) 10.57)
	(= (slew_time star0 star4) 10.57)
	(= (slew_time star4 star1) 64.75)
	(= (slew_time star1 star4) 64.75)
	(= (slew_time star4 groundstation2) 27.12)
	(= (slew_time groundstation2 star4) 27.12)
	(= (slew_time star4 star3) 89.01)
	(= (slew_time star3 star4) 89.01)
	(= (slew_time star1 star0) 43.3)
	(= (slew_time star0 star1) 43.3)
	(= (slew_time star3 star0) 3.603)
	(= (slew_time star0 star3) 3.603)
	(= (slew_time star3 star1) 8.159)
	(= (slew_time star1 star3) 8.159)
	(= (slew_time star3 groundstation2) 46.54)
	(= (slew_time groundstation2 star3) 46.54)
	(= (slew_time phenomenon5 star0) 32.62)
	(= (slew_time star0 phenomenon5) 32.62)
	(= (slew_time phenomenon5 star1) 31.66)
	(= (slew_time star1 phenomenon5) 31.66)
	(= (slew_time phenomenon5 groundstation2) 11.33)
	(= (slew_time groundstation2 phenomenon5) 11.33)
	(= (slew_time phenomenon5 star3) 47.92)
	(= (slew_time star3 phenomenon5) 47.92)
	(= (slew_time phenomenon5 star4) 47.88)
	(= (slew_time star4 phenomenon5) 47.88)
	(= (slew_time planet6 star0) 42.33)
	(= (slew_time star0 planet6) 42.33)
	(= (slew_time planet6 star1) 10.62)
	(= (slew_time star1 planet6) 10.62)
	(= (slew_time planet6 groundstation2) 22.7)
	(= (slew_time groundstation2 planet6) 22.7)
	(= (slew_time planet6 star3) 28.47)
	(= (slew_time star3 planet6) 28.47)
	(= (slew_time planet6 star4) 43.77)
	(= (slew_time star4 planet6) 43.77)
	(= (slew_time planet6 phenomenon5) 17.52)
	(= (slew_time phenomenon5 planet6) 17.52)
	(= (slew_time planet7 star0) 49.23)
	(= (slew_time star0 planet7) 49.23)
	(= (slew_time planet7 star1) 49.42)
	(= (slew_time star1 planet7) 49.42)
	(= (slew_time planet7 groundstation2) 20.99)
	(= (slew_time groundstation2 planet7) 20.99)
	(= (slew_time planet7 star3) 45.42)
	(= (slew_time star3 planet7) 45.42)
	(= (slew_time planet7 star4) 28.59)
	(= (slew_time star4 planet7) 28.59)
	(= (slew_time planet7 phenomenon5) 52.19)
	(= (slew_time phenomenon5 planet7) 52.19)
	(= (slew_time planet7 planet6) 44)
	(= (slew_time planet6 planet7) 44)
	(= (slew_time star8 star0) 41.91)
	(= (slew_time star0 star8) 41.91)
	(= (slew_time star8 star1) 52.55)
	(= (slew_time star1 star8) 52.55)
	(= (slew_time star8 groundstation2) 13.05)
	(= (slew_time groundstation2 star8) 13.05)
	(= (slew_time star8 star3) 42.85)
	(= (slew_time star3 star8) 42.85)
	(= (slew_time star8 star4) 73.44)
	(= (slew_time star4 star8) 73.44)
	(= (slew_time star8 phenomenon5) 77.25)
	(= (slew_time phenomenon5 star8) 77.25)
	(= (slew_time star8 planet6) 24)
	(= (slew_time planet6 star8) 24)
	(= (slew_time star8 planet7) 18.76)
	(= (slew_time planet7 star8) 18.76)
	(= (slew_time star9 star0) 73.72)
	(= (slew_time star0 star9) 73.72)
	(= (slew_time star9 star1) 2.29)
	(= (slew_time star1 star9) 2.29)
	(= (slew_time star9 groundstation2) 26.5)
	(= (slew_time groundstation2 star9) 26.5)
	(= (slew_time star9 star3) 4.975)
	(= (slew_time star3 star9) 4.975)
	(= (slew_time star9 star4) 30.13)
	(= (slew_time star4 star9) 30.13)
	(= (slew_time star9 phenomenon5) 38.11)
	(= (slew_time phenomenon5 star9) 38.11)
	(= (slew_time star9 planet6) 6.19)
	(= (slew_time planet6 star9) 6.19)
	(= (slew_time star9 planet7) 34.01)
	(= (slew_time planet7 star9) 34.01)
	(= (slew_time star9 star8) 57.98)
	(= (slew_time star8 star9) 57.98)
	(= (slew_time star10 star0) 55.77)
	(= (slew_time star0 star10) 55.77)
	(= (slew_time star10 star1) 7.609)
	(= (slew_time star1 star10) 7.609)
	(= (slew_time star10 groundstation2) 32.79)
	(= (slew_time groundstation2 star10) 32.79)
	(= (slew_time star10 star3) 66.63)
	(= (slew_time star3 star10) 66.63)
	(= (slew_time star10 star4) 38.53)
	(= (slew_time star4 star10) 38.53)
	(= (slew_time star10 phenomenon5) 0.8326)
	(= (slew_time phenomenon5 star10) 0.8326)
	(= (slew_time star10 planet6) 25.68)
	(= (slew_time planet6 star10) 25.68)
	(= (slew_time star10 planet7) 24.64)
	(= (slew_time planet7 star10) 24.64)
	(= (slew_time star10 star8) 70.36)
	(= (slew_time star8 star10) 70.36)
	(= (slew_time star10 star9) 84.22)
	(= (slew_time star9 star10) 84.22)
	(= (slew_time planet11 star0) 41.35)
	(= (slew_time star0 planet11) 41.35)
	(= (slew_time planet11 star1) 22.86)
	(= (slew_time star1 planet11) 22.86)
	(= (slew_time planet11 groundstation2) 9.333)
	(= (slew_time groundstation2 planet11) 9.333)
	(= (slew_time planet11 star3) 19.34)
	(= (slew_time star3 planet11) 19.34)
	(= (slew_time planet11 star4) 12.69)
	(= (slew_time star4 planet11) 12.69)
	(= (slew_time planet11 phenomenon5) 58.77)
	(= (slew_time phenomenon5 planet11) 58.77)
	(= (slew_time planet11 planet6) 22.65)
	(= (slew_time planet6 planet11) 22.65)
	(= (slew_time planet11 planet7) 68.79)
	(= (slew_time planet7 planet11) 68.79)
	(= (slew_time planet11 star8) 30.06)
	(= (slew_time star8 planet11) 30.06)
	(= (slew_time planet11 star9) 11.89)
	(= (slew_time star9 planet11) 11.89)
	(= (slew_time planet11 star10) 71.24)
	(= (slew_time star10 planet11) 71.24)
	(= (slew_time phenomenon12 star0) 33.33)
	(= (slew_time star0 phenomenon12) 33.33)
	(= (slew_time phenomenon12 star1) 5.894)
	(= (slew_time star1 phenomenon12) 5.894)
	(= (slew_time phenomenon12 groundstation2) 57.27)
	(= (slew_time groundstation2 phenomenon12) 57.27)
	(= (slew_time phenomenon12 star3) 38.14)
	(= (slew_time star3 phenomenon12) 38.14)
	(= (slew_time phenomenon12 star4) 47.15)
	(= (slew_time star4 phenomenon12) 47.15)
	(= (slew_time phenomenon12 phenomenon5) 1.191)
	(= (slew_time phenomenon5 phenomenon12) 1.191)
	(= (slew_time phenomenon12 planet6) 15.73)
	(= (slew_time planet6 phenomenon12) 15.73)
	(= (slew_time phenomenon12 planet7) 40.94)
	(= (slew_time planet7 phenomenon12) 40.94)
	(= (slew_time phenomenon12 star8) 14.04)
	(= (slew_time star8 phenomenon12) 14.04)
	(= (slew_time phenomenon12 star9) 69.14)
	(= (slew_time star9 phenomenon12) 69.14)
	(= (slew_time phenomenon12 star10) 17.32)
	(= (slew_time star10 phenomenon12) 17.32)
	(= (slew_time phenomenon12 planet11) 35.82)
	(= (slew_time planet11 phenomenon12) 35.82)
	(= (slew_time phenomenon13 star0) 59.94)
	(= (slew_time star0 phenomenon13) 59.94)
	(= (slew_time phenomenon13 star1) 19.25)
	(= (slew_time star1 phenomenon13) 19.25)
	(= (slew_time phenomenon13 groundstation2) 17.7)
	(= (slew_time groundstation2 phenomenon13) 17.7)
	(= (slew_time phenomenon13 star3) 52.95)
	(= (slew_time star3 phenomenon13) 52.95)
	(= (slew_time phenomenon13 star4) 58.1)
	(= (slew_time star4 phenomenon13) 58.1)
	(= (slew_time phenomenon13 phenomenon5) 28.2)
	(= (slew_time phenomenon5 phenomenon13) 28.2)
	(= (slew_time phenomenon13 planet6) 3.63)
	(= (slew_time planet6 phenomenon13) 3.63)
	(= (slew_time phenomenon13 planet7) 16.25)
	(= (slew_time planet7 phenomenon13) 16.25)
	(= (slew_time phenomenon13 star8) 1.805)
	(= (slew_time star8 phenomenon13) 1.805)
	(= (slew_time phenomenon13 star9) 40.24)
	(= (slew_time star9 phenomenon13) 40.24)
	(= (slew_time phenomenon13 star10) 53.82)
	(= (slew_time star10 phenomenon13) 53.82)
	(= (slew_time phenomenon13 planet11) 23.62)
	(= (slew_time planet11 phenomenon13) 23.62)
	(= (slew_time phenomenon13 phenomenon12) 39.59)
	(= (slew_time phenomenon12 phenomenon13) 39.59)
	(= (slew_time planet14 star0) 7.335)
	(= (slew_time star0 planet14) 7.335)
	(= (slew_time planet14 star1) 48.7)
	(= (slew_time star1 planet14) 48.7)
	(= (slew_time planet14 groundstation2) 4.126)
	(= (slew_time groundstation2 planet14) 4.126)
	(= (slew_time planet14 star3) 79.46)
	(= (slew_time star3 planet14) 79.46)
	(= (slew_time planet14 star4) 82.38)
	(= (slew_time star4 planet14) 82.38)
	(= (slew_time planet14 phenomenon5) 14.33)
	(= (slew_time phenomenon5 planet14) 14.33)
	(= (slew_time planet14 planet6) 52.21)
	(= (slew_time planet6 planet14) 52.21)
	(= (slew_time planet14 planet7) 15.41)
	(= (slew_time planet7 planet14) 15.41)
	(= (slew_time planet14 star8) 57.79)
	(= (slew_time star8 planet14) 57.79)
	(= (slew_time planet14 star9) 30.2)
	(= (slew_time star9 planet14) 30.2)
	(= (slew_time planet14 star10) 16.88)
	(= (slew_time star10 planet14) 16.88)
	(= (slew_time planet14 planet11) 5.436)
	(= (slew_time planet11 planet14) 5.436)
	(= (slew_time planet14 phenomenon12) 59.01)
	(= (slew_time phenomenon12 planet14) 59.01)
	(= (slew_time planet14 phenomenon13) 25.08)
	(= (slew_time phenomenon13 planet14) 25.08)
	(= (slew_time star15 star0) 38.53)
	(= (slew_time star0 star15) 38.53)
	(= (slew_time star15 star1) 20.49)
	(= (slew_time star1 star15) 20.49)
	(= (slew_time star15 groundstation2) 50.38)
	(= (slew_time groundstation2 star15) 50.38)
	(= (slew_time star15 star3) 58.85)
	(= (slew_time star3 star15) 58.85)
	(= (slew_time star15 star4) 11.07)
	(= (slew_time star4 star15) 11.07)
	(= (slew_time star15 phenomenon5) 11.39)
	(= (slew_time phenomenon5 star15) 11.39)
	(= (slew_time star15 planet6) 4.376)
	(= (slew_time planet6 star15) 4.376)
	(= (slew_time star15 planet7) 37.73)
	(= (slew_time planet7 star15) 37.73)
	(= (slew_time star15 star8) 22.22)
	(= (slew_time star8 star15) 22.22)
	(= (slew_time star15 star9) 60.71)
	(= (slew_time star9 star15) 60.71)
	(= (slew_time star15 star10) 28.64)
	(= (slew_time star10 star15) 28.64)
	(= (slew_time star15 planet11) 1.87)
	(= (slew_time planet11 star15) 1.87)
	(= (slew_time star15 phenomenon12) 16.11)
	(= (slew_time phenomenon12 star15) 16.11)
	(= (slew_time star15 phenomenon13) 26.45)
	(= (slew_time phenomenon13 star15) 26.45)
	(= (slew_time star15 planet14) 35)
	(= (slew_time planet14 star15) 35)
	(= (slew_time phenomenon16 star0) 35.09)
	(= (slew_time star0 phenomenon16) 35.09)
	(= (slew_time phenomenon16 star1) 39.33)
	(= (slew_time star1 phenomenon16) 39.33)
	(= (slew_time phenomenon16 groundstation2) 27.44)
	(= (slew_time groundstation2 phenomenon16) 27.44)
	(= (slew_time phenomenon16 star3) 72.58)
	(= (slew_time star3 phenomenon16) 72.58)
	(= (slew_time phenomenon16 star4) 10.8)
	(= (slew_time star4 phenomenon16) 10.8)
	(= (slew_time phenomenon16 phenomenon5) 34.97)
	(= (slew_time phenomenon5 phenomenon16) 34.97)
	(= (slew_time phenomenon16 planet6) 40.37)
	(= (slew_time planet6 phenomenon16) 40.37)
	(= (slew_time phenomenon16 planet7) 15.01)
	(= (slew_time planet7 phenomenon16) 15.01)
	(= (slew_time phenomenon16 star8) 40.33)
	(= (slew_time star8 phenomenon16) 40.33)
	(= (slew_time phenomenon16 star9) 34.62)
	(= (slew_time star9 phenomenon16) 34.62)
	(= (slew_time phenomenon16 star10) 55.93)
	(= (slew_time star10 phenomenon16) 55.93)
	(= (slew_time phenomenon16 planet11) 27.47)
	(= (slew_time planet11 phenomenon16) 27.47)
	(= (slew_time phenomenon16 phenomenon12) 77.79)
	(= (slew_time phenomenon12 phenomenon16) 77.79)
	(= (slew_time phenomenon16 phenomenon13) 48.07)
	(= (slew_time phenomenon13 phenomenon16) 48.07)
	(= (slew_time phenomenon16 planet14) 75.09)
	(= (slew_time planet14 phenomenon16) 75.09)
	(= (slew_time phenomenon16 star15) 67.18)
	(= (slew_time star15 phenomenon16) 67.18)
	(= (slew_time phenomenon17 star0) 35.54)
	(= (slew_time star0 phenomenon17) 35.54)
	(= (slew_time phenomenon17 star1) 67.74)
	(= (slew_time star1 phenomenon17) 67.74)
	(= (slew_time phenomenon17 groundstation2) 0.1914)
	(= (slew_time groundstation2 phenomenon17) 0.1914)
	(= (slew_time phenomenon17 star3) 32.32)
	(= (slew_time star3 phenomenon17) 32.32)
	(= (slew_time phenomenon17 star4) 24.95)
	(= (slew_time star4 phenomenon17) 24.95)
	(= (slew_time phenomenon17 phenomenon5) 47.05)
	(= (slew_time phenomenon5 phenomenon17) 47.05)
	(= (slew_time phenomenon17 planet6) 4.874)
	(= (slew_time planet6 phenomenon17) 4.874)
	(= (slew_time phenomenon17 planet7) 23.31)
	(= (slew_time planet7 phenomenon17) 23.31)
	(= (slew_time phenomenon17 star8) 58.44)
	(= (slew_time star8 phenomenon17) 58.44)
	(= (slew_time phenomenon17 star9) 30.68)
	(= (slew_time star9 phenomenon17) 30.68)
	(= (slew_time phenomenon17 star10) 8.398)
	(= (slew_time star10 phenomenon17) 8.398)
	(= (slew_time phenomenon17 planet11) 2.273)
	(= (slew_time planet11 phenomenon17) 2.273)
	(= (slew_time phenomenon17 phenomenon12) 59.62)
	(= (slew_time phenomenon12 phenomenon17) 59.62)
	(= (slew_time phenomenon17 phenomenon13) 2.875)
	(= (slew_time phenomenon13 phenomenon17) 2.875)
	(= (slew_time phenomenon17 planet14) 75.41)
	(= (slew_time planet14 phenomenon17) 75.41)
	(= (slew_time phenomenon17 star15) 25.62)
	(= (slew_time star15 phenomenon17) 25.62)
	(= (slew_time phenomenon17 phenomenon16) 53.59)
	(= (slew_time phenomenon16 phenomenon17) 53.59)
	(= (slew_time phenomenon18 star0) 52.79)
	(= (slew_time star0 phenomenon18) 52.79)
	(= (slew_time phenomenon18 star1) 2.299)
	(= (slew_time star1 phenomenon18) 2.299)
	(= (slew_time phenomenon18 groundstation2) 50.27)
	(= (slew_time groundstation2 phenomenon18) 50.27)
	(= (slew_time phenomenon18 star3) 10.77)
	(= (slew_time star3 phenomenon18) 10.77)
	(= (slew_time phenomenon18 star4) 51.91)
	(= (slew_time star4 phenomenon18) 51.91)
	(= (slew_time phenomenon18 phenomenon5) 8.553)
	(= (slew_time phenomenon5 phenomenon18) 8.553)
	(= (slew_time phenomenon18 planet6) 20.3)
	(= (slew_time planet6 phenomenon18) 20.3)
	(= (slew_time phenomenon18 planet7) 14.71)
	(= (slew_time planet7 phenomenon18) 14.71)
	(= (slew_time phenomenon18 star8) 40.07)
	(= (slew_time star8 phenomenon18) 40.07)
	(= (slew_time phenomenon18 star9) 36.56)
	(= (slew_time star9 phenomenon18) 36.56)
	(= (slew_time phenomenon18 star10) 7.676)
	(= (slew_time star10 phenomenon18) 7.676)
	(= (slew_time phenomenon18 planet11) 47.7)
	(= (slew_time planet11 phenomenon18) 47.7)
	(= (slew_time phenomenon18 phenomenon12) 9.734)
	(= (slew_time phenomenon12 phenomenon18) 9.734)
	(= (slew_time phenomenon18 phenomenon13) 23.36)
	(= (slew_time phenomenon13 phenomenon18) 23.36)
	(= (slew_time phenomenon18 planet14) 11.19)
	(= (slew_time planet14 phenomenon18) 11.19)
	(= (slew_time phenomenon18 star15) 33.39)
	(= (slew_time star15 phenomenon18) 33.39)
	(= (slew_time phenomenon18 phenomenon16) 52.7)
	(= (slew_time phenomenon16 phenomenon18) 52.7)
	(= (slew_time phenomenon18 phenomenon17) 22.55)
	(= (slew_time phenomenon17 phenomenon18) 22.55)
	(= (slew_time planet19 star0) 62.22)
	(= (slew_time star0 planet19) 62.22)
	(= (slew_time planet19 star1) 43.13)
	(= (slew_time star1 planet19) 43.13)
	(= (slew_time planet19 groundstation2) 13.25)
	(= (slew_time groundstation2 planet19) 13.25)
	(= (slew_time planet19 star3) 0.4584)
	(= (slew_time star3 planet19) 0.4584)
	(= (slew_time planet19 star4) 4.367)
	(= (slew_time star4 planet19) 4.367)
	(= (slew_time planet19 phenomenon5) 20.22)
	(= (slew_time phenomenon5 planet19) 20.22)
	(= (slew_time planet19 planet6) 16.02)
	(= (slew_time planet6 planet19) 16.02)
	(= (slew_time planet19 planet7) 21.17)
	(= (slew_time planet7 planet19) 21.17)
	(= (slew_time planet19 star8) 34.01)
	(= (slew_time star8 planet19) 34.01)
	(= (slew_time planet19 star9) 69.87)
	(= (slew_time star9 planet19) 69.87)
	(= (slew_time planet19 star10) 34.63)
	(= (slew_time star10 planet19) 34.63)
	(= (slew_time planet19 planet11) 15.33)
	(= (slew_time planet11 planet19) 15.33)
	(= (slew_time planet19 phenomenon12) 71.31)
	(= (slew_time phenomenon12 planet19) 71.31)
	(= (slew_time planet19 phenomenon13) 31.15)
	(= (slew_time phenomenon13 planet19) 31.15)
	(= (slew_time planet19 planet14) 32.15)
	(= (slew_time planet14 planet19) 32.15)
	(= (slew_time planet19 star15) 19.35)
	(= (slew_time star15 planet19) 19.35)
	(= (slew_time planet19 phenomenon16) 69.35)
	(= (slew_time phenomenon16 planet19) 69.35)
	(= (slew_time planet19 phenomenon17) 38.2)
	(= (slew_time phenomenon17 planet19) 38.2)
	(= (slew_time planet19 phenomenon18) 5.816)
	(= (slew_time phenomenon18 planet19) 5.816)
	(= (slew_time planet20 star0) 4.861)
	(= (slew_time star0 planet20) 4.861)
	(= (slew_time planet20 star1) 1.61)
	(= (slew_time star1 planet20) 1.61)
	(= (slew_time planet20 groundstation2) 53.21)
	(= (slew_time groundstation2 planet20) 53.21)
	(= (slew_time planet20 star3) 13.38)
	(= (slew_time star3 planet20) 13.38)
	(= (slew_time planet20 star4) 62.85)
	(= (slew_time star4 planet20) 62.85)
	(= (slew_time planet20 phenomenon5) 0.7936)
	(= (slew_time phenomenon5 planet20) 0.7936)
	(= (slew_time planet20 planet6) 25.19)
	(= (slew_time planet6 planet20) 25.19)
	(= (slew_time planet20 planet7) 1.508)
	(= (slew_time planet7 planet20) 1.508)
	(= (slew_time planet20 star8) 10.7)
	(= (slew_time star8 planet20) 10.7)
	(= (slew_time planet20 star9) 43.07)
	(= (slew_time star9 planet20) 43.07)
	(= (slew_time planet20 star10) 66.79)
	(= (slew_time star10 planet20) 66.79)
	(= (slew_time planet20 planet11) 31.45)
	(= (slew_time planet11 planet20) 31.45)
	(= (slew_time planet20 phenomenon12) 40.24)
	(= (slew_time phenomenon12 planet20) 40.24)
	(= (slew_time planet20 phenomenon13) 2.054)
	(= (slew_time phenomenon13 planet20) 2.054)
	(= (slew_time planet20 planet14) 76.59)
	(= (slew_time planet14 planet20) 76.59)
	(= (slew_time planet20 star15) 25.3)
	(= (slew_time star15 planet20) 25.3)
	(= (slew_time planet20 phenomenon16) 30.81)
	(= (slew_time phenomenon16 planet20) 30.81)
	(= (slew_time planet20 phenomenon17) 16.6)
	(= (slew_time phenomenon17 planet20) 16.6)
	(= (slew_time planet20 phenomenon18) 38.93)
	(= (slew_time phenomenon18 planet20) 38.93)
	(= (slew_time planet20 planet19) 14.39)
	(= (slew_time planet19 planet20) 14.39)
	(= (slew_time phenomenon21 star0) 0.2815)
	(= (slew_time star0 phenomenon21) 0.2815)
	(= (slew_time phenomenon21 star1) 29.33)
	(= (slew_time star1 phenomenon21) 29.33)
	(= (slew_time phenomenon21 groundstation2) 27.51)
	(= (slew_time groundstation2 phenomenon21) 27.51)
	(= (slew_time phenomenon21 star3) 41.2)
	(= (slew_time star3 phenomenon21) 41.2)
	(= (slew_time phenomenon21 star4) 0.3751)
	(= (slew_time star4 phenomenon21) 0.3751)
	(= (slew_time phenomenon21 phenomenon5) 13.21)
	(= (slew_time phenomenon5 phenomenon21) 13.21)
	(= (slew_time phenomenon21 planet6) 20.32)
	(= (slew_time planet6 phenomenon21) 20.32)
	(= (slew_time phenomenon21 planet7) 25.84)
	(= (slew_time planet7 phenomenon21) 25.84)
	(= (slew_time phenomenon21 star8) 48.37)
	(= (slew_time star8 phenomenon21) 48.37)
	(= (slew_time phenomenon21 star9) 8.296)
	(= (slew_time star9 phenomenon21) 8.296)
	(= (slew_time phenomenon21 star10) 27.43)
	(= (slew_time star10 phenomenon21) 27.43)
	(= (slew_time phenomenon21 planet11) 1.378)
	(= (slew_time planet11 phenomenon21) 1.378)
	(= (slew_time phenomenon21 phenomenon12) 64.72)
	(= (slew_time phenomenon12 phenomenon21) 64.72)
	(= (slew_time phenomenon21 phenomenon13) 20.19)
	(= (slew_time phenomenon13 phenomenon21) 20.19)
	(= (slew_time phenomenon21 planet14) 7.053)
	(= (slew_time planet14 phenomenon21) 7.053)
	(= (slew_time phenomenon21 star15) 0.6336)
	(= (slew_time star15 phenomenon21) 0.6336)
	(= (slew_time phenomenon21 phenomenon16) 43.11)
	(= (slew_time phenomenon16 phenomenon21) 43.11)
	(= (slew_time phenomenon21 phenomenon17) 11.79)
	(= (slew_time phenomenon17 phenomenon21) 11.79)
	(= (slew_time phenomenon21 phenomenon18) 26.26)
	(= (slew_time phenomenon18 phenomenon21) 26.26)
	(= (slew_time phenomenon21 planet19) 39.59)
	(= (slew_time planet19 phenomenon21) 39.59)
	(= (slew_time phenomenon21 planet20) 75.57)
	(= (slew_time planet20 phenomenon21) 75.57)
	(= (slew_time star22 star0) 22.37)
	(= (slew_time star0 star22) 22.37)
	(= (slew_time star22 star1) 33.48)
	(= (slew_time star1 star22) 33.48)
	(= (slew_time star22 groundstation2) 32.23)
	(= (slew_time groundstation2 star22) 32.23)
	(= (slew_time star22 star3) 11.65)
	(= (slew_time star3 star22) 11.65)
	(= (slew_time star22 star4) 76.02)
	(= (slew_time star4 star22) 76.02)
	(= (slew_time star22 phenomenon5) 3.974)
	(= (slew_time phenomenon5 star22) 3.974)
	(= (slew_time star22 planet6) 15.62)
	(= (slew_time planet6 star22) 15.62)
	(= (slew_time star22 planet7) 81.03)
	(= (slew_time planet7 star22) 81.03)
	(= (slew_time star22 star8) 58.93)
	(= (slew_time star8 star22) 58.93)
	(= (slew_time star22 star9) 53.34)
	(= (slew_time star9 star22) 53.34)
	(= (slew_time star22 star10) 27.18)
	(= (slew_time star10 star22) 27.18)
	(= (slew_time star22 planet11) 67.37)
	(= (slew_time planet11 star22) 67.37)
	(= (slew_time star22 phenomenon12) 74.34)
	(= (slew_time phenomenon12 star22) 74.34)
	(= (slew_time star22 phenomenon13) 9.547)
	(= (slew_time phenomenon13 star22) 9.547)
	(= (slew_time star22 planet14) 74.05)
	(= (slew_time planet14 star22) 74.05)
	(= (slew_time star22 star15) 11.51)
	(= (slew_time star15 star22) 11.51)
	(= (slew_time star22 phenomenon16) 42.31)
	(= (slew_time phenomenon16 star22) 42.31)
	(= (slew_time star22 phenomenon17) 4.957)
	(= (slew_time phenomenon17 star22) 4.957)
	(= (slew_time star22 phenomenon18) 71.94)
	(= (slew_time phenomenon18 star22) 71.94)
	(= (slew_time star22 planet19) 14.7)
	(= (slew_time planet19 star22) 14.7)
	(= (slew_time star22 planet20) 34.19)
	(= (slew_time planet20 star22) 34.19)
	(= (slew_time star22 phenomenon21) 26.67)
	(= (slew_time phenomenon21 star22) 26.67)
	(= (slew_time planet23 star0) 37.55)
	(= (slew_time star0 planet23) 37.55)
	(= (slew_time planet23 star1) 39.71)
	(= (slew_time star1 planet23) 39.71)
	(= (slew_time planet23 groundstation2) 6.052)
	(= (slew_time groundstation2 planet23) 6.052)
	(= (slew_time planet23 star3) 64.16)
	(= (slew_time star3 planet23) 64.16)
	(= (slew_time planet23 star4) 48.79)
	(= (slew_time star4 planet23) 48.79)
	(= (slew_time planet23 phenomenon5) 46.08)
	(= (slew_time phenomenon5 planet23) 46.08)
	(= (slew_time planet23 planet6) 37.22)
	(= (slew_time planet6 planet23) 37.22)
	(= (slew_time planet23 planet7) 24.26)
	(= (slew_time planet7 planet23) 24.26)
	(= (slew_time planet23 star8) 29.13)
	(= (slew_time star8 planet23) 29.13)
	(= (slew_time planet23 star9) 3.663)
	(= (slew_time star9 planet23) 3.663)
	(= (slew_time planet23 star10) 1.679)
	(= (slew_time star10 planet23) 1.679)
	(= (slew_time planet23 planet11) 59.12)
	(= (slew_time planet11 planet23) 59.12)
	(= (slew_time planet23 phenomenon12) 45.45)
	(= (slew_time phenomenon12 planet23) 45.45)
	(= (slew_time planet23 phenomenon13) 62.03)
	(= (slew_time phenomenon13 planet23) 62.03)
	(= (slew_time planet23 planet14) 53.77)
	(= (slew_time planet14 planet23) 53.77)
	(= (slew_time planet23 star15) 5.582)
	(= (slew_time star15 planet23) 5.582)
	(= (slew_time planet23 phenomenon16) 10.8)
	(= (slew_time phenomenon16 planet23) 10.8)
	(= (slew_time planet23 phenomenon17) 53.11)
	(= (slew_time phenomenon17 planet23) 53.11)
	(= (slew_time planet23 phenomenon18) 5.595)
	(= (slew_time phenomenon18 planet23) 5.595)
	(= (slew_time planet23 planet19) 86.92)
	(= (slew_time planet19 planet23) 86.92)
	(= (slew_time planet23 planet20) 21.21)
	(= (slew_time planet20 planet23) 21.21)
	(= (slew_time planet23 phenomenon21) 41.82)
	(= (slew_time phenomenon21 planet23) 41.82)
	(= (slew_time planet23 star22) 10.82)
	(= (slew_time star22 planet23) 10.82)
	(= (slew_time phenomenon24 star0) 91.49)
	(= (slew_time star0 phenomenon24) 91.49)
	(= (slew_time phenomenon24 star1) 14.18)
	(= (slew_time star1 phenomenon24) 14.18)
	(= (slew_time phenomenon24 groundstation2) 12.16)
	(= (slew_time groundstation2 phenomenon24) 12.16)
	(= (slew_time phenomenon24 star3) 37.27)
	(= (slew_time star3 phenomenon24) 37.27)
	(= (slew_time phenomenon24 star4) 20.18)
	(= (slew_time star4 phenomenon24) 20.18)
	(= (slew_time phenomenon24 phenomenon5) 43.42)
	(= (slew_time phenomenon5 phenomenon24) 43.42)
	(= (slew_time phenomenon24 planet6) 11.84)
	(= (slew_time planet6 phenomenon24) 11.84)
	(= (slew_time phenomenon24 planet7) 50.11)
	(= (slew_time planet7 phenomenon24) 50.11)
	(= (slew_time phenomenon24 star8) 66.74)
	(= (slew_time star8 phenomenon24) 66.74)
	(= (slew_time phenomenon24 star9) 0.7288)
	(= (slew_time star9 phenomenon24) 0.7288)
	(= (slew_time phenomenon24 star10) 27.93)
	(= (slew_time star10 phenomenon24) 27.93)
	(= (slew_time phenomenon24 planet11) 14.11)
	(= (slew_time planet11 phenomenon24) 14.11)
	(= (slew_time phenomenon24 phenomenon12) 59.78)
	(= (slew_time phenomenon12 phenomenon24) 59.78)
	(= (slew_time phenomenon24 phenomenon13) 18.3)
	(= (slew_time phenomenon13 phenomenon24) 18.3)
	(= (slew_time phenomenon24 planet14) 37.54)
	(= (slew_time planet14 phenomenon24) 37.54)
	(= (slew_time phenomenon24 star15) 8.038)
	(= (slew_time star15 phenomenon24) 8.038)
	(= (slew_time phenomenon24 phenomenon16) 13.76)
	(= (slew_time phenomenon16 phenomenon24) 13.76)
	(= (slew_time phenomenon24 phenomenon17) 39.28)
	(= (slew_time phenomenon17 phenomenon24) 39.28)
	(= (slew_time phenomenon24 phenomenon18) 31.6)
	(= (slew_time phenomenon18 phenomenon24) 31.6)
	(= (slew_time phenomenon24 planet19) 1.879)
	(= (slew_time planet19 phenomenon24) 1.879)
	(= (slew_time phenomenon24 planet20) 19.44)
	(= (slew_time planet20 phenomenon24) 19.44)
	(= (slew_time phenomenon24 phenomenon21) 11.19)
	(= (slew_time phenomenon21 phenomenon24) 11.19)
	(= (slew_time phenomenon24 star22) 3.994)
	(= (slew_time star22 phenomenon24) 3.994)
	(= (slew_time phenomenon24 planet23) 11.27)
	(= (slew_time planet23 phenomenon24) 11.27)
	(= (data-stored) 0)
	(= (fuel-used) 0)
)
(:goal (and
	(have_image phenomenon5 thermograph4)
	(have_image planet7 image1)
	(have_image star8 thermograph3)
	(have_image star9 image1)
	(have_image star10 image1)
	(have_image phenomenon13 thermograph2)
	(have_image star15 thermograph2)
	(have_image phenomenon17 thermograph4)
	(have_image phenomenon18 image1)
	(have_image planet19 thermograph2)
	(have_image planet20 thermograph4)
	(have_image phenomenon21 image1)
	(have_image star22 thermograph3)
))
(:metric minimize (fuel-used))

)
