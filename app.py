from flask import Flask, jsonify, render_template
import grid  # Import grid logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grid')
def get_grid():
    return jsonify(grid.grid)

@app.route('/add_obstacle/<int:x>/<int:y>')
def add_obstacle(x, y):
    grid.grid[x][y] = 1  # Set obstacle at (x, y)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
