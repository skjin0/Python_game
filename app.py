
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
        <section id="title-screen" class="screen active">
            <div class="illustration">🏰</div>
            <h2>전설의 코딩 모험</h2>
            <p>마왕에게 납치된 공주를 구하기 위해<br>파이썬의 힘을 익혀라!</p>
            <button id="start-button">모험 시작</button>
        </section>

        <section id="story-screen" class="screen">
            <h2>📜 왕국의 위기</h2>
            <div class="illustration">👑</div>
            <div class="dialogue">
                <p id="story-text"></p>
            </div>
            <button id="story-next">다음</button>
        </section>

        <section id="map-screen" class="screen">
            <h2>🗺️ 모험 지도</h2>
            <p>파이썬의 힘을 익혀 모든 관문을 통과하라!</p>
            <div id="stage-list" class="stage-list"></div>
        </section>

        <section id="stage-screen" class="screen">
            <div class="stage-heading">
                <span id="stage-name"></span>
                <span id="stage-level" class="level"></span>
            </div>

            <div class="battle-area">
                <div id="monster" class="monster">🟢</div>
                <h2 id="monster-name"></h2>
                <div class="hp-bar">
                    <div id="monster-hp-fill"></div>
                </div>
                <p id="monster-hp-text"></p>
            </div>

            <div class="dialogue">
                <p id="battle-message"></p>
            </div>

            <div class="lesson">
                <h3>📖 오늘의 파이썬 수업</h3>
                <h2 id="lesson-title"></h2>
                <p id="lesson-description"></p>
                <pre id="lesson-example"></pre>
                <p id="lesson-tip" class="tip"></p>
            </div>

            <div class="mission">
                <h3>⚔️ 코딩 퀘스트</h3>
                <p id="mission-description"></p>

                <textarea id="python-code"
                    spellcheck="false"
                    placeholder="# 여기에 파이썬 코드를 작성하세요"></textarea>

                <button id="run-button">▶ 코드 실행</button>

                <div class="output-box">
                    <h4>💻 실행 결과</h4>
                    <pre id="output">아직 실행한 코드가 없어!</pre>
                </div>

                <p id="result-message"></p>
            </div>

            <button id="next-stage-button" class="hidden">
                보상 획득!
            </button>
            <button id="map-button" class="secondary-button">
                지도 돌아가기
            </button>
        </section>

        <section id="clear-screen" class="screen">
            <div class="illustration">🎉</div>
            <h2 id="clear-title">관문 통과!</h2>
            <p id="clear-description"></p>
            <div class="reward">
                <h3>획득 보상</h3>
                <p id="clear-reward"></p>
            </div>
            <button id="clear-next-button">다음 모험으로!</button>
        </section>

        <section id="ending-screen" class="screen">
            <div class="illustration">👑</div>
            <h2>왕국을 구한 용사!</h2>
            <p>
                마왕을 물리치고 공주를 구했어!<br>
                이제 너는 파이썬의 진정한 용사야.
            </p>
            <div class="reward">
                <h3>🏆 최종 업적</h3>
                <p>print() 학습 완료</p>
                <p>변수와 자료형 학습 완료</p>
                <p>리스트 학습 완료</p>
                <p>조건문 학습 완료</p>
                <p>반복문 학습 완료</p>
                <p>함수 학습 완료</p>
                <p>종합 응용 완료</p>
            </div>
            <button id="ending-map-button">모험 지도 보기</button>
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
    margin: 15px 5px;
    transition: 0.2s;
}

button:hover {
    background: #968aff;
    transform: scale(1.03);
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
    padding: 14px;
    font-weight: bold;
    text-align: left;
    width: 100%;
    margin: 0;
}

.stage.current {
    border-color: #ffe66d;
    color: #ffe66d;
}

.stage.completed {
    border-color: #80dfa0;
    color: #80dfa0;
}

