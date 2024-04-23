
        (define (problem prob24)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 r21 r22 r23 - robot
              l0 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 l16 l17 l18 l19 l20 l21 l22 l23 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17) (= (i r18) 18) (= (i r19) 19) (= (i r20) 20) (= (i r21) 21) (= (i r22) 22) (= (i r23) 23)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340) (= (x r18) 360) (= (x r19) 380) (= (x r20) 400) (= (x r21) 420) (= (x r22) 440) (= (x r23) 460)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r0 l2) 1) (= (p r0 l3) 1) (= (p r0 l4) 1) (= (p r0 l5) 1) (= (p r0 l6) 1) (= (p r0 l7) 1) (= (p r0 l8) 1) (= (p r0 l9) 1) (= (p r0 l10) 1) (= (p r0 l11) 1) (= (p r0 l12) 1) (= (p r0 l13) 1) (= (p r0 l14) 1) (= (p r0 l15) 1) (= (p r0 l16) 1) (= (p r0 l17) 1) (= (p r0 l18) 1) (= (p r0 l19) 1) (= (p r0 l20) 1) (= (p r0 l21) 1) (= (p r0 l22) 1) (= (p r0 l23) 1) (= (p r1 l0) 0) (= (p r1 l1) 0) (= (p r1 l2) 0) (= (p r1 l3) 0) (= (p r1 l4) 0) (= (p r1 l5) 0) (= (p r1 l6) 0) (= (p r1 l7) 0) (= (p r1 l8) 0) (= (p r1 l9) 0) (= (p r1 l10) 0) (= (p r1 l11) 0) (= (p r1 l12) 0) (= (p r1 l13) 0) (= (p r1 l14) 0) (= (p r1 l15) 0) (= (p r1 l16) 0) (= (p r1 l17) 0) (= (p r1 l18) 0) (= (p r1 l19) 0) (= (p r1 l20) 0) (= (p r1 l21) 0) (= (p r1 l22) 0) (= (p r1 l23) 0) (= (p r2 l0) 0) (= (p r2 l1) 0) (= (p r2 l2) 0) (= (p r2 l3) 0) (= (p r2 l4) 0) (= (p r2 l5) 0) (= (p r2 l6) 0) (= (p r2 l7) 0) (= (p r2 l8) 0) (= (p r2 l9) 0) (= (p r2 l10) 0) (= (p r2 l11) 0) (= (p r2 l12) 0) (= (p r2 l13) 0) (= (p r2 l14) 0) (= (p r2 l15) 0) (= (p r2 l16) 0) (= (p r2 l17) 0) (= (p r2 l18) 0) (= (p r2 l19) 0) (= (p r2 l20) 0) (= (p r2 l21) 0) (= (p r2 l22) 0) (= (p r2 l23) 0) (= (p r3 l0) 0) (= (p r3 l1) 0) (= (p r3 l2) 0) (= (p r3 l3) 0) (= (p r3 l4) 0) (= (p r3 l5) 0) (= (p r3 l6) 0) (= (p r3 l7) 0) (= (p r3 l8) 0) (= (p r3 l9) 0) (= (p r3 l10) 0) (= (p r3 l11) 0) (= (p r3 l12) 0) (= (p r3 l13) 0) (= (p r3 l14) 0) (= (p r3 l15) 0) (= (p r3 l16) 0) (= (p r3 l17) 0) (= (p r3 l18) 0) (= (p r3 l19) 0) (= (p r3 l20) 0) (= (p r3 l21) 0) (= (p r3 l22) 0) (= (p r3 l23) 0) (= (p r4 l0) 0) (= (p r4 l1) 0) (= (p r4 l2) 0) (= (p r4 l3) 0) (= (p r4 l4) 0) (= (p r4 l5) 0) (= (p r4 l6) 0) (= (p r4 l7) 0) (= (p r4 l8) 0) (= (p r4 l9) 0) (= (p r4 l10) 0) (= (p r4 l11) 0) (= (p r4 l12) 0) (= (p r4 l13) 0) (= (p r4 l14) 0) (= (p r4 l15) 0) (= (p r4 l16) 0) (= (p r4 l17) 0) (= (p r4 l18) 0) (= (p r4 l19) 0) (= (p r4 l20) 0) (= (p r4 l21) 0) (= (p r4 l22) 0) (= (p r4 l23) 0) (= (p r5 l0) 0) (= (p r5 l1) 0) (= (p r5 l2) 0) (= (p r5 l3) 0) (= (p r5 l4) 0) (= (p r5 l5) 0) (= (p r5 l6) 0) (= (p r5 l7) 0) (= (p r5 l8) 0) (= (p r5 l9) 0) (= (p r5 l10) 0) (= (p r5 l11) 0) (= (p r5 l12) 0) (= (p r5 l13) 0) (= (p r5 l14) 0) (= (p r5 l15) 0) (= (p r5 l16) 0) (= (p r5 l17) 0) (= (p r5 l18) 0) (= (p r5 l19) 0) (= (p r5 l20) 0) (= (p r5 l21) 0) (= (p r5 l22) 0) (= (p r5 l23) 0) (= (p r6 l0) 0) (= (p r6 l1) 0) (= (p r6 l2) 0) (= (p r6 l3) 0) (= (p r6 l4) 0) (= (p r6 l5) 0) (= (p r6 l6) 0) (= (p r6 l7) 0) (= (p r6 l8) 0) (= (p r6 l9) 0) (= (p r6 l10) 0) (= (p r6 l11) 0) (= (p r6 l12) 0) (= (p r6 l13) 0) (= (p r6 l14) 0) (= (p r6 l15) 0) (= (p r6 l16) 0) (= (p r6 l17) 0) (= (p r6 l18) 0) (= (p r6 l19) 0) (= (p r6 l20) 0) (= (p r6 l21) 0) (= (p r6 l22) 0) (= (p r6 l23) 0) (= (p r7 l0) 0) (= (p r7 l1) 0) (= (p r7 l2) 0) (= (p r7 l3) 0) (= (p r7 l4) 0) (= (p r7 l5) 0) (= (p r7 l6) 0) (= (p r7 l7) 0) (= (p r7 l8) 0) (= (p r7 l9) 0) (= (p r7 l10) 0) (= (p r7 l11) 0) (= (p r7 l12) 0) (= (p r7 l13) 0) (= (p r7 l14) 0) (= (p r7 l15) 0) (= (p r7 l16) 0) (= (p r7 l17) 0) (= (p r7 l18) 0) (= (p r7 l19) 0) (= (p r7 l20) 0) (= (p r7 l21) 0) (= (p r7 l22) 0) (= (p r7 l23) 0) (= (p r8 l0) 0) (= (p r8 l1) 0) (= (p r8 l2) 0) (= (p r8 l3) 0) (= (p r8 l4) 0) (= (p r8 l5) 0) (= (p r8 l6) 0) (= (p r8 l7) 0) (= (p r8 l8) 0) (= (p r8 l9) 0) (= (p r8 l10) 0) (= (p r8 l11) 0) (= (p r8 l12) 0) (= (p r8 l13) 0) (= (p r8 l14) 0) (= (p r8 l15) 0) (= (p r8 l16) 0) (= (p r8 l17) 0) (= (p r8 l18) 0) (= (p r8 l19) 0) (= (p r8 l20) 0) (= (p r8 l21) 0) (= (p r8 l22) 0) (= (p r8 l23) 0) (= (p r9 l0) 0) (= (p r9 l1) 0) (= (p r9 l2) 0) (= (p r9 l3) 0) (= (p r9 l4) 0) (= (p r9 l5) 0) (= (p r9 l6) 0) (= (p r9 l7) 0) (= (p r9 l8) 0) (= (p r9 l9) 0) (= (p r9 l10) 0) (= (p r9 l11) 0) (= (p r9 l12) 0) (= (p r9 l13) 0) (= (p r9 l14) 0) (= (p r9 l15) 0) (= (p r9 l16) 0) (= (p r9 l17) 0) (= (p r9 l18) 0) (= (p r9 l19) 0) (= (p r9 l20) 0) (= (p r9 l21) 0) (= (p r9 l22) 0) (= (p r9 l23) 0) (= (p r10 l0) 0) (= (p r10 l1) 0) (= (p r10 l2) 0) (= (p r10 l3) 0) (= (p r10 l4) 0) (= (p r10 l5) 0) (= (p r10 l6) 0) (= (p r10 l7) 0) (= (p r10 l8) 0) (= (p r10 l9) 0) (= (p r10 l10) 0) (= (p r10 l11) 0) (= (p r10 l12) 0) (= (p r10 l13) 0) (= (p r10 l14) 0) (= (p r10 l15) 0) (= (p r10 l16) 0) (= (p r10 l17) 0) (= (p r10 l18) 0) (= (p r10 l19) 0) (= (p r10 l20) 0) (= (p r10 l21) 0) (= (p r10 l22) 0) (= (p r10 l23) 0) (= (p r11 l0) 0) (= (p r11 l1) 0) (= (p r11 l2) 0) (= (p r11 l3) 0) (= (p r11 l4) 0) (= (p r11 l5) 0) (= (p r11 l6) 0) (= (p r11 l7) 0) (= (p r11 l8) 0) (= (p r11 l9) 0) (= (p r11 l10) 0) (= (p r11 l11) 0) (= (p r11 l12) 0) (= (p r11 l13) 0) (= (p r11 l14) 0) (= (p r11 l15) 0) (= (p r11 l16) 0) (= (p r11 l17) 0) (= (p r11 l18) 0) (= (p r11 l19) 0) (= (p r11 l20) 0) (= (p r11 l21) 0) (= (p r11 l22) 0) (= (p r11 l23) 0) (= (p r12 l0) 0) (= (p r12 l1) 0) (= (p r12 l2) 0) (= (p r12 l3) 0) (= (p r12 l4) 0) (= (p r12 l5) 0) (= (p r12 l6) 0) (= (p r12 l7) 0) (= (p r12 l8) 0) (= (p r12 l9) 0) (= (p r12 l10) 0) (= (p r12 l11) 0) (= (p r12 l12) 0) (= (p r12 l13) 0) (= (p r12 l14) 0) (= (p r12 l15) 0) (= (p r12 l16) 0) (= (p r12 l17) 0) (= (p r12 l18) 0) (= (p r12 l19) 0) (= (p r12 l20) 0) (= (p r12 l21) 0) (= (p r12 l22) 0) (= (p r12 l23) 0) (= (p r13 l0) 0) (= (p r13 l1) 0) (= (p r13 l2) 0) (= (p r13 l3) 0) (= (p r13 l4) 0) (= (p r13 l5) 0) (= (p r13 l6) 0) (= (p r13 l7) 0) (= (p r13 l8) 0) (= (p r13 l9) 0) (= (p r13 l10) 0) (= (p r13 l11) 0) (= (p r13 l12) 0) (= (p r13 l13) 0) (= (p r13 l14) 0) (= (p r13 l15) 0) (= (p r13 l16) 0) (= (p r13 l17) 0) (= (p r13 l18) 0) (= (p r13 l19) 0) (= (p r13 l20) 0) (= (p r13 l21) 0) (= (p r13 l22) 0) (= (p r13 l23) 0) (= (p r14 l0) 0) (= (p r14 l1) 0) (= (p r14 l2) 0) (= (p r14 l3) 0) (= (p r14 l4) 0) (= (p r14 l5) 0) (= (p r14 l6) 0) (= (p r14 l7) 0) (= (p r14 l8) 0) (= (p r14 l9) 0) (= (p r14 l10) 0) (= (p r14 l11) 0) (= (p r14 l12) 0) (= (p r14 l13) 0) (= (p r14 l14) 0) (= (p r14 l15) 0) (= (p r14 l16) 0) (= (p r14 l17) 0) (= (p r14 l18) 0) (= (p r14 l19) 0) (= (p r14 l20) 0) (= (p r14 l21) 0) (= (p r14 l22) 0) (= (p r14 l23) 0) (= (p r15 l0) 0) (= (p r15 l1) 0) (= (p r15 l2) 0) (= (p r15 l3) 0) (= (p r15 l4) 0) (= (p r15 l5) 0) (= (p r15 l6) 0) (= (p r15 l7) 0) (= (p r15 l8) 0) (= (p r15 l9) 0) (= (p r15 l10) 0) (= (p r15 l11) 0) (= (p r15 l12) 0) (= (p r15 l13) 0) (= (p r15 l14) 0) (= (p r15 l15) 0) (= (p r15 l16) 0) (= (p r15 l17) 0) (= (p r15 l18) 0) (= (p r15 l19) 0) (= (p r15 l20) 0) (= (p r15 l21) 0) (= (p r15 l22) 0) (= (p r15 l23) 0) (= (p r16 l0) 0) (= (p r16 l1) 0) (= (p r16 l2) 0) (= (p r16 l3) 0) (= (p r16 l4) 0) (= (p r16 l5) 0) (= (p r16 l6) 0) (= (p r16 l7) 0) (= (p r16 l8) 0) (= (p r16 l9) 0) (= (p r16 l10) 0) (= (p r16 l11) 0) (= (p r16 l12) 0) (= (p r16 l13) 0) (= (p r16 l14) 0) (= (p r16 l15) 0) (= (p r16 l16) 0) (= (p r16 l17) 0) (= (p r16 l18) 0) (= (p r16 l19) 0) (= (p r16 l20) 0) (= (p r16 l21) 0) (= (p r16 l22) 0) (= (p r16 l23) 0) (= (p r17 l0) 0) (= (p r17 l1) 0) (= (p r17 l2) 0) (= (p r17 l3) 0) (= (p r17 l4) 0) (= (p r17 l5) 0) (= (p r17 l6) 0) (= (p r17 l7) 0) (= (p r17 l8) 0) (= (p r17 l9) 0) (= (p r17 l10) 0) (= (p r17 l11) 0) (= (p r17 l12) 0) (= (p r17 l13) 0) (= (p r17 l14) 0) (= (p r17 l15) 0) (= (p r17 l16) 0) (= (p r17 l17) 0) (= (p r17 l18) 0) (= (p r17 l19) 0) (= (p r17 l20) 0) (= (p r17 l21) 0) (= (p r17 l22) 0) (= (p r17 l23) 0) (= (p r18 l0) 0) (= (p r18 l1) 0) (= (p r18 l2) 0) (= (p r18 l3) 0) (= (p r18 l4) 0) (= (p r18 l5) 0) (= (p r18 l6) 0) (= (p r18 l7) 0) (= (p r18 l8) 0) (= (p r18 l9) 0) (= (p r18 l10) 0) (= (p r18 l11) 0) (= (p r18 l12) 0) (= (p r18 l13) 0) (= (p r18 l14) 0) (= (p r18 l15) 0) (= (p r18 l16) 0) (= (p r18 l17) 0) (= (p r18 l18) 0) (= (p r18 l19) 0) (= (p r18 l20) 0) (= (p r18 l21) 0) (= (p r18 l22) 0) (= (p r18 l23) 0) (= (p r19 l0) 0) (= (p r19 l1) 0) (= (p r19 l2) 0) (= (p r19 l3) 0) (= (p r19 l4) 0) (= (p r19 l5) 0) (= (p r19 l6) 0) (= (p r19 l7) 0) (= (p r19 l8) 0) (= (p r19 l9) 0) (= (p r19 l10) 0) (= (p r19 l11) 0) (= (p r19 l12) 0) (= (p r19 l13) 0) (= (p r19 l14) 0) (= (p r19 l15) 0) (= (p r19 l16) 0) (= (p r19 l17) 0) (= (p r19 l18) 0) (= (p r19 l19) 0) (= (p r19 l20) 0) (= (p r19 l21) 0) (= (p r19 l22) 0) (= (p r19 l23) 0) (= (p r20 l0) 0) (= (p r20 l1) 0) (= (p r20 l2) 0) (= (p r20 l3) 0) (= (p r20 l4) 0) (= (p r20 l5) 0) (= (p r20 l6) 0) (= (p r20 l7) 0) (= (p r20 l8) 0) (= (p r20 l9) 0) (= (p r20 l10) 0) (= (p r20 l11) 0) (= (p r20 l12) 0) (= (p r20 l13) 0) (= (p r20 l14) 0) (= (p r20 l15) 0) (= (p r20 l16) 0) (= (p r20 l17) 0) (= (p r20 l18) 0) (= (p r20 l19) 0) (= (p r20 l20) 0) (= (p r20 l21) 0) (= (p r20 l22) 0) (= (p r20 l23) 0) (= (p r21 l0) 0) (= (p r21 l1) 0) (= (p r21 l2) 0) (= (p r21 l3) 0) (= (p r21 l4) 0) (= (p r21 l5) 0) (= (p r21 l6) 0) (= (p r21 l7) 0) (= (p r21 l8) 0) (= (p r21 l9) 0) (= (p r21 l10) 0) (= (p r21 l11) 0) (= (p r21 l12) 0) (= (p r21 l13) 0) (= (p r21 l14) 0) (= (p r21 l15) 0) (= (p r21 l16) 0) (= (p r21 l17) 0) (= (p r21 l18) 0) (= (p r21 l19) 0) (= (p r21 l20) 0) (= (p r21 l21) 0) (= (p r21 l22) 0) (= (p r21 l23) 0) (= (p r22 l0) 0) (= (p r22 l1) 0) (= (p r22 l2) 0) (= (p r22 l3) 0) (= (p r22 l4) 0) (= (p r22 l5) 0) (= (p r22 l6) 0) (= (p r22 l7) 0) (= (p r22 l8) 0) (= (p r22 l9) 0) (= (p r22 l10) 0) (= (p r22 l11) 0) (= (p r22 l12) 0) (= (p r22 l13) 0) (= (p r22 l14) 0) (= (p r22 l15) 0) (= (p r22 l16) 0) (= (p r22 l17) 0) (= (p r22 l18) 0) (= (p r22 l19) 0) (= (p r22 l20) 0) (= (p r22 l21) 0) (= (p r22 l22) 0) (= (p r22 l23) 0) (= (p r23 l0) 0) (= (p r23 l1) 0) (= (p r23 l2) 0) (= (p r23 l3) 0) (= (p r23 l4) 0) (= (p r23 l5) 0) (= (p r23 l6) 0) (= (p r23 l7) 0) (= (p r23 l8) 0) (= (p r23 l9) 0) (= (p r23 l10) 0) (= (p r23 l11) 0) (= (p r23 l12) 0) (= (p r23 l13) 0) (= (p r23 l14) 0) (= (p r23 l15) 0) (= (p r23 l16) 0) (= (p r23 l17) 0) (= (p r23 l18) 0) (= (p r23 l19) 0) (= (p r23 l20) 0) (= (p r23 l21) 0) (= (p r23 l22) 0) (= (p r23 l23) 0)
                (= (h r0) 5) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0) (= (h r10) 0) (= (h r11) 0) (= (h r12) 0) (= (h r13) 0) (= (h r14) 0) (= (h r15) 0) (= (h r16) 0) (= (h r17) 0) (= (h r18) 0) (= (h r19) 0) (= (h r20) 0) (= (h r21) 0) (= (h r22) 0) (= (h r23) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r0 l2) (psd r0 l3) (psd r0 l4) (psd r0 l5) (psd r0 l6) (psd r0 l7) (psd r0 l8) (psd r0 l9) (psd r0 l10) (psd r0 l11) (psd r0 l12) (psd r0 l13) (psd r0 l14) (psd r0 l15) (psd r0 l16) (psd r0 l17) (psd r0 l18) (psd r0 l19) (psd r0 l20) (psd r0 l21) (psd r0 l22) (psd r0 l23) (psd r1 l0) (psd r1 l1) (psd r1 l2) (psd r1 l3) (psd r1 l4) (psd r1 l5) (psd r1 l6) (psd r1 l7) (psd r1 l8) (psd r1 l9) (psd r1 l10) (psd r1 l11) (psd r1 l12) (psd r1 l13) (psd r1 l14) (psd r1 l15) (psd r1 l16) (psd r1 l17) (psd r1 l18) (psd r1 l19) (psd r1 l20) (psd r1 l21) (psd r1 l22) (psd r1 l23) (psd r2 l0) (psd r2 l1) (psd r2 l2) (psd r2 l3) (psd r2 l4) (psd r2 l5) (psd r2 l6) (psd r2 l7) (psd r2 l8) (psd r2 l9) (psd r2 l10) (psd r2 l11) (psd r2 l12) (psd r2 l13) (psd r2 l14) (psd r2 l15) (psd r2 l16) (psd r2 l17) (psd r2 l18) (psd r2 l19) (psd r2 l20) (psd r2 l21) (psd r2 l22) (psd r2 l23) (psd r3 l0) (psd r3 l1) (psd r3 l2) (psd r3 l3) (psd r3 l4) (psd r3 l5) (psd r3 l6) (psd r3 l7) (psd r3 l8) (psd r3 l9) (psd r3 l10) (psd r3 l11) (psd r3 l12) (psd r3 l13) (psd r3 l14) (psd r3 l15) (psd r3 l16) (psd r3 l17) (psd r3 l18) (psd r3 l19) (psd r3 l20) (psd r3 l21) (psd r3 l22) (psd r3 l23) (psd r4 l0) (psd r4 l1) (psd r4 l2) (psd r4 l3) (psd r4 l4) (psd r4 l5) (psd r4 l6) (psd r4 l7) (psd r4 l8) (psd r4 l9) (psd r4 l10) (psd r4 l11) (psd r4 l12) (psd r4 l13) (psd r4 l14) (psd r4 l15) (psd r4 l16) (psd r4 l17) (psd r4 l18) (psd r4 l19) (psd r4 l20) (psd r4 l21) (psd r4 l22) (psd r4 l23) (psd r5 l0) (psd r5 l1) (psd r5 l2) (psd r5 l3) (psd r5 l4) (psd r5 l5) (psd r5 l6) (psd r5 l7) (psd r5 l8) (psd r5 l9) (psd r5 l10) (psd r5 l11) (psd r5 l12) (psd r5 l13) (psd r5 l14) (psd r5 l15) (psd r5 l16) (psd r5 l17) (psd r5 l18) (psd r5 l19) (psd r5 l20) (psd r5 l21) (psd r5 l22) (psd r5 l23) (psd r6 l0) (psd r6 l1) (psd r6 l2) (psd r6 l3) (psd r6 l4) (psd r6 l5) (psd r6 l6) (psd r6 l7) (psd r6 l8) (psd r6 l9) (psd r6 l10) (psd r6 l11) (psd r6 l12) (psd r6 l13) (psd r6 l14) (psd r6 l15) (psd r6 l16) (psd r6 l17) (psd r6 l18) (psd r6 l19) (psd r6 l20) (psd r6 l21) (psd r6 l22) (psd r6 l23) (psd r7 l0) (psd r7 l1) (psd r7 l2) (psd r7 l3) (psd r7 l4) (psd r7 l5) (psd r7 l6) (psd r7 l7) (psd r7 l8) (psd r7 l9) (psd r7 l10) (psd r7 l11) (psd r7 l12) (psd r7 l13) (psd r7 l14) (psd r7 l15) (psd r7 l16) (psd r7 l17) (psd r7 l18) (psd r7 l19) (psd r7 l20) (psd r7 l21) (psd r7 l22) (psd r7 l23) (psd r8 l0) (psd r8 l1) (psd r8 l2) (psd r8 l3) (psd r8 l4) (psd r8 l5) (psd r8 l6) (psd r8 l7) (psd r8 l8) (psd r8 l9) (psd r8 l10) (psd r8 l11) (psd r8 l12) (psd r8 l13) (psd r8 l14) (psd r8 l15) (psd r8 l16) (psd r8 l17) (psd r8 l18) (psd r8 l19) (psd r8 l20) (psd r8 l21) (psd r8 l22) (psd r8 l23) (psd r9 l0) (psd r9 l1) (psd r9 l2) (psd r9 l3) (psd r9 l4) (psd r9 l5) (psd r9 l6) (psd r9 l7) (psd r9 l8) (psd r9 l9) (psd r9 l10) (psd r9 l11) (psd r9 l12) (psd r9 l13) (psd r9 l14) (psd r9 l15) (psd r9 l16) (psd r9 l17) (psd r9 l18) (psd r9 l19) (psd r9 l20) (psd r9 l21) (psd r9 l22) (psd r9 l23) (psd r10 l0) (psd r10 l1) (psd r10 l2) (psd r10 l3) (psd r10 l4) (psd r10 l5) (psd r10 l6) (psd r10 l7) (psd r10 l8) (psd r10 l9) (psd r10 l10) (psd r10 l11) (psd r10 l12) (psd r10 l13) (psd r10 l14) (psd r10 l15) (psd r10 l16) (psd r10 l17) (psd r10 l18) (psd r10 l19) (psd r10 l20) (psd r10 l21) (psd r10 l22) (psd r10 l23) (psd r11 l0) (psd r11 l1) (psd r11 l2) (psd r11 l3) (psd r11 l4) (psd r11 l5) (psd r11 l6) (psd r11 l7) (psd r11 l8) (psd r11 l9) (psd r11 l10) (psd r11 l11) (psd r11 l12) (psd r11 l13) (psd r11 l14) (psd r11 l15) (psd r11 l16) (psd r11 l17) (psd r11 l18) (psd r11 l19) (psd r11 l20) (psd r11 l21) (psd r11 l22) (psd r11 l23) (psd r12 l0) (psd r12 l1) (psd r12 l2) (psd r12 l3) (psd r12 l4) (psd r12 l5) (psd r12 l6) (psd r12 l7) (psd r12 l8) (psd r12 l9) (psd r12 l10) (psd r12 l11) (psd r12 l12) (psd r12 l13) (psd r12 l14) (psd r12 l15) (psd r12 l16) (psd r12 l17) (psd r12 l18) (psd r12 l19) (psd r12 l20) (psd r12 l21) (psd r12 l22) (psd r12 l23) (psd r13 l0) (psd r13 l1) (psd r13 l2) (psd r13 l3) (psd r13 l4) (psd r13 l5) (psd r13 l6) (psd r13 l7) (psd r13 l8) (psd r13 l9) (psd r13 l10) (psd r13 l11) (psd r13 l12) (psd r13 l13) (psd r13 l14) (psd r13 l15) (psd r13 l16) (psd r13 l17) (psd r13 l18) (psd r13 l19) (psd r13 l20) (psd r13 l21) (psd r13 l22) (psd r13 l23) (psd r14 l0) (psd r14 l1) (psd r14 l2) (psd r14 l3) (psd r14 l4) (psd r14 l5) (psd r14 l6) (psd r14 l7) (psd r14 l8) (psd r14 l9) (psd r14 l10) (psd r14 l11) (psd r14 l12) (psd r14 l13) (psd r14 l14) (psd r14 l15) (psd r14 l16) (psd r14 l17) (psd r14 l18) (psd r14 l19) (psd r14 l20) (psd r14 l21) (psd r14 l22) (psd r14 l23) (psd r15 l0) (psd r15 l1) (psd r15 l2) (psd r15 l3) (psd r15 l4) (psd r15 l5) (psd r15 l6) (psd r15 l7) (psd r15 l8) (psd r15 l9) (psd r15 l10) (psd r15 l11) (psd r15 l12) (psd r15 l13) (psd r15 l14) (psd r15 l15) (psd r15 l16) (psd r15 l17) (psd r15 l18) (psd r15 l19) (psd r15 l20) (psd r15 l21) (psd r15 l22) (psd r15 l23) (psd r16 l0) (psd r16 l1) (psd r16 l2) (psd r16 l3) (psd r16 l4) (psd r16 l5) (psd r16 l6) (psd r16 l7) (psd r16 l8) (psd r16 l9) (psd r16 l10) (psd r16 l11) (psd r16 l12) (psd r16 l13) (psd r16 l14) (psd r16 l15) (psd r16 l16) (psd r16 l17) (psd r16 l18) (psd r16 l19) (psd r16 l20) (psd r16 l21) (psd r16 l22) (psd r16 l23) (psd r17 l0) (psd r17 l1) (psd r17 l2) (psd r17 l3) (psd r17 l4) (psd r17 l5) (psd r17 l6) (psd r17 l7) (psd r17 l8) (psd r17 l9) (psd r17 l10) (psd r17 l11) (psd r17 l12) (psd r17 l13) (psd r17 l14) (psd r17 l15) (psd r17 l16) (psd r17 l17) (psd r17 l18) (psd r17 l19) (psd r17 l20) (psd r17 l21) (psd r17 l22) (psd r17 l23) (psd r18 l0) (psd r18 l1) (psd r18 l2) (psd r18 l3) (psd r18 l4) (psd r18 l5) (psd r18 l6) (psd r18 l7) (psd r18 l8) (psd r18 l9) (psd r18 l10) (psd r18 l11) (psd r18 l12) (psd r18 l13) (psd r18 l14) (psd r18 l15) (psd r18 l16) (psd r18 l17) (psd r18 l18) (psd r18 l19) (psd r18 l20) (psd r18 l21) (psd r18 l22) (psd r18 l23) (psd r19 l0) (psd r19 l1) (psd r19 l2) (psd r19 l3) (psd r19 l4) (psd r19 l5) (psd r19 l6) (psd r19 l7) (psd r19 l8) (psd r19 l9) (psd r19 l10) (psd r19 l11) (psd r19 l12) (psd r19 l13) (psd r19 l14) (psd r19 l15) (psd r19 l16) (psd r19 l17) (psd r19 l18) (psd r19 l19) (psd r19 l20) (psd r19 l21) (psd r19 l22) (psd r19 l23) (psd r20 l0) (psd r20 l1) (psd r20 l2) (psd r20 l3) (psd r20 l4) (psd r20 l5) (psd r20 l6) (psd r20 l7) (psd r20 l8) (psd r20 l9) (psd r20 l10) (psd r20 l11) (psd r20 l12) (psd r20 l13) (psd r20 l14) (psd r20 l15) (psd r20 l16) (psd r20 l17) (psd r20 l18) (psd r20 l19) (psd r20 l20) (psd r20 l21) (psd r20 l22) (psd r20 l23) (psd r21 l0) (psd r21 l1) (psd r21 l2) (psd r21 l3) (psd r21 l4) (psd r21 l5) (psd r21 l6) (psd r21 l7) (psd r21 l8) (psd r21 l9) (psd r21 l10) (psd r21 l11) (psd r21 l12) (psd r21 l13) (psd r21 l14) (psd r21 l15) (psd r21 l16) (psd r21 l17) (psd r21 l18) (psd r21 l19) (psd r21 l20) (psd r21 l21) (psd r21 l22) (psd r21 l23) (psd r22 l0) (psd r22 l1) (psd r22 l2) (psd r22 l3) (psd r22 l4) (psd r22 l5) (psd r22 l6) (psd r22 l7) (psd r22 l8) (psd r22 l9) (psd r22 l10) (psd r22 l11) (psd r22 l12) (psd r22 l13) (psd r22 l14) (psd r22 l15) (psd r22 l16) (psd r22 l17) (psd r22 l18) (psd r22 l19) (psd r22 l20) (psd r22 l21) (psd r22 l22) (psd r22 l23) (psd r23 l0) (psd r23 l1) (psd r23 l2) (psd r23 l3) (psd r23 l4) (psd r23 l5) (psd r23 l6) (psd r23 l7) (psd r23 l8) (psd r23 l9) (psd r23 l10) (psd r23 l11) (psd r23 l12) (psd r23 l13) (psd r23 l14) (psd r23 l15) (psd r23 l16) (psd r23 l17) (psd r23 l18) (psd r23 l19) (psd r23 l20) (psd r23 l21) (psd r23 l22) (psd r23 l23)
                    (= (h r0) 5)
                )
            )
        )