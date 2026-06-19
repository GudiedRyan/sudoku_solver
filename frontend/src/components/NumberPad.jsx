function NumberPad({ onNumber, disabled }) {
  return (
    <div className="number-pad">
      {[1, 2, 3, 4, 5, 6, 7, 8, 9].map(n => (
        <button
          key={n}
          className="num-btn"
          onClick={() => onNumber(n)}
          disabled={disabled}
        >
          {n}
        </button>
      ))}
      <button className="num-btn clear" onClick={() => onNumber(0)} disabled={disabled}>
        Clear
      </button>
    </div>
  )
}

export default NumberPad
