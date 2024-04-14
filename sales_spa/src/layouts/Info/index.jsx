import React from 'react';

import style from './style.module.scss';

const Info = () => {
	const [chartType, setChartType] = React.useState([
		{name: ""}
	]);

    return (
        <div className={style.container}>
            <h2>Анализ в виде диаграммы</h2>
            <ul className={style.flexContainer}>

			</ul>
        </div>
    );
};

export default Info;
