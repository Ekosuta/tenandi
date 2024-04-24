import React from "react";
import { useParams, Link } from 'react-router-dom';
import unitsData from '../data/units.json';
import lessonsData from '../data/lessons.json'
import './unit.css'

function Unit() {
    const { unitId } = useParams();
    
    return (
        <div>
            <h1>{unitsData[unitId].title}</h1>
            {unitsData[unitId].lessons.map((lessonId) => (
                <div className="card w-80" key={lessonId}>
                    <div className="card-body">
                        <h5 className="card-title">{lessonsData[lessonId].title}</h5>
                        <p className="card-text">{lessonsData[lessonId].subtitle}</p>
                        <Link className="btn btn-primary" to={`/units/${unitId}/${lessonId}`}>Go to slides</Link>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default Unit;