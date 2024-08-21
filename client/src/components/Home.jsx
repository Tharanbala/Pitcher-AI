import Footer from "./Footer"
import HomeCard from "./HomeCard"
import Navbar from "./Navbar"

const HomePage = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-grow">
        {/* Add your main content here */}
        <HomeCard/>
      </main>
      <Footer />
    </div>
  )
}

export default HomePage