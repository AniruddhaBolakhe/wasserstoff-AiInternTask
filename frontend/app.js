const form = document.getElementById('guessForm');
const resultDiv = document.getElementById('result');
const scoreDiv = document.getElementById('score');
const historyDiv = document.getElementById('history');
const restartButton = document.getElementById('restartButton');

const BACKEND_URL = "https://genai-backend-tp1g.onrender.com/guess";

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const sessionId = document.getElementById('sessionId').value;
  const seedWord = document.getElementById('seedWord').value;
  const guess = document.getElementById('guess').value;

  try {
    const response = await fetch(BACKEND_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        session_id: sessionId,
        seed: seedWord,
        guess: guess
      })
    });

    const data = await response.json();
    console.log(data);

    // ✅ Show the Gemini response verdict
    resultDiv.innerHTML = `<h3>${data.verdict}</h3>`;

    // ✅ Score and guess history
    scoreDiv.innerHTML = `<h3>Score: ${data.score}</h3>`;
    historyDiv.innerHTML = `<h3>Guess History: ${data.history.join(", ")}</h3>`;

    // ✅ Update the seed word field if a new one is given
    if (data.next_seed) {
      document.getElementById('seedWord').value = data.next_seed;
    }

    // Clear guess input
    document.getElementById('guess').value = '';

  } catch (error) {
    console.error('Error:', error);
    resultDiv.innerHTML = "<h3>Error connecting to backend.</h3>";
  }
});

restartButton.addEventListener('click', () => {
  document.getElementById('seedWord').value = "rock";
  resultDiv.innerHTML = '';
  scoreDiv.innerHTML = '';
  historyDiv.innerHTML = '';
  document.getElementById('guess').value = '';
});
