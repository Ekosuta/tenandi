import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
    return (
        <header style={ {backgroundColor: '#ACBFA4'} }>
            <nav className='nav justify-content-center'>
                <Link className='nav-link' to='/'>Home</Link>
                <Link className='nav-link' to='/units'>Units</Link>
                <Link className='nav-link' to='/progress'>Progress</Link>
            </nav>
        </header>
    )
}

export default Header;