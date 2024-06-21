'''
# Question
public class MinValue {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        int min = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }

        System.out.println("배열의 최소값: " + min);
    }
}
'''

arr = [64, 34, 25, 12, 22, 11, 90]
min = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] < min:
        min = arr[i]

print("배열의 최소값: " + str(min))

'''
제출하신 코드는 정확히 변환되었습니다. Java 코드를 Python으로 변환하는 과정에서 모든 부분이 정확하게 구현되었습니다.

평가:
최소값 초기화: 정확히 구현됨.
최소값 계산: 정확히 구현됨.
출력 형식: 정확히 구현됨.
'''
