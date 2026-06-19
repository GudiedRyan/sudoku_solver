import Cell from './Cell'

function Board({ puzzle, originalPuzzle, selectedCell, onCellSelect }) {
  const selectedValue = selectedCell
    ? puzzle[selectedCell.row][selectedCell.col]
    : 0

  return (
    <div className="board">
      {puzzle.map((row, rowIdx) =>
        row.map((value, colIdx) => (
          <Cell
            key={`${rowIdx}-${colIdx}`}
            value={value}
            isGiven={originalPuzzle[rowIdx][colIdx] !== 0}
            isSelected={selectedCell?.row === rowIdx && selectedCell?.col === colIdx}
            isSameNumber={selectedValue !== 0 && value === selectedValue}
            isBoxRight={colIdx === 2 || colIdx === 5}
            isBoxBottom={rowIdx === 2 || rowIdx === 5}
            onClick={() => onCellSelect(rowIdx, colIdx)}
          />
        ))
      )}
    </div>
  )
}

export default Board
