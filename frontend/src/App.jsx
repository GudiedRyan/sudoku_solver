import { useState, useEffect, useCallback } from 'react'
import Board from './components/Board'
import Controls from './components/Controls'
import NumberPad from './components/NumberPad'
import { fetchPuzzle, fetchHint, fetchSolution, checkPuzzle } from './api'
import './App.css'

const emptyGrid = () => Array.from({ length: 9 }, () => Array(9).fill(0))

function App() {
  const [darkMode, setDarkMode] = useState(() => {
    const saved = localStorage.getItem('theme')
    if (saved) return saved === 'dark'
    return window.matchMedia('(prefers-color-scheme: dark)').matches
  })

  useEffect(() => {
    document.documentElement.dataset.theme = darkMode ? 'dark' : 'light'
    localStorage.setItem('theme', darkMode ? 'dark' : 'light')
  }, [darkMode])

  const [mode, setMode] = useState('play')
  const [originalPuzzle, setOriginalPuzzle] = useState(null)
  const [currentPuzzle, setCurrentPuzzle] = useState(null)
  const [createGrid, setCreateGrid] = useState(emptyGrid)
  const [selectedCell, setSelectedCell] = useState(null)
  const [difficulty, setDifficulty] = useState('medium')
  const [status, setStatus] = useState('idle')
  const [message, setMessage] = useState('')
  const [messageType, setMessageType] = useState('')
  const [hintCount, setHintCount] = useState(0)
  const [hintLoading, setHintLoading] = useState(false)
  const [solveLoading, setSolveLoading] = useState(false)
  const [checkLoading, setCheckLoading] = useState(false)
  const [puzzleId, setPuzzleId] = useState(null)

  const isSolved = useCallback(
    puzzle => puzzle && puzzle.every(row => row.every(cell => cell !== 0)),
    []
  )

  const loadPuzzle = useCallback(async (diff, initial = false) => {
    setStatus('loading')
    setSelectedCell(null)
    setMessage('')
    setMessageType('')
    try {
      const data = await fetchPuzzle(diff, initial)
      const puzzle = data.puzzle.map(row => [...row])
      setOriginalPuzzle(puzzle.map(row => [...row]))
      setCurrentPuzzle(puzzle)
      setPuzzleId(data.puzzleId)
      setHintCount(0)
      setStatus('playing')
    } catch {
      setStatus('error')
      setMessage('Failed to load puzzle. Is the backend running?')
      setMessageType('error')
    }
  }, [])

  useEffect(() => {
    loadPuzzle(difficulty, true)
  }, [])

  const handleCellSelect = (row, col) => {
    if (mode === 'play' && status !== 'playing') return
    setSelectedCell({ row, col })
  }

  const fillCell = useCallback(
    num => {
      if (!selectedCell) return
      const { row, col } = selectedCell

      if (mode === 'create') {
        const next = createGrid.map(r => [...r])
        next[row][col] = num
        setCreateGrid(next)
        return
      }

      if (status !== 'playing') return
      if (originalPuzzle[row][col] !== 0) return

      const next = currentPuzzle.map(r => [...r])
      next[row][col] = num
      setCurrentPuzzle(next)
      if (num !== 0 && isSolved(next)) {
        setStatus('solved')
        setMessage('Puzzle solved!')
        setMessageType('success')
        setSelectedCell(null)
      }
    },
    [selectedCell, mode, createGrid, currentPuzzle, originalPuzzle, status, isSolved]
  )

  const handleKeyDown = useCallback(
    e => {
      if (mode === 'play' && status !== 'playing') return
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
    [selectedCell, mode, status, fillCell]
  )

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [handleKeyDown])

  const handleHint = async () => {
    if (mode === 'play' && status !== 'playing') return
    setMessage('')
    setMessageType('')
    setHintLoading(true)
    try {
      if (mode === 'create') {
        const data = await fetchHint(createGrid, null)
        setCreateGrid(data.puzzle)
      } else {
        const data = await fetchHint(currentPuzzle, puzzleId)
        const next = data.puzzle
        setCurrentPuzzle(next)
        setHintCount(h => h + 1)
        if (isSolved(next)) {
          setStatus('solved')
          setMessage('Puzzle solved!')
          setMessageType('success')
          setSelectedCell(null)
        }
      }
    } catch (e) {
      setMessage(e.message || 'Could not get hint')
      setMessageType('error')
    } finally {
      setHintLoading(false)
    }
  }

  const handleSolve = async () => {
    if (mode === 'play' && status !== 'playing') return
    setMessage('')
    setMessageType('')
    setSolveLoading(true)
    try {
      if (mode === 'create') {
        const data = await fetchSolution(createGrid, null)
        setCreateGrid(data.solution)
      } else {
        const data = await fetchSolution(currentPuzzle, puzzleId)
        setCurrentPuzzle(data.solution)
        setStatus('solved')
        setMessage('Puzzle solved!')
        setMessageType('success')
        setSelectedCell(null)
      }
    } catch (e) {
      setMessage(e.message || 'Could not solve puzzle')
      setMessageType('error')
    } finally {
      setSolveLoading(false)
    }
  }

  const handleCheckPuzzle = async () => {
    setMessage('')
    setMessageType('')
    setCheckLoading(true)
    try {
      const data = await checkPuzzle(createGrid)
      if (data.result === 'invalid') {
        setMessage('This puzzle contains a contradiction (a duplicate in a row, column, or box).')
        setMessageType('error')
      } else if (data.result === 'unsolvable') {
        setMessage('This puzzle has no solution.')
        setMessageType('error')
      } else if (data.result === 'multiple') {
        setMessage("This puzzle has multiple solutions — it isn't a valid unique puzzle.")
        setMessageType('error')
      } else if (data.result === 'unique') {
        setMessage('Valid puzzle! It has exactly one solution.')
        setMessageType('success')
      }
    } catch (e) {
      setMessage(e.message || 'Could not check puzzle')
      setMessageType('error')
    } finally {
      setCheckLoading(false)
    }
  }

  const handleEnterCreate = () => {
    setMode('create')
    setCreateGrid(emptyGrid())
    setSelectedCell(null)
    setMessage('')
    setMessageType('')
  }

  const handleExitCreate = () => {
    setMode('play')
    setSelectedCell(null)
    setMessage('')
    setMessageType('')
  }

  const handleClearGrid = () => {
    setCreateGrid(emptyGrid())
    setSelectedCell(null)
    setMessage('')
    setMessageType('')
  }

  const isNumberPadDisabled =
    mode === 'create'
      ? !selectedCell
      : !selectedCell ||
        (selectedCell && originalPuzzle?.[selectedCell.row]?.[selectedCell.col] !== 0)

  const boardPuzzle = mode === 'create' ? createGrid : currentPuzzle
  const boardOriginal = mode === 'create' ? emptyGrid() : originalPuzzle

  return (
    <div className="app">
      <button
        className="btn btn-theme-toggle"
        onClick={() => setDarkMode(d => !d)}
        aria-label={darkMode ? 'Switch to light mode' : 'Switch to dark mode'}
      >
        {darkMode ? 'Light Mode' : 'Dark Mode'}
      </button>
      <h1>Sudoku</h1>
      <Controls
        mode={mode}
        difficulty={difficulty}
        onDifficultyChange={setDifficulty}
        onNewGame={() => loadPuzzle(difficulty)}
        onHint={handleHint}
        onSolve={handleSolve}
        status={status}
        hintCount={hintCount}
        hintLoading={hintLoading}
        solveLoading={solveLoading}
        onEnterCreate={handleEnterCreate}
        onExitCreate={handleExitCreate}
        onClearGrid={handleClearGrid}
        onCheckPuzzle={handleCheckPuzzle}
        checkLoading={checkLoading}
      />
      {message && (
        <div className={`message ${messageType}`}>
          {message}
        </div>
      )}
      {mode === 'play' && status === 'loading' && <div className="message">Loading puzzle...</div>}
      {(mode === 'create' || currentPuzzle) && (
        <>
          <Board
            puzzle={boardPuzzle}
            originalPuzzle={boardOriginal}
            selectedCell={selectedCell}
            onCellSelect={handleCellSelect}
          />
          {(mode === 'create' || status === 'playing') && (
            <NumberPad onNumber={fillCell} disabled={isNumberPadDisabled} />
          )}
        </>
      )}
    </div>
  )
}

export default App
