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
	instrument7 - instrument
	satellite2 - satellite
	instrument8 - instrument
	instrument9 - instrument
	instrument10 - instrument
	instrument11 - instrument
	instrument12 - instrument
	instrument13 - instrument
	satellite3 - satellite
	instrument14 - instrument
	instrument15 - instrument
	instrument16 - instrument
	instrument17 - instrument
	instrument18 - instrument
	instrument19 - instrument
	instrument20 - instrument
	instrument21 - instrument
	satellite4 - satellite
	instrument22 - instrument
	instrument23 - instrument
	instrument24 - instrument
	image4 - mode
	spectrograph6 - mode
	infrared2 - mode
	image5 - mode
	thermograph1 - mode
	infrared7 - mode
	spectrograph0 - mode
	infrared3 - mode
	star1 - direction
	groundstation4 - direction
	star2 - direction
	star3 - direction
	groundstation0 - direction
	phenomenon5 - direction
	star6 - direction
	phenomenon7 - direction
	phenomenon8 - direction
	planet9 - direction
	star10 - direction
	phenomenon11 - direction
	star12 - direction
	phenomenon13 - direction
	star14 - direction
	planet15 - direction
	star16 - direction
	planet17 - direction
	star18 - direction
	star19 - direction
	phenomenon20 - direction
	planet21 - direction
	planet22 - direction
	star23 - direction
	phenomenon24 - direction
)
(:init
	(supports instrument0 infrared2)
	(supports instrument0 image4)
	(calibration_target instrument0 groundstation0)
	(supports instrument1 spectrograph0)
	(calibration_target instrument1 star3)
	(supports instrument2 infrared3)
	(supports instrument2 thermograph1)
	(supports instrument2 spectrograph0)
	(calibration_target instrument2 star1)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument2 satellite0)
	(power_avail satellite0)
	(pointing satellite0 planet21)
	(= (data_capacity satellite0) 1000)
	(= (fuel satellite0) 111)
	(supports instrument3 thermograph1)
	(supports instrument3 image5)
	(calibration_target instrument3 star1)
	(supports instrument4 spectrograph0)
	(calibration_target instrument4 star3)
	(supports instrument5 thermograph1)
	(supports instrument5 spectrograph0)
	(supports instrument5 spectrograph6)
	(calibration_target instrument5 groundstation4)
	(supports instrument6 image5)
	(supports instrument6 infrared7)
	(calibration_target instrument6 star3)
	(supports instrument7 spectrograph6)
	(supports instrument7 thermograph1)
	(supports instrument7 spectrograph0)
	(calibration_target instrument7 star2)
	(on_board instrument3 satellite1)
	(on_board instrument4 satellite1)
	(on_board instrument5 satellite1)
	(on_board instrument6 satellite1)
	(on_board instrument7 satellite1)
	(power_avail satellite1)
	(pointing satellite1 planet21)
	(= (data_capacity satellite1) 1000)
	(= (fuel satellite1) 155)
	(supports instrument8 infrared3)
	(supports instrument8 infrared7)
	(calibration_target instrument8 star1)
	(supports instrument9 spectrograph0)
	(calibration_target instrument9 star3)
	(supports instrument10 image4)
	(supports instrument10 infrared7)
	(supports instrument10 image5)
	(calibration_target instrument10 groundstation4)
	(supports instrument11 infrared2)
	(calibration_target instrument11 star2)
	(supports instrument12 thermograph1)
	(calibration_target instrument12 star3)
	(supports instrument13 infrared3)
	(calibration_target instrument13 star2)
	(on_board instrument8 satellite2)
	(on_board instrument9 satellite2)
	(on_board instrument10 satellite2)
	(on_board instrument11 satellite2)
	(on_board instrument12 satellite2)
	(on_board instrument13 satellite2)
	(power_avail satellite2)
	(pointing satellite2 phenomenon5)
	(= (data_capacity satellite2) 1000)
	(= (fuel satellite2) 176)
	(supports instrument14 thermograph1)
	(supports instrument14 infrared2)
	(calibration_target instrument14 groundstation4)
	(supports instrument15 infrared2)
	(calibration_target instrument15 star1)
	(supports instrument16 image4)
	(supports instrument16 spectrograph6)
	(calibration_target instrument16 star2)
	(supports instrument17 image4)
	(supports instrument17 infrared7)
	(supports instrument17 image5)
	(calibration_target instrument17 groundstation0)
	(supports instrument18 image4)
	(supports instrument18 spectrograph6)
	(calibration_target instrument18 star2)
	(supports instrument19 infrared3)
	(supports instrument19 infrared7)
	(supports instrument19 spectrograph6)
	(calibration_target instrument19 star3)
	(supports instrument20 infrared3)
	(supports instrument20 infrared2)
	(calibration_target instrument20 star2)
	(supports instrument21 infrared2)
	(supports instrument21 thermograph1)
	(calibration_target instrument21 groundstation4)
	(on_board instrument14 satellite3)
	(on_board instrument15 satellite3)
	(on_board instrument16 satellite3)
	(on_board instrument17 satellite3)
	(on_board instrument18 satellite3)
	(on_board instrument19 satellite3)
	(on_board instrument20 satellite3)
	(on_board instrument21 satellite3)
	(power_avail satellite3)
	(pointing satellite3 phenomenon20)
	(= (data_capacity satellite3) 1000)
	(= (fuel satellite3) 125)
	(supports instrument22 thermograph1)
	(supports instrument22 image5)
	(calibration_target instrument22 star2)
	(supports instrument23 infrared7)
	(supports instrument23 thermograph1)
	(calibration_target instrument23 star3)
	(supports instrument24 infrared3)
	(supports instrument24 spectrograph0)
	(calibration_target instrument24 groundstation0)
	(on_board instrument22 satellite4)
	(on_board instrument23 satellite4)
	(on_board instrument24 satellite4)
	(power_avail satellite4)
	(pointing satellite4 star14)
	(= (data_capacity satellite4) 1000)
	(= (fuel satellite4) 124)
	(= (data phenomenon5 image4) 65)
	(= (data star6 image4) 69)
	(= (data phenomenon7 image4) 189)
	(= (data phenomenon8 image4) 16)
	(= (data planet9 image4) 132)
	(= (data star10 image4) 185)
	(= (data phenomenon11 image4) 121)
	(= (data star12 image4) 150)
	(= (data phenomenon13 image4) 33)
	(= (data star14 image4) 138)
	(= (data planet15 image4) 37)
	(= (data star16 image4) 193)
	(= (data planet17 image4) 112)
	(= (data star18 image4) 99)
	(= (data star19 image4) 100)
	(= (data phenomenon20 image4) 143)
	(= (data planet21 image4) 179)
	(= (data planet22 image4) 119)
	(= (data star23 image4) 50)
	(= (data phenomenon24 image4) 64)
	(= (data phenomenon5 spectrograph6) 152)
	(= (data star6 spectrograph6) 45)
	(= (data phenomenon7 spectrograph6) 5)
	(= (data phenomenon8 spectrograph6) 163)
	(= (data planet9 spectrograph6) 105)
	(= (data star10 spectrograph6) 25)
	(= (data phenomenon11 spectrograph6) 5)
	(= (data star12 spectrograph6) 147)
	(= (data phenomenon13 spectrograph6) 73)
	(= (data star14 spectrograph6) 59)
	(= (data planet15 spectrograph6) 4)
	(= (data star16 spectrograph6) 23)
	(= (data planet17 spectrograph6) 67)
	(= (data star18 spectrograph6) 3)
	(= (data star19 spectrograph6) 61)
	(= (data phenomenon20 spectrograph6) 149)
	(= (data planet21 spectrograph6) 63)
	(= (data planet22 spectrograph6) 91)
	(= (data star23 spectrograph6) 124)
	(= (data phenomenon24 spectrograph6) 176)
	(= (data phenomenon5 infrared2) 186)
	(= (data star6 infrared2) 187)
	(= (data phenomenon7 infrared2) 23)
	(= (data phenomenon8 infrared2) 190)
	(= (data planet9 infrared2) 64)
	(= (data star10 infrared2) 80)
	(= (data phenomenon11 infrared2) 28)
	(= (data star12 infrared2) 35)
	(= (data phenomenon13 infrared2) 155)
	(= (data star14 infrared2) 58)
	(= (data planet15 infrared2) 134)
	(= (data star16 infrared2) 198)
	(= (data planet17 infrared2) 20)
	(= (data star18 infrared2) 49)
	(= (data star19 infrared2) 177)
	(= (data phenomenon20 infrared2) 35)
	(= (data planet21 infrared2) 60)
	(= (data planet22 infrared2) 111)
	(= (data star23 infrared2) 14)
	(= (data phenomenon24 infrared2) 144)
	(= (data phenomenon5 image5) 156)
	(= (data star6 image5) 171)
	(= (data phenomenon7 image5) 71)
	(= (data phenomenon8 image5) 12)
	(= (data planet9 image5) 75)
	(= (data star10 image5) 15)
	(= (data phenomenon11 image5) 156)
	(= (data star12 image5) 147)
	(= (data phenomenon13 image5) 174)
	(= (data star14 image5) 192)
	(= (data planet15 image5) 51)
	(= (data star16 image5) 145)
	(= (data planet17 image5) 122)
	(= (data star18 image5) 114)
	(= (data star19 image5) 122)
	(= (data phenomenon20 image5) 62)
	(= (data planet21 image5) 87)
	(= (data planet22 image5) 44)
	(= (data star23 image5) 31)
	(= (data phenomenon24 image5) 17)
	(= (data phenomenon5 thermograph1) 153)
	(= (data star6 thermograph1) 71)
	(= (data phenomenon7 thermograph1) 111)
	(= (data phenomenon8 thermograph1) 106)
	(= (data planet9 thermograph1) 117)
	(= (data star10 thermograph1) 80)
	(= (data phenomenon11 thermograph1) 66)
	(= (data star12 thermograph1) 12)
	(= (data phenomenon13 thermograph1) 125)
	(= (data star14 thermograph1) 87)
	(= (data planet15 thermograph1) 90)
	(= (data star16 thermograph1) 186)
	(= (data planet17 thermograph1) 200)
	(= (data star18 thermograph1) 130)
	(= (data star19 thermograph1) 142)
	(= (data phenomenon20 thermograph1) 45)
	(= (data planet21 thermograph1) 148)
	(= (data planet22 thermograph1) 3)
	(= (data star23 thermograph1) 65)
	(= (data phenomenon24 thermograph1) 124)
	(= (data phenomenon5 infrared7) 144)
	(= (data star6 infrared7) 64)
	(= (data phenomenon7 infrared7) 175)
	(= (data phenomenon8 infrared7) 4)
	(= (data planet9 infrared7) 136)
	(= (data star10 infrared7) 56)
	(= (data phenomenon11 infrared7) 86)
	(= (data star12 infrared7) 116)
	(= (data phenomenon13 infrared7) 143)
	(= (data star14 infrared7) 134)
	(= (data planet15 infrared7) 158)
	(= (data star16 infrared7) 195)
	(= (data planet17 infrared7) 191)
	(= (data star18 infrared7) 159)
	(= (data star19 infrared7) 68)
	(= (data phenomenon20 infrared7) 16)
	(= (data planet21 infrared7) 12)
	(= (data planet22 infrared7) 183)
	(= (data star23 infrared7) 80)
	(= (data phenomenon24 infrared7) 126)
	(= (data phenomenon5 spectrograph0) 196)
	(= (data star6 spectrograph0) 49)
	(= (data phenomenon7 spectrograph0) 72)
	(= (data phenomenon8 spectrograph0) 157)
	(= (data planet9 spectrograph0) 115)
	(= (data star10 spectrograph0) 193)
	(= (data phenomenon11 spectrograph0) 133)
	(= (data star12 spectrograph0) 169)
	(= (data phenomenon13 spectrograph0) 124)
	(= (data star14 spectrograph0) 165)
	(= (data planet15 spectrograph0) 60)
	(= (data star16 spectrograph0) 183)
	(= (data planet17 spectrograph0) 134)
	(= (data star18 spectrograph0) 197)
	(= (data star19 spectrograph0) 189)
	(= (data phenomenon20 spectrograph0) 2)
	(= (data planet21 spectrograph0) 195)
	(= (data planet22 spectrograph0) 194)
	(= (data star23 spectrograph0) 38)
	(= (data phenomenon24 spectrograph0) 160)
	(= (data phenomenon5 infrared3) 115)
	(= (data star6 infrared3) 114)
	(= (data phenomenon7 infrared3) 135)
	(= (data phenomenon8 infrared3) 28)
	(= (data planet9 infrared3) 143)
	(= (data star10 infrared3) 68)
	(= (data phenomenon11 infrared3) 158)
	(= (data star12 infrared3) 140)
	(= (data phenomenon13 infrared3) 2)
	(= (data star14 infrared3) 150)
	(= (data planet15 infrared3) 189)
	(= (data star16 infrared3) 164)
	(= (data planet17 infrared3) 13)
	(= (data star18 infrared3) 15)
	(= (data star19 infrared3) 31)
	(= (data phenomenon20 infrared3) 164)
	(= (data planet21 infrared3) 121)
	(= (data planet22 infrared3) 46)
	(= (data star23 infrared3) 25)
	(= (data phenomenon24 infrared3) 153)
	(= (slew_time star1 groundstation0) 34.76)
	(= (slew_time groundstation0 star1) 34.76)
	(= (slew_time groundstation4 groundstation0) 49.23)
	(= (slew_time groundstation0 groundstation4) 49.23)
	(= (slew_time groundstation4 star1) 53.28)
	(= (slew_time star1 groundstation4) 53.28)
	(= (slew_time groundstation4 star2) 5.807)
	(= (slew_time star2 groundstation4) 5.807)
	(= (slew_time groundstation4 star3) 15.9)
	(= (slew_time star3 groundstation4) 15.9)
	(= (slew_time star2 groundstation0) 20.17)
	(= (slew_time groundstation0 star2) 20.17)
	(= (slew_time star2 star1) 56.75)
	(= (slew_time star1 star2) 56.75)
	(= (slew_time star3 groundstation0) 14.58)
	(= (slew_time groundstation0 star3) 14.58)
	(= (slew_time star3 star1) 32.13)
	(= (slew_time star1 star3) 32.13)
	(= (slew_time star3 star2) 29.15)
	(= (slew_time star2 star3) 29.15)
	(= (slew_time phenomenon5 groundstation0) 19.16)
	(= (slew_time groundstation0 phenomenon5) 19.16)
	(= (slew_time phenomenon5 star1) 4.713)
	(= (slew_time star1 phenomenon5) 4.713)
	(= (slew_time phenomenon5 star2) 35.6)
	(= (slew_time star2 phenomenon5) 35.6)
	(= (slew_time phenomenon5 star3) 47.5)
	(= (slew_time star3 phenomenon5) 47.5)
	(= (slew_time phenomenon5 groundstation4) 22.09)
	(= (slew_time groundstation4 phenomenon5) 22.09)
	(= (slew_time star6 groundstation0) 5.654)
	(= (slew_time groundstation0 star6) 5.654)
	(= (slew_time star6 star1) 73.23)
	(= (slew_time star1 star6) 73.23)
	(= (slew_time star6 star2) 2.725)
	(= (slew_time star2 star6) 2.725)
	(= (slew_time star6 star3) 6.397)
	(= (slew_time star3 star6) 6.397)
	(= (slew_time star6 groundstation4) 8.293)
	(= (slew_time groundstation4 star6) 8.293)
	(= (slew_time star6 phenomenon5) 14.07)
	(= (slew_time phenomenon5 star6) 14.07)
	(= (slew_time phenomenon7 groundstation0) 46.7)
	(= (slew_time groundstation0 phenomenon7) 46.7)
	(= (slew_time phenomenon7 star1) 4.542)
	(= (slew_time star1 phenomenon7) 4.542)
	(= (slew_time phenomenon7 star2) 27.51)
	(= (slew_time star2 phenomenon7) 27.51)
	(= (slew_time phenomenon7 star3) 6.504)
	(= (slew_time star3 phenomenon7) 6.504)
	(= (slew_time phenomenon7 groundstation4) 43.25)
	(= (slew_time groundstation4 phenomenon7) 43.25)
	(= (slew_time phenomenon7 phenomenon5) 55.38)
	(= (slew_time phenomenon5 phenomenon7) 55.38)
	(= (slew_time phenomenon7 star6) 55.86)
	(= (slew_time star6 phenomenon7) 55.86)
	(= (slew_time phenomenon8 groundstation0) 55.74)
	(= (slew_time groundstation0 phenomenon8) 55.74)
	(= (slew_time phenomenon8 star1) 58.11)
	(= (slew_time star1 phenomenon8) 58.11)
	(= (slew_time phenomenon8 star2) 34.13)
	(= (slew_time star2 phenomenon8) 34.13)
	(= (slew_time phenomenon8 star3) 28.1)
	(= (slew_time star3 phenomenon8) 28.1)
	(= (slew_time phenomenon8 groundstation4) 6.014)
	(= (slew_time groundstation4 phenomenon8) 6.014)
	(= (slew_time phenomenon8 phenomenon5) 70.95)
	(= (slew_time phenomenon5 phenomenon8) 70.95)
	(= (slew_time phenomenon8 star6) 32.57)
	(= (slew_time star6 phenomenon8) 32.57)
	(= (slew_time phenomenon8 phenomenon7) 45.79)
	(= (slew_time phenomenon7 phenomenon8) 45.79)
	(= (slew_time planet9 groundstation0) 42.36)
	(= (slew_time groundstation0 planet9) 42.36)
	(= (slew_time planet9 star1) 55.88)
	(= (slew_time star1 planet9) 55.88)
	(= (slew_time planet9 star2) 41.71)
	(= (slew_time star2 planet9) 41.71)
	(= (slew_time planet9 star3) 40.5)
	(= (slew_time star3 planet9) 40.5)
	(= (slew_time planet9 groundstation4) 18.78)
	(= (slew_time groundstation4 planet9) 18.78)
	(= (slew_time planet9 phenomenon5) 22)
	(= (slew_time phenomenon5 planet9) 22)
	(= (slew_time planet9 star6) 30.81)
	(= (slew_time star6 planet9) 30.81)
	(= (slew_time planet9 phenomenon7) 62.69)
	(= (slew_time phenomenon7 planet9) 62.69)
	(= (slew_time planet9 phenomenon8) 63.14)
	(= (slew_time phenomenon8 planet9) 63.14)
	(= (slew_time star10 groundstation0) 42.95)
	(= (slew_time groundstation0 star10) 42.95)
	(= (slew_time star10 star1) 45.15)
	(= (slew_time star1 star10) 45.15)
	(= (slew_time star10 star2) 37.05)
	(= (slew_time star2 star10) 37.05)
	(= (slew_time star10 star3) 15.83)
	(= (slew_time star3 star10) 15.83)
	(= (slew_time star10 groundstation4) 22.09)
	(= (slew_time groundstation4 star10) 22.09)
	(= (slew_time star10 phenomenon5) 51.47)
	(= (slew_time phenomenon5 star10) 51.47)
	(= (slew_time star10 star6) 21.95)
	(= (slew_time star6 star10) 21.95)
	(= (slew_time star10 phenomenon7) 40.02)
	(= (slew_time phenomenon7 star10) 40.02)
	(= (slew_time star10 phenomenon8) 39.38)
	(= (slew_time phenomenon8 star10) 39.38)
	(= (slew_time star10 planet9) 17.99)
	(= (slew_time planet9 star10) 17.99)
	(= (slew_time phenomenon11 groundstation0) 40.36)
	(= (slew_time groundstation0 phenomenon11) 40.36)
	(= (slew_time phenomenon11 star1) 0.3915)
	(= (slew_time star1 phenomenon11) 0.3915)
	(= (slew_time phenomenon11 star2) 56.93)
	(= (slew_time star2 phenomenon11) 56.93)
	(= (slew_time phenomenon11 star3) 77.4)
	(= (slew_time star3 phenomenon11) 77.4)
	(= (slew_time phenomenon11 groundstation4) 18.68)
	(= (slew_time groundstation4 phenomenon11) 18.68)
	(= (slew_time phenomenon11 phenomenon5) 17.79)
	(= (slew_time phenomenon5 phenomenon11) 17.79)
	(= (slew_time phenomenon11 star6) 20.13)
	(= (slew_time star6 phenomenon11) 20.13)
	(= (slew_time phenomenon11 phenomenon7) 23.22)
	(= (slew_time phenomenon7 phenomenon11) 23.22)
	(= (slew_time phenomenon11 phenomenon8) 5.645)
	(= (slew_time phenomenon8 phenomenon11) 5.645)
	(= (slew_time phenomenon11 planet9) 60.59)
	(= (slew_time planet9 phenomenon11) 60.59)
	(= (slew_time phenomenon11 star10) 35.25)
	(= (slew_time star10 phenomenon11) 35.25)
	(= (slew_time star12 groundstation0) 25.07)
	(= (slew_time groundstation0 star12) 25.07)
	(= (slew_time star12 star1) 12.69)
	(= (slew_time star1 star12) 12.69)
	(= (slew_time star12 star2) 79.5)
	(= (slew_time star2 star12) 79.5)
	(= (slew_time star12 star3) 32.44)
	(= (slew_time star3 star12) 32.44)
	(= (slew_time star12 groundstation4) 22.15)
	(= (slew_time groundstation4 star12) 22.15)
	(= (slew_time star12 phenomenon5) 73.65)
	(= (slew_time phenomenon5 star12) 73.65)
	(= (slew_time star12 star6) 95.82)
	(= (slew_time star6 star12) 95.82)
	(= (slew_time star12 phenomenon7) 40.36)
	(= (slew_time phenomenon7 star12) 40.36)
	(= (slew_time star12 phenomenon8) 88.43)
	(= (slew_time phenomenon8 star12) 88.43)
	(= (slew_time star12 planet9) 30.41)
	(= (slew_time planet9 star12) 30.41)
	(= (slew_time star12 star10) 32.64)
	(= (slew_time star10 star12) 32.64)
	(= (slew_time star12 phenomenon11) 62.2)
	(= (slew_time phenomenon11 star12) 62.2)
	(= (slew_time phenomenon13 groundstation0) 32.4)
	(= (slew_time groundstation0 phenomenon13) 32.4)
	(= (slew_time phenomenon13 star1) 26.96)
	(= (slew_time star1 phenomenon13) 26.96)
	(= (slew_time phenomenon13 star2) 44.56)
	(= (slew_time star2 phenomenon13) 44.56)
	(= (slew_time phenomenon13 star3) 19.22)
	(= (slew_time star3 phenomenon13) 19.22)
	(= (slew_time phenomenon13 groundstation4) 14.47)
	(= (slew_time groundstation4 phenomenon13) 14.47)
	(= (slew_time phenomenon13 phenomenon5) 35.02)
	(= (slew_time phenomenon5 phenomenon13) 35.02)
	(= (slew_time phenomenon13 star6) 85.6)
	(= (slew_time star6 phenomenon13) 85.6)
	(= (slew_time phenomenon13 phenomenon7) 42.56)
	(= (slew_time phenomenon7 phenomenon13) 42.56)
	(= (slew_time phenomenon13 phenomenon8) 49.53)
	(= (slew_time phenomenon8 phenomenon13) 49.53)
	(= (slew_time phenomenon13 planet9) 12.91)
	(= (slew_time planet9 phenomenon13) 12.91)
	(= (slew_time phenomenon13 star10) 22.39)
	(= (slew_time star10 phenomenon13) 22.39)
	(= (slew_time phenomenon13 phenomenon11) 80.48)
	(= (slew_time phenomenon11 phenomenon13) 80.48)
	(= (slew_time phenomenon13 star12) 7.052)
	(= (slew_time star12 phenomenon13) 7.052)
	(= (slew_time star14 groundstation0) 34.95)
	(= (slew_time groundstation0 star14) 34.95)
	(= (slew_time star14 star1) 28.93)
	(= (slew_time star1 star14) 28.93)
	(= (slew_time star14 star2) 66.87)
	(= (slew_time star2 star14) 66.87)
	(= (slew_time star14 star3) 12.57)
	(= (slew_time star3 star14) 12.57)
	(= (slew_time star14 groundstation4) 7.936)
	(= (slew_time groundstation4 star14) 7.936)
	(= (slew_time star14 phenomenon5) 30.51)
	(= (slew_time phenomenon5 star14) 30.51)
	(= (slew_time star14 star6) 48.54)
	(= (slew_time star6 star14) 48.54)
	(= (slew_time star14 phenomenon7) 25.74)
	(= (slew_time phenomenon7 star14) 25.74)
	(= (slew_time star14 phenomenon8) 4.894)
	(= (slew_time phenomenon8 star14) 4.894)
	(= (slew_time star14 planet9) 43.92)
	(= (slew_time planet9 star14) 43.92)
	(= (slew_time star14 star10) 8.531)
	(= (slew_time star10 star14) 8.531)
	(= (slew_time star14 phenomenon11) 6.76)
	(= (slew_time phenomenon11 star14) 6.76)
	(= (slew_time star14 star12) 7.831)
	(= (slew_time star12 star14) 7.831)
	(= (slew_time star14 phenomenon13) 7.47)
	(= (slew_time phenomenon13 star14) 7.47)
	(= (slew_time planet15 groundstation0) 37.49)
	(= (slew_time groundstation0 planet15) 37.49)
	(= (slew_time planet15 star1) 64.38)
	(= (slew_time star1 planet15) 64.38)
	(= (slew_time planet15 star2) 20.06)
	(= (slew_time star2 planet15) 20.06)
	(= (slew_time planet15 star3) 9.161)
	(= (slew_time star3 planet15) 9.161)
	(= (slew_time planet15 groundstation4) 51.3)
	(= (slew_time groundstation4 planet15) 51.3)
	(= (slew_time planet15 phenomenon5) 18.51)
	(= (slew_time phenomenon5 planet15) 18.51)
	(= (slew_time planet15 star6) 69.76)
	(= (slew_time star6 planet15) 69.76)
	(= (slew_time planet15 phenomenon7) 67.88)
	(= (slew_time phenomenon7 planet15) 67.88)
	(= (slew_time planet15 phenomenon8) 8.491)
	(= (slew_time phenomenon8 planet15) 8.491)
	(= (slew_time planet15 planet9) 14.97)
	(= (slew_time planet9 planet15) 14.97)
	(= (slew_time planet15 star10) 81.8)
	(= (slew_time star10 planet15) 81.8)
	(= (slew_time planet15 phenomenon11) 58.87)
	(= (slew_time phenomenon11 planet15) 58.87)
	(= (slew_time planet15 star12) 27.03)
	(= (slew_time star12 planet15) 27.03)
	(= (slew_time planet15 phenomenon13) 63.22)
	(= (slew_time phenomenon13 planet15) 63.22)
	(= (slew_time planet15 star14) 61.66)
	(= (slew_time star14 planet15) 61.66)
	(= (slew_time star16 groundstation0) 16.57)
	(= (slew_time groundstation0 star16) 16.57)
	(= (slew_time star16 star1) 36.76)
	(= (slew_time star1 star16) 36.76)
	(= (slew_time star16 star2) 29.72)
	(= (slew_time star2 star16) 29.72)
	(= (slew_time star16 star3) 11.71)
	(= (slew_time star3 star16) 11.71)
	(= (slew_time star16 groundstation4) 87.54)
	(= (slew_time groundstation4 star16) 87.54)
	(= (slew_time star16 phenomenon5) 43.68)
	(= (slew_time phenomenon5 star16) 43.68)
	(= (slew_time star16 star6) 12.81)
	(= (slew_time star6 star16) 12.81)
	(= (slew_time star16 phenomenon7) 23.78)
	(= (slew_time phenomenon7 star16) 23.78)
	(= (slew_time star16 phenomenon8) 37.43)
	(= (slew_time phenomenon8 star16) 37.43)
	(= (slew_time star16 planet9) 23.85)
	(= (slew_time planet9 star16) 23.85)
	(= (slew_time star16 star10) 15.42)
	(= (slew_time star10 star16) 15.42)
	(= (slew_time star16 phenomenon11) 51.78)
	(= (slew_time phenomenon11 star16) 51.78)
	(= (slew_time star16 star12) 11.71)
	(= (slew_time star12 star16) 11.71)
	(= (slew_time star16 phenomenon13) 54.24)
	(= (slew_time phenomenon13 star16) 54.24)
	(= (slew_time star16 star14) 47.68)
	(= (slew_time star14 star16) 47.68)
	(= (slew_time star16 planet15) 16.19)
	(= (slew_time planet15 star16) 16.19)
	(= (slew_time planet17 groundstation0) 77.24)
	(= (slew_time groundstation0 planet17) 77.24)
	(= (slew_time planet17 star1) 61.65)
	(= (slew_time star1 planet17) 61.65)
	(= (slew_time planet17 star2) 23.64)
	(= (slew_time star2 planet17) 23.64)
	(= (slew_time planet17 star3) 70.82)
	(= (slew_time star3 planet17) 70.82)
	(= (slew_time planet17 groundstation4) 28.31)
	(= (slew_time groundstation4 planet17) 28.31)
	(= (slew_time planet17 phenomenon5) 22.04)
	(= (slew_time phenomenon5 planet17) 22.04)
	(= (slew_time planet17 star6) 5.039)
	(= (slew_time star6 planet17) 5.039)
	(= (slew_time planet17 phenomenon7) 11.9)
	(= (slew_time phenomenon7 planet17) 11.9)
	(= (slew_time planet17 phenomenon8) 7.604)
	(= (slew_time phenomenon8 planet17) 7.604)
	(= (slew_time planet17 planet9) 83.83)
	(= (slew_time planet9 planet17) 83.83)
	(= (slew_time planet17 star10) 42.75)
	(= (slew_time star10 planet17) 42.75)
	(= (slew_time planet17 phenomenon11) 14.58)
	(= (slew_time phenomenon11 planet17) 14.58)
	(= (slew_time planet17 star12) 60.38)
	(= (slew_time star12 planet17) 60.38)
	(= (slew_time planet17 phenomenon13) 58.79)
	(= (slew_time phenomenon13 planet17) 58.79)
	(= (slew_time planet17 star14) 62.9)
	(= (slew_time star14 planet17) 62.9)
	(= (slew_time planet17 planet15) 4.333)
	(= (slew_time planet15 planet17) 4.333)
	(= (slew_time planet17 star16) 6.165)
	(= (slew_time star16 planet17) 6.165)
	(= (slew_time star18 groundstation0) 19.75)
	(= (slew_time groundstation0 star18) 19.75)
	(= (slew_time star18 star1) 31.68)
	(= (slew_time star1 star18) 31.68)
	(= (slew_time star18 star2) 0.1349)
	(= (slew_time star2 star18) 0.1349)
	(= (slew_time star18 star3) 58.94)
	(= (slew_time star3 star18) 58.94)
	(= (slew_time star18 groundstation4) 58.3)
	(= (slew_time groundstation4 star18) 58.3)
	(= (slew_time star18 phenomenon5) 3.465)
	(= (slew_time phenomenon5 star18) 3.465)
	(= (slew_time star18 star6) 75.84)
	(= (slew_time star6 star18) 75.84)
	(= (slew_time star18 phenomenon7) 61.61)
	(= (slew_time phenomenon7 star18) 61.61)
	(= (slew_time star18 phenomenon8) 54)
	(= (slew_time phenomenon8 star18) 54)
	(= (slew_time star18 planet9) 44.25)
	(= (slew_time planet9 star18) 44.25)
	(= (slew_time star18 star10) 9.177)
	(= (slew_time star10 star18) 9.177)
	(= (slew_time star18 phenomenon11) 10.84)
	(= (slew_time phenomenon11 star18) 10.84)
	(= (slew_time star18 star12) 43.47)
	(= (slew_time star12 star18) 43.47)
	(= (slew_time star18 phenomenon13) 7.849)
	(= (slew_time phenomenon13 star18) 7.849)
	(= (slew_time star18 star14) 79.84)
	(= (slew_time star14 star18) 79.84)
	(= (slew_time star18 planet15) 13.56)
	(= (slew_time planet15 star18) 13.56)
	(= (slew_time star18 star16) 11.22)
	(= (slew_time star16 star18) 11.22)
	(= (slew_time star18 planet17) 86.56)
	(= (slew_time planet17 star18) 86.56)
	(= (slew_time star19 groundstation0) 48.84)
	(= (slew_time groundstation0 star19) 48.84)
	(= (slew_time star19 star1) 2.154)
	(= (slew_time star1 star19) 2.154)
	(= (slew_time star19 star2) 19.71)
	(= (slew_time star2 star19) 19.71)
	(= (slew_time star19 star3) 0.379)
	(= (slew_time star3 star19) 0.379)
	(= (slew_time star19 groundstation4) 15.88)
	(= (slew_time groundstation4 star19) 15.88)
	(= (slew_time star19 phenomenon5) 1.77)
	(= (slew_time phenomenon5 star19) 1.77)
	(= (slew_time star19 star6) 46.36)
	(= (slew_time star6 star19) 46.36)
	(= (slew_time star19 phenomenon7) 44.19)
	(= (slew_time phenomenon7 star19) 44.19)
	(= (slew_time star19 phenomenon8) 6.326)
	(= (slew_time phenomenon8 star19) 6.326)
	(= (slew_time star19 planet9) 68.93)
	(= (slew_time planet9 star19) 68.93)
	(= (slew_time star19 star10) 30)
	(= (slew_time star10 star19) 30)
	(= (slew_time star19 phenomenon11) 3.295)
	(= (slew_time phenomenon11 star19) 3.295)
	(= (slew_time star19 star12) 15.55)
	(= (slew_time star12 star19) 15.55)
	(= (slew_time star19 phenomenon13) 21.41)
	(= (slew_time phenomenon13 star19) 21.41)
	(= (slew_time star19 star14) 30.77)
	(= (slew_time star14 star19) 30.77)
	(= (slew_time star19 planet15) 53.1)
	(= (slew_time planet15 star19) 53.1)
	(= (slew_time star19 star16) 9.814)
	(= (slew_time star16 star19) 9.814)
	(= (slew_time star19 planet17) 62.38)
	(= (slew_time planet17 star19) 62.38)
	(= (slew_time star19 star18) 59.63)
	(= (slew_time star18 star19) 59.63)
	(= (slew_time phenomenon20 groundstation0) 39.41)
	(= (slew_time groundstation0 phenomenon20) 39.41)
	(= (slew_time phenomenon20 star1) 8.078)
	(= (slew_time star1 phenomenon20) 8.078)
	(= (slew_time phenomenon20 star2) 12.81)
	(= (slew_time star2 phenomenon20) 12.81)
	(= (slew_time phenomenon20 star3) 45.62)
	(= (slew_time star3 phenomenon20) 45.62)
	(= (slew_time phenomenon20 groundstation4) 8.927)
	(= (slew_time groundstation4 phenomenon20) 8.927)
	(= (slew_time phenomenon20 phenomenon5) 57.68)
	(= (slew_time phenomenon5 phenomenon20) 57.68)
	(= (slew_time phenomenon20 star6) 1.086)
	(= (slew_time star6 phenomenon20) 1.086)
	(= (slew_time phenomenon20 phenomenon7) 73.84)
	(= (slew_time phenomenon7 phenomenon20) 73.84)
	(= (slew_time phenomenon20 phenomenon8) 31.75)
	(= (slew_time phenomenon8 phenomenon20) 31.75)
	(= (slew_time phenomenon20 planet9) 78.86)
	(= (slew_time planet9 phenomenon20) 78.86)
	(= (slew_time phenomenon20 star10) 5.312)
	(= (slew_time star10 phenomenon20) 5.312)
	(= (slew_time phenomenon20 phenomenon11) 15)
	(= (slew_time phenomenon11 phenomenon20) 15)
	(= (slew_time phenomenon20 star12) 1.708)
	(= (slew_time star12 phenomenon20) 1.708)
	(= (slew_time phenomenon20 phenomenon13) 6.053)
	(= (slew_time phenomenon13 phenomenon20) 6.053)
	(= (slew_time phenomenon20 star14) 11.45)
	(= (slew_time star14 phenomenon20) 11.45)
	(= (slew_time phenomenon20 planet15) 1.328)
	(= (slew_time planet15 phenomenon20) 1.328)
	(= (slew_time phenomenon20 star16) 37.82)
	(= (slew_time star16 phenomenon20) 37.82)
	(= (slew_time phenomenon20 planet17) 26.66)
	(= (slew_time planet17 phenomenon20) 26.66)
	(= (slew_time phenomenon20 star18) 28.6)
	(= (slew_time star18 phenomenon20) 28.6)
	(= (slew_time phenomenon20 star19) 44.78)
	(= (slew_time star19 phenomenon20) 44.78)
	(= (slew_time planet21 groundstation0) 27.84)
	(= (slew_time groundstation0 planet21) 27.84)
	(= (slew_time planet21 star1) 25.45)
	(= (slew_time star1 planet21) 25.45)
	(= (slew_time planet21 star2) 9.415)
	(= (slew_time star2 planet21) 9.415)
	(= (slew_time planet21 star3) 42.25)
	(= (slew_time star3 planet21) 42.25)
	(= (slew_time planet21 groundstation4) 59.04)
	(= (slew_time groundstation4 planet21) 59.04)
	(= (slew_time planet21 phenomenon5) 52.91)
	(= (slew_time phenomenon5 planet21) 52.91)
	(= (slew_time planet21 star6) 63.17)
	(= (slew_time star6 planet21) 63.17)
	(= (slew_time planet21 phenomenon7) 70.59)
	(= (slew_time phenomenon7 planet21) 70.59)
	(= (slew_time planet21 phenomenon8) 60.61)
	(= (slew_time phenomenon8 planet21) 60.61)
	(= (slew_time planet21 planet9) 11.44)
	(= (slew_time planet9 planet21) 11.44)
	(= (slew_time planet21 star10) 2.476)
	(= (slew_time star10 planet21) 2.476)
	(= (slew_time planet21 phenomenon11) 54.43)
	(= (slew_time phenomenon11 planet21) 54.43)
	(= (slew_time planet21 star12) 52.45)
	(= (slew_time star12 planet21) 52.45)
	(= (slew_time planet21 phenomenon13) 91.17)
	(= (slew_time phenomenon13 planet21) 91.17)
	(= (slew_time planet21 star14) 53.61)
	(= (slew_time star14 planet21) 53.61)
	(= (slew_time planet21 planet15) 65.5)
	(= (slew_time planet15 planet21) 65.5)
	(= (slew_time planet21 star16) 9.079)
	(= (slew_time star16 planet21) 9.079)
	(= (slew_time planet21 planet17) 10.99)
	(= (slew_time planet17 planet21) 10.99)
	(= (slew_time planet21 star18) 22.46)
	(= (slew_time star18 planet21) 22.46)
	(= (slew_time planet21 star19) 83.54)
	(= (slew_time star19 planet21) 83.54)
	(= (slew_time planet21 phenomenon20) 3.184)
	(= (slew_time phenomenon20 planet21) 3.184)
	(= (slew_time planet22 groundstation0) 59.7)
	(= (slew_time groundstation0 planet22) 59.7)
	(= (slew_time planet22 star1) 81.63)
	(= (slew_time star1 planet22) 81.63)
	(= (slew_time planet22 star2) 38.51)
	(= (slew_time star2 planet22) 38.51)
	(= (slew_time planet22 star3) 82.56)
	(= (slew_time star3 planet22) 82.56)
	(= (slew_time planet22 groundstation4) 14.93)
	(= (slew_time groundstation4 planet22) 14.93)
	(= (slew_time planet22 phenomenon5) 30.95)
	(= (slew_time phenomenon5 planet22) 30.95)
	(= (slew_time planet22 star6) 69.15)
	(= (slew_time star6 planet22) 69.15)
	(= (slew_time planet22 phenomenon7) 79.98)
	(= (slew_time phenomenon7 planet22) 79.98)
	(= (slew_time planet22 phenomenon8) 18.99)
	(= (slew_time phenomenon8 planet22) 18.99)
	(= (slew_time planet22 planet9) 63.54)
	(= (slew_time planet9 planet22) 63.54)
	(= (slew_time planet22 star10) 32.44)
	(= (slew_time star10 planet22) 32.44)
	(= (slew_time planet22 phenomenon11) 43.48)
	(= (slew_time phenomenon11 planet22) 43.48)
	(= (slew_time planet22 star12) 64.28)
	(= (slew_time star12 planet22) 64.28)
	(= (slew_time planet22 phenomenon13) 61.77)
	(= (slew_time phenomenon13 planet22) 61.77)
	(= (slew_time planet22 star14) 25.2)
	(= (slew_time star14 planet22) 25.2)
	(= (slew_time planet22 planet15) 9.173)
	(= (slew_time planet15 planet22) 9.173)
	(= (slew_time planet22 star16) 2.13)
	(= (slew_time star16 planet22) 2.13)
	(= (slew_time planet22 planet17) 67.04)
	(= (slew_time planet17 planet22) 67.04)
	(= (slew_time planet22 star18) 3.539)
	(= (slew_time star18 planet22) 3.539)
	(= (slew_time planet22 star19) 43.66)
	(= (slew_time star19 planet22) 43.66)
	(= (slew_time planet22 phenomenon20) 7.138)
	(= (slew_time phenomenon20 planet22) 7.138)
	(= (slew_time planet22 planet21) 7.82)
	(= (slew_time planet21 planet22) 7.82)
	(= (slew_time star23 groundstation0) 10.59)
	(= (slew_time groundstation0 star23) 10.59)
	(= (slew_time star23 star1) 44.8)
	(= (slew_time star1 star23) 44.8)
	(= (slew_time star23 star2) 3.063)
	(= (slew_time star2 star23) 3.063)
	(= (slew_time star23 star3) 0.4892)
	(= (slew_time star3 star23) 0.4892)
	(= (slew_time star23 groundstation4) 8.08)
	(= (slew_time groundstation4 star23) 8.08)
	(= (slew_time star23 phenomenon5) 31.19)
	(= (slew_time phenomenon5 star23) 31.19)
	(= (slew_time star23 star6) 48)
	(= (slew_time star6 star23) 48)
	(= (slew_time star23 phenomenon7) 15.93)
	(= (slew_time phenomenon7 star23) 15.93)
	(= (slew_time star23 phenomenon8) 25.19)
	(= (slew_time phenomenon8 star23) 25.19)
	(= (slew_time star23 planet9) 31.43)
	(= (slew_time planet9 star23) 31.43)
	(= (slew_time star23 star10) 88.45)
	(= (slew_time star10 star23) 88.45)
	(= (slew_time star23 phenomenon11) 1.243)
	(= (slew_time phenomenon11 star23) 1.243)
	(= (slew_time star23 star12) 40.97)
	(= (slew_time star12 star23) 40.97)
	(= (slew_time star23 phenomenon13) 52.44)
	(= (slew_time phenomenon13 star23) 52.44)
	(= (slew_time star23 star14) 10.48)
	(= (slew_time star14 star23) 10.48)
	(= (slew_time star23 planet15) 30.22)
	(= (slew_time planet15 star23) 30.22)
	(= (slew_time star23 star16) 17.86)
	(= (slew_time star16 star23) 17.86)
	(= (slew_time star23 planet17) 14.5)
	(= (slew_time planet17 star23) 14.5)
	(= (slew_time star23 star18) 10.65)
	(= (slew_time star18 star23) 10.65)
	(= (slew_time star23 star19) 73.88)
	(= (slew_time star19 star23) 73.88)
	(= (slew_time star23 phenomenon20) 46.49)
	(= (slew_time phenomenon20 star23) 46.49)
	(= (slew_time star23 planet21) 23.27)
	(= (slew_time planet21 star23) 23.27)
	(= (slew_time star23 planet22) 7.409)
	(= (slew_time planet22 star23) 7.409)
	(= (slew_time phenomenon24 groundstation0) 50.09)
	(= (slew_time groundstation0 phenomenon24) 50.09)
	(= (slew_time phenomenon24 star1) 40.88)
	(= (slew_time star1 phenomenon24) 40.88)
	(= (slew_time phenomenon24 star2) 67.95)
	(= (slew_time star2 phenomenon24) 67.95)
	(= (slew_time phenomenon24 star3) 55.16)
	(= (slew_time star3 phenomenon24) 55.16)
	(= (slew_time phenomenon24 groundstation4) 2.092)
	(= (slew_time groundstation4 phenomenon24) 2.092)
	(= (slew_time phenomenon24 phenomenon5) 60.56)
	(= (slew_time phenomenon5 phenomenon24) 60.56)
	(= (slew_time phenomenon24 star6) 84.53)
	(= (slew_time star6 phenomenon24) 84.53)
	(= (slew_time phenomenon24 phenomenon7) 18.96)
	(= (slew_time phenomenon7 phenomenon24) 18.96)
	(= (slew_time phenomenon24 phenomenon8) 1.533)
	(= (slew_time phenomenon8 phenomenon24) 1.533)
	(= (slew_time phenomenon24 planet9) 47)
	(= (slew_time planet9 phenomenon24) 47)
	(= (slew_time phenomenon24 star10) 41.03)
	(= (slew_time star10 phenomenon24) 41.03)
	(= (slew_time phenomenon24 phenomenon11) 32.22)
	(= (slew_time phenomenon11 phenomenon24) 32.22)
	(= (slew_time phenomenon24 star12) 84.44)
	(= (slew_time star12 phenomenon24) 84.44)
	(= (slew_time phenomenon24 phenomenon13) 32.86)
	(= (slew_time phenomenon13 phenomenon24) 32.86)
	(= (slew_time phenomenon24 star14) 19.72)
	(= (slew_time star14 phenomenon24) 19.72)
	(= (slew_time phenomenon24 planet15) 17.4)
	(= (slew_time planet15 phenomenon24) 17.4)
	(= (slew_time phenomenon24 star16) 13.3)
	(= (slew_time star16 phenomenon24) 13.3)
	(= (slew_time phenomenon24 planet17) 49.76)
	(= (slew_time planet17 phenomenon24) 49.76)
	(= (slew_time phenomenon24 star18) 18.71)
	(= (slew_time star18 phenomenon24) 18.71)
	(= (slew_time phenomenon24 star19) 34.7)
	(= (slew_time star19 phenomenon24) 34.7)
	(= (slew_time phenomenon24 phenomenon20) 29.28)
	(= (slew_time phenomenon20 phenomenon24) 29.28)
	(= (slew_time phenomenon24 planet21) 59.36)
	(= (slew_time planet21 phenomenon24) 59.36)
	(= (slew_time phenomenon24 planet22) 67.09)
	(= (slew_time planet22 phenomenon24) 67.09)
	(= (slew_time phenomenon24 star23) 36.95)
	(= (slew_time star23 phenomenon24) 36.95)
	(= (data-stored) 0)
	(= (fuel-used) 0)
)
(:goal (and
	(pointing satellite0 planet17)
	(have_image phenomenon5 infrared7)
	(have_image phenomenon5 image4)
	(have_image phenomenon7 thermograph1)
	(have_image planet9 spectrograph0)
	(have_image planet9 spectrograph6)
	(have_image star10 infrared3)
	(have_image star10 spectrograph6)
	(have_image phenomenon11 infrared2)
	(have_image star12 spectrograph6)
	(have_image star12 thermograph1)
	(have_image phenomenon13 infrared7)
	(have_image phenomenon13 infrared2)
	(have_image star14 infrared2)
	(have_image planet15 infrared2)
	(have_image star16 image4)
	(have_image planet17 image5)
	(have_image planet17 image4)
	(have_image star18 infrared2)
	(have_image star19 infrared3)
	(have_image star19 thermograph1)
	(have_image phenomenon20 spectrograph0)
	(have_image planet21 infrared3)
	(have_image planet21 image5)
	(have_image planet22 infrared2)
	(have_image star23 infrared2)
	(have_image phenomenon24 spectrograph6)
	(have_image phenomenon24 image5)
))
(:metric minimize (fuel-used))

)
