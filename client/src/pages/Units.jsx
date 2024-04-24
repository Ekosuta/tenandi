import React from "react";
import { Link } from "react-router-dom";
import unitsData from '../data/units.json'

function Units() {
    return (
        <div className="container-mt-5">
            <h1>Units</h1>
            <ul style={{listStyleType: "none"}}>
                {Object.keys(unitsData).map((unitId) => (
                    <li key={unitId} className="card">
                        <Link to={`/units/${unitId}`}>{unitsData[unitId].title}</Link>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Units;