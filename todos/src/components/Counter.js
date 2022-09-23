import { useState } from "react"

export const Counter = () => {
    const [count, setCount] = useState(0);

    return (
        <>
            <h2>{count}</h2>
            <button onClick={() => setCount(count + 1)}>+</button>
            <button onClick={() => setCount(count - 1)}>-</button>
        </>
    )
}