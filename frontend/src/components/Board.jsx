import Cell from './Cell'

function markConflicts(puzzle, cells, conflicts) {
  const seen = new Map()
  cells.forEach(([r, c]) => {
    const value = puzzle[r][c]
    if (value === 0) return
    const key = `${r}-${c}`
    if (seen.has(value)) {
      conflicts.add(key)
      conflicts.add(seen.get(value))
    } else {
      seen.set(value, key)
    }
  })
}

function getConflictKeys(puzzle) {
  const conflicts = new Set()

  for (let i = 0; i < 9; i++) {
    markConflicts(puzzle, Array.from({ length: 9 }, (_, j) => [i, j]), conflicts)
    markConflicts(puzzle, Array.from({ length: 9 }, (_, j) => [j, i]), conflicts)
  }

  for (let boxRow = 0; boxRow < 3; boxRow++) {
    for (let boxCol = 0; boxCol < 3; boxCol++) {
      const cells = []
      for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 3; c++) {
          cells.push([boxRow * 3 + r, boxCol * 3 + c])
        }
      }
      markConflicts(puzzle, cells, conflicts)
    }
  }

  return conflicts
}

function Board({ puzzle, originalPuzzle, selectedCell, onCellSelect }) {
  const selectedValue = selectedCell
    ? puzzle[selectedCell.row][selectedCell.col]
    : 0
  const conflicts = getConflictKeys(puzzle)

  return (
    <div className="board">
      {puzzle.map((row, rowIdx) =>
        row.map((value, colIdx) => {
          const isGiven = originalPuzzle[rowIdx][colIdx] !== 0
          return (
            <Cell
              key={`${rowIdx}-${colIdx}`}
              value={value}
              isGiven={isGiven}
              isSelected={selectedCell?.row === rowIdx && selectedCell?.col === colIdx}
              isSameNumber={selectedValue !== 0 && value === selectedValue}
              isError={!isGiven && conflicts.has(`${rowIdx}-${colIdx}`)}
              isBoxRight={colIdx === 2 || colIdx === 5}
              isBoxBottom={rowIdx === 2 || rowIdx === 5}
              onClick={() => onCellSelect(rowIdx, colIdx)}
            />
          )
        })
      )}
    </div>
  )
}

export default Board
