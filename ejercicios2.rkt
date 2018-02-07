#lang racket

(define (suma-lista b)
  (if (null? b)
      0
      (+ (car b) (suma-lista (cdr b)))
  )
)

(define (operador-lista f i lista)
  (if (null? lista)
      i
      (f (car lista) (operador-lista f i (cdr lista)))
  )
)

(define (lista-reversa lista)
  (if (null? lista)
      lista
      (append (lista-reversa (cdr lista)) (list(car lista)))
  )
)

(foldl + 0 '(1 2 3 4))

(define (fact n)
  (if (= n 0)
      1
      (* n (fact(- n 1)))
  )
)

(define (ofile archivo)
  (leer-archivo (open-input-file archivo))
)

(define (leer-archivo archivo)
  (if (eof-object? archivo)
      '()
      (read-line archivo)
  )
)

(define out (open-output-file "numeros.txt") )