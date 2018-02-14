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

(define (bubble-sort-inner lista)
  (let ((ca1 (car lista)) (cd1 (cdr lista)))
    (if (null? cd1)
        lista 
        (let ((cd (bubble-sort-inner cd1))) 
          (let ((ca2 (car cd)) (cd2 (cdr cd)))
            (if (<= ca1 ca2)
                (cons ca1 cd)
                (cons ca2 (cons ca1 cd2))
            )
          )
        )
     )
  )
)

(define (ordenamiento-burbuja lista)
  (if (null? lista)
      '()
      (
        (lambda (lo)
          (cons (car lo) (ordenamiento-burbuja (cdr lo)))
        ) (bubble-sort-inner lista)
      )
      ;(let ((s (bubble-sort-inner lista)))
      ;  (cons (car s) (ordenamiento-burbuja (cdr s)))
      ;)
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