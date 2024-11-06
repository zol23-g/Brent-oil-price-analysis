import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api';

export const fetchData = (startDate, endDate) => 
    axios.get(`${API_URL}/data`, { params: { start_date: startDate, end_date: endDate } });

export const fetchForecast = () => 
    axios.get(`${API_URL}/forecast`);

export const fetchMetrics = () => 
    axios.get(`${API_URL}/metrics`);
