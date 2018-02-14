#lang racket

(define (leer-archivo archivo)
 (call-with-input-file archivo
   (lambda (p)
     (let f ((x (read p)))
       (if (eof-object? x)
           '()
           (cons x (f (read p)))
       )
     )
   )
 )
)

(define (guardar-archivo string2 lista)
  (call-with-output-file string2
    (lambda (p)
      (let f ((ls lista))
        (if (not (null? ls))
          (begin
            (write (car ls) p)
            (newline p)
            (f (cdr ls))
          )
          null
        )
      )
    )
  )
)

(define (ordenamiento-interno operador lista)
  (
    (lambda (primero resto)
      (if (null? resto)
          lista
          (
            (lambda (resto-menos-uno)
              (
                (lambda (segundo resto-menos-dos)
                  (if (operador primero segundo)
                      (cons primero resto-menos-uno)
                      (cons segundo (cons primero resto-menos-dos))
                  )
                )(car resto-menos-uno)(cdr resto-menos-uno)  
              )
            )(ordenamiento-interno operador resto)
          )   
      )
    )(car lista)(cdr lista)
  )
  
)

(define (ordenamiento-burbuja operador lista)
  (if (null? lista)
      '()
      (
        (lambda (lo)
          (cons (car lo) (ordenamiento-burbuja operador (cdr lo)))
        )(ordenamiento-interno operador lista)
      )
  )
)

(define (burbuja operador string1 string2)
  (guardar-archivo string2 (ordenamiento-burbuja operador (leer-archivo string1)))
)

;multiplicacion con asignacion
(let ((x 2) (y 3))
  (* x y)
)

;multiplicacion con lambda
((lambda (x y)
  (* x y)
) 2 3)