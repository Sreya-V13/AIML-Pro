from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Sample dataset of skills
skills_data = pd.DataFrame({
    'Skill Name': ['HTML', 'CSS', 'JavaScript', 'React.js', 'Python', 'Generative AI', 'Node.js', 'Django', 'Machine Learning', 'SQL'],
    'Domain': ['Web Development', 'Web Development', 'Web Development', 'Web Development', 'Data Science/AI', 'AI', 'Web Development', 'Data Science/AI', 'Data Science/AI', 'Database'],
    'Level': ['Beginner', 'Intermediate', 'Beginner', 'Intermediate', 'Beginner', 'Advanced', 'Intermediate', 'Intermediate', 'Advanced', 'Beginner'],
    'Learning Path': ['HTML Basics → Forms → CSS Basics', 'Selectors → Flexbox → Grid Layout', 'Variables → Loops → DOM Manipulation', 'Components → State → Props → Hooks', 'Syntax → Data Structures → Libraries', 'AI Concepts → Model Training → Deployment', 'Basics → Express.js → REST APIs', 'Python Basics → MVC → REST APIs', 'Data Preprocessing → Models → Evaluation', 'Basics → Queries → Joins'],
    'Duration (hours)': [10, 12, 15, 20, 15, 25, 18, 22, 30, 12]
})

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Route for About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Skills Page
@app.route('/skills')
def skills():
    return render_template('skills.html', skills=skills_data)

# Route for generating roadmap (simple mockup here)
@app.route('/roadmap/<skill_name>')
def roadmap(skill_name):
    skill_info = skills_data[skills_data['Skill Name'] == skill_name].to_dict(orient='records')[0]
    return render_template('roadmap.html', skill=skill_info)


# New Route for Start Learning
@app.route('/start-learning/<skill_name>')
def start_learning(skill_name):
    return f"<h1>You're now learning {skill_name}!</h1><p>Keep going and complete the course.</p>"


if __name__ == "__main__":
    app.run(debug=True)
