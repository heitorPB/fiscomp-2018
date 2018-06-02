program power
        implicit none
        integer, parameter :: dp = kind(0.d0)

        integer :: n    ! matrix size
        integer :: i, j

        real (kind = dp), allocatable, dimension(:,:) :: A, B   ! matrix


        ! read matrix size, allocate matrix, read matrix
        read(*, *) n
        allocate(A(n,n), B(n,n))

        read(*, *) A
        do i = 1, n
                print *, (A(i, j), j = 1, n)
        end do

        do i = 1, n
                read(*, *) (B(i, j), j = 1, n)
        end do
        do i = 1, n
                print *, (B(i, j), j = 1, n)
        end do

        deallocate(A, B)
end program power