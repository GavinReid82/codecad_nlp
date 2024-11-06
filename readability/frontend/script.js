async function calculateGrade() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });
    const result = await response.json();
    document.getElementById('result').innerText = result.grade;
}
