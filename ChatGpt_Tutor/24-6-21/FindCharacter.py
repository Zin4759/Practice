'''
public class FindCharacter {
    public static void main(String[] args) {
        String[] arr = {"apple", "banana", "cherry", "date"};
        char target = 'a';
        boolean found = false;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i].indexOf(target) != -1) {
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println("문자 " + target + "가 배열에 있습니다.");
        } else {
            System.out.println("문자 " + target + "가 배열에 없습니다.");
        }
    }
} 를 변환하시오.

# 제출했던 코드 : 2점 만점에 1점
arr = ["apple", "banana", "cherry", "date"]
target = 'a'
found = false
n = len(arr)

for i in range(n):
    for j in range(arr[i]):
        if j != target:
            found = false
            break
        elif j == target:
            found = true
            break
if found:
    print("문자 "+target+"가 배열에 있습니다")
else:
    print("문자 "+target+"가 배열에 없습니다")


제출하신 코드는 Java의 for 루프와 indexOf 메서드를 Python으로 변환하는 과정에서 몇 가지 오류가 발생했습니다.
Python에서는 in 연산자를 사용하여 문자열 내에서 특정 문자가 존재하는지 확인할 수 있습니다.

평가:
불리언 값의 표기: 잘못된 표기(감점 요소).
문자열 검사 방식: 비효율적인 접근(감점 요소).
출력 부분: 잘 작성됨.
점수:
불리언 값 표기: 0.5점 (올바르게 표기하지 못함)
문자열 검사 방식: 0.5점 (비효율적인 방법 사용)
전반적인 구조: 1점 (출력 및 기본 구조는 적절함)
'''

arr = ["apple", "banana", "cherry", "date"]
target = 'a'
found = False  # Python에서 불리언 값은 False와 True입니다.

for word in arr:
    if target in word:
        found = True
        break

if found:
    print("문자 " + target + "가 배열에 있습니다.")
else:
    print("문자 " + target + "가 배열에 없습니다.")

