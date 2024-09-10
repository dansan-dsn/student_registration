import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Student = () => {
  const { id } = useParams<{ id: string }>();
  const url = "http:/localhost:8008/student";

  return (
    <div>
      <div>
        <span>Name</span>
        <span></span>
      </div>
      <div>
        <span>Reg_no</span>
        <span></span>
      </div>
      <div>
        <span>Phone</span>
        <span></span>
      </div>
      <div>
        <span>Course</span>
        <span></span>
      </div>
    </div>
  );
};

export default Student;
