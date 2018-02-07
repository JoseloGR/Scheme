#lang racket

(define (un-nuevo-mes d m y)
  (write '1)
  (write '-)
  (write (+ m 1))
  (write '-)
  (write (+ y 0))
)

(define (feliz-anio-nuevo d m y)
  (write '1)
  (write '-)
  (write '1)
  (write '-)
  (write (+ y 1))
)

(define (un-nuevo-dia d m y)
  (write (+ d 1))
  (write '-)
  (write (+ m 0))
  (write '-)
  (write (+ y 0))
)

(define (busqueda-mes m)
  (case m
    [(1 3 5 7 8 10) 1]
    [(4 6 9 11) 2]
    [(2) 3]
  )
)

(define (es-bisiesto? y)
    (if (or (and (eq? (modulo y 4) 0) (eq? (modulo y 100) 0)) (eq? (modulo y 400) 0))
        1
        0
    )
)

(define (fecha-no-valida)
  '(No te puedo ayudar con esta fecha escribe una nueva fecha por favor)
)

(define (dia-siguiente d m y)
  (cond
    ( (and (eq? (busqueda-mes m) 1) (eq? d 31)) (un-nuevo-mes d m y) )
    ( (and (eq? (busqueda-mes m) 2) (eq? d 30)) (un-nuevo-mes d m y) )
    ( (and (eq? (busqueda-mes m) 3) (eq? (es-bisiesto? m) 1) (eq? d 29)) (un-nuevo-mes d m y) )
    ( (and (eq? (busqueda-mes m) 3) (eq? (es-bisiesto? m) 0) (eq? d 28)) (un-nuevo-mes d m y) )
    ( (and (eq? m 12) (eq? d 31)) (feliz-anio-nuevo d m y) )
    ( (and (> d 0) (< d 32)) (un-nuevo-dia d m y) )
    ( (fecha-no-valida))
  )
)