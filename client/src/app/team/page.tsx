import { Linkedin, Twitter } from 'lucide-react';
import React from 'react';

const Team = () => {
    return (
        <div className="flex justify-center p-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl">
                <div className="max-w-sm rounded overflow-hidden shadow-lg ">
                    <img className="w-full h-70 object-cover" src="/assets/shubham.png" alt="Member 1"/>
                    <div className="px-6 py-4">
                        <div className="font-bold text-xl mb-2 text-black">Shubham Verma</div>
                    </div>
                    <div className="px-6 pt-4 pb-2 flex items-center justify-between">
                        <a href="https://www.linkedin.com/in/a-shubham-verma/" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Linkedin />
                        </a>
                        <a href="https://x.com/npm_shubham" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Twitter />
                        </a>
                        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mb-2">
                            College: XYZ University
                        </span>
                    </div>
                </div>
                <div className="max-w-sm rounded overflow-hidden shadow-lg bg-white">
                    <img className="w-full h-48 object-cover" src="https://example.com/member2.jpg" alt="Member 2"/>
                    <div className="px-6 py-4">
                        <div className="font-bold text-xl mb-2 text-black">Tharan Bala</div>
                    </div>
                    <div className="px-6 pt-4 pb-2 flex items-center justify-between">
                        <a href="https://linkedin.com/member2" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Linkedin />
                        </a>
                        <a href="https://twitter.com/member2" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Twitter />
                        </a>
                        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mb-2">
                            College: ABC University
                        </span>
                    </div>
                </div>
                <div className="max-w-sm rounded overflow-hidden shadow-lg bg-white">
                    <img className="w-full h-48 object-cover" src="https://example.com/member3.jpg" alt="Member 3"/>
                    <div className="px-6 py-4">
                        <div className="font-bold text-xl mb-2 text-black">Tirth Shah</div>
                    </div>
                    <div className="px-6 pt-4 pb-2 flex items-center justify-between">
                        <a href="https://linkedin.com/member3" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Linkedin />
                        </a>
                        <a href="https://twitter.com/member3" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Twitter />
                        </a>
                        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mb-2">
                            College: DEF University
                        </span>
                    </div>
                </div>
                <div className="max-w-sm rounded overflow-hidden shadow-lg bg-white">
                    <img className="w-full h-48 object-cover" src="https://example.com/member4.jpg" alt="Member 4"/>
                    <div className="px-6 py-4">
                        <div className="font-bold text-xl mb-2 text-black">Shoby</div>
                    </div>
                    <div className="px-6 pt-4 pb-2 flex items-center justify-between">
                        <a href="https://linkedin.com/member4" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Linkedin />
                        </a>
                        <a href="https://twitter.com/member4" className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                            <Twitter />
                        </a>
                        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mb-2">
                            College: GHI University
                        </span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Team;
