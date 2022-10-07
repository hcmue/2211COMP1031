import axios from 'axios';
import React, { useEffect, useState } from 'react';

export const DemoApi = () => {
    //Dùng fetch() 10 users 
    // Dùng axios GET lấy 5000 photos
    const [users, setUsers] = useState([]);
    const [photos, setPhotos] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        setIsLoading(true);
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(response => response.json())
            .then(json => setUsers(json))
            .catch((err) => console.log(err));

        axios.get("https://jsonplaceholder.typicode.com/photos")
            .then((json) => {
                setPhotos(json.data);
                setIsLoading(false);
            })
            .catch((err) => console.log(err));
    }, []);

    return (
        <>
            {isLoading && (
                <div>
                    Đang tải dữ liệu, vui lòng chờ
                </div>
            )}
            <h2>DEMO CALL API</h2>
            {isLoading ? (
                <div>
                    <image src="../loading.png" />
                </div>
            ) : (
                <div>
                    {photos.map((item) => (
                        <div>
                            {item.title}
                        </div>
                    ))}
                </div>
            )}


        </>
    )
}