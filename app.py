
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PYTHON QUEST</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.js"></script>
</head>
<body>

<div class="game-container">

    <header>
        <h1>⚔️ PYTHON QUEST</h1>
        <p>코드의 힘으로 공주를 구하라!</p>
    </header>

    <main>

        <!-- 타이틀 화면 -->
        <section id="title-screen" class="screen active">
            <div class="illustration">🏰</div>
            <h2>전설의 코딩 모험</h2>
            <p>
                마왕에게 납치된 공주를 구하기 위해<br>
                파이썬의 힘을 익혀라!
            </p>
            <button onclick="startGame()">모험 시작</button>
        </section>

        <!-- 스토리 화면 -->
        <section id="story-screen" class="screen">
            <h2>📜 왕국의 위기</h2>
            <div class="illustration">👑</div>
            <div class="dialogue">
                <p id="story-text"></p>
            </div>
            <button onclick="nextStory()">다음</button>
        </section>

        <!-- 지도 화면 -->
        <section id="map-screen" class="screen">
            <h2>🗺️ 모험 지도</h2>
            <p>파이썬의 힘을 익혀 다섯 개의 관문을 통과하라!</p>

            <div class="stage-list">
                <div class="stage current">🌳 초보자의 숲 - print()</div>
                <div class="stage locked">🏘️ 시작의 마을 - 변수와 자료형</div>
                <div class="stage locked">🎒 아이템 동굴 - 리스트</div>
                <div class="stage locked">🕳️ 조건의 동굴 - if</div>
                <div class="stage locked">🌾 반복의 평원 - for</div>
                <div class="stage locked">🗼 함수의 탑 - def</div>
                <div class="stage locked">🏰 마왕의 성 - 종합 응용</div>
            </div>

            <button onclick="startFirstStage()">첫 번째 모험 시작</button>
        </section>

        <!-- 첫 번째 스테이지 -->
        <section id="stage-screen" class="screen">

            <div class="stage-heading">
                <span>🌳 초보자의 숲</span>
                <span class="level">LEVEL 1</span>
            </div>

            <div class="battle-area">
                <div class="monster">🟢</div>
                <h2>슬라임</h2>
                <div class="hp-bar">
                    <div id="monster-hp-fill"></div>
                </div>
                <p id="monster-hp-text">슬라임 HP: 100 / 100</p>
            </div>

            <div class="dialogue">
                <p id="battle-message">
                    슬라임이 나타났다! 파이썬의 힘으로 물리쳐라!
                </p>
            </div>

            <div class="lesson">
                <h3>📖 오늘의 파이썬 수업</h3>
                <h2>print()</h2>
                <p>
                    파이썬에서 <strong>print()</strong>는
                    화면에 글자를 출력하는 명령어야.
                </p>

                <div class="code-example">
                    <code>print("안녕하세요!")</code>
                </div>

                <p>실행 결과:</p>

                <div class="example-output">
                    안녕하세요!
                </div>

                <p class="tip">
                    💡 출력하고 싶은 글자는 큰따옴표 안에 넣어야 해!
                </p>
            </div>

            <div class="mission">
                <h3>⚔️ 첫 번째 코딩 퀘스트</h3>

                <p>
                    슬라임에게 인사해 보자!<br>
                    <strong>"안녕!"</strong> 이라는 글자를 출력하면 성공이야.
                </p>

                <textarea
                    id="python-code"
                    spellcheck="false"
                    placeholder="# 여기에 코드를 작성하세요"
                ></textarea>

                <button id="run-button" onclick="runPythonCode()">
                    ▶ 코드 실행
                </button>

                <div class="output-box">
                    <h4>💻 실행 결과</h4>
                    <pre id="output">아직 실행한 코드가 없어!</pre>
                </div>

                <p id="result-message"></p>
            </div>

            <button
                id="next-stage-button"
                class="hidden"
                onclick="completeFirstStage()"
            >
                다음 모험으로!
            </button>

        </section>

        <!-- 첫 번째 스테이지 성공 -->
        <section id="clear-screen" class="screen">
            <div class="illustration">🎉</div>
            <h2>첫 번째 관문 통과!</h2>
            <p>슬라임을 물리쳤어!</p>
            <p>새로운 파이썬 기술을 익혔어.</p>

            <div class="reward">
                <h3>획득 보상</h3>
                <p>⭐ 경험치 +100</p>
                <p>📘 print() 학습 완료</p>
            </div>

            <button onclick="showScreen('map-screen')">
                모험 지도 돌아가기
            </button>
        </section>

    </main>

    <footer>
        <p>PYTHON QUEST © 2026</p>
    </footer>

