import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import ArticlesListPage from './components/ArticlesListPage/ArticlesListPage';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ArticlesListPage />
  </React.StrictMode>
);


reportWebVitals();
