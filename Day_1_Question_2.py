def count_k_divisible_pairs(arr, k):
  count = 0
  remainder_count = {0: 1} 

  for num in arr:
    remainder = num % k
    count += remainder_count.get(k - remainder, 0) 
    remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

  return count

arr = [1, 3, 2, 6, 1, 2]
k = 3
result = count_k_divisible_pairs(arr, k)
print(f"Number of (i, j) pairs with sum divisible by {k}: {result}")

