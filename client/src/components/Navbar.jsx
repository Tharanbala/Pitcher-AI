
import { Link } from 'react-router-dom';


const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-white text-2xl font-bold">
          PitcherAI
        </Link>
        <div className="hidden md:flex space-x-4">
          <Link to="/Auth" className="bg-yellow-400 hover:hover:bg-yellow-500 text-white px-4 py-2 rounded">
            Sign In/Sign Up
          </Link>
        </div>
        <div className="md:hidden">

          <Link to="/Auth" className="bg-yellow-600 hover:bg-yellow-500 text-white px-4 py-2 rounded">
            Sign In/Sign Up
          </Link>

        </div>
      </div>
    </nav>
  );
};

export default Navbar;
