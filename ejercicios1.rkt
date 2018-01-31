#lang racket

(define (comparar a b c)
  (if (< (/ (+ a b c) 3.0) 70.0) "reprobado" "aprobado" )
)

(define (es-bisiesto? a)
    (if (and (= (modulo a 4) 0) (= (modulo a 100) 0) (= (modulo a 400) 0))
        "Si es bisiesto"
        "No lo es"
    )
)

(define (quien-es-mayor? a b c)
  (if (> a b)
      (if (> a c) "A es mayor" "C es mayor")
      (if (> b c) "B es mayor" "C es mayor ")
  )
)

(define (selecciona a)
  (case a
    [(0 2 4 6 8) "es digito par"]
  )
)

(define (ordena3 n1 n2 n3)
  (if (> n1 n2)
      (if (> n1 n3)
          (if (> n2 n3)
              (list n1 n2 n3)
              (list n1 n3 n2)
          )
          (list n3 n1 n2)
      )
      (if (> n2 n3)
          (if (> n1 n3)
              (list n2 n1 n3)
              (list n2 n3 n1)
          )
          (list n3 n2 n1)
      )
  )
)

(define (opera-funcion-string s a b)
  (case s
    [("resta") (- a b)]
    [("suma") (+ a b)]
    [("multiplica") (* a b)]
    [("divide") (/ a b)]
  )
)

(define (cuantos-dias-tiene? a)
  (case a
    [(1 3 5 7 8 10 12) 31]
    [(4 6 9 11) 30]
    [(2) 28]
  )
)

(define (evalua-fx x)
  (cond
    [(< x -1)(+ x 2)]
    [(and(<= x -1)(< x 0)) (1)]
    [(>= x 0)(+(* (* x x) -1) 1)]
  )
)

(define (nombra)
  (let
      ((x1 (+ 2 3)))
    (+ x1 6)
  )
)

(define (nombra-dos)
  (let*
      ((x1 (+ 2 3))
       (x2 (+ 2 2))
      )
    (+ x1 x2)
  )
)

(define (opera f a b)
  (f a b)
)

(define (mult a b)
  (write (list a b))
  (if (= a 0)
      0
      (+ b (mult (- a 1) b))
  )
)