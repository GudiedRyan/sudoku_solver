import copy
import os
from flask import Flask, request, jsonify, send_from_directory
import full_sudoku as fs
from puzzles import get_puzzle

app = Flask(__name__, static_folder='static', static_url_path='')


def _reset_solver():
    fs.columns = []
    fs.boxes = [[], [], [], [], [], [], [], [], []]
    fs.change_list = []


def solve_puzzle(puzzle):
    _reset_solver()
    puzzle_copy = copy.deepcopy(puzzle)
    return fs.sudoku_king(puzzle_copy)


def hint_puzzle(puzzle):
    _reset_solver()
    puzzle_copy = copy.deepcopy(puzzle)
    return fs.sudoku_hint(puzzle_copy)


@app.route('/api/puzzle', methods=['GET'])
def get_puzzle_route():
    difficulty = request.args.get('difficulty', 'medium')
    if difficulty not in ('easy', 'medium', 'hard'):
        difficulty = 'medium'
    puzzle = get_puzzle(difficulty)
    return jsonify({'puzzle': puzzle, 'difficulty': difficulty})


@app.route('/api/hint', methods=['POST'])
def hint():
    data = request.get_json()
    if not data or 'puzzle' not in data:
        return jsonify({'error': 'Missing puzzle'}), 400
    result = hint_puzzle(data['puzzle'])
    if result == 'Unsolvable Puzzle' or result is False:
        return jsonify({'error': 'Puzzle is unsolvable from current state'}), 400
    return jsonify({'puzzle': result})


@app.route('/api/solve', methods=['POST'])
def solve():
    data = request.get_json()
    if not data or 'puzzle' not in data:
        return jsonify({'error': 'Missing puzzle'}), 400
    result = solve_puzzle(data['puzzle'])
    if result is False:
        return jsonify({'error': 'Puzzle is unsolvable from current state'}), 400
    return jsonify({'solution': result})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    full_path = os.path.join(app.static_folder, path)
    if path and os.path.isfile(full_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    # threaded=False keeps global solver state safe in development
    app.run(debug=True, port=5000, threaded=False)
