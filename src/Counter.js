import { useEffect, useState } from "react";

export const Counter = () => {
    const [count, setCount] = useState(0);
    useEffect(() => {
        console.log('useEffect always');
    });
    useEffect(() => {
        console.log('useEffect first time');
    }, []);
    useEffect(() => {
        console.log('useEffect count change');
    }, [count]);
    return (
        <div>
            <h1>COUNTER</h1>
            <h3>Value: {count}</h3>
            <button type="button" onClick={() => setCount(count + 1)}>
                +
            </button>
            <button type="button" onClick={() => setCount(count - 1)}>
                -
            </button>
        </div>
    );
}