import { useEffect, useState } from "react"

export const Counter = () => {
    const [count, setCount] = useState(0);
    const [jobName, setJobName] = useState('');

    // Alway runs
    useEffect(() => {
        console.log(`Running......, count = ${count}`);
    });

    // Run in first time
    useEffect(() => {
        console.log(`Running in first time......, count = ${count}`);
    }, []);

    // Run in every count changes
    useEffect(() => {
        console.log(`Count change......, count = ${count}`);
    }, [count]);

    return (
        <>
            <input value={jobName} onChange={(e) => setJobName(e.target.value)} />
            <h2>Job: {jobName}</h2>
            <h2>{count}</h2>
            <button onClick={() => setCount(count + 1)}>+</button>
            <button onClick={() => setCount(count - 1)}>-</button>
        </>
    )
}