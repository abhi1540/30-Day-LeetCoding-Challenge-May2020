    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        tot_sum = A[0]
        max_cur = max_global = A[0]
        min_cur = min_global = A[0]
        for i in range(1, len(A)):
            #print(i, A[i])
            tot_sum += A[i]
            min_cur = min(A[i], min_cur + A[i])
            max_cur = max(A[i], max_cur + A[i])
            #print(max_cur, A[i],  max_cur + A[i])
            if max_cur > max_global:
                max_global = max_cur
            if min_cur < min_global:
                min_global = min_cur
        #print(tot_sum, max_global, min_global)
        if tot_sum != min_global:
            return max(max_global, (tot_sum - min_global))
        return max_global