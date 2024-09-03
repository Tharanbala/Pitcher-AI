import Icons from "@/components/global/icons";
import { Heart } from "lucide-react";
import Link from "next/link";


const Footer = () => {
  return (
    <footer className="flex flex-col relative items-center justify-center border-t border-border pt-16 pb-8 px-6 lg:px-8 w-full max-w-6xl mx-auto lg:pt-32">
      <div className="hidden lg:block absolute -top-1/3 -right-1/4 bg-primary w-72 h-72 rounded-full -z-10 blur-[14rem]"></div>
      <div className="hidden lg:block absolute bottom-0 -left-1/4 bg-primary w-72 h-72 rounded-full -z-10 blur-[14rem]"></div>

      <div className="grid gap-8 xl:grid-cols-3 xl:gap-8 w-full">
        <div className="flex flex-col items-start justify-start md:max-w-[200px]">
          <div className="flex items-start">
          <img src='/icons/icon.png' width={30} height={30}/>
          </div>
          <p className="text-muted-foreground mt-4 text-sm text-start">
          Turning Reviews into Winning Pitches
          </p>
          
        </div>

        <div className="grid-cols-2 gap-8 grid mt-16 xl:col-span-2 xl:mt-0">
          <div className="md:grid md:grid-cols-2 md:gap-8">
            <div>
              <h3 className="text-base font-medium text-white">Company</h3>
              <ul className="mt-4 text-sm text-muted-foreground">
                <li className="mt-2">
                  <Link
                    href="#about"
                    className="hover:text-foreground transition-all duration-300"
                  >
                    About
                  </Link>
                </li>
                <li className="mt-2">
                  <Link
                    href="#process"
                    className="hover:text-foreground transition-all duration-300"
                  >
                    Process
                  </Link>
                </li>
                <li className="mt-2">
                  <Link
                    href="#feature"
                    className="hover:text-foreground transition-all duration-300"
                  >
                    Features
                  </Link>
                </li>
              </ul>
            </div>
            
          </div>
          <div className="md:grid md:grid-cols-2 md:gap-8">
            
            {/* Team Section  of founder*/}
            <div className="mt-10 md:mt-0 flex flex-col">
              <a href='/team'>
              <h3 className="text-base font-medium text-white">Meet the Team</h3>
              </a>
              
              <ul className="mt-1 text-sm text-muted-foreground">
                <li className="mt-2">
                  <Link
                    href="https://www.linkedin.com/in/a-shubham-verma/"
                    className="hover:text-foreground transition-all duration-300"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Shubham Verma
                  </Link>
                </li>
                <li className="mt-2">
                  <Link
                    href="https://www.linkedin.com/in/shobygnanasekaran/"
                    className="hover:text-foreground transition-all duration-300"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Shoby Gnanasekaran
                  </Link>
                </li>
                <li className="mt-2">
                  <Link
                    href="https://www.linkedin.com/in/tharan-bala/"
                    className="hover:text-foreground transition-all duration-300"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Tharan Bala
                  </Link>
                </li>
                <li className="mt-2">
                  <Link
                    href="https://www.linkedin.com/in/tirthgshah/"
                    className="hover:text-foreground transition-all duration-300"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Tirth Shah
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <div className="mt-8 border-t border-border/40 pt-4 md:pt-8 md:flex md:items-center md:justify-between w-full">
        <p className="text-sm text-muted-foreground mt-8 md:mt-0">
          &copy; {new Date().getFullYear()} Pitcher AI INC. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
