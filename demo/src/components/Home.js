import { useContext } from 'react';
import { MyContext } from '../contexts/MyContext';
export const HomePage = () => {
    const { username, isLogged } = useContext(MyContext);

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
            </div>
        </>
    )
}