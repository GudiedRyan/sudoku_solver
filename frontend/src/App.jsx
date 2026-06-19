import { useState, useEffect, useCallback } from 'react'
import Board from './components/Board'
import Controls from './components/Controls'
import NumberPad from './components/NumberPad'
import { fetchPuzzle, fetchHint, fetchSolution } from './api'
import './App.css'

function App() {
  const [originalPuzzle, setOriginalPuzzle] = useState(null)
  const [currentPuzzle, setCurrentPuzzle] = useState(null)
  const [selectedCell, setSelectedCell] = useState(null)
  const [difficulty, setDifficulty] = useState('medium')
  const [status, setStatus] = useState('idle')
  const [message, setMessage] = useState('')
  const [hintCount, setHintCount] = useState(0)

  const isSolved = useCallback(
    puzzle => puzzle && puzzle.every(row => row.every(cell => cell !== 0)),
    []
  )

  const loadPuzzle = useCallback(async diff => {
    setStatus('loading')
    setSelectedCell(null)
    setMessage('')
    try {
      const data = await fetchPuzzle(diff)
      const puzzle = data.puzzle.map(row => [...row])
      setOriginalPuzzle(puzzle.map(row => [...row]))
      setCurrentPuzzle(puzzle)
      setHintCount(0)
      setStatus('playing')
    } catch {
      setStatus('error')
      setMessage('Failed to load puzzle. Is the backend running?')
    }
  }, [])

  useEffect(() => {
    loadPuzzle(difficulty)
  }, [])

  const handleCellSelect = (row, col) => {
    if (status !== 'playing') return
    setSelectedCell({ row, col })
  }

  const fillCell = useCallback(
    num => {
      if (!selectedCell || status !== 'playing') return
      const { row, col } = selectedCell
      if (originalPuzzle[row][col] !== 0) return

      const next = currentPuzzle.map(r => [...r])
      next[row][col] = num
      setCurrentPuzzle(next)
      if (num !== 0 && isSolved(next)) {
        setStatus('solved')
        setMessage('Puzzle solved!')
        setSelectedCell(null)
      }
    },
    [selectedCell, currentPuzzle, originalPuzzle, status, isSolved]
  )

  const handleKeyDown = useCallback(
    e => {
      if (status !== 'playing') return
      if (!selectedCell) return
      const { row, col } = selectedCell

      const num = parseInt(e.key)
      if (num >= 1 && num <= 9) {
        fillCell(num)
      } else if (e.key === 'Backspace' || e.key === 'Delete' || e.key === '0') {
        fillCell(0)
      } else if (e.key === 'ArrowUp') {
        setSelectedCell({ row: Math.max(0, row - 1), col })
      } else if (e.key === 'ArrowDown') {
        setSelectedCell({ row: Math.min(8, row + 1), col })
      } else if (e.key === 'ArrowLeft') {
        setSelectedCell({ row, col: Math.max(0, col - 1) })
      } else if (e.key === 'ArrowRight') {
        setSelectedCell({ row, col: Math.min(8, col + 1) })
      }
    },
    [selectedCell, status, fillCell]
  )

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [handleKeyDown])

  const handleHint = async () => {
    if (status !== 'playing') return
    setMessage('')
    try {
      const data = await fetchHint(currentPuzzle)
      const next = data.puzzle
      setCurrentPuzzle(next)
      setHintCount(h => h + 1)
      if (isSolved(next)) {
        setStatus('solved')
        setMessage('Puzzle solved!')
        setSelectedCell(null)
      }
    } catch (e) {
      setMessage(e.message || 'Could not get hint')
    }
  }

  const handleSolve = async () => {
    if (status !== 'playing') return
    setMessage('')
    try {
      const data = await fetchSolution(currentPuzzle)
      setCurrentPuzzle(data.solution)
      setStatus('solved')
      setMessage('Puzzle solved!')
      setSelectedCell(null)
    } catch (e) {
      setMessage(e.message || 'Could not solve puzzle')
    }
  }

  const isNumberPadDisabled =
    !selectedCell ||
    (selectedCell && originalPuzzle?.[selectedCell.row]?.[selectedCell.col] !== 0)

  return (
    <div className="app">
      <h1>Sudoku</h1>
      <Controls
        difficulty={difficulty}
        onDifficultyChange={setDifficulty}
        onNewGame={() => loadPuzzle(difficulty)}
        onHint={handleHint}
        onSolve={handleSolve}
        status={status}
        hintCount={hintCount}
      />
      {message && (
        <div className={`message ${status === 'solved' ? 'success' : status === 'error' ? 'error' : ''}`}>
          {message}
        </div>
      )}
      {status === 'loading' && <div className="message">Loading puzzle...</div>}
      {currentPuzzle && (
        <>
          <Board
            puzzle={currentPuzzle}
            originalPuzzle={originalPuzzle}
            selectedCell={selectedCell}
            onCellSelect={handleCellSelect}
          />
          {status === 'playing' && (
            <NumberPad onNumber={fillCell} disabled={isNumberPadDisabled} />
          )}
        </>
      )}
    </div>
  )
}

export default App
