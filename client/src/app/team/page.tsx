import { Linkedin, Twitter } from "lucide-react";
import React from "react";

const Team = () => {
  return (
    <div className="flex justify-center p-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl">
        <div className="max-w-sm rounded overflow-hidden shadow-lg ">
          <img
            className="w-full h-70 object-cover"
            src="/assets/shubham.png"
            alt="Member 1"
          />
          <div className="px-6 py-4">
            <div className="font-bold text-xl mb-2 text-white">
              Shubham Verma
            </div>
          </div>
          <div className="px-6 pt-4 pb-2 flex flex-col items-start space-y-2">
            <div className="flex items-center space-x-2">
              <a
                href="https://www.linkedin.com/in/a-shubham-verma/"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Linkedin />
              </a>
              <a
                href="https://x.com/npm_shubham"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Twitter />
              </a>
            </div>
          </div>
        </div>
        <div className="max-w-sm rounded overflow-hidden shadow-lg">
          <img
            className="w-full h-70 object-cover"
            src="/assets/tharan.jpeg"
            alt="Member 2"
          />
          <div className="px-6 py-4">
            <div className="font-bold text-xl mb-2 text-white">Tharan Bala</div>
          </div>
          <div className="px-6 pt-4 pb-2 flex flex-col items-start space-y-2">
            <div className="flex items-center space-x-2">
              <a
                href="https://www.linkedin.com/in/tharan-bala/"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Linkedin />
              </a>
              <a
                href="https://x.com/tharan_tb"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Twitter />
              </a>
            </div>
          </div>
        </div>
        <div className="max-w-sm rounded overflow-hidden shadow-lg">
          <img
            className="w-full h-70 object-cover"
            src="/assets/tirth.png"
            alt="Member 3"
          />
          <div className="px-6 py-4">
            <div className="font-bold text-xl mb-2 text-white">Tirth Shah</div>
          </div>
          <div className="px-6 pt-4 pb-2 flex flex-col items-start space-y-2">
            <div className="flex items-center space-x-2">
              <a
                href="https://www.linkedin.com/in/tirthgshah/"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Linkedin />
              </a>
              <a
                href="https://twitter.com/TirthGShah"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Twitter />
              </a>
            </div>
          </div>
        </div>
        <div className="max-w-sm rounded overflow-hidden shadow-lg ">
          <img
            className="w-full h-70 object-cover"
            src="/assets/shoby.png"
            alt="Member 4"
          />
          <div className="px-6 py-4">
            <div className="font-bold text-xl mb-2 text-white">
              Shoby Gnanasekaran
            </div>
          </div>
          <div className="px-6 pt-4 pb-2 flex flex-col items-start space-y-2">
            <div className="flex items-center space-x-2">
              <a
                href="https://www.linkedin.com/in/shobygnanasekaran/"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Linkedin />
              </a>
              <a
                href="https://x.com/shobysekar"
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700"
              >
                <Twitter />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Team;
