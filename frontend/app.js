const form = document.getElementById('guessForm');
const resultDiv = document.getElementById('result');
const scoreDiv = document.getElementById('score');
const historyDiv = document.getElementById('history');
const restartButton = document.getElementById('restartButton');

// ⚡️ Change this to your deployed backend URL later
const BACKEND_URL = "https://your-backend-deployed-link/guess";

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

    resultDiv.innerHTML = `<h3>Result: ${data.result}</h3>`;
    scoreDiv.innerHTML = `<h3>Score: ${data.score}</h3>`;
    historyDiv.innerHTML = `<h3>Guess History: ${data.history.join(", ")}</h3>`;

    if (data.next_seed) {
      document.getElementById('seedWord').value = data.next_seed;
    }

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
});
