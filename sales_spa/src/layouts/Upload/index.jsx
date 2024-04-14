import React from 'react';
import axios from 'axios';

import style from './style.module.scss';

const Upload = () => {
    const [file, setFile] = React.useState(null);
    const [errorMessage, setErrorMessage] = React.useState('');

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (
            selectedFile &&
            selectedFile.type ===
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ) {
            setFile(selectedFile);
            setErrorMessage('');
        } else {
            setFile(null);
            setErrorMessage('Пожалуйста, выберите файл Excel⛔');
        }
    };

    const handleFileUpload = async () => {
        if (file) {
            try {
                const formData = new FormData();
                formData.append('file', file);
                await axios.post('http://127.0.0.1:8000/api/upload', formData);
                setFile(null);
            } catch (error) {
                setErrorMessage(
                    `Ой! Произошла непредвиденная ошибка 😣
        Попробуйте загрузить файл заново и повторить попытку`,
                );
            }
        }
    };

    const handleUploadTest = async () => {
        try {
            const response = await axios.get('/test_data.xlsx');
            const testFile = new Blob([response.data], {
                type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            });
            const formData = new FormData();
            formData.append('file', testFile);
            await axios.post('http://127.0.0.1:8000/api/upload', formData); //Обновить API
        } catch (error) {
            setErrorMessage('Произошла ошибка при загрузке тестового файла.');
        }
    };

    return (
        <div className={style.container}>
            <h1 className={style.head}>Добро пожаловать, пользователь!</h1>
            <div className={style.wrapper}>
                {!file ? (
                    <h2>Чтобы начать анализ, загрузите Excel-файл 📁</h2>
                ) : (
                    <h2>
                        Выбранный файл: <span className={style.fileName}>{file.name}</span> 📂
                    </h2>
                )}
                <div className={style.wrapperFile}>
                    {file ? (
                        <p className={style.infoFile}>
                            Для изменения файла <br />
                            нажмите или перетащите сюда
                        </p>
                    ) : (
                        <p className={style.infoFile}>
                            Перетащите сюда файл <br />
                            или нажмите, чтобы выбрать
                        </p>
                    )}

                    <input type="file" onChange={handleFileChange} />

                    {errorMessage && <p className={style.error}>{errorMessage}</p>}
                </div>
                <div className={style.alternate}>
                    {file && !errorMessage ? (
                        <button onClick={handleFileUpload}>
                            Начать! 🚀
                        </button>
                    ) : (
                        <>
                            <h2>..или вы можете протестировать на</h2>
                            <button onClick={handleUploadTest}>заготовленном файле!</button>
                        </>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Upload;
