## [Assignment Title]<br>[과제 제목]

* Prompt file 프롬프트 파일 : `prompt.md`
* [Assignment description goes here — describe the numerical method or algorithm to implement]
* [과제 설명 — 구현할 수치 해석 방법이나 알고리즘을 설명하시오]

### What to implement 구현 내용

[Describe the function(s) the AI must generate based on the student's prompt.]
[프롬프트에서 AI가 생성해야 할 함수를 설명하시오.]

| argument<br>매개변수 | type<br>자료형 | description<br>설명 |
|:---:|:---:|---|
| `param1` | `float` | [description] |

[Describe the expected return value.]

### How this assignment works 과제 수행 방식

This is a **prompt engineering** assignment.<br>이 과제는 **프롬프트 엔지니어링** 과제입니다.

1. Write a prompt in `prompt.md` that instructs the AI to implement the required function.<br>`prompt.md` 에 필요한 함수를 구현하도록 AI에게 지시하는 프롬프트를 작성하시오.
2. Push your changes. The workflow will call the AI to generate `exercise.py` from your prompt.<br>변경 사항을 푸시하면, 워크플로우가 AI를 호출하여 프롬프트로부터 `exercise.py` 를 생성합니다.
3. The generated code is graded automatically by the test suite.<br>생성된 코드는 테스트 스위트에 의해 자동으로 채점됩니다.
4. If the tests fail, revise your prompt and push again.<br>테스트가 실패하면 프롬프트를 수정하고 다시 푸시하시오.

**Tips for writing effective prompts 효과적인 프롬프트 작성 팁:**
- Specify the exact function name and signature.<br>정확한 함수 이름과 시그니처를 명시하시오.
- Describe edge cases and error conditions.<br>경계 조건과 오류 조건을 설명하시오.
- Include the expected return type and structure.<br>예상 반환 자료형과 구조를 포함하시오.
- Use mathematical notation when helpful.<br>수식 표기법을 활용하면 도움이 될 수 있습니다.

## Grading Criteria<br>채점 기준

| Criteria<br>기준 | Points<br>배점 |
|:---:|:---:|
| Is the generated code written according to Python syntax?<br>생성된 코드가 Python 문법대로 작성되었는가? | 2 |
| Does the generated code respect style guidelines?<br>생성된 코드가 코드 스타일 권고사항을 준수하는가? | 1 |
| Is the generated code implemented as required?<br>생성된 코드가 요구사항을 만족하는가? | 2 |

``From here is common to all assignments.``

## Submission 제출 방법

1. Write your prompt in the `prompt.md` file.<br>`prompt.md` 파일에 프롬프트를 작성합니다.
2. Use the GitHub online editor to commit and push your changes. (See below for detailed instructions)<br>GitHub 온라인 편집기를 사용하여 수정 사항을 커밋하고 푸시합니다. (자세한 사용법은 아래 참조)
3. At the Actions tab of your Github repository, please check the result.<br>깃헙 저장소의 Actions 탭에서 결과를 확인 바랍니다.

## How to Use the GitHub Online Editor<br>Github 온라인 편집기 사용법

* Press the <kbd>.</kbd> key while viewing the files in your repository on GitHub. This will launch a web version of VS Code.<br>저장소의 [Code] 탭을 선택 후 <kbd>.</kbd> 키를 누르면 MS VS Code 의 Web version 이 시작됨
* Make your changes to the `prompt.md` file.<br>`prompt.md` 파일을 수정
* To commit your changes, click on the branch icon on the left sidebar (the third icon after the magnifying glass).<br>수정 사항을 commit 등록 하려면 왼쪽에서 줄 셋 아래 (확대경 다음) 세번째 가지치기 아이콘 선택
* Click the "+" sign next to the filename to stage your changes.<br>파일 이름의 오른쪽 + 기호 선택 (staging)
* Write a brief description of your changes in the text box above.<br>위 빈칸에 변경 사항 설명 입력
* Click "Commit & Push."<br>[커밋 및 푸시] 선택
* Click "Back to Repository" on the branch icon to return to your repository.<br>줄 셋 의 [리포지토리로 이동] 선택하여 저장소로 복귀

## Writing Descriptive Git Commit Messages<br>커밋 메시지 작성 권고안

* To help you develop better coding habits, we encourage descriptive Git commit messages.<br>보다 바람직한 코딩 습관을 기르기 위해, 커밋 메시지에 보다 자세히 설명하는 것을 권합니다.

### Guidelines for Commit Messages<br>메시지 작성 지침
* Describe the change specifically, e.g., "Add edge case for zero input" or "Specify return type in constraints section".<br>변경 사항을 구체적으로 설명합니다. 예: "0 입력 경계 조건 추가" 또는 "제약 조건에 반환 자료형 명시"
* Use Action Verbs: "Add", "Fix", "Update", "Clarify".<br>영문의 경우, "Add", "Fix", "Update", "Clarify"와 같은 동사로 시작합니다.
* Keep It Concise: Aim for 15-50 characters.<br>15-50자 정도로 간결하게 작성합니다.

## NOTICE REGARDING STUDENT SUBMISSIONS<br>제출 결과물에 대한 알림

* Your submissions for this assignment may be used for various educational purposes. These purposes may include developing and improving educational tools, research, creating test cases, and training datasets.<br>제출 결과물은 다양한 교육 목적으로 사용될 수 있을 밝혀둡니다.

* The submissions will be anonymized and used solely for educational or research purposes. No personally identifiable information will be shared.<br>제출된 결과물은 익명화되어 교육 및 연구 목적으로만 사용되며, 개인 식별 정보는 공유되지 않을 것입니다.

* If you do not wish to have your submission used for any of these purposes, please inform the instructor before the assignment deadline.<br>위와 같은 목적으로 사용되기 원하지 않는 경우, 과제 마감일 전에 강사에게 알려주기 바랍니다.

## Acknowledgments

* The template for this assignment is registered as a part of #C-2025-016393 in the Korea Copyright Commission.

``Until here is common to all assignments.``
