'''
public class ReverseArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
    }
}
를 파이썬으로 변환하시오


# my answer -> need a little bit edit
arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n-1, 0, -1):
    print(arr[i])
'''

# edited code
arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n-1, -1, -1):
    print(arr[i])
