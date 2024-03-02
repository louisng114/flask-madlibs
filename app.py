from flask import Flask, request, render_template
from stories import Story, story_list, find_story


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", story_list=story_list)

@app.route("/form")
def form():
    chosen_story_id = request.args["stories"]
    chosen_story = find_story(chosen_story_id)
    return render_template("form.html", story_id=chosen_story.story_id, prompts=chosen_story.prompts)

@app.route("/story/<story_id>")
def story(story_id):
    answers = request.args
    chosen_story = find_story(story_id)
    template = chosen_story.template
    for prompt in answers:
        template = template.replace("{"+ prompt +"}", str(answers[prompt]))
    return render_template("story.html", template=template)
