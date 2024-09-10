import React from "react";

interface bgColor {
  setMode: any;
  mode: any;
}

const ChangeMode: React.FC<bgColor> = ({ setMode, mode }) => {
  const toggleMode = () => {
    setMode(!mode);
  };
  return (
    <div className="absolute -top-8 md:-top-20 right-0 md:-right-24 xl:-right-72">
      <div
        className={`rounded-full w-14 h-7 ${
          mode ? "bg-gray-300" : "bg-gray-800"
        } grid items-center cursor-pointer`}
        title="change theme"
        onClick={toggleMode}
      >
        <div className="">
          <div
            className={`rounded-full w-6 h-6 ${
              mode ? "translate-x-7 bg-red-300 " : "bg-red-200 ml-1"
            }`}
            style={{ transition: "transform 0.3s ease" }}
          />
        </div>
      </div>
    </div>
  );
};

export default ChangeMode;
