function Cell({ value, isGiven, isSelected, isSameNumber, isBoxRight, isBoxBottom, onClick }) {
  const classes = [
    'cell',
    isGiven ? 'given' : value !== 0 ? 'user-filled' : 'empty',
    isSelected ? 'selected' : '',
    isSameNumber ? 'same-number' : '',
    isBoxRight ? 'box-border-right' : '',
    isBoxBottom ? 'box-border-bottom' : '',
  ].filter(Boolean).join(' ')

  return (
    <div className={classes} onClick={onClick}>
      {value !== 0 ? value : ''}
    </div>
  )
}

export default Cell
