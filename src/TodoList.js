import react, { useState } from "react";

export const ToDoList = () => {
    const [data, setData] = useState([]);
    return (
        <div>
            <h1>TODOs</h1>
        </div>
    );
}