</div>

<script src="script.js"></script>

</body>
</html>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #121222;
    color: white;
    font-family: Arial, sans-serif;
    min-height: 100vh;
    padding: 25px 0;
    display: flex;
    justify-content: center;
}

.game-container {
    width: 92%;
    max-width: 850px;
    background: #24243b;
    border: 4px solid #7770c9;
    border-radius: 15px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 0 25px #655cc9;
}

header {
    margin-bottom: 35px;
}

header h1 {
    color: #ffe66d;
    font-size: 34px;
    letter-spacing: 2px;
}

header p {
    color: #c7c4ff;
    margin-top: 10px;
}

.screen {
    display: none;
    animation: appear 0.4s ease;
}

.screen.active {
    display: block;
}

h2 {
    color: #ffe66d;
    margin-bottom: 18px;
}

p {
    line-height: 1.8;
}

button {
    background: #7568dc;
    color: white;
    border: 2px solid #aaa0ff;
    border-radius: 8px;
    padding: 14px 25px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    margin: 18px 5px;
    transition: 0.2s;
}

button:hover {
    background: #968aff;
    transform: scale(1.04);
}

button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
}

.illustration {
    font-size: 90px;
    margin: 25px;
}

.dialogue {
    background: #30304b;
    border: 2px solid #55527f;
    border-radius: 10px;
    padding: 18px;
    margin: 20px 0;
}

.stage-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 25px 0;
}

.stage {
    background: #373653;
    border: 2px solid #55527f;
    border-radius: 8px;
    padding: 13px;
    font-weight: bold;
}

.stage.current {
    border-color: #ffe66d;
    color: #ffe66d;
}

.stage.locked {
    opacity: 0.4;
}

.stage-heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #ffe66d;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}

.level {
    background: #7568dc;
    color: white;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 13px;
}

.battle-area {
    background: #373653;
    border: 2px solid #7770c9;
    border-radius: 12px;
    padding: 20px;
}

.monster {
    font-size: 85px;
    animation: bounce 1.5s infinite;
}

.hp-bar {
    width: 85%;
    height: 13px;
    background: #171725;
    border-radius: 20px;
    margin: 12px auto;
    overflow: hidden;
}

#monster-hp-fill {
    width: 100%;
    height: 100%;
    background: #ff6565;
    transition: width 0.5s;
}

.lesson, .mission {
    background: #30304b;
    border: 2px solid #55527f;
    border-radius: 10px;
    padding: 20px;
    margin: 18px 0;
    text-align: left;
}

.lesson h3, .mission h3 {
    color: #ffe66d;
    margin-bottom: 15px;
}

.lesson h2 {
    color: #9dffb0;
    text-align: left;
}

.code-example, .example-output {
    background: #171725;
    padding: 14px;
    border-radius: 8px;
    margin: 12px 0;
    color: #9dffb0;
}

.tip {
    color: #ffe66d;
    font-size: 14px;
}

textarea {
    width: 100%;
    height: 140px;
    background: #171725;
    color: #9dffb0;
    border: 2px solid #7770c9;
    border-radius: 8px;
    padding: 15px;
    font-family: monospace;
    font-size: 15px;
    resize: vertical;
    margin-top: 15px;
}

.output-box {
    background: #171725;
    border: 2px solid #55527f;
    border-radius: 8px;
    padding: 15px;
    margin-top: 15px;
}

.output-box h4 {
    color: #ffe66d;
    margin-bottom: 10px;
}

#output {
    color: #9dffb0;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    min-height: 30px;
    font-family: monospace;
}

#result-message {
    text-align: center;
    font-weight: bold;
    margin-top: 15px;
}

.success {
    color: #9dffb0;
}

.error {
    color: #ff8585;
}

.reward {
    background: #373653;
    border: 2px solid #ffe66d;
    border-radius: 10px;
    padding: 20px;
    margin: 25px 0;
}

.reward h3 {
    color: #ffe66d;
    margin-bottom: 10px;
}

.hidden {
    display: none !important;
}

footer {
    margin-top: 40px;
    color: #9995c9;
    font-size: 12px;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-10px);
    }
}

