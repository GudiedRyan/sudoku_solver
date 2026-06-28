function Controls({
  mode,
  difficulty,
  onDifficultyChange,
  onNewGame,
  onHint,
  onSolve,
  status,
  hintCount,
  hintLoading,
  solveLoading,
  onEnterCreate,
  onExitCreate,
  onClearGrid,
  onCheckPuzzle,
  checkLoading,
}) {
  const isPlaying = status === 'playing'

  if (mode === 'create') {
    return (
      <div className="controls">
        <button className="btn" onClick={onExitCreate}>
          Back to Play
        </button>
        <button className="btn" onClick={onClearGrid}>
          Clear Grid
        </button>
        <button className="btn btn-primary" onClick={onCheckPuzzle} disabled={checkLoading}>
          {checkLoading ? (
            <span className="btn-loading">
              <span className="spinner" /> Checking...
            </span>
          ) : (
            'Check Puzzle'
          )}
        </button>
        <button className="btn" onClick={onHint} disabled={hintLoading}>
          {hintLoading ? (
            <span className="btn-loading">
              <span className="spinner" /> Thinking...
            </span>
          ) : (
            'Hint'
          )}
        </button>
        <button className="btn" onClick={onSolve} disabled={solveLoading}>
          {solveLoading ? (
            <span className="btn-loading">
              <span className="spinner" /> Solving...
            </span>
          ) : (
            'Solve'
          )}
        </button>
      </div>
    )
  }

  return (
    <div className="controls">
      <select
        className="difficulty-select"
        value={difficulty}
        onChange={e => onDifficultyChange(e.target.value)}
      >
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>
      <button className="btn btn-primary" onClick={onNewGame}>
        New Game
      </button>
      <button className="btn" onClick={onHint} disabled={!isPlaying || hintLoading}>
        {hintLoading ? (
          <span className="btn-loading">
            <span className="spinner" /> Thinking...
          </span>
        ) : (
          'Hint'
        )}
      </button>
      <button className="btn" onClick={onSolve} disabled={!isPlaying || solveLoading}>
        {solveLoading ? (
          <span className="btn-loading">
            <span className="spinner" /> Solving...
          </span>
        ) : (
          'Solve'
        )}
      </button>
      <button className="btn" onClick={onEnterCreate}>
        Create Puzzle
      </button>
    </div>
  )
}

export default Controls
