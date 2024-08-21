

const HomeCard = () => {
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="bg-white rounded-lg shadow-lg p-6 w-full max-w-2xl">
        <h2 className="text-2xl font-bold mb-4 text-center">Product Demo</h2>
        <div className="aspect-w-16 aspect-h-9 h-96"> 
          <iframe
            className="w-full h-full"
            src="" // Replace with your actual video URL
            title="Product Demo Video"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          ></iframe>
        </div>
        <p className="mt-4 text-center text-gray-600">
          Watch our product demo to see Pitcher AI in action!
        </p>
      </div>
    </div>
  );
};

export default HomeCard;
