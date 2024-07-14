from flask import Flask, render_template

htmlPage = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Importance of Healthy Eating</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        header {
            background: #0073e6;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        nav {
            background: #333;
            color: #fff;
            padding: 0.5rem;
            text-align: center;
        }
        nav a {
            color: #fff;
            margin: 0 1rem;
            text-decoration: none;
        }
        section {
            padding: 2rem;
        }
        h2 {
            color: #0073e6;
        }
        .content {
            display: flex;
            flex-wrap: wrap;
        }
        .content article {
            flex: 1;
            margin: 1rem;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>The Importance of Healthy Eating</h1>
    </header>
    <nav>
        <a href="#introduction">Introduction</a>
        <a href="#benefits">Benefits</a>
        <a href="#foods">Healthy Foods</a>
        <a href="#tips">Tips</a>
    </nav>
    <section id="introduction">
        <h2>Introduction</h2>
        <p>Healthy eating is essential for maintaining a healthy body and mind. It involves consuming a balanced diet that provides all the necessary nutrients for growth, energy, and overall well-being. In this article, we will explore the importance of healthy eating, the benefits it brings, and some tips to incorporate healthier choices into your daily routine.</p>
    </section>
    <section id="benefits">
        <h2>Benefits of Healthy Eating</h2>
        <div class="content">
            <article>
                <h3>Improved Mental Health</h3>
                <p>A balanced diet can have a positive impact on your mental health. Nutrient-rich foods like fruits, vegetables, and whole grains provide the vitamins and minerals that support brain function and can improve mood and reduce the risk of mental health disorders.</p>
            </article>
            <article>
                <h3>Increased Energy Levels</h3>
                <p>Eating a variety of healthy foods ensures that your body gets the energy it needs to perform daily activities. Complex carbohydrates, lean proteins, and healthy fats provide sustained energy, helping you stay active and productive throughout the day.</p>
            </article>
            <article>
                <h3>Reduced Risk of Chronic Diseases</h3>
                <p>A diet rich in fruits, vegetables, and whole grains can lower the risk of chronic diseases such as heart disease, diabetes, and certain cancers. These foods are high in antioxidants, fiber, and other nutrients that protect the body against harmful conditions.</p>
            </article>
        </div>
    </section>
    <section id="foods">
        <h2>Healthy Foods to Include in Your Diet</h2>
        <ul>
            <li>Fruits and Vegetables: Aim for a variety of colors and types to ensure a wide range of nutrients.</li>
            <li>Whole Grains: Choose whole grains like brown rice, quinoa, and whole wheat bread over refined grains.</li>
            <li>Lean Proteins: Incorporate lean proteins such as chicken, fish, beans, and legumes.</li>
            <li>Healthy Fats: Include sources of healthy fats like avocados, nuts, seeds, and olive oil.</li>
            <li>Dairy or Dairy Alternatives: Opt for low-fat or non-dairy alternatives that are fortified with calcium and vitamin D.</li>
        </ul>
    </section>
    <section id="tips">
        <h2>Tips for Healthy Eating</h2>
        <ul>
            <li>Plan Your Meals: Plan your meals ahead of time to ensure you have healthy options available.</li>
            <li>Stay Hydrated: Drink plenty of water throughout the day to stay hydrated and support overall health.</li>
            <li>Read Labels: Pay attention to food labels to make informed choices about what you are eating.</li>
            <li>Limit Processed Foods: Reduce your intake of processed and sugary foods that can negatively impact your health.</li>
            <li>Practice Moderation: Enjoy all foods in moderation and avoid restrictive diets that can lead to unhealthy eating habits.</li>
        </ul>
    </section>
    <footer>
        <p>&copy; 2024 Healthy Living. All rights reserved.</p>
    </footer>
</body>
</html>
"""

app = Flask(__name__)

@app.route("/")
def index():
    return htmlPage


if __name__ == '__main__':
    app.run(host="0.0.0.0")

