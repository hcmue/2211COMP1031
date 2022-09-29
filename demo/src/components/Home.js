import { useContext } from 'react';
import { MyContext } from '../contexts/MyContext';
import { TodoContext } from '../contexts/TodoContext';
export const HomePage = () => {
    const { username, isLogged } = useContext(MyContext);
    const { tasks } = useContext(TodoContext);

    return (
        <>
            <h2>MY HOMEPAGE</h2>
            <div>
                {isLogged && (
                    <div>WELCOME MY PRO</div>
                )}
                {isLogged ? (
                    <div>Chào mừng bạn <strong>{username}</strong> thăm trang của tui</div>
                ) : (
                    <div>Bạn chưa đăng nhập</div>
                )}

                {tasks.map(item => (
                    <div>
                        <h2>{item.name}</h2>
                        <h5>{item.isCompleted ? 'DONE' : 'IN-PROGRESS'}</h5>
                    </div>
                ))}
            </div>
        </>
    )
}