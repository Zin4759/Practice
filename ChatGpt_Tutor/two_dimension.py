'''
public class TwoDArraySum {
    public static void main(String[] args) {
        int[][] arr = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                sum += arr[i][j];
            }
        }

        System.out.println("2차원 배열 요소의 합: " + sum);
    }
}
를 파이썬으로 변환하시오

제출한 답
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
n = len(arr)
for i in range(n):
for j in range(len(arr[i]):
sum = sum + arr[i][j]

print("sum of 2 dimenssion element :"+str(sum))

채점 : for문에서 괄호가 하나 빠졌고, 출력 문자열을 수정하길 권함.
'''

# 수정된 코드
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
n = len(arr)
for i in range(n):
    for j in range(len(arr[i])):
        sum += arr[i][j]

print("2차원 배열 요소의 합: " + str(sum))

# 잘 작동함