@media (max-width: 550px) {
    .game-container {
        padding: 16px;
    }

    header h1 {
        font-size: 25px;
    }

    .stage-heading {
        font-size: 16px;
    }
}

const stories = [
    "평화롭던 왕국에 마왕이 나타났다!",
    "마왕은 공주를 납치해 어둠의 성으로 데려갔다.",
    "왕은 용사를 불러 왕국을 구해달라고 부탁했다.",
    "하지만 마왕을 물리치려면 파이썬의 힘이 필요하다.",
    "파이썬을 처음부터 배워 왕국을 구하자!"
];

let storyIndex = 0;
let pyodide = null;
let monsterDefeated = false;

function showScreen(screenId) {
    document.querySelectorAll(".screen").forEach(screen => {
        screen.classList.remove("active");
    });

    document.getElementById(screenId).classList.add("active");
}

function startGame() {
    storyIndex = 0;
    showScreen("story-screen");
    showStory();
}

function showStory() {
    document.getElementById("story-text").textContent =
        stories[storyIndex];
}

function nextStory() {
    storyIndex++;

    if (storyIndex < stories.length) {
        showStory();
    } else {
        showScreen("map-screen");
    }
}

function startFirstStage() {
    monsterDefeated = false;

    document.getElementById("python-code").value = "";

    document.getElementById("output").textContent =
        "아직 실행한 코드가 없어!";

    document.getElementById("result-message").textContent = "";
    document.getElementById("result-message").className = "";

    document.getElementById("battle-message").textContent =
        "슬라임이 나타났다! 파이썬의 힘으로 물리쳐라!";

    document.getElementById("monster-hp-fill").style.width = "100%";
    document.getElementById("monster-hp-text").textContent =
        "슬라임 HP: 100 / 100";

    document.getElementById("next-stage-button")
        .classList.add("hidden");

    document.getElementById("run-button").disabled = false;

    showScreen("stage-screen");
}

async function loadPython() {
    if (pyodide) {
        return pyodide;
    }

    document.getElementById("output").textContent =
        "파이썬 실행 환경을 불러오는 중...";

    pyodide = await loadPyodide();

    return pyodide;
}

async function runPythonCode() {
    if (monsterDefeated) return;

    const runButton = document.getElementById("run-button");
    const output = document.getElementById("output");
    const resultMessage = document.getElementById("result-message");

    const code = document.getElementById("python-code").value;

    runButton.disabled = true;

    output.textContent = "코드를 실행하는 중...";
    resultMessage.textContent = "";
    resultMessage.className = "";

    try {
        const python = await loadPython();

        python.globals.set("student_code", code);

        await python.runPythonAsync(`
import io
import contextlib

output_buffer = io.StringIO()

try:
    with contextlib.redirect_stdout(output_buffer):
        exec(compile(student_code, "<student>", "exec"), {})

    execution_result = output_buffer.getvalue()

except Exception as error:
    execution_result = "오류: " + str(error)
`);

        const result = python.globals.get("execution_result");
        const outputText = String(result);

        output.textContent =
            outputText || "(출력 결과가 없습니다.)";

        if (outputText.trim() === "안녕!") {
            monsterDefeated = true;

            document.getElementById("monster-hp-fill").style.width = "0%";

            document.getElementById("monster-hp-text").textContent =
                "슬라임 HP: 0 / 100";

            document.getElementById("battle-message").textContent =
                "슬라임이 쓰러졌다! 훌륭한 공격이야!";

            resultMessage.textContent =
                "🎉 정답! print() 명령어를 익혔어!";

            resultMessage.className = "success";

            document.getElementById("next-stage-button")
                .classList.remove("hidden");

        } else if (outputText.startsWith("오류:")) {
            resultMessage.textContent =
                "코드에 오류가 있어. 괄호와 따옴표를 확인해 보자!";

            resultMessage.className = "error";

        } else {
            resultMessage.textContent =
                "아직 정답이 아니야! print()를 사용해서 안녕!을 출력해 봐.";

            resultMessage.className = "error";
        }

    } catch (error) {
        output.textContent = String(error);

        resultMessage.textContent =
            "파이썬 실행 환경을 불러오지 못했어. 인터넷 연결을 확인해 줘.";

        resultMessage.className = "error";
    }

    runButton.disabled = monsterDefeated;
}

function completeFirstStage() {
    showScreen("clear-screen");
}
