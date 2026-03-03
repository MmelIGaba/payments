import React, { useState } from 'react';
import axios from 'axios';

function SchoolRevenueDashboard() {
    const [schoolId, setSchoolId] = useState('');
    const [revenue, setRevenue] = useState(null);

    const fetchRevenue = async () => {
        try {
            const response = await axios.get(`${process.env.REACT_APP_API_URL}/schools/${schoolId}/revenue`);
            setRevenue(response.data);
        } catch (error) {
            console.error("Error fetching revenue:", error);
        }
    };

    return (
        <div>
            <h1>School Revenue Dashboard</h1>
            <input type="number" placeholder="School ID" value={schoolId} onChange={(e) => setSchoolId(e.target.value)} required />
            <button onClick={fetchRevenue}>Get Revenue</button>
            {revenue && (
                <div>
                    <h2>Revenue</h2>
                    <p>Total Collected: {revenue.total_collected}</p>
                    <p>Total Knit Fees: {revenue.total_knit_fees}</p>
                    <p>Total Paid to School: {revenue.total_paid_to_school}</p>
                </div>
            )}
        </div>
    );
}

export default SchoolRevenueDashboard;