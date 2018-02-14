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

(define (ordenamiento-interno lista)
  (
    (lambda (primero resto)
      (if (null? resto)
          lista
          (
            (lambda (cd)
              (let ((ca2 (car cd)) (cd2 (cdr cd)))
                (if (>= primero ca2)
                    (cons primero cd)
                    (cons ca2 (cons primero cd2))
                    )
              )
            )(ordenamiento-interno resto)
          )
          
      )
    )(car lista)(cdr lista)
  )
  
)

(define (ordenamiento-burbuja lista)
  (if (null? lista)
      '()
      (
        (lambda (lo)
          (cons (car lo) (ordenamiento-burbuja (cdr lo)))
        )(ordenamiento-interno lista)
      )
  )
)

(define (burbuja string1)
  (ordenamiento-burbuja (leer-archivo string1))
)

;multiplicacion con asignacion
(let ((x 2) (y 3))
  (* x y)
)

;multiplicacion con lambda
((lambda (x y)
  (* x y)
) 2 3)