def main():
  N = int(input("Введіть бажаний розмір матриці: "))
  A = [[0] * N for _ in range(N)]
  sum_val = 0
  positive_count = 0
  print("Введіть елементи матриці {}x{}:".format(N, N))
  for i in range(N):
      row_input = input().split() 
      for j in range(N):
          A[i][j] = int(row_input[j])  
          if i < j and A[i][j] > 0:
              sum_val += A[i][j]
              positive_count += 1
  print("Сума додатніх елементів над головною діагоналлю:", sum_val)
  print("Кількість додатніх елементів над головною діагоналлю:", positive_count)
if __name__ == "__main__":
  main()
