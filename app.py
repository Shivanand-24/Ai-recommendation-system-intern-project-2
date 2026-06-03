from flask import Flask, render_template, request, redirect, url_for, flash
from model import DataModel

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'ai-data-classification-secret'

# Build the data model and train the Decision Tree classifier at startup
ml_model = DataModel()
previous_predictions = []


@app.route('/')
def index():
    stats = ml_model.summary
    return render_template(
        'index.html',
        title='AI Data Classification System',
        accuracy_score=stats['accuracy'],
        rows=stats['rows'],
        cols=stats['cols'],
        preview=stats['preview'],
    )


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            sepal_length = request.form.get('sepal_length', '').strip()
            sepal_width = request.form.get('sepal_width', '').strip()
            petal_length = request.form.get('petal_length', '').strip()
            petal_width = request.form.get('petal_width', '').strip()

            if not all([sepal_length, sepal_width, petal_length, petal_width]):
                flash('All measurement fields are required.', 'error')
                return redirect(url_for('predict'))

            features = [
                float(sepal_length),
                float(sepal_width),
                float(petal_length),
                float(petal_width),
            ]

            predicted_class, confidence, accuracy = ml_model.predict(features)
            record = {
                'input': features,
                'prediction': predicted_class,
                'confidence': f'{confidence:.2%}',
                'accuracy': f'{accuracy:.2%}',
            }
            previous_predictions.insert(0, record)
            if len(previous_predictions) > 8:
                previous_predictions.pop()

            return render_template(
                'result.html',
                prediction=predicted_class,
                confidence=f'{confidence:.2%}',
                accuracy=f'{accuracy:.2%}',
                input_values=features,
                previous_predictions=previous_predictions,
            )
        except ValueError:
            flash('Please enter valid numeric values for each field.', 'error')
            return redirect(url_for('predict'))

    return render_template('predict.html', title='Predict Iris Species')


if __name__ == '__main__':
    app.run(debug=True)
