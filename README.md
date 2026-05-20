# Python Coding Test Example

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Learning%20Archive-orange)

Python 코딩 테스트와 기초 알고리즘 학습을 위한 예제 저장소입니다.

이 저장소는 Python 문법을 처음 학습하거나, 코딩 테스트 문제 해결 방식을 단계적으로 익히고 싶은 학습자를 위해 만들어졌습니다.  
간단한 문제부터 시작하여 변수, 연산자, 조건문, 반복문, 함수, 리스트, 문자열 처리, 기본 알고리즘 문제까지 차근차근 정리하는 것을 목표로 합니다.

---

## 📌 Repository Overview

이 저장소는 다음과 같은 목적을 가지고 있습니다.

- Python 기초 문법 복습
- 코딩 테스트 입문 문제 풀이
- PCCE 유형 문제 연습
- 문제 해결 과정을 코드로 정리
- 초보자도 이해하기 쉬운 주석 기반 예제 제공

---

## 🗂️ Project Structure

```text
Python-Coding-Test-Example
├── Python-Coding-Test-Example
│   ├── PCCE
│   │   └── hour_wage.py
│   ├── Python_Coding_Test_Example.py
│   └── Python-Coding-Test-Example.pyproj
├── .gitattributes
├── .gitignore
├── LICENSE.txt
├── Python-Coding-Test-Example.slnx
└── README.md

## 🧩 Example

### 시급 계산 예제

`PCCE/hour_wage.py`

```python
# 시급 계산
# 시급이란? 시간당 받는 돈을 뜻한다.
# 급여란 받은 돈이다.
# 총 일한 시간은 월급제인지 주급제인지에 따라 다르게 구할 수 있다.
# 예를 들어 월급제인 경우 하루에 일하는 시간 * 한 달
# 이는 급여 지급의 조건(월 기준인지 주 기준인지)에 따라 달라진다.

# 시급 = 급여 / 총 일한 시간

# money 만큼의 급여를 받은 사람이 하루 hour시간 만큼 일하며
# 총 day일 만큼 일했다고 한다면 시급은?

money = 890000
hour = 7
day = 15

hour_wage = money / (hour * day)

print(hour_wage)
```

### 실행 결과

```text
8476.190476190477
```

### 설명

시급은 다음 공식으로 계산할 수 있습니다.

```text
시급 = 급여 / 총 일한 시간
```

위 예제에서는 다음과 같이 계산됩니다.

```text
총 일한 시간 = 하루 근무 시간 × 근무일 수
            = 7 × 15
            = 105시간

시급 = 890000 / 105
     ≈ 8476.19원
```

---

## 🚀 How to Run

### 1. 저장소 복제

```bash
git clone https://github.com/VisualStudy/Python-Coding-Test-Example.git
```

### 2. 프로젝트 폴더로 이동

```bash
cd Python-Coding-Test-Example
```

### 3. Python 파일 실행

```bash
python Python-Coding-Test-Example/PCCE/hour_wage.py
```

또는 운영체제 환경에 따라 다음 명령어를 사용할 수 있습니다.

```bash
python3 Python-Coding-Test-Example/PCCE/hour_wage.py
```

---

## 📚 Learning Topics

앞으로 다음과 같은 Python 코딩 테스트 예제를 추가할 수 있습니다.

| Category | Description |
|---|---|
| Basic Syntax | 변수, 자료형, 연산자 |
| Conditional | if, elif, else |
| Loop | for, while |
| Function | 함수 정의와 호출 |
| List | 리스트 생성, 탐색, 정렬 |
| String | 문자열 인덱싱, 슬라이싱, 변환 |
| Math | 나머지, 몫, 평균, 최대값, 최소값 |
| Algorithm | 완전탐색, 정렬, 탐색 |
| PCCE | 프로그래머스 PCCE 유형 문제 |

---

## ✅ Recommended Naming Rule

예제 파일은 다음과 같은 방식으로 관리하면 좋습니다.

```text
PCCE/
├── hour_wage.py
├── average_score.py
├── find_max_value.py
├── count_character.py
└── simple_calculator.py
```

파일 이름은 가능하면 다음 규칙을 따릅니다.

```text
문제 내용을 영어 소문자와 언더스코어(_)로 표현
```

예시:

```text
hour_wage.py
average_score.py
find_max_value.py
```

---

## 🧠 Study Guide

Python 코딩 테스트를 처음 공부한다면 다음 순서로 학습하는 것을 추천합니다.

1. 변수와 자료형 이해하기
2. 산술 연산자와 비교 연산자 익히기
3. 조건문으로 상황 나누기
4. 반복문으로 여러 데이터 처리하기
5. 리스트와 문자열 다루기
6. 함수를 사용해 코드 정리하기
7. 간단한 PCCE 문제 풀이하기
8. 풀이 후 코드 주석으로 개념 정리하기

---

## 🛠️ Development Environment

이 저장소는 Python 기반 예제 저장소입니다.

권장 환경:

```text
Python 3.x
Visual Studio Code
Visual Studio
PyCharm
```

Python 버전 확인:

```bash
python --version
```

또는

```bash
python3 --version
```

---

## 📖 Purpose

이 저장소는 단순히 정답 코드만 모아두는 것이 아니라,  
문제를 어떻게 이해하고 어떤 공식이나 사고 과정을 통해 코드로 바꾸는지 기록하는 것을 목표로 합니다.

따라서 각 예제는 가능하면 다음 흐름을 따릅니다.

```text
문제 이해 → 필요한 공식 정리 → 변수 설정 → 코드 작성 → 결과 확인
```

---

## 🤝 Contribution

학습용 예제 저장소이므로 다음과 같은 방식의 기여를 환영합니다.

- 새로운 Python 예제 추가
- 기존 코드의 주석 개선
- 더 쉬운 풀이 방식 제안
- 파일 구조 정리
- README 문서 개선

---

## 📄 License

This project is licensed under the MIT License.

See the [LICENSE.txt](LICENSE.txt) file for details.

---

## 🙌 Author

Created by [VisualStudy](https://github.com/VisualStudy)
