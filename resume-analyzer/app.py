from flask import Flask, render_template, request
from model import predict_role
from pdfminer.high_level import extract_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    prediction = ""
    found_skills = []
    filename = ""
    score = 0
    score_color = "gray"

    if request.method == "POST":

        file = request.files["resume"]
        filename = file.filename

        if file:
            filepath = "resume.pdf"
            file.save(filepath)

            text = extract_text(filepath)

            skill_list = [
                "python","java","c++","sql","pandas","numpy","machine learning",
                "deep learning","data analysis","html","css","javascript","react",
                "flask","django","powerbi","tableau","excel","tensorflow","pytorch"
            ]

            for skill in skill_list:
                if skill.lower() in text.lower():
                    found_skills.append(skill)

            prediction = predict_role(text)
            # check if resume has enough relevant skills
            if len(found_skills) < 2:
                prediction = "Resume does not match any supported job role. Please upload a technical resume."
            score = min(len(found_skills) * 10, 100)
            if score < 40:
                score_color = "red"
            elif score < 70:
                score_color = "orange"
            else:
                score_color = "green"
            
    return render_template(
    "index.html",
    prediction=prediction,
    skills=found_skills,
    filename=filename,
    score=score,
    score_color=score_color
)


if __name__ == "__main__":
    app.run(debug=True)