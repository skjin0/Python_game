import streamlit as st
import ast
import io
import contextlib
from pathlib import Path

st.set_page_config(page_title="PYTHON QUEST", page_icon="⚔️", layout="wide")

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"

# -----------------------------
# 디자인
# -----------------------------
st.markdown("""
<style>
.stApp { background: #F5F3EA; color: #222222; }
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
h1, h2, h3, h4, p, label, li { color: #222222 !important; }
[data-testid="stMarkdownContainer"] p { color: #222222 !important; }
.stCaption, small { color: #514735 !important; }
.stButton > button {
    width: 100%; min-height: 46px; border-radius: 12px;
    background: #F2BD55; color: #21180B; border: 2px solid #C58A2B;
    font-weight: 800;
}
.stButton > button:hover { background: #FFDA87; color: #21180B; border-color: #9C6920; }
[data-testid="stAlert"] { color: #222222; }
[data-testid="stTextArea"] textarea {
    color: #222222 !important; background: #FFFFFF !important;
    font-family: monospace;
}
.quest-card {
    background: #FFFDF7; border: 2px solid #E5D4B4;
    border-radius: 18px; padding: 18px; margin: 8px 0 16px 0;
}
.stage-title { text-align: center; font-weight: 900; color: #2B2115; }
div[data-testid="stProgressBar"] > div > div { background: #65AD49; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 게임 데이터
# -----------------------------
stages = [
    {
        "name": "초보자의 숲", "image": "forest.png", "concept": "print()",
        "story": "숲의 입구가 막혀 있다. 마법의 주문을 외워 길을 열자!",
        "lesson": "print()는 화면에 글자나 숫자를 출력하는 명령어야.",
        "question": "화면에 안녕! 이라고 출력해 봐.",
        "example": 'print("안녕!")', "answer": "안녕!"
    },
    {
        "name": "시작의 마을", "image": "village.png", "concept": "변수와 자료형",
        "story": "마을 주민이 용사의 이름을 물어본다!",
        "lesson": "변수는 데이터를 저장하는 공간이야. name = '용사'처럼 사용할 수 있어.",
        "question": "name 변수에 '용사'를 저장하고 name을 출력해 봐.",
        "example": 'name = "용사"\nprint(name)', "answer": "용사"
    },
    {
        "name": "아이템 동굴", "image": "cave.png", "concept": "리스트",
        "story": "동굴 안에는 여러 아이템이 놓여 있다!",
        "lesson": "리스트는 여러 데이터를 하나로 묶어 저장해. 예: items = ['검', '방패']",
        "question": "items 리스트의 첫 번째 요소를 출력해 봐.",
        "example": 'items = ["검", "방패", "물약"]\nprint(items[0])', "answer": "검"
    },
    {
        "name": "조건의 문", "image": "door.png", "concept": "if 조건문",
        "story": "신비한 문이 길을 막고 있다. 조건을 만족해야 통과할 수 있다!",
        "lesson": "if는 조건이 참일 때 코드를 실행해. 예: if key == True:",
        "question": "key가 True일 때 '문이 열렸다!'를 출력해 봐.",
        "example": 'key = True\nif key:\n    print("문이 열렸다!")', "answer": "문이 열렸다!"
    },
    {
        "name": "반복의 평원", "image": "plains.png", "concept": "for 반복문",
        "story": "세 번의 마법 주문을 외워야 다리를 건널 수 있다!",
        "lesson": "for는 같은 작업을 반복할 때 사용해. range(3)은 0부터 2까지 반복해.",
        "question": "for와 range(3)을 사용해 반복!을 세 번 출력해 봐.",
        "example": 'for i in range(3):\n    print("반복!")',
        "answer": "반복!\n반복!\n반복!"
    },
    {
        "name": "함수의 탑", "image": "tower.png", "concept": "def 함수",
        "story": "탑 꼭대기의 마법사가 함수를 만들라고 한다!",
        "lesson": "def는 함수를 만드는 명령어야. 만든 함수는 이름()으로 실행할 수 있어.",
        "question": "인사라는 함수를 만들고 실행해서 안녕하세요!를 출력해 봐.",
        "example": 'def 인사():\n    print("안녕하세요!")\n\n인사()', "answer": "안녕하세요!"
    },
    {
        "name": "마왕의 성", "image": "castle.png", "concept": "종합 문제",
        "story": "드디어 마왕과 마주했다! 지금까지 배운 개념을 활용하자!",
        "lesson": "리스트, for, if, def를 함께 사용해 문제를 해결해 보자.",
        "question": "몬스터 목록을 만들고, 몬스터가 마왕이면 '마왕 처치!'를 출력하는 함수를 만들어 실행해 봐.",
        "example": 'monsters = ["슬라임", "마왕"]\n\ndef battle():\n    for monster in monsters:\n        if monster == "마왕":\n            print("마왕 처치!")\n\nbattle()',
        "answer": "마왕 처치!"
    }
]

def show_image(filename, caption=None):
    path = IMAGE_DIR / filename
    if path.exists():
        st.image(str(path), use_container_width=True, caption=caption)
    else:
        st.warning(f"이미지를 찾을 수 없어: {filename}")

# -----------------------------
# 학습 코드 실행
# -----------------------------
# 학습용 제한 실행기: 허용된 기본 문법만 통과시킴.
# 공개 서비스에서는 별도의 격리 실행 환경 사용을 권장함.
ALLOWED_NODES = (
    ast.Module, ast.Expr, ast.Assign, ast.Name, ast.Load, ast.Store,
    ast.Constant, ast.Call, ast.List, ast.Tuple, ast.Subscript,
    ast.If, ast.Compare, ast.Eq, ast.NotEq, ast.Lt, ast.LtE,
    ast.Gt, ast.GtE, ast.For, ast.FunctionDef, ast.arguments,
    ast.arg, ast.Return, ast.BinOp, ast.Add, ast.Sub, ast.Mult,
    ast.Div, ast.Mod, ast.UnaryOp, ast.Not, ast.USub, ast.Pass,
    ast.BoolOp, ast.And, ast.Or
)

SAFE_BUILTINS = {
    "print": print, "range": range, "len": len,
    "str": str, "int": int, "float": float, "bool": bool, "list": list
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
                return None, "아직 사용할 수 없는 문법이 포함되어 있어!"
            if isinstance(node, ast.Name) and node.id.startswith("_"):
                return None, "사용할 수 없는 이름이 포함되어 있어!"
            if isinstance(node, ast.Call):
                if not isinstance(node.func, ast.Name):
                    return None, "허용되지 않은 함수 호출이야!"
                if node.func.id not in SAFE_BUILTINS and node.func.id not in function_names:
                    return None, f"아직 배운 함수가 아니야: {node.func.id}"

        output = io.StringIO()
        safe_globals = {"__builtins__": SAFE_BUILTINS}
        with contextlib.redirect_stdout(output):
            exec(compile(tree, "<student_code>", "exec"), safe_globals, safe_globals)
        return output.getvalue().strip(), None
    except Exception as exc:
        return None, str(exc)

# -----------------------------
# 상태
# -----------------------------
st.session_state.setdefault("stage", 0)
st.session_state.setdefault("cleared", [])
st.session_state.setdefault("started", False)

# -----------------------------
# 헤더
# -----------------------------
st.title("⚔️ PYTHON QUEST")
st.caption("파이썬을 배우고 마왕으로부터 왕국을 구하라!")

# -----------------------------
# 시작 화면
# -----------------------------
if not st.session_state.started:
    show_image("ending.png")
    st.markdown('<div class="quest-card"><h2 class="stage-title">🏰 모험의 시작</h2><p style="text-align:center">평화롭던 파이썬 왕국에 마왕이 나타났다!<br>일곱 개의 스테이지를 통과하고 왕국을 구하자!</p></div>', unsafe_allow_html=True)
    st.subheader("🗺️ 모험의 여정")
    journey = st.columns(7)
    journey_labels = ["🌳 숲", "🏘️ 마을", "💎 동굴", "🚪 문", "🌾 평원", "🗼 탑", "🏰 성"]
    for col, label in zip(journey, journey_labels):
        col.markdown(f"**{label}**")
    st.info("🎯 목표: 파이썬 코드를 직접 작성하여 모든 스테이지를 클리어하자!")
    if st.button("⚔️ 모험 시작하기"):
        st.session_state.started = True
        st.rerun()

# -----------------------------
# 엔딩 화면
# -----------------------------
elif st.session_state.stage >= len(stages):
    show_image("ending.png")
    st.title("👑 PYTHON QUEST CLEAR!")
    st.header("🎉 마왕을 물리쳤다!")
    st.success("축하해! 너는 일곱 개의 스테이지를 모두 통과했어.")
    st.markdown("""
    **배운 개념**
    - `print()`
    - 변수와 자료형
    - 리스트
    - `if` 조건문
    - `for` 반복문
    - `def` 함수
    - 종합 활용
    """)
    if st.button("🔄 처음부터 다시 시작"):
        st.session_state.stage = 0
        st.session_state.cleared = []
        st.session_state.started = False
        for i in range(len(stages)):
            st.session_state.pop(f"passed_{i}", None)
        st.rerun()

# -----------------------------
# 게임 화면
# -----------------------------
else:
    stage_index = st.session_state.stage
    stage = stages[stage_index]

    st.subheader("🗺️ 스테이지 진행 상황")
    progress_cols = st.columns(7)
    for i, col in enumerate(progress_cols):
        if i in st.session_state.cleared:
            col.success(f"✅ {i + 1}")
        elif i == stage_index:
            col.info(f"📍 {i + 1}")
        else:
            col.caption(f"🔒 {i + 1}")
    st.progress(len(st.session_state.cleared) / len(stages))

    st.divider()
    left, right = st.columns([0.9, 1.1], gap="large")

    with left:
        show_image(stage["image"])
        st.markdown(f"<h2 class='stage-title'>{stage['name']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center'><b>STAGE {stage_index + 1} / 7</b></p>", unsafe_allow_html=True)

    with right:
        st.subheader(f"📚 학습 개념: {stage['concept']}")
        st.markdown("**📖 스토리**")
        st.info(stage["story"])
        st.markdown("**💡 개념 배우기**")
        st.success(stage["lesson"])
        st.markdown("**🎯 미션**")
        st.warning(stage["question"])

    st.divider()
    st.subheader("⌨️ 코드 작성하기")
    code = st.text_area(
        "아래에 Python 코드를 작성해 봐!",
        value=stage["example"],
        height=190,
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
        st.success("🏆 경험치 획득! 다음 스테이지로 이동할 수 있어.")
        if st.button("다음 스테이지로 이동 ➡️" if stage_index < 6 else "👑 엔딩 확인하기"):
            st.session_state.stage += 1
            st.rerun()

st.divider()
st.caption("PYTHON QUEST · 파이썬 기초 학습 RPG")
