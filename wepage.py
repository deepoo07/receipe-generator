from groq import Groq
from flask import Flask, render_template_string, request
import os

# Create Groq client
client = Groq(api_key=os.environ["GROQ_API_KEY"])

app = Flask(__name__)

def generate_tutorial(components):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"""
                Suggest a recipe using the items listed.
                Give it a nice name.
                Then give a funny version of the name.
                Then explain step-by-step.
                Here are the items: {components}
                """
            }
        ]
    )

    return response.choices[0].message.content


@app.route('/')
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>Recipe Generator</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
<script>
async function generateTutorial() {
    const output = document.querySelector("#output");
    output.textContent = "Cooking a recipe for you...";

    const response = await fetch("/generate", {
        method: "POST",
        body: new FormData(document.querySelector("#tutorial-form"))
    });

    const data = await response.text();
    output.textContent = data;
}
</script>
</head>

<body>
<div class="container mt-5">
    <h1 class="mb-4">Custom Recipe Tutorial Generator</h1>

    <form id="tutorial-form" onsubmit="event.preventDefault(); generateTutorial();">
        <input type="text" name="components" class="form-control"
        placeholder="Bread, eggs, butter..." required>
        <br>
        <button type="submit" class="btn btn-primary">
            Share with me a tutorial
        </button>
    </form>

    <div class="card mt-4">
        <div class="card-header">Output</div>
        <div class="card-body">
            <pre id="output" style="white-space: pre-wrap;"></pre>
        </div>
    </div>
</div>
</body>
</html>
""")


@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    return generate_tutorial(components)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)