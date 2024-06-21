'''
# Question
public class AverageValue {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        double average = (double) sum / arr.length;
        System.out.println("배열 요소의 평균값: " + average);
    }
}
'''

#  제출된 내용
arr = [10, 20, 30, 40, 50]
sum = 0
n = len(arr)

for i in range(n):
    sum += arr[i]

average = sum / n
print("배열 요소의 평균값: " + str(average))

'''
평가:
배열의 합 계산: 정확히 구현됨.
평균 계산: 정확히 구현됨.
출력 형식: 정확히 구현됨.
'''
