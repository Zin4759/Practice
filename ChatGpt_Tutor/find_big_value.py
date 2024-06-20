# Write your code here :-)
'''
public class MaxValue {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        System.out.println("배열의 최대값: " + max);
    }
}
를 파이썬으로 변환하시오.
'''

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
max = arr[0]

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print("Most big value is" + str(max))
