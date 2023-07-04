from flask import Flask, render_template
import utils

app = Flask(__name__, template_folder='templates/')
candidates = utils.load_candidates_from_json()


@app.route("/")
def page_index():
    return render_template('main.html', candidates=candidates)


@app.route("/candidate/<candidate_name>")
def page_candidate(candidate_name):
    candidate = utils.get_candidates_by_name(candidate_name, candidates)
    return render_template('candidate.html', candidate=candidate[0])


@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    correct_candidates = utils.get_candidates_by_name(candidate_name, candidates)
    return render_template('search_name.html',
                           count_candidates=len(correct_candidates),
                           candidates=correct_candidates)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    correct_skills = utils.get_candidates_by_skill(skill_name, candidates)
    return render_template('skills.html',
                           skill_name=skill_name,
                           count_skill=len(correct_skills),
                           candidates=correct_skills)


app.run()
