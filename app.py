# from flask import Flask, jsonify, render_template
# import grid  # Import the grid logic

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/grid')
# def get_grid():
#     return jsonify(grid.grid)

# @app.route('/add_obstacle/<int:x>/<int:y>')
# def add_obstacle(x, y):
#     grid.add_obstacle(x, y)  # Update the grid
#     return jsonify(success=True)

# @app.route('/reroute/<int:start_x>/<int:start_y>/<int:goal_x>/<int:goal_y>')
# def reroute(start_x, start_y, goal_x, goal_y):
#     start = (start_x, start_y)
#     goal = (goal_x, goal_y)
#     path = grid.a_star_search(start, goal)
#     return jsonify(path=path)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, render_template
import grid  # Import the grid logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grid')
def get_grid():
    return jsonify(grid.grid)

@app.route('/add_obstacle/<int:x>/<int:y>')
def add_obstacle(x, y):
    if x < 0 or x >= grid.GRID_SIZE or y < 0 or y >= grid.GRID_SIZE:
        return jsonify(success=False, error="Invalid grid coordinates"), 400
    grid.add_obstacle(x, y)
    return jsonify(success=True)

@app.route('/reroute/<int:start_x>/<int:start_y>/<int:goal_x>/<int:goal_y>')
def reroute(start_x, start_y, goal_x, goal_y):
    start = (start_x, start_y)
    goal = (goal_x, goal_y)
    path = grid.a_star_search(start, goal)
    return jsonify(path=path)

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')

