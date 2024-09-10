import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import ChangeMode from "../components/ChangeMode";

type Option = {
  value: string;
};
const Register = () => {
  const [name, setName] = useState<string>("");
  const [reg_no, setReg_no] = useState<string>("");
  const [phone, setPhone] = useState<string>("");
  const [err, setErr] = useState<string>("");
  const [success, setSuccess] = useState("");
  const [select, setSelect] = useState<string>("");
  const [course, setCourse] = useState<Option[]>([
    { value: "Bachelors of Computer Science(BCS)" },
    { value: "Bachelors of Information Technology(BIT)" },
    { value: " Diploma in Computer Science(DCS)" },
    { value: "Diploma in Information Technology(DIT)" },
  ]);
  const navigate = useNavigate();
  const [mode, setMode] = useState<boolean>(false);

  const handleSubmit = async (e: React.FormEvent) => {
    console.log(name, phone, reg_no, select);
    e.preventDefault();
    setErr("");
    setSuccess("");
    if (!name) return setErr("Name is required");
    if (!reg_no) return setErr("REG_no is required");
    if (!phone) return setErr("Phone number is required");
    if (!select) return setErr("Course is required");
    try {
      const response = await axios.post(
        "http://localhost:8008/student/new_student",
        { name, reg_no, phone_no: phone, course: select }
      );

      if (response.status === 201) {
        const studentId = response.data.id;
        setSuccess("Student Created Successfully");
        setErr("");
        setName("");
        setReg_no("");
        setPhone("");
        setSelect("");
        setTimeout(() => {
          setSuccess("");
          navigate(`/student/${studentId}`);
        }, 3000);
      }
    } catch (error: any) {
      if (error.response?.status === 401) {
        setErr("Reg_no exists, try a new one");
      } else {
        setErr("An error occurred");
      }
    }
  };

  return (
    <div
      className={`p-5 min-h-screen flex bg-neutral-200" ${
        mode ? "bg-neutral-200" : "bg-slate-800"
      } `}
    >
      <div
        className={` shadow-2xl bg-slate-200 ${
          mode ? "bg-slate-200 text-black" : "bg-slate-700 text-slate-500"
        }  p-2 w-full rounded flex items-center justify-center  `}
      >
        <form className="gap-3 flex flex-col relative" onSubmit={handleSubmit}>
          {success && (
            <p className="absolute -top-14 md:-top-32 bg-green-500 p-2 rounded text-white text-sm">
              {success}
            </p>
          )}
          <ChangeMode mode={mode} setMode={setMode} />
          <p className="text-center text-2xl">Student Registration Form</p>
          <label
            htmlFor="name"
            className="flex flex-col md:flex-row md:items-center gap-3"
          >
            <span className="text-left">Name:</span>
            <input
              type="text"
              placeholder="Name"
              value={name}
              id="name"
              onChange={(e) => setName(e.target.value)}
              className="p-3 rounded outline-none  border-none w-full"
            />
          </label>
          <div className="flex flex-col md:flex-row  gap-4">
            <label
              htmlFor="reg_no"
              className="flex flex-col md:flex-row md:items-center gap-3"
            >
              <span className="text-left">REG_no:</span>
              <input
                type="text"
                placeholder="Registration number..."
                value={reg_no}
                id="reg_no"
                onChange={(e) => setReg_no(e.target.value)}
                className="p-3 rounded outline-none border-none w-full"
              />
            </label>
            <label
              htmlFor="phone"
              className="flex flex-col md:flex-row md:items-center gap-3"
            >
              <span className="text-left">Phone:</span>
              <input
                type="text"
                placeholder="Phone number"
                value={phone}
                id="phone"
                onChange={(e) => setPhone(e.target.value)}
                className="p-3 rounded outline-none border-none w-full"
              />
            </label>
          </div>
          <label
            htmlFor="course"
            className="flex flex-col md:flex-row md:items-center gap-3"
          >
            <span className="text-left">Course:</span>
            <select
              className="p-3 rounded outline-none border-none w-full appearance-auto"
              value={select}
              onChange={(e: React.ChangeEvent<HTMLSelectElement>) =>
                setSelect(e.target.value)
              }
            >
              <option value="" disabled>
                -- Select your course
              </option>
              {course.map((course) => (
                <option key={course.value} value={course.value}>
                  {course.value}
                </option>
              ))}
            </select>
          </label>
          {err && (
            <p
              className={` ${
                mode ? "text-red-700" : "text-red-500"
              }  text-right -mt-2 motion-safe:animate-bounce`}
            >
              {err}
            </p>
          )}
          <button className="p-5 bg-red-200 w-full rounded hover:scale-105 hover:shadow-md mt-2">
            Register Now
          </button>
        </form>
      </div>
    </div>
  );
};

export default Register;
