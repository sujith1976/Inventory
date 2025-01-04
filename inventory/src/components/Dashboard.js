import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
  return (
    <div>
      <h2>Dashboard</h2>
      <p>Welcome to the Telecom Inventory Management System!</p>
      <nav>
        <Link to="/products">Go to Products</Link>
      </nav>
    </div>
  );
};

export default Dashboard;



