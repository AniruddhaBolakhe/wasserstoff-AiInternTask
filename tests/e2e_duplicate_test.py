# tests/e2e_duplicate_test.py

import requests

def test_duplicate_guess():
    session_id = "test_player"
    seed = "rock"
    guess = "paper"
    persona = "serious"

    url = "http://localhost:8000/guess"

    # First Guess (should succeed)
    res1 = requests.post(url, json={
        "session_id": session_id,
        "seed": seed,
        "guess": guess,
        "persona": persona
    })
    data1 = res1.json()
    assert "Game Over" not in data1["verdict"], "First guess should not cause Game Over"

    # Second Guess (should trigger Game Over)
    res2 = requests.post(url, json={
        "session_id": session_id,
        "seed": guess,  # Now guess becomes seed
        "guess": guess,  # Guessing same again
        "persona": persona
    })
    data2 = res2.json()
    assert "Game Over" in data2["verdict"], "Duplicate guess should trigger Game Over"

    print("End-to-end duplicate guess test passed.")

if __name__ == "__main__":
    test_duplicate_guess()
