import React, { useState } from 'react';
import axios from 'axios';

function MakePayment() {
    const [studentId, setStudentId] = useState('');
    const [amount, setAmount] = useState('');
    const [reference, setReference] = useState('');
    const [paymentBreakdown, setPaymentBreakdown] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`${process.env.REACT_APP_API_URL}/payments`, {
                student_id: studentId,
                amount,
                reference
            });
            setPaymentBreakdown(response.data);
        } catch (error) {
            console.error("Error making payment:", error);
        }
    };

    return (
        <div>
            <h1>Make Payment</h1>
            <form onSubmit={handleSubmit}>
                <input type="number" placeholder="Student ID" value={studentId} onChange={(e) => setStudentId(e.target.value)} required />
                <input type="number" placeholder="Amount" value={amount} onChange={(e) => setAmount(e.target.value)} required />
                <input type="text" placeholder="Reference" value={reference} onChange={(e) => setReference(e.target.value)} required />
                <button type="submit">Submit Payment</button>
            </form>
            {paymentBreakdown && (
                <div>
                    <h2>Payment Breakdown</h2>
                    <p>Total: {paymentBreakdown.amount}</p>
                    <p>Knit Fee: {paymentBreakdown.knit_fee}</p>
                    <p>School Amount: {paymentBreakdown.school_amount}</p>
                </div>
            )}
        </div>
    );
}

export default MakePayment;
