const API_BASE = '/api'

export async function fetchPuzzle(difficulty) {
  const res = await fetch(`${API_BASE}/puzzle?difficulty=${difficulty}`)
  if (!res.ok) throw new Error('Failed to fetch puzzle')
  return res.json()
}

export async function fetchHint(puzzle) {
  const res = await fetch(`${API_BASE}/hint`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ puzzle }),
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to get hint')
  return data
}

export async function fetchSolution(puzzle) {
  const res = await fetch(`${API_BASE}/solve`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ puzzle }),
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to solve puzzle')
  return data
}
