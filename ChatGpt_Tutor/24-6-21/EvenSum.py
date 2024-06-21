# Write your code here :-)
'''
public class EvenSum {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 0) {
                sum += arr[i];
            }
        }

        System.out.println("짝수의 합: " + sum);
    }
}
을 변환하시오

# 제출한거
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
n = len(arr)

for i in range(n):
    if arr[i] % 2 == 0:
        sum += arr[i]

print("짝수의 합: "+sum)
'''

#  수정된 코드 : str(sum)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
n = len(arr)

for i in range(n):
    if arr[i] % 2 == 0:
        sum += arr[i]

print("짝수의 합: "+str(sum))