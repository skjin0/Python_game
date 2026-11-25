
import streamlit as st
import ast
import io
import contextlib
from pathlib import Path

st.set_page_config(
    page_title="PYTHON QUEST",
    page_icon="⚔️",
    layout="centered"
)

# -----------------------------
# 디자인
# -----------------------------

st.markdown("""
<style>
.stApp {
    background: #F5F3EA;
    color: #222222;
}
h1, h2, h3, h4, p, label {
    color: #222222 !important;
}
[data-testid="stMarkdownContainer"] p {
    color: #222222 !important;
}
.stButton > button {
    width: 100%;
    background: #E7B75C;
    color: #222222;
    border: 2px solid #C89437;
    border-radius: 12px;
    font-weight: bold;
    min-height: 45px;
}
.stButton > button:hover {
    background: #F4D28D;
    color: #222222;
}
textarea {
    color: #222222 !important;
    background: white !important;
}
.quest-card {
    background: white;
    border: 2px solid #E5DCC7;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    margin: 10px 0 20px 0;
}
.quest-picture {
    font-size: 75px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 세션 설정
# -----------------------------

st.session_state.setdefault("stage", 0)
st.session_state.setdefault("cleared", [])
st.session_state.setdefault("started", False)

# -----------------------------
# 스테이지 데이터
# -----------------------------

stages = [
    {
        "name": "초보자의 숲",
        "picture": "🌳",
        "image": "images/forest.png",
        "concept": "print()",
        "story": "숲의 입구가 막혀 있다. 마법의 주문을 외워 길을 열자!",
        "lesson": "print()는 화면에 글자나 숫자를 출력하는 명령어야.",
        "question": "print()를 사용해서 화면에 안녕!을 출력해 봐.",
        "hint": "화면에 글자를 출력하는 명령어는 print()야. 출력할 글자는 따옴표 안에 넣어야 해.",
        "answer": "안녕!",
        "type": "print"
    },
    {
        "name": "시작의 마을",
        "picture": "🏘️",
        "image": "images/village.png",
        "concept": "변수",
        "story": "마을 주민이 용사의 이름을 물어본다!",
        "lesson": "변수는 데이터를 저장하는 공간이야.",
        "question": "name이라는 변수에 '용사'를 저장하고 name을 출력해 봐.",
        "hint": "name = '용사'처럼 변수에 값을 저장할 수 있어. 그다음 print()로 name을 출력해 봐.",
        "answer": "용사",
        "type": "variable"
    },
    {
        "name": "아이템 동굴",
        "picture": "💎",
        "image": "images/cave.png",
        "concept": "리스트",
        "story": "동굴 안에는 여러 아이템이 놓여 있다!",
        "lesson": "리스트는 여러 데이터를 하나로 묶어 저장해. 첫 번째 요소의 위치는 0이야.",
        "question": "items라는 리스트에 '검', '방패', '물약'을 저장하고 첫 번째 요소를 출력해 봐.",
        "hint": "리스트는 대괄호 []를 사용해. 첫 번째 요소는 인덱스 0으로 접근할 수 있어.",
        "answer": "검",
        "type": "list"
    },
    {
        "name": "조건의 동굴",
        "picture": "🚪",
        "image": "images/door.png",
        "concept": "if 조건문",
        "story": "문지기가 암호를 확인하고 있다. 조건을 만족해야 통과할 수 있다!",
        "lesson": "if는 조건이 참일 때 코드를 실행하는 조건문이야.",
        "question": "key 변수에 True를 저장하고, if문을 사용해 key가 참이면 '문이 열렸다!'를 출력해 봐.",
        "hint": "if key: 다음 줄에 실행할 코드를 들여쓰기해서 작성해 봐.",
        "answer": "문이 열렸다!",
        "type": "if"
    },
    {
        "name": "반복의 평원",
        "picture": "🌾",
        "image": "images/plains.png",
        "concept": "for 반복문",
        "story": "세 번의 마법 주문을 외워야 다리를 건널 수 있다!",
        "lesson": "for는 같은 작업을 반복할 때 사용해. range(3)은 세 번 반복할 수 있게 해 줘.",
        "question": "for와 range(3)을 사용해 '반복!'을 세 번 출력해 봐.",
        "hint": "for i in range(3): 형태로 시작해 봐. 반복할 명령은 들여쓰기해야 해.",
        "answer": "반복!\n반복!\n반복!",
        "type": "for"
    },
    {
        "name": "함수의 탑",
        "picture": "🗼",
        "image": "images/tower.png",
        "concept": "def 함수",
        "story": "탑 꼭대기의 마법사가 함수를 만들라고 한다!",
        "lesson": "def는 함수를 만드는 명령어야. 만든 함수는 함수이름()으로 실행할 수 있어.",
        "question": "인사라는 함수를 만들고 실행해서 '안녕하세요!'를 출력해 봐.",
        "hint": "def 인사():로 함수를 정의하고, 함수 안에서 print()를 사용해 봐. 마지막에는 인사()로 실행해야 해.",
        "answer": "안녕하세요!",
        "type": "def"
    },
    {
        "name": "마왕의 성",
        "picture": "🏰",
        "image": "images/castle.png",
        "concept": "종합 문제",
        "story": "드디어 마왕과 마주했다! 지금까지 배운 개념을 활용하자!",
        "lesson": "리스트, for, if, def를 함께 사용해 문제를 해결해 보자.",
        "question": "monsters 리스트에 '슬라임'과 '마왕'을 저장해. battle이라는 함수를 만들고, for문과 if문으로 마왕을 찾으면 '마왕 처치!'를 출력해 봐.",
        "hint": "① monsters 리스트를 만들어 봐. ② def battle():로 함수를 정의해. ③ 함수 안에서 for문으로 몬스터를 하나씩 확인해. ④ if문으로 몬스터가 '마왕'인지 비교해 봐.",
        "answer": "마왕 처치!",
        "type": "final"
    }
]

# -----------------------------
# 코드 구조 검사
# -----------------------------

def check_structure(code, stage_type):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return False, f"문법 오류: {e}"

    nodes = list(ast.walk(tree))

    if stage_type == "print":
        valid = any(
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == "print"
            for n in nodes
        )

    elif stage_type == "variable":
        assigned = any(
            isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "name"
                    for t in n.targets)
            for n in nodes
        )
        printed = any(
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == "print"
            and n.args
            and isinstance(n.args[0], ast.Name)
            and n.args[0].id == "name"
            for n in nodes
        )
        valid = assigned and printed

    elif stage_type == "list":
        assigned = any(
            isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "items"
                    for t in n.targets)
            and isinstance(n.value, ast.List)
            for n in nodes
        )
        indexed = any(
            isinstance(n, ast.Subscript)
            and isinstance(n.value, ast.Name)
            and n.value.id == "items"
            for n in nodes
        )
        valid = assigned and indexed

    elif stage_type == "if":
        valid = any(isinstance(n, ast.If) for n in nodes)

    elif stage_type == "for":
        valid = any(isinstance(n, ast.For) for n in nodes) and any(
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == "range"
            for n in nodes
        )

    elif stage_type == "def":
        defined = any(
            isinstance(n, ast.FunctionDef) and n.name == "인사"
            for n in nodes
        )
        called = any(
            isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == "인사"
            for n in nodes
        )
        valid = defined and called

    elif stage_type == "final":
        has_list = any(
            isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "monsters"
                    for t in n.targets)
            and isinstance(n.value, ast.List)
            for n in nodes
        )
        has_def = any(
            isinstance(n, ast.FunctionDef) and n.name == "battle"
            for n in nodes
        )
        has_for = any(isinstance(n, ast.For) for n in nodes)
        has_if = any(isinstance(n, ast.If) for n in nodes)
        valid = has_list and has_def and has_for and has_if

    else:
        valid = False

    if not valid:
        return False, "이번 미션에서 배운 파이썬 문법을 직접 사용해야 해!"

    return True, None


# -----------------------------
# 코드 실행
# -----------------------------

ALLOWED_NODES = (
    ast.Module, ast.Expr, ast.Assign, ast.Name, ast.Load,
    ast.Store, ast.Constant, ast.Call, ast.List, ast.Tuple,
    ast.Subscript, ast.If, ast.Compare, ast.Eq, ast.NotEq,
    ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.For,
    ast.FunctionDef, ast.arguments, ast.arg, ast.Return,
    ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div,
    ast.Mod, ast.UnaryOp, ast.Not, ast.USub, ast.Pass,
    ast.BoolOp, ast.And, ast.Or
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
            n.name for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef)
        }

        for node in ast.walk(tree):
            if not isinstance(node, ALLOWED_NODES):
                return None, "허용되지 않은 문법이 포함되어 있어!"

            if isinstance(node, ast.Name) and node.id.startswith("_"):
                return None, "사용할 수 없는 이름이 포함되어 있어!"

            if isinstance(node, ast.Call):
                if not isinstance(node.func, ast.Name):
                    return None, "허용되지 않은 함수 호출이야!"

                name = node.func.id
                if name not in SAFE_BUILTINS and name not in function_names:
                    return None, "사용할 수 없는 함수야: " + name

                if name == "range" and node.args:
                    try:
                        if len(range(*[ast.literal_eval(a) for a in node.args])) > 100:
                            return None, "반복 횟수가 너무 많아!"
                    except Exception:
                        return None, "range에는 숫자를 사용해 줘."

        output = io.StringIO()
        safe_globals = {"__builtins__": SAFE_BUILTINS}

        with contextlib.redirect_stdout(output):
            exec(
                compile(tree, "<student_code>", "exec"),
                safe_globals,
                safe_globals
            )

        return output.getvalue().strip(), None

    except Exception as e:
        return None, str(e)


# -----------------------------
# 제목
# -----------------------------

st.title("⚔️ PYTHON QUEST")
st.caption("파이썬을 배우고 마왕으로부터 왕국을 구하라!")

# -----------------------------
# 시작 화면
# -----------------------------

if not st.session_state.started:

    st.markdown("""
    <div class="quest-card">
        <div class="quest-picture">🏰⚔️🐉</div>
        <h1>PYTHON QUEST</h1>
        <p>파이썬 왕국을 구하기 위한 위대한 모험!</p>
    </div>
    """, unsafe_allow_html=True)

    st.header("📖 모험의 시작")

    st.write("""
    평화롭던 파이썬 왕국에 마왕이 나타났다.

    일곱 개의 스테이지를 통과하고
    파이썬의 힘으로 왕국을 구하자!
    """)

    st.info("🎯 직접 코드를 작성하고 실행해야 미션을 통과할 수 있어!")

    if st.button("⚔️ 모험 시작하기"):
        st.session_state.started = True
        st.rerun()

# -----------------------------
# 엔딩 화면
# -----------------------------

elif st.session_state.stage == 7:

    st.balloons()

    ending_image = Path("images/ending.png")

    if ending_image.exists():
        st.image(str(ending_image), use_container_width=True)
    else:
        st.markdown('<div class="quest-card"><div class="quest-picture">👑🏆🎉</div></div>',
                    unsafe_allow_html=True)

    st.title("PYTHON QUEST CLEAR!")
    st.header("🎉 마왕을 물리쳤다!")
    st.success("축하해! 일곱 개의 스테이지를 모두 통과했어.")

    st.markdown("""
    ### 📚 배운 개념
    - print()
    - 변수와 자료형
    - 리스트
    - if 조건문
    - for 반복문
    - def 함수
    - 종합 활용
    """)

    if st.button("🔄 처음부터 다시 시작"):
        st.session_state.stage = 0
        st.session_state.cleared = []
        st.session_state.started = False

        for i in range(7):
            st.session_state.pop(f"passed_{i}", None)

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

    image_path = Path(stage["image"])

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.markdown(
            f'<div class="quest-card"><div class="quest-picture">{stage["picture"]}</div></div>',
            unsafe_allow_html=True
        )

    st.header(f"🏞️ {stage['name']}")
    st.caption(f"STAGE {stage_index + 1} / 7")

    st.subheader(f"📚 학습 개념: {stage['concept']}")

    st.write("📖 스토리")
    st.info(stage["story"])

    st.write("💡 개념 배우기")
    st.success(stage["lesson"])

    st.write("🎯 미션")
    st.warning(stage["question"])

    # 힌트는 기본적으로 닫혀 있음
    with st.expander("💡 힌트 보기", expanded=False):
        st.write(stage["hint"])

    st.write("⌨️ 나의 코드 작성하기")

    code = st.text_area(
        "직접 Python 코드를 작성해 봐!",
        value="",
        placeholder="# 여기에 직접 코드를 작성하세요.",
        height=200,
        key=f"code_{stage_index}"
    )

    if st.button("▶️ 코드 실행하기"):

        if not code.strip():
            st.warning("먼저 코드를 작성해 줘!")

        else:
            structure_ok, structure_error = check_structure(
                code, stage["type"]
            )

            if not structure_ok:
                st.error(structure_error)

            else:
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
        st.success("🏆 미션 성공! 다음 스테이지가 열렸어.")

        if stage_index < len(stages) - 1:

            if st.button("다음 스테이지로 이동 ➡️"):
                st.session_state.stage += 1
                st.rerun()

        else:

            if st.button("👑 엔딩 확인하기"):
                st.session_state.stage = 7
                st.rerun()
