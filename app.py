
import streamlit as st
import ast
import io
import contextlib

st.set_page_config(
    page_title="PYTHON QUEST",
    page_icon="⚔️",
    layout="centered"
)

# -----------------------------
# 게임 기본 설정
# -----------------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10182c, #202c49);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("⚔️ PYTHON QUEST")
st.caption("파이썬을 배우고 마왕으로부터 왕국을 구하라!")

st.session_state.setdefault("stage", 0)
st.session_state.setdefault("cleared", [])
st.session_state.setdefault("started", False)

# -----------------------------
# 스테이지 데이터
# -----------------------------

stages = [
    {
        "name": "초보자의 숲",
        "concept": "print()",
        "story": "숲의 입구가 막혀 있다. 마법의 주문을 외워 길을 열자!",
        "lesson": "print()는 화면에 글자나 숫자를 출력하는 명령어야.",
        "question": "화면에 안녕! 이라고 출력해 봐.",
        "example": 'print("안녕!")',
        "answer": "안녕!"
    },
    {
        "name": "시작의 마을",
        "concept": "변수",
        "story": "마을 주민이 용사의 이름을 물어본다!",
        "lesson": "변수는 데이터를 저장하는 공간이야. name = '용사'처럼 사용할 수 있어.",
        "question": "name 변수에 '용사'를 저장하고 name을 출력해 봐.",
        "example": 'name = "용사"\nprint(name)',
        "answer": "용사"
    },
    {
        "name": "아이템 동굴",
        "concept": "리스트",
        "story": "동굴 안에는 여러 아이템이 놓여 있다!",
        "lesson": "리스트는 여러 데이터를 하나로 묶어 저장해. 예: items = ['검', '방패']",
        "question": "items 리스트의 첫 번째 요소를 출력해 봐.",
        "example": 'items = ["검", "방패", "물약"]\nprint(items[0])',
        "answer": "검"
    },
    {
        "name": "조건의 동굴",
        "concept": "if 조건문",
        "story": "문지기가 암호를 확인하고 있다. 조건을 만족해야 통과할 수 있다!",
        "lesson": "if는 조건이 참일 때 코드를 실행해. 예: if score >= 10:",
        "question": "key가 True일 때 '문이 열렸다!'를 출력해 봐.",
        "example": 'key = True\nif key:\n    print("문이 열렸다!")',
        "answer": "문이 열렸다!"
    },
    {
        "name": "반복의 평원",
        "concept": "for 반복문",
        "story": "세 번의 마법 주문을 외워야 다리를 건널 수 있다!",
        "lesson": "for는 같은 작업을 반복할 때 사용해. range(3)은 0부터 2까지 반복해.",
        "question": "for와 range(3)을 사용해 반복!을 세 번 출력해 봐.",
        "example": 'for i in range(3):\n    print("반복!")',
        "answer": "반복!\n반복!\n반복!"
    },
    {
        "name": "함수의 탑",
        "concept": "def 함수",
        "story": "탑 꼭대기의 마법사가 함수를 만들라고 한다!",
        "lesson": "def는 함수를 만드는 명령어야. 만든 함수는 이름()으로 실행할 수 있어.",
        "question": "인사라는 함수를 만들고 실행해서 안녕하세요!를 출력해 봐.",
        "example": 'def 인사():\n    print("안녕하세요!")\n\n인사()',
        "answer": "안녕하세요!"
    },
    {
        "name": "마왕의 성",
        "concept": "종합 문제",
        "story": "드디어 마왕과 마주했다! 지금까지 배운 개념을 활용하자!",
        "lesson": "리스트, for, if, def를 함께 사용해 문제를 해결해 보자.",
        "question": "몬스터 목록을 만들고, 몬스터가 마왕이면 '마왕 처치!'를 출력하는 함수를 만들어 실행해 봐.",
        "example": 'monsters = ["슬라임", "마왕"]\n\ndef battle():\n    for monster in monsters:\n        if monster == "마왕":\n            print("마왕 처치!")\n\nbattle()',
        "answer": "마왕 처치!"
    }
]

# -----------------------------
# 제한된 Python 코드 실행
# -----------------------------

ALLOWED_NODES = (
    ast.Module, ast.Expr, ast.Assign, ast.Name, ast.Load,
    ast.Store, ast.Constant, ast.Call, ast.List, ast.Tuple,
    ast.Subscript, ast.Index, ast.If, ast.Compare,
    ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
    ast.For, ast.FunctionDef, ast.arguments, ast.arg,
    ast.Return, ast.BinOp, ast.Add, ast.Sub, ast.Mult,
    ast.Div, ast.Mod, ast.UnaryOp, ast.Not, ast.USub,
    ast.Pass, ast.BoolOp, ast.And, ast.Or
)

SAFE_BUILTINS = {
    "print": print,
    "range": range,
    "len": len,
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list
}

