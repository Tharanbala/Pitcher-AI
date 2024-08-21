import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/Home';
import Auth from './components/Auth';

   const App = () => {
     return (
       <Router>
         <Routes>
           <Route path="/" element={<HomePage />} />
           <Route path="/signin" element={<Auth />} />
         </Routes>
       </Router>
     );
   }

   export default App