import copy
import os
import uuid
from flask import Flask, request, jsonify, send_from_directory
import full_sudoku as fs
from puzzles import get_puzzle, get_default_puzzle

app = Flask(__name__, static_folder='static', static_url_path='')

# Maps puzzle_id -> solved grid, so repeat hints/solves on the same puzzle
# can skip re-running the backtracking solver.
SOLUTION_CACHE = {}


def _matches_solution(puzzle, solution):
    return all(
        puzzle[r][c] == 0 or puzzle[r][c] == solution[r][c]
        for r in range(9) for c in range(9)
    )


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
    initial = request.args.get('initial') == 'true'
    puzzle, solution = get_default_puzzle(difficulty) if initial else get_puzzle(difficulty)
    puzzle_id = str(uuid.uuid4())
    SOLUTION_CACHE[puzzle_id] = solution
    return jsonify({'puzzle': puzzle, 'difficulty': difficulty, 'puzzleId': puzzle_id})


@app.route('/api/hint', methods=['POST'])
def hint():
    data = request.get_json()
    if not data or 'puzzle' not in data:
        return jsonify({'error': 'Missing puzzle'}), 400
    puzzle = data['puzzle']

    solution = SOLUTION_CACHE.get(data.get('puzzleId'))
    if solution and _matches_solution(puzzle, solution):
        next_puzzle = [row[:] for row in puzzle]
        for r in range(9):
            for c in range(9):
                if next_puzzle[r][c] == 0:
                    next_puzzle[r][c] = solution[r][c]
                    return jsonify({'puzzle': next_puzzle})
        return jsonify({'puzzle': next_puzzle})

    result = hint_puzzle(puzzle)
    if result == 'Unsolvable Puzzle' or result is False:
        return jsonify({'error': 'Puzzle is unsolvable from current state'}), 400
    return jsonify({'puzzle': result})


@app.route('/api/solve', methods=['POST'])
def solve():
    data = request.get_json()
    if not data or 'puzzle' not in data:
        return jsonify({'error': 'Missing puzzle'}), 400
    puzzle = data['puzzle']

    solution = SOLUTION_CACHE.get(data.get('puzzleId'))
    if solution and _matches_solution(puzzle, solution):
        return jsonify({'solution': copy.deepcopy(solution)})

    result = solve_puzzle(puzzle)
    if result is False:
        return jsonify({'error': 'Puzzle is unsolvable from current state'}), 400
    return jsonify({'solution': result})


@app.route('/api/check', methods=['POST'])
def check_puzzle():
    data = request.get_json()
    if not data or 'puzzle' not in data:
        return jsonify({'error': 'Missing puzzle'}), 400
    puzzle = data['puzzle']

    if fs.has_contradiction(puzzle):
        return jsonify({'result': 'invalid'})

    count, solution = fs.count_solutions(puzzle, limit=2)
    if count == 0:
        return jsonify({'result': 'unsolvable'})
    if count == 1:
        return jsonify({'result': 'unique', 'solution': solution})
    return jsonify({'result': 'multiple'})


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
