function Controls({ difficulty, onDifficultyChange, onNewGame, onHint, onSolve, status, hintCount, hintLoading, solveLoading }) {
  const isPlaying = status === 'playing'

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
        ) : hintCount > 0 ? (
          `Hint (${hintCount})`
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
    </div>
  )
}

export default Controls
