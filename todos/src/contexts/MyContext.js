import { createContext, useState } from "react";

export const MyContext = createContext({
    title: '',
    setTitle: () => { }
});

export const MyContextProvider = ({ children }) => {
    const [title, setTitle] = useState('Software Engineer');
    return (
        <MyContext.Provider value={{
            title,
            setTitle
        }}>
            {children}
        </MyContext.Provider >
    )
}