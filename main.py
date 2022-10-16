from flask import Flask, render_template
import utils


app = Flask(__name__)

@app.route('/')
def all_candidates():
    candidates = utils.get_candidates_all()
    return render_template('list_candidates.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def get_candidate(id):
    candidate = utils.get_candidate(id)
    if not candidate:
        return 'Не найдено'

    return render_template('single_candidate.html', candidate=candidate)


@app.route('/candidate/<skill_name>')
def get_candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    candidates_count = len(candidates)
    return render_template('skills_candidate.html',
                           candidates=candidates,
                           candidates_count=candidates_count,
                           skill_name=skill_name
                           )


@app.route('/search/<candidate_name>')
def get_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    candidates_count = len(candidates)
    return render_template('search_candidate.html',
                           candidates=candidates,
                           candidates_count=candidates_count,
                           )


if __name__ == '__main__':
    app.run(debug=True)
