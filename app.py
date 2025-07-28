from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        name = request.form['name']
        place = request.form['place']
        object_ = request.form['object']
        animal = request.form['animal']
        action = request.form['action']

        # Story template
        story = f"""
        One sunny day, {name} packed their bag and headed to {place}.<br><br>
        In their bag, they carried a very special {object_} that they believed would help them {action} a wild {animal}.<br><br>
        As they entered {place}, they were met with strange noises and rustling trees.<br><br>
        Suddenly, a {animal} appeared, looking curious and hungry.<br><br>
        Without hesitation, {name} held out the {object_} and tried to {action} the creature.<br><br>
        It worked! The {animal} smiled and became their friend.<br><br>
        From that day on, {name} and the {animal} explored {place} together, sharing many more adventures.
        """

        return render_template('story.html', story=story)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
