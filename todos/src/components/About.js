import { useContext } from "react"
import { MyContext } from "../contexts/MyContext"

export const About = () => {
    const { title } = useContext(MyContext);

    return (
        <>
            <h2>ABOUT</h2>
            <em>First App demo</em>
            <h3>{title}</h3>
        </>
    )
}