def run_python(code):
    try:
        tree = ast.parse(code)

        function_names = {
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        }

        for node in ast.walk(tree):
            if not isinstance(node, ALLOWED_NODES):
                return None, "허용되지 않은 문법이 포함되어 있어!"

            if isinstance(node, ast.Name):
                if node.id.startswith("_"):
                    return None, "사용할 수 없는 이름이 포함되어 있어!"

            if isinstance(node, ast.Call):
                if not isinstance(node.func, ast.Name):
                    return None, "허용되지 않은 함수 호출이야!"

                name = node.func.id
                if name not in SAFE_BUILTINS and name not in function_names:
                    return None, "사용할 수 없는 함수야: " + name

        output = io.StringIO()

        safe_globals = {
            "__builtins__": SAFE_BUILTINS
        }

        with contextlib.redirect_stdout(output):
            exec(compile(tree, "<student_code>", "exec"),
                 safe_globals, safe_globals)

        return output.getvalue().strip(), None

    except Exception as e:
        return None, str(e)


# -----------------------------
# 시작 화면
# -----------------------------

if not st.session_state.started:
    st.markdown("---")
    st.header("🏰 왕국에 어둠이 찾아왔다!")
    st.write("""
    평화롭던 파이썬 왕국에 마왕이 나타났다.

    왕국을 구하기 위해서는 일곱 개의 스테이지를 통과해야 한다.

    파이썬의 기초부터 차근차근 배우고
    최종 보스 마왕을 물리쳐라!
    """)
    st.info("🎯 목표: 파이썬 코드를 직접 작성하여 모든 스테이지를 클리어하자!")
    
    if st.button("⚔️ 모험 시작하기"):
        st.session_state.started = True
        st.rerun()

# -----------------------------
# 게임 화면
# -----------------------------

else:
    stage_index = st.session_state.stage
    stage = stages[stage_index]

    st.markdown("---")

    st.subheader("🗺️ 스테이지 진행 상황")

    cols = st.columns(7)
    for i, col in enumerate(cols):
        if i in st.session_state.cleared:
            col.success(f"{i + 1}단계")
        elif i == stage_index:
            col.info(f"{i + 1}단계")
        else:
            col.write(f"🔒 {i + 1}단계")

    st.progress(len(st.session_state.cleared) / len(stages))

    st.markdown("---")

    st.header(f"🏞️ {stage['name']}")
    st.subheader(f"📚 학습 개념: {stage['concept']}")

    st.write("📖 **스토리**")
    st.info(stage["story"])

    st.write("💡 **개념 배우기**")
    st.success(stage["lesson"])

    st.write("🎯 **미션**")
    st.warning(stage["question"])

    st.write("⌨️ **코드 작성하기**")

    code = st.text_area(
        "아래에 Python 코드를 작성해 봐!",
        value=stage["example"],
        height=180,
        key=f"code_{stage_index}"
    )

    if st.button("▶️ 코드 실행하기"):
        result, error = run_python(code)

        if error:
            st.error("코드 오류: " + error)
        else:
            st.markdown("### 💻 실행 결과")
            st.code(result if result else "(출력 결과 없음)")

            if result == stage["answer"]:
                if stage_index not in st.session_state.cleared:
                    st.session_state.cleared.append(stage_index)

                st.session_state[f"passed_{stage_index}"] = True
                st.success("🎉 미션 성공! 스테이지를 클리어했어!")
            else:
                st.error("아직 정답이 아니야. 코드를 다시 확인해 보자!")

    if st.session_state.get(f"passed_{stage_index}", False):
        st.markdown("---")
        st.success("🏆 경험치 획득! 다음 스테이지로 이동할 수 있어.")

        if stage_index < len(stages) - 1:
            if st.button("다음 스테이지로 이동 ➡️"):
                st.session_state.stage += 1
                st.rerun()
        else:
            if st.button("👑 엔딩 확인하기"):
                st.session_state.stage = 7
                st.rerun()

    # -----------------------------
    # 엔딩
    # -----------------------------

    if st.session_state.stage == 7:
        st.balloons()
        st.markdown("---")
        st.title("👑 PYTHON QUEST CLEAR!")
        st.header("🎉 마왕을 물리쳤다!")
        st.write("""
        축하해! 너는 일곱 개의 스테이지를 모두 통과했어.

        이제 파이썬의 기초 개념을 배운 진정한 용사야!

        **배운 개념**
        - print()
        - 변수와 자료형
        - 리스트
        - if 조건문
        - for 반복문
        - def 함수
        - 종합 활용
        """)
        st.success("🏆 파이썬 왕국의 평화가 돌아왔다!")

        if st.button("🔄 처음부터 다시 시작"):
            st.session_state.stage = 0
            st.session_state.cleared = []
            st.session_state.started = False
            for i in range(7):
                st.session_state.pop(f"passed_{i}", None)
            st.rerun()
