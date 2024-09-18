from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    required_midterm = None
    required_final = None
    is_pass_possible = True
    prelim_grade = None
    is_deans_lister_possible = False

    if request.method == 'POST':
        try:
            prelim_grade = float(request.form['prelim'])

            if prelim_grade < 0 or prelim_grade > 100:
                error = "Prelim grade must be between 0 and 100."
            else:
                passing_grade = 75
                deans_list_grade = 90
                prelim_contribution = 0.2 * prelim_grade
                remaining_grade_needed = passing_grade - prelim_contribution

                if remaining_grade_needed > 80:
                    is_pass_possible = False
                else:
                    required_midterm = (remaining_grade_needed * (0.3 / (0.3 + 0.5)))
                    required_final = (remaining_grade_needed * (0.5 / (0.3 + 0.5)))
                    if prelim_grade >= deans_list_grade:
                        is_deans_lister_possible = True

        except ValueError:
            error = "Please enter a valid number for the Prelim grade."

    return render_template('index.html', error=error, prelim_grade=prelim_grade, required_midterm=required_midterm, required_final=required_final, is_pass_possible=is_pass_possible, is_deans_lister_possible=is_deans_lister_possible)

if __name__ == '__main__':
    app.run(debug=True)
