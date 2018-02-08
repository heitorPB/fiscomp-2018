program powerEigenStuff
        implicit none
        integer, parameter :: dp = kind(0.d0)

        integer :: n                                            ! matrix size
        integer, parameter :: max_iter = 1000                   ! maximum number of iterations
        integer :: i

        real (kind = dp), allocatable, dimension(:,:) :: A      ! matrix to get eigenstuff
        real (kind = dp), allocatable, dimension(:)   :: x_k, x_k1 ! eigenvectors
        real (kind = dp) :: lambda                              ! eigenvalue
        real (kind = dp), parameter :: prec = 1d-6              ! desired precision
        real (kind = dp) :: diff = 666

        open(unit = 10, file = "matrix3.txt")

        ! read matrix size, allocate matrix, read matrix
        read(10, *) n
        allocate(A(n,n))
        read(10, *) A
        !print *, n
        !print *, A
        close(10)       ! we don't need the file anymore

        allocate(x_k(n), x_k1(n))
        ! initial guess: x0 = (1, 1, 1, ..., 1)
        x_k = 1d0

        lambda = 0d0
        i = 0
        do while (abs(diff) > prec .and. i < max_iter)
                ! x_k1 = A x_k
                x_k1 = matmul(A, x_k)
                ! normalize x_k1 and atribute it to x_k
                x_k  = x_k1 / dsqrt(dot_product(x_k1, x_k1))

                diff = lambda - dot_product(x_k, matmul(A, x_k))
                lambda = dot_product(x_k, matmul(A, x_k))

                i = i + 1
        end do

        print *, lambda
        print *, x_k
        deallocate(A, x_k, x_k1)
end program powerEigenStuff