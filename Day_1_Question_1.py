def count_candy_segments(candy_bar, birth_month, birth_day):
  count = 0
  for i in range(len(candy_bar) - birth_month + 1):  
    segment_sum = sum(candy_bar[i:i + birth_month]) 
    if segment_sum == birth_day:
      count += 1
  return count