.stage.locked {
    opacity: 0.4;
    cursor: not-allowed;
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

pre {
    background: #171725;
    color: #9dffb0;
    padding: 14px;
    border-radius: 8px;
    margin: 12px 0;
    overflow-x: auto;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    line-height: 1.6;
}

.tip {
    color: #ffe66d;
    font-size: 14px;
}

textarea {
    width: 100%;
    height: 155px;
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
    min-height: 35px;
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

.secondary-button {
    background: #44445d;
    border-color: #77778f;
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

const stages = [
    {
        name: "초보자의 숲",
        level: "LEVEL 1",
        monster: "🟢",
        enemy: "슬라임",
        lesson: "print()",
        description: "print()는 화면에 글자나 값을 출력하는 명령어야.",
        example: 'print("안녕하세요!")',
        tip: "글자를 출력할 때는 따옴표 안에 글자를 넣어야 해!",
        mission: '"안녕!"이라는 글자를 출력하는 코드를 작성해 봐.',
        answer: "안녕!",
        reward: "print() 학습 완료",
        message: "슬라임이 나타났다! 먼저 인사해 보자!"
    },
    {
        name: "시작의 마을",
        level: "LEVEL 2",
        monster: "👾",
        enemy: "장난꾸러기 고블린",
        lesson: "변수와 자료형",
        description: "변수는 데이터를 저장하는 상자와 같아. 이름을 붙여 값을 저장할 수 있어.",
        example: 'name = "용사"\nprint(name)',
        tip: "문자열은 따옴표로 감싸고, 변수 이름으로 저장한 값을 사용할 수 있어!",
        mission: 'name 변수에 "용사"를 저장하고, name을 출력해 봐.',
        answer: "용사",
        reward: "변수와 자료형 학습 완료",
        message: "고블린이 나타났다! 변수에 용사의 이름을 저장해 보자!"
    },
    {
        name: "아이템 동굴",
        level: "LEVEL 3",
        monster: "🦇",
        enemy: "동굴 박쥐",
        lesson: "리스트(List)",
        description: "리스트는 여러 개의 데이터를 하나의 변수에 모아 저장하는 방법이야.",
        example: 'items = ["검", "물약", "방패"]\nprint(items[0])',
        tip: "리스트의 첫 번째 데이터 번호는 0이야. 따라서 두 번째 데이터는 [1]로 불러와!",
        mission: 'items 리스트에서 두 번째 아이템인 "물약"을 출력해 봐.',
        answer: "물약",
        reward: "리스트 학습 완료",
        message: "박쥐가 나타났다! 가방에서 물약을 찾아보자!"
    },
    {
        name: "조건의 동굴",
        level: "LEVEL 4",
        monster: "👹",
        enemy: "동굴 수호자",
        lesson: "조건문(if)",
        description: "if는 어떤 조건이 참인지 확인하고, 참일 때 정해진 코드를 실행해.",
        example: 'key = True\n\nif key:\n    print("문이 열렸다!")',
        tip: "if 다음에는 조건을 쓰고, 다음 줄의 실행 코드는 들여쓰기를 해야 해!",
        mission: 'key가 True일 때 "문이 열렸다!"를 출력하는 조건문을 작성해 봐.',
        answer: "문이 열렸다!",
        reward: "조건문 학습 완료",
        message: "수호자가 길을 막았다! 열쇠가 있는지 확인해 보자!"
    },
    {
        name: "반복의 평원",
        level: "LEVEL 5",
        monster: "👺",
        enemy: "오크 군단",
        lesson: "반복문(for)",
        description: "for는 리스트와 같은 여러 데이터의 항목을 하나씩 꺼내 반복해서 실행해.",
        example: 'for i in range(3):\n    print("안녕!")',
        tip: "range(3)은 0부터 2까지, 총 3번 반복해!",
        mission: '"슬라임"이라는 글자가 세 번 출력되도록 for 반복문을 작성해 봐.',
        answer: "슬라임\n슬라임\n슬라임",
        reward: "반복문 학습 완료",
        message: "오크 군단이 나타났다! 반복 공격으로 물리쳐 보자!"
    },
    {
        name: "함수의 탑",
        level: "LEVEL 6",
        monster: "🧙",
        enemy: "마법사",
        lesson: "함수(def)",
        description: "def는 내가 원하는 기능을 함수로 만드는 명령어야. 함수를 만들고 이름을 불러 실행할 수 있어.",
        example: 'def hello():\n    print("안녕!")\n\nhello()',
        tip: "함수를 정의하는 것만으로는 실행되지 않아. 마지막에 함수 이름을 불러야 해!",
        mission: 'hello라는 함수를 만들고 실행해서 "마법 발동!"을 출력해 봐.',
        answer: "마법 발동!",
        reward: "함수 학습 완료",
        message: "마법사가 나타났다! 새로운 마법 함수를 만들어 보자!"
    },
    {
        name: "마왕의 성",
        level: "FINAL",
        monster: "👿",
        enemy: "마왕",
        lesson: "파이썬 종합 응용",
        description: "지금까지 배운 리스트, 조건문, 반복문, 함수를 함께 사용해 보자!",
        example: 'enemies = ["슬라임", "마왕"]\n\ndef attack(items):\n    for item in items:\n        if item == "마왕":\n            print("왕국을 구했다!")\n\nattack(enemies)',
        tip: "함수 안에 반복문을 넣고, 반복문 안에서 조건문을 사용해 보자!",
        mission: 'enemies 리스트, attack 함수, for 반복문, if 조건문을 모두 사용해서 마왕을 발견하면 "왕국을 구했다!"를 출력해 봐.',
        answer: "왕국을 구했다!",
        reward: "파이썬 종합 응용 완료",
        message: "마왕이 나타났다! 지금까지 배운 모든 기술을 사용하자!"
    }
];

let storyIndex = 0;
let currentStage = 0;
let unlockedStage = 0;
let completedStages = [];
let pyodide = null;
let isRunning = false;

const $ = id => document.getElementById(id);

function showScreen(screenId) {
    document.querySelectorAll(".screen").forEach(screen => {
        screen.classList.remove("active");
    });

    $(screenId).classList.add("active");
}

function startGame() {
    storyIndex = 0;
    showScreen("story-screen");
    showStory();
}

function showStory() {
    $("story-text").textContent = stories[storyIndex];
}

function nextStory() {
    storyIndex++;

    if (storyIndex < stories.length) {
        showStory();
    } else {
        renderMap();
        showScreen("map-screen");
    }
}

function renderMap() {
    const list = $("stage-list");
    list.innerHTML = "";

    stages.forEach((stage, index) => {
        const button = document.createElement("button");
        button.className = "stage";

        if (completedStages.includes(index)) {
            button.classList.add("completed");
            button.textContent = "✅ " + stage.name + " - 완료";
        } else if (index === unlockedStage) {
            button.classList.add("current");
            button.textContent = "⚔️ " + stage.name + " - 도전 가능";
        } else {
            button.classList.add("locked");
            button.textContent = "🔒 " + stage.name + " - 잠김";
            button.disabled = true;
        }

        if (index <= unlockedStage) {
            button.addEventListener("click", () => startStage(index));
        }

        list.appendChild(button);
    });
}

function startStage(index) {
    currentStage = index;

    const stage = stages[index];

    $("stage-name").textContent = stage.name;
    $("stage-level").textContent = stage.level;

    $("monster").textContent = stage.monster;
    $("monster-name").textContent = stage.enemy;
    $("monster-hp-fill").style.width = "100%";
    $("monster-hp-text").textContent = "적 HP: 100 / 100";

    $("battle-message").textContent = stage.message;

    $("lesson-title").textContent = stage.lesson;
    $("lesson-description").textContent = stage.description;
    $("lesson-example").textContent = stage.example;
    $("lesson-tip").textContent = "💡 " + stage.tip;

    $("mission-description").textContent = stage.mission;

    $("python-code").value = "";
    $("output").textContent = "아직 실행한 코드가 없어!";
    $("result-message").textContent = "";
    $("result-message").className = "";

    $("run-button").disabled = false;
    $("next-stage-button").classList.add("hidden");

    showScreen("stage-screen");
}

async function loadPython() {
    if (pyodide) {
        return pyodide;
    }

    $("output").textContent = "파이썬 실행 환경을 불러오는 중...";

    pyodide = await loadPyodide();

    return pyodide;
}

async function runPythonCode() {
    if (isRunning || completedStages.includes(currentStage)) {
        return;
    }

    isRunning = true;

    const stage = stages[currentStage];
    const code = $("python-code").value;

    $("run-button").disabled = true;
    $("output").textContent = "코드를 실행하는 중...";
    $("result-message").textContent = "";

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

        $("output").textContent =
            outputText || "(출력 결과가 없습니다.)";

        if (outputText.trim() === stage.answer) {
            completeStage();
        } else if (outputText.startsWith("오류:")) {
            $("result-message").textContent =
                "코드에 오류가 있어! 다시 확인해 보자.";

            $("result-message").className = "error";
        } else {
            $("result-message").textContent =
                "아직 정답이 아니야! 수업 내용을 다시 확인해 보자.";

            $("result-message").className = "error";
        }

    } catch (error) {
        $("output").textContent = String(error);

        $("result-message").textContent =
            "파이썬 실행 환경을 불러오지 못했어. 인터넷 연결을 확인해 줘.";

        $("result-message").className = "error";
    }

    isRunning = false;

    if (!completedStages.includes(currentStage)) {
        $("run-button").disabled = false;
    }
}

function completeStage() {
    const stage = stages[currentStage];

    completedStages.push(currentStage);

    $("monster-hp-fill").style.width = "0%";
    $("monster-hp-text").textContent = "적 HP: 0 / 100";

    $("battle-message").textContent =
        stage.enemy + "을(를) 물리쳤다!";

    $("result-message").textContent =
        "🎉 정답! " + stage.lesson + " 학습 성공!";

    $("result-message").className = "success";

    $("run-button").disabled = true;
    $("next-stage-button").classList.remove("hidden");
}

function continueAfterClear() {
    $("clear-title").textContent =
        stages[currentStage].level === "FINAL"
            ? "최종 관문 통과!"
            : "관문 통과!";

    $("clear-description").textContent =
        stages[currentStage].enemy + "을(를) 물리쳤어!";

    $("clear-reward").textContent =
        "⭐ 경험치 +100\n📘 " + stages[currentStage].reward;

    if (currentStage === stages.length - 1) {
        $("clear-next-button").textContent = "엔딩 보기";
    } else {
        $("clear-next-button").textContent = "다음 모험으로!";
    }

    showScreen("clear-screen");
}

function goToNextStage() {
    if (currentStage === stages.length - 1) {
        showScreen("ending-screen");
        return;
    }

    unlockedStage = Math.max(unlockedStage, currentStage + 1);
    renderMap();
    showScreen("map-screen");
}

$("start-button").addEventListener("click", startGame);
$("story-next").addEventListener("click", nextStory);
$("run-button").addEventListener("click", runPythonCode);
$("next-stage-button").addEventListener("click", continueAfterClear);
$("clear-next-button").addEventListener("click", goToNextStage);

$("map-button").addEventListener("click", () => {
    renderMap();
    showScreen("map-screen");
});

$("ending-map-button").addEventListener("click", () => {
    renderMap();
    showScreen("map-screen");
});

renderMap();
