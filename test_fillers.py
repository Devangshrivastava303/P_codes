import cupy as cp

cuda_kernel = cp.RawKernel(r'''
extern "C" __global__
void matrix_add(const float* A, const float* B, float* C, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) {
        C[idx] = A[idx] + B[idx];
    }
}
''', 'matrix_add')

def run():
    N = 1 << 20  # 1 million elements

    A = cp.random.random(N, dtype=cp.float32)
    B = cp.random.random(N, dtype=cp.float32)
    C = cp.zeros(N, dtype=cp.float32)

    threads_per_block = 256
    blocks = (N + threads_per_block - 1) // threads_per_block

    cuda_kernel((blocks,), (threads_per_block,), (A, B, C, N))
    cp.cuda.Stream.null.synchronize()

    print("Kernel ran successfully!")
    print("Result sample:", C[:5])

if __name__ == "__main__":
    run()