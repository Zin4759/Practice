'''
문제
public class ArraySum {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        System.out.println("배열 요소의 합: " + sum);
    }
}
를 python으로 변환하시오
'''

arr = [1, 2, 3, 4, 5]
sum = 0
n = len(arr)

for i in range(n):
    sum = sum + arr[i]

print("result is"+str(sum))

# 10 